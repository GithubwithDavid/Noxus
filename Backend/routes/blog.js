import express from "express";
const router = express.Router();

router.get('/', (req, res) => {
    res.send("Blog Page");
});

router.get('/about', (req, res) => {
    res.send("About Blog Page");
});

export default router;