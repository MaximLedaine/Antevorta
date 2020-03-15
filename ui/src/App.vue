<template>
  <v-app>
    <snackbar/>
    <AppToolbar></AppToolbar>
    <v-content>      
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import appToolbar from './components/appToolbar'
import snackbar from './components/snackbar'
export default {
  components: {
    AppToolbar: appToolbar,
    Snackbar: snackbar
  },
  name: 'App',
  data () {
    return {
      //
    }
  }
}
</script>

<style lang="scss">
  @import './main.scss';
</style>
