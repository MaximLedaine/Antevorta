const MongoClient = require('mongodb').MongoClient
const config = require('../db')

class Connection {
    static connectToMongo() {
        if ( this.db ) return Promise.resolve(this.db)
        return MongoClient.connect(this.url, this.options)
            .then(client => this.db = client.db('test'))
    }
}

Connection.client = null
Connection.db = null
Connection.url = config.DB
Connection.options = {
    bufferMaxEntries: 0,
    reconnectTries: 5000,
    useNewUrlParser: true
}

module.exports = { Connection }