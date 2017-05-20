from flask import request
from flask_restplus import Resource
from api.restplus import api


ns = api.namespace('am/schools', description='Operations related to schools')

@ns.route('/')
class SchoolsCollection(Resource):

    def get(self):
        """
        Returns a list of schools.
        """
        return { '100' : 'Cass Technical High School'}
