import types from '../../types'
import router from '../../../router'
export default {
  [types.auth.actions.login]: (context) => {
    var provider = new context.rootState.firebase.auth.OAuthProvider('microsoft.com');
    context.rootState.firebase.auth().signInWithRedirect(provider)
  },
  [types.auth.actions.redirect]: (context) => {
    return context.rootState.firebase.auth().setPersistence(context.rootState.firebase.auth.Auth.Persistence.LOCAL).then(() => {
      return context.rootState.firebase.auth().getRedirectResult().then(result => {
        if(result.user) {
          result.user.getIdTokenResult().then(idTokenResult => {
            localStorage.setItem('anteverta:token', JSON.stringify(idTokenResult))
            return true
          })
        }
        if(context.rootState.firebase.auth().currentUser) router.push({path: '/'})
        return false
      })
      .catch(function(error) {
        console.log(error)
      })
    }).catch(error => {
      context.dispatch(types.errorHandling.actions.setError, error)
    })
  },
  [types.auth.actions.signOut]: (context) => {
    context.rootState.firebase.auth().signOut().then(() => {
      router.push({name: 'authView'})
    }).catch(function(error) {})
  },
  [types.auth.actions.onAuthStateChanged]: context => {
    context.rootState.firebase.auth().onAuthStateChanged(function (user) {
      let callback = null
      let metadataRef = null
      if (callback) {
        metadataRef.off('value', callback)
      }
      if (user) {
        // Check if refresh is required.
        metadataRef = context.rootState.firebase.database().ref('metadata/' + user.uid + '/refreshTime')
        callback = (snapshot) => {
          user.getIdToken(true)
        }
        // Subscribe new listener to changes on that node.
        metadataRef.on('value', callback)
        context.rootState.firebase.auth().currentUser.getIdTokenResult().then((idTokenResult) => {
          
          // Confirm the user is an Admin.
          if (idTokenResult.claims) {
            user.claims = idTokenResult.claims
          } else {
            console.log('cant acces jwt')
          }
        })
      } else {
        if (context.rootState.route.meta.requiresAuth) {
          localStorage.removeItem('anteverta:token');
          context.dispatch(types.auth.actions.signOut)
        }
      }
    })
  },
  [types.auth.actions.getAuthToken]: async (context) => {
    if (!localStorage.getItem('anteverta:token')) return null
    return JSON.parse(localStorage.getItem('anteverta:token')).token
  }
}