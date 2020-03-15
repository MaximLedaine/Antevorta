import types from '../../types'
import { cloneDeep } from 'lodash'
export default {
  [types.errorHandling.getters.error]: state => cloneDeep(state.error),
  [types.errorHandling.getters.runningActions]: state => action => state.runningActions.some(x => x.action === action)
}
