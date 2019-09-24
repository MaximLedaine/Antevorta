from flask import Blueprint
from flask_restful import Api
from .resources.statistics import Statistics, StatisticsList
from .resources.stats import Stats, StatsList
from .resources.company import Company, CompanyList

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(StatsList, '/yahoo/stats')
api.add_resource(Stats, '/yahoo/stats/<string:symbol>')

api.add_resource(StatisticsList, '/yahoo/statistics')
api.add_resource(Statistics, '/yahoo/statistics/<string:symbol>')

api.add_resource(CompanyList, '/yahoo/company')
api.add_resource(Company, '/yahoo/company/<string:symbol>')

