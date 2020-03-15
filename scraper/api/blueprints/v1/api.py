from flask import Blueprint
from flask_restful import Api
from .resources.statistics import Statistics, StatisticsList
from .resources.stats import Stats, StatsList
from .resources.company import Company, CompanyList
from .resources.history import History, HistoryList

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(StatsList, '/yahoo/stocks/market/stats')
api.add_resource(Stats, '/yahoo/stocks/<string:symbol>/stats')

api.add_resource(StatisticsList, '/yahoo/stocks/market/statistics')
api.add_resource(Statistics, '/yahoo/stocks/<string:symbol>/statistics')

api.add_resource(CompanyList, '/yahoo/stocks/market/company')
api.add_resource(Company, '/yahoo/stocks/<string:symbol>/company')

api.add_resource(HistoryList, '/yahoo/stocks/market/history')
api.add_resource(History, '/yahoo/stocks/<string:symbol>/history')

