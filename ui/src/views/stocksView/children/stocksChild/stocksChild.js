import types from '../../../../store/types'
import {mapActions,mapGetters} from 'vuex'
export default {
  name: 'stocks-child',
  components: {},
  props: [],
  data () {
    return {

    }
  },
  computed: {
    ...mapGetters({
      stock: types.db.getters.stock
    })
  },
  mounted () {
    this.$route.meta.calls.forEach(call => {
      this.$store.dispatch(call, this.$route.params.symbol)
    })
  },
  methods: {
    ...mapActions({
      getStats: types.db.actions.getStats,
      getCompany: types.db.actions.getCompany,
      getHistory: types.db.actions.getHistory,
      getStatistics: types.db.actions.getStatistics
    })
  }
}
