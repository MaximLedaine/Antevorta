export default {
  actions: {
    getStats: 'actGetStats',
    getStatistics: 'actGetStatistics',
    getCompany: 'actGetCompany',
    getHistory: 'actGetHistory'
  },
  mutations: {
    setStats:'mutSetStats',
    setStatistics:'mutSetStatistics',
    setCompany:'mutSetCompany',
    setHistory:'mutSetHistory',
  },
  getters: {
    stats: 'getStats',
    statistics: 'getStatistics',
    company: 'getCompany',
    history: 'getHistory'
  }
}
