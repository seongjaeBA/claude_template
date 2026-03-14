# Boilerplate Patterns

## Drizzle ORM Setup

```typescript
// src/server/db/schema.ts
import { pgTable, text, timestamp, uuid } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: uuid("id").primaryKey().defaultRandom(),
  email: text("email").notNull().unique(),
  name: text("name"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

// src/server/db/index.ts
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import { env } from "~/env";
import * as schema from "./schema";

const client = postgres(env.DATABASE_URL);
export const db = drizzle(client, { schema });
```

## tRPC Router Scaffold

```typescript
// src/server/routers/example.ts
import { z } from "zod";
import { createTRPCRouter, protectedProcedure } from "../trpc";

export const exampleRouter = createTRPCRouter({
  list: protectedProcedure.query(async ({ ctx }) => {
    return ctx.db.query.examples.findMany();
  }),
  create: protectedProcedure
    .input(z.object({ name: z.string().min(1) }))
    .mutation(async ({ ctx, input }) => {
      return ctx.db.insert(examples).values(input).returning();
    }),
});
```

## t3-env Schema
See `.claude/docs/env-validation.md` for full schema.

## Sentry + LogTape Init
See `.claude/docs/observability.md` for setup instructions.
