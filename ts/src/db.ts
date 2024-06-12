import * as postgres from 'postgres'
import * as schema from './schema'
import { drizzle } from 'drizzle-orm/postgres-js'
import 'dotenv/config'

if (!process.env.DATABASE_URL) {
  throw new Error('DATABASE_URL must be set')
}
const queryClient = postgres(process.env.DATABASE_URL)
export const db = drizzle(queryClient, { schema })
