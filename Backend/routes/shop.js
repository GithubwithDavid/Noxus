import express from 'express';
const router = express.Router();

router.get('/', (req, res) => {
    res.send('You can shop here')
});

router.get('/mobile', (req, res) => {
    res.send('This is the shop of mobiles.')
});

export default router;