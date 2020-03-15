import types from '../../types'
export default {
  [types.errorHandling.actions.setRunningAction]: (context, payload) => context.commit(types.errorHandling.mutations.setRunningAction, payload),
  [types.errorHandling.actions.removeRunningAction]: (context, payload) => context.commit(types.errorHandling.mutations.removeRunningAction, payload),
  [types.errorHandling.actions.setError]: (context, error) => context.commit(types.errorHandling.mutations.setError, error)
}
