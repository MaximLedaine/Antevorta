export default {
  actions: {
    getItems: 'actGetItems',
    createItem: 'actCreateItem',
    getItem: 'actionGetItem',
    itemIdAvailable: 'actItemIdAvailable',
    updateItem: 'actionUpdateItem',
    deleteItem: 'actionDeleteItem',
    getLists: 'actGetLists',
    getList: 'actGetList',
    updateListSettings: 'actUpdateListSettings',
    getOrganization: 'actGetOrganization'
  },
  mutations: {
    setItems: 'mutSetItems',
    setItem: 'mutSetItem',
    setLists: 'mutSetLists',
    setList: 'mutSetList',
    setOrganization: 'mutSetOrganization'
  },
  getters: {
    items: 'getItems',
    item: 'getItem',
    lists: 'getLists',
    list: 'getList',
    organization: 'getOrganization'
  }
}
