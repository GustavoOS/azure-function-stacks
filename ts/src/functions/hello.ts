import { app } from "@azure/functions";
import { hello } from "../controllers/hello";



app.http('hello', {
    methods: ['GET'],
    authLevel: 'anonymous',
    handler: hello
});
