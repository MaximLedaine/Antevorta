export default {
  name: 'app-toolbar',
  components: {},
  props: [],
  data () {
    return {
      routes: [
        { title: 'Dashboard', icon: 'dashboard', to:'dashboard' },
        { title: 'Query', icon: 'search', to:'query' },
        { title: 'Stocks', icon: 'attach_money', to:'stocks' },
        { title: 'Analysis', icon: 'pie_chart', to:'analysis' }
      ],
      drawer: true,
      miniVariant: true,
      loading: false,
      items: [],
      search: null,
      select: null,
      states: [
        'Alabama',
        'Alaska',
        'American Samoa',
        'Arizona',
        'Arkansas'
      ]
    }
  },
  watch: {
    search (val) {
      val && val !== this.select && this.querySelections(val)
    },
  },
  methods: {
    querySelections (v) {
      this.loading = true
      // Simulated ajax query
      setTimeout(() => {
        this.items = this.states.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loading = false
      }, 500)
    },
  },
}
