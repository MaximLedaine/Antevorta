// version = v1
const express = require('express')
const api = express()
const {stocks} = require(`./routes`)

api.get('/', (req, res) => {
	res.send({
		message: 'V1',
	})
})

api.use('/stocks', stocks)

module.exports = api;