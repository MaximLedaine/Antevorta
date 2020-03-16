const axios = require('axios')

const ApiVersion = `v1`

class scraper {
  constructor (url) {
    this.url = url
  }
  // items
  async getStats (symbol) {
    let res
    try {
      res = await axios({
        method: 'get',
        url: `${this.url}/api/${ApiVersion}/yahoo/stocks/${symbol}/stats`,
        headers: {
          'Content-Type': 'application/json',
          // 'Authorization': "Bearer " + authToken
        }
      })
      return res.data
    } catch (e) {
      throw e
    }
  }
  async getHistory (symbol) {
    let res
    try {
      res = await axios({
        method: 'get',
        url: `${this.url}/api/${ApiVersion}/yahoo/stocks/${symbol}/history`,
        headers: {
          'Content-Type': 'application/json',
          // 'Authorization': "Bearer " + authToken
        }
      })
      return res.data
    } catch (e) {
      throw e
    }
  }
  async getStatistics (symbol) {
    let res
    try {
      res = await axios({
        method: 'get',
        url: `${this.url}/api/${ApiVersion}/yahoo/stocks/${symbol}/statistics`,
        headers: {
          'Content-Type': 'application/json',
          // 'Authorization': "Bearer " + authToken
        }
      })
      return res.data
    } catch (e) {
      throw e
    }
  }
  async getCompany (symbol) {
    let res
    try {
      res = await axios({
        method: 'get',
        url: `${this.url}/api/${ApiVersion}/yahoo/stocks/${symbol}/company`,
        headers: {
          'Content-Type': 'application/json',
          // 'Authorization': "Bearer " + authToken
        }
      })
      return res.data
    } catch (e) {
      throw e
    }
  }
}

module.exports = scraper