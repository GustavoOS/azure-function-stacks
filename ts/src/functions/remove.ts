import { app } from "@azure/functions";
import { remove } from "../controllers/content";


app.http('remove', {
    methods: ['DELETE'],
    authLevel: 'anonymous',
    handler: remove,
    route: 'content'
});
