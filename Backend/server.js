import express from "express";
import blog from './routes/blog.js';
import shop from './routes/shop.js';

const app = express();
const port = 3000;

app.use(express.static("public"));
app.use('/blog', blog)
app.use('/shop', shop)

app.get("/", (req, res) => {
    res.sendFile("index.html", { root: "./" });
});

app.get("/about", (req, res) => {
    res.send("<div>About Page</div>");
});

app.get('/api', (req, res) => {
    res.json({
        a: 1,
        b: 2,
        c: 3,
        data: [1,2,3,4,5,6,7,8,9,10]
    });
});

app.listen(port, () => {
    console.log(`Server is running on port localhost:${port}`);
});