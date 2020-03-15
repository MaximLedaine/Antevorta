const express = require('express');
const api = express()

const v1 = require('./v1')

api.get('/', (req, res) => {
  res.send({
    message: 'Hello from the API',
  });
});

api.use('/v1', v1)

module.exports = api;