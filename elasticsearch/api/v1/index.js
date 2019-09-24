// version = v1
const express = require('express')
const api = express()
const {company, stats, statistics} = require(`./routes`)

api.get('/', (req, res) => {
	res.send({
		message: 'V1',
	})
})

api.use('/company', company)
api.use('/stats', stats)
api.use('/statistics', statistics)

module.exports = api;