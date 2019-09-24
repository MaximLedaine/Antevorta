const { Connection } = require('../../../lib/connection')
const collection = 'statistics'

exports.get_all = async (req, res, next) => {
	try {
		var docs = await Connection.db.collection(collection).find({}).toArray()
		res.send(docs)
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.create = async (req, res, next) => {
	try {
		let result = await Connection.db.collection(collection).replaceOne(
    {
      _id: req.params.id
    }, {
			_id: req.params.id,
			...req.body
		}, { 
      upsert: true 
    })
		res.send(result)
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.get = async (req, res, next) => {
	try {
		let result = await Connection.db.collection(collection).findOne({
			_id: req.params.id
		})
		res.send(result)
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.update = async (req, res, next) => {
	try {
		let result = await Connection.db.collection(collection).updateOne({
			_id: req.params.id,
			...req.body
		})
		res.send(result)
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.delete = async (req, res, next) => {
	try {
		let result = await Connection.db.collection(collection).deleteOne({
			_id: req.params.id
		})
		res.send(result)
	} catch (e) {
		res.status(500).send(e)
	}
}