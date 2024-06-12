import { app } from "@azure/functions";
import { update } from "../controllers/content";



app.http('update', {
    methods: ['PUT'],
    authLevel: 'anonymous',
    handler: update,
    route: 'content'
});
