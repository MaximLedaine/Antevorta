import types from '../../types'
import { cloneDeep } from 'lodash'
export default {
  [types.db.getters.items]: state => cloneDeep(state.items),
  [types.db.getters.item]: state => cloneDeep(state.item),
  [types.db.getters.lists]: state => cloneDeep(state.lists),
  [types.db.getters.list]: state => cloneDeep(state.list),
  [types.db.getters.organization]: state => cloneDeep({
    _id: state.organization._id || "",
    name: state.organization.name || "",
    lists: state.organization.lists || []
  })
}
