import { pgTable, serial, varchar } from "drizzle-orm/pg-core";

export const ContentTable = pgTable("content", {
    id: serial("id").primaryKey(),
    title: varchar("title", { length: 25 }),
    color: varchar("color", { length: 7 }),
})
