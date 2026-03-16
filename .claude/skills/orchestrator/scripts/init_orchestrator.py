import os
import json
import platform
import subprocess
import shutil
from pathlib import Path

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_symlink(source, target, options):
    source = Path(source).expanduser().resolve()
    target = Path(target).expanduser()

    # 1. 기존 타겟 처리 (Backup 및 Force 옵션)
    if target.exists() or target.is_symlink():
        if options.get("create_backup"):
            backup_path = target.with_suffix(f"{target.suffix}.bak")
            # 기존 백업이 있으면 제거 후 생성
            if backup_path.exists():
                if backup_path.is_dir(): shutil.rmtree(backup_path)
                else: backup_path.unlink()
            target.rename(backup_path)
            print(f"    [Backup] Moved existing to {backup_path.name}")
        
        if options.get("force_symlink"):
            if target.exists() or target.is_symlink():
                if target.is_dir() and not target.is_symlink(): shutil.rmtree(target)
                else: target.unlink()

    # 2. 심볼릭 링크 생성
    if platform.system() == "Windows":
        subprocess.run(["powershell", "-Command", f"New-Item -ItemType SymbolicLink -Path '{target}' -Target '{source}'"], check=True)
    else:
        os.symlink(source, target)

def main():
    # 경로 설정
    script_dir = Path(__file__).parent
    assets_dir = script_dir.parent / "assets"
    config = load_config(assets_dir / "config.json")
    
    home = Path.expanduser(Path("~"))
    skills_source_root = home / ".agent-hub" / "skills"
    ignore_list = config.get("ignore_list", [])
    options = config.get("options", {})

    print(f"[*] Starting Orchestration...")

    for plat_name, plat_path in config.get("platforms", {}).items():
        target_root = Path(plat_path).expanduser()
        target_root.mkdir(parents=True, exist_ok=True)

        for skill_dir in skills_source_root.iterdir():
            # ignore_list에 포함되거나 숨김 파일인 경우 건너뜀
            if skill_dir.name in ignore_list or skill_dir.name.startswith('.'):
                continue

            if skill_dir.is_dir():
                target_link = target_root / skill_dir.name
                try:
                    create_symlink(skill_dir, target_link, options)
                    print(f"  [OK] {plat_name}: {skill_dir.name} linked.")
                except Exception as e:
                    print(f"  [FAIL] {plat_name}: {skill_dir.name} - {e}")

    # Claude settings.json 업데이트 (선택 사항: 경로 등록 자동화)
    claude_config_path = home / ".claude" / "settings.json"
    if claude_config_path.exists():
        try:
            with open(claude_config_path, 'r+', encoding='utf-8') as f:
                data = json.load(f)
                target_path_str = str(Path(config["platforms"]["claude"]).expanduser())
                if data.get("customSkillsPath") != target_path_str:
                    data["customSkillsPath"] = target_path_str
                    f.seek(0)
                    json.dump(data, f, indent=2)
                    f.truncate()
                    print("[+] Claude settings.json updated.")
        except Exception as e:
            print(f"[!] Claude settings update failed: {e}")

if __name__ == "__main__":
    main()