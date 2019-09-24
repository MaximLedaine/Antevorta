const { Connection } = require('../../../lib/connection')
const client = Connection.client
const index = 'company'

exports.get_all = async (req, res, next) => {
	try {
		let query = {
		
    }
		let results = await client.search({
			index: index,
			size: 50,
			body: {
				query
			}
		})
    res.json(results)
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.get = async (req, res, next) => {
	try {
		let query = {
			"terms": {
				"_id": [req.params.id]
			}
		}
    let results = await client.search({
			index: index,
			size: 15,
			body: {
				query
			}
		})
    res.json(results)
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.create = async (req, res, next) => {
	try {
		await client.update({
			index: index,
			type: '_doc',
			id: req.params.id,
			body: {
				doc: req.body,
				doc_as_upsert: true
			}
		})
		res.status(200).json({message:"succes"})
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.update = async (req, res, next) => {
	try {
		await client.update({
			index: index,
			type: '_doc',
			id: req.params.id,
			body: req.body
		})
		res.status(200).json({message:"succes"})
	} catch (e) {
		res.status(500).send(e)
	}
}

exports.delete = async (req, res, next) => {
	try {
		await client.delete({
			index: index,
			type: '_doc',
			id: req.params.id
		})
		res.status(200).json({message:"succes"})
	} catch (e) {
		res.status(500).send(e)
	}
}

function getFilters (filters) {
  let filterArray = []
  Object.keys(filters).forEach(x => {
    let term = {}
    term[x + '.keyword'] = filters[x]
    filterArray.push({term: term})
  })
  return filterArray
}
