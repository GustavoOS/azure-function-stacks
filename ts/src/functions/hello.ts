import { app } from "@azure/functions";
import { hello } from "../controllers/hello";



app.http('hello', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    handler: hello
});
