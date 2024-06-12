import { app } from "@azure/functions";
import { read } from "../controllers/content";


app.http('read', {
    methods: ['GET'],
    authLevel: 'anonymous',
    handler: read,
    route: 'content'
});
