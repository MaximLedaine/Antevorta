import types from '../../types'
import { cloneDeep } from 'lodash'
export default {
  [types.error.getters.error]: state => cloneDeep(state.error),
  [types.error.getters.runningActions]: state => action => state.runningActions.some(x => x.action === action)
}
