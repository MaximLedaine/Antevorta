const { Client } = require('@elastic/elasticsearch')
const config = require('../db')

class Connection {
    static connect() {
        if ( this.client ) return Promise.resolve(this.client)
        this.client = new Client(config)
        return this.client
    }
}

Connection.client = null
Connection.db = null
Connection.url = config.node
Connection.options = {
    bufferMaxEntries: 0,
    reconnectTries: 5000,
    useNewUrlParser: true
}

module.exports = { Connection }