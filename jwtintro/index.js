const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();

app.get('/', (req, res) => {
    console.log('test');

    let token = jwt.sign({
        'username': 'pikachu'
    }, 'sehrgeheim', {
        algorithm: 'HS256',
        expiresIn: '40m'
    });

    res.setHeader('Authorization', token);
    console.log(token);
    res.send('<html><h1> Success</h1><form></form></html>', 200);
});

app.listen(12345, () => {
    console.log('server started');
});

app.post('/test', (req, res) => {
    let token = req.get('Authorization');

    console.log(token);
    console.log(jwt.verify(token, 'sehrgeheim', { algorithms: ['H256'] }));
});