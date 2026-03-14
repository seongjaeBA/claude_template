# Coding Style (Python)

## Standards
- PEP 8
- Type annotations on all function signatures
- Formatter: black | Linter: ruff | Import sort: isort

## Immutability
Prefer frozen dataclasses and NamedTuple over plain dicts/classes.

```python
@dataclass(frozen=True)
class Entity:
    id: str
    name: str

class Point(NamedTuple):
    x: float
    y: float
```

## Patterns
- Protocol for duck typing (not ABC unless inheritance needed)
- Dataclass for DTOs
- Context managers for resources
- Generators for lazy iteration

## Security
- `os.environ["KEY"]` not `os.environ.get("KEY")` — fail fast on missing secrets
- Run `bandit -r src/` before commits

## Testing
- Framework: pytest
- Coverage target: 80%+
- Marks: `@pytest.mark.unit`, `@pytest.mark.integration`
