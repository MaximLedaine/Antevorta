const express = require('express')
const app = express()
const { Connection } = require('./lib/connection')
Connection.connect()

const PORT = 4100

const bodyParser = require('body-parser')
const api =  require('./api')

// Parse incoming requests data
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.use((req, res, next) => {
	res.header("Access-Control-Allow-Origin", "*")
	res.header(
		"Access-Control-Allow-Headers",
		"Origin, X-Requested-With, Content-Type, Accept, Authorization"
	);
	if (req.method === "OPTIONS") {
		res.header("Access-Control-Allow-Methods", "PUT, POST, PATCH, DELETE, GET")
		return res.status(200).json({})
	}
	next()
})

// Routes which should handle requests
app.use('/', api)

app.use((req, res, next) => {
  const error = new Error("Not found")
  error.status = 404
  next(error)
})

app.use((error, req, res, next) => {
  res.status(error.status || 500);
  res.json({
    error: {
      message: error.message
    }
  })
})

app.listen(PORT, function(){
	console.log('Your node js server is running on PORT:',PORT)
})

module.exports = app
