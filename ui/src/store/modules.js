const files = require.context('./', true, /store$/)
var modules = {}

files.keys().forEach(key => {
  if (key === './types.js') return
  modules[key.replace(/(\.\/|\/store)/g, '')] = files(key).default
})

export default modules
