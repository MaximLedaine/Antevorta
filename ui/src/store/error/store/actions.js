import types from '../../types'
export default {
  [types.error.actions.setAction]: (context, payload) => context.commit(types.error.mutations.setAction, payload),
  [types.error.actions.removeAction]: (context, payload) => context.commit(types.error.mutations.removeAction, payload),
  [types.error.actions.setError]: (context, error) => context.commit(types.error.mutations.setError, error)
}
