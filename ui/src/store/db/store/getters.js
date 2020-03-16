import types from '../../types'
import { cloneDeep } from 'lodash'
export default {
  [types.db.getters.stock]: state => cloneDeep(state.stock),
}
