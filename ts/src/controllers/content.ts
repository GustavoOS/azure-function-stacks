import { HttpRequest, HttpResponseInit, InvocationContext } from "@azure/functions"
import { eq } from "drizzle-orm"
import { ZodError, z } from "zod"
import { db } from "../db"
import { ContentTable } from "../schema"


export async function create(request: HttpRequest, context: InvocationContext): Promise<HttpResponseInit> {
    context.log(`Http function processed request for url "${request.url}"`)
    try {
        const body = await request.json()
        const input = z.object({
            title: z.string(),
            color: z.string().regex(/^#[0-9a-f]{6}$/i),
        }).parse(body)
        const [created] = await db
            .insert(ContentTable)
            .values(input)
            .returning()
        return { status: 201, body: JSON.stringify(created) }
    } catch (error) {
        context.error(error)
        return handleError(error)
    }
}

export async function read(request: HttpRequest, context: InvocationContext): Promise<HttpResponseInit> {
    context.log(`Http function processed request for url "${request.url}"`)
    try {
        const id = getId(request)
        const found = await db
            .select()
            .from(ContentTable)
            .where(eq(ContentTable.id, id))
            .limit(1)
        if (found.length === 0) {
            throw new RangeError()
        }
        return { status: 200, body: JSON.stringify(found[0]) }
    } catch (error) {
        context.error(error)
        return handleError(error)
    }
}

export async function update(request: HttpRequest, context: InvocationContext): Promise<HttpResponseInit> {
    context.log(`Http function processed request for url "${request.url}"`)
    try {
        const id = getId(request)
        const body = await request.json()
        const input = z.object({
            title: z.string(),
            color: z.string().regex(/^#[0-9a-f]{6}$/i),
        }).parse(body)
        const [updated] = await db
            .update(ContentTable)
            .set(input)
            .where(eq(ContentTable.id, id))
            .returning()

        return { status: 200, body: JSON.stringify(updated) }
    } catch (error) {
        context.error(error)
        return handleError(error)
    }
}


export async function remove(request: HttpRequest, context: InvocationContext): Promise<HttpResponseInit> {
    context.log(`Http function processed request for url "${request.url}"`)
    try {
        const id = getId(request)
        await db
            .delete(ContentTable)
            .where(eq(ContentTable.id, id))

        return { status: 200, body: "Deleted" }
    } catch (error) {
        context.error(error)
        return handleError(error)
    }
}

function getId(request: HttpRequest) {
    return z.coerce.number().int().parse(request.query.get('id'))
}

function handleError(error: unknown) {
    if (error instanceof ZodError) {
        return { status: 400, body: error.toString() }
    }
    if (error instanceof RangeError) {
        return { status: 404, body: "Not Found" }
    }
    return { status: 500, body: "Internal Server Error" }
}
