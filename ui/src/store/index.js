import Vue from 'vue'
import Vuex from 'vuex'
import modules from './modules.js'
Vue.use(Vuex)

// const firebase = require('firebase/app')
// // Required for side-effects
// require('firebase/auth')
// require('firebase/database')

// const firebaseapp = firebase.initializeApp({

// })

const state = {
  // firebase: firebase,
}

const getters = {
  // firebase: state => state.firebase
}

const store = new Vuex.Store({
  state,
  getters,
  modules,
  strict: false
})

// store.watch((state, getters) => getters[types.firestoreAuth.getters.currentUser], (newValue, oldValue) => {
//   // if (oldValue !== newValue) console.log(newValue) // store.dispatch()
// })

export default store
