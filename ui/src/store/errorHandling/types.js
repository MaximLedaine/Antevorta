export default {
  actions: {
    setRunningAction: 'actSetRunningAction',
    removeRunningAction: 'actRemoveRunningAction',
    setError: 'actSetError'
  },
  mutations: {
    setRunningAction: 'mutSetRunningAction',
    removeRunningAction: 'mutRemoveRunningAction',
    setError: 'mutSetError'
  },
  getters: {
    error: 'getError',
    runningActions: 'getRunningActions'
  }
}
