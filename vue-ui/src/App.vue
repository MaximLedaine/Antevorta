<template>
  <v-app>
    <AppToolbar></AppToolbar>
    <v-content>      
      <keep-alive>
       <router-view/>
      </keep-alive>
    </v-content>
  </v-app>
</template>

<script>
import appToolbar from './components/appToolbar'
export default {
  components: {
    AppToolbar: appToolbar
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
