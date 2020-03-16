import types from '../../types'
import axios from 'axios'
const url = "http://localhost:9081"
import {scraper} from '../../../services/client'
const scraperClient = new scraper(url)
export default {
  [types.db.actions.getStats]: async (context, symbol) => {
    try {
      context.commit(types.error.mutations.setAction, types.db.actions.getStats)
      context.commit(types.db.mutations.setStats, {})
      let res = await scraperClient.getStats(symbol)
      context.commit(types.db.mutations.setStats, res.data)
      context.commit(types.error.mutations.removeAction, types.db.actions.getStats)
    } catch (e) {
      context.dispatch(types.error.actions.setError, {error: e, action: types.db.actions.getStats})
    }
  },
  [types.db.actions.getStatistics]: async (context, symbol) => {
    try {
      context.commit(types.error.mutations.setAction, types.db.actions.getStatistics)
      context.commit(types.db.mutations.setStatistics, {})
      let res = await scraperClient.getStatistics(symbol)
      context.commit(types.db.mutations.setStatistics, res.data)
      context.commit(types.error.mutations.removeAction, types.db.actions.getStatistics)
    } catch (e) {
      context.dispatch(types.error.actions.setError, {error: e, action: types.db.actions.getStatistics})
    }
  },
  [types.db.actions.getCompany]: async (context, symbol) => {
    try {
      context.commit(types.error.mutations.setAction, types.db.actions.getCompany)
      context.commit(types.db.mutations.setCompany, {})
      let res = await scraperClient.getCompany(symbol)
      context.commit(types.db.mutations.setCompany, res.data)
      context.commit(types.error.mutations.removeAction, types.db.actions.getCompany)
    } catch (e) {
      context.dispatch(types.error.actions.setError, {error: e, action: types.db.actions.getCompany})
    }
  },
  [types.db.actions.getHistory]: async (context, symbol) => {
    try {
      context.commit(types.error.mutations.setAction, types.db.actions.getHistory)
      context.commit(types.db.mutations.setHistory, {})
      let res = await scraperClient.getHistory(symbol)
      context.commit(types.db.mutations.setHistory, res.data)
      context.commit(types.error.mutations.removeAction, types.db.actions.getHistory)
    } catch (e) {
      context.dispatch(types.error.actions.setError, {error: e, action: types.db.actions.getHistory})
    }
  },
}

