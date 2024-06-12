import { app } from "@azure/functions";
import { create } from "../controllers/content";

app.http('create', {
    methods: ['POST'],
    authLevel: 'anonymous',
    handler: create,
    route: 'content'
});
