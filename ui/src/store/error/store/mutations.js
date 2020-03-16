import store from '../../../store'
import types from '../../types'
import {EventBus} from '../../../eventBus.js'
import router from '../../../router'
export default {
  [types.error.mutations.setAction]: (state, payload) => {
    state.runningActions.push({action: payload, page: store.state.route.name})
  },
  [types.error.mutations.removeAction]: (state, payload) => {
    state.runningActions.splice(state.runningActions.indexOf(state.runningActions.find(x => x.action === payload)), 1)
  },
  [types.error.mutations.setError]: (state, payload) => {
    console.log(payload)
    if (!payload.action) {
      let error = {error: payload}
      EventBus.$emit('openSnackbar', error)
    }
    else {
      EventBus.$emit('openSnackbar', payload)
      state.runningActions.splice(state.runningActions.indexOf(state.runningActions.find(x => x.action === payload.action)), 1)
    }
  }
}
