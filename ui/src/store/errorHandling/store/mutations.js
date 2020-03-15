import store from '../../../store'
import types from '../../types'
import {EventBus} from '../../../eventBus.js'
import router from '../../../router'
export default {
  [types.errorHandling.mutations.setRunningAction]: (state, payload) => {
    state.runningActions.push({action: payload, page: store.state.route.name})
  },
  [types.errorHandling.mutations.removeRunningAction]: (state, payload) => {
    state.runningActions.splice(state.runningActions.indexOf(state.runningActions.find(x => x.action === payload)), 1)
  },
  [types.errorHandling.mutations.setError]: (state, payload) => {
    if (payload.error && payload.error.response.status == 403) {
      location.assign(location.origin + '/#/')
    }
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
