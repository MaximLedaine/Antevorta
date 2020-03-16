export default {
  actions: {
    setAction: 'actSetAction',
    removeAction: 'actRemoveAction',
    setError: 'actSetError'
  },
  mutations: {
    setAction: 'mutSetAction',
    removeAction: 'mutRemoveAction',
    setError: 'mutSetError'
  },
  getters: {
    error: 'getError',
    runningActions: 'getRunningActions'
  }
}
