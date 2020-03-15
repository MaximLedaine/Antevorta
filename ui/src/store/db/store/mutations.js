import store from '../../../store'
import types from '../../types'
export default {
  [types.db.mutations.setItems]: (state, payload) => {
    state.items = payload
  },
  [types.db.mutations.setItem]: (state, payload) => {
    state.item = payload
  },
  [types.db.mutations.setLists]: (state, payload) => {
    state.lists = payload
  },
  [types.db.mutations.setList]: (state, payload) => {
    state.list = payload
  },
  [types.db.mutations.setOrganization]: (state, payload) => {
    state.organization = payload
  }
}
