import store from '../../../store'
import types from '../../types'
export default {
  [types.db.mutations.setStats]: (state, payload) => {
    state.stock.stats = payload
  },
  [types.db.mutations.setStatistics]: (state, payload) => {
    state.stock.statistics = payload
  },
  [types.db.mutations.setCompany]: (state, payload) => {
    state.stock.company = payload
  },
  [types.db.mutations.setHistory]: (state, payload) => {
    state.stock.history = payload
  }
}
