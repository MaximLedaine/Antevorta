export default {
  name: 'app-toolbar',
  components: {},
  props: [],
  data () {
    return {
      items: [
        { title: 'Dashboard', icon: 'dashboard', to:'dashboard' }
      ],
      drawer: true,
      expandOnHover: false,
      miniVariant: true,
    }
  },
  computed: {
    bg () {
      return 'https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg'
    },
  },
  mounted () {

  },
  methods: {

  }
}
