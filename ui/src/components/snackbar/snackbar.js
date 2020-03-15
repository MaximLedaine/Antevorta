import { EventBus } from '../../eventBus.js'
export default {
  name: 'snackbar',
  components: {},
  props: [],
  data () {
    return {
      text: "",
      snackbar: false
    }
  },
  computed: {

  },
  mounted () {
    EventBus.$on('openSnackbar', (payload) => {
      if(payload.error) {
        // console.log(payload.error.message)
        // console.log(payload.error.name)
        this.text = payload.error.message
        this.snackbar= true
      } 
      if(payload.message) {
        this.text = payload.message
        this.snackbar = true
      }
    })
  },
  beforeDestroy () {
    EventBus.$off('openSnackbar')
  },
  methods: {

  }
}
