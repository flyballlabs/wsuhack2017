from flask import Flask, Blueprint,request
from flask_restplus import Resource, Api, fields
from api.am.endpoints.schools import ns as schools_namespace
from api.am.business import auth_user, create_user, create_school, create_activity
from flask_cors import CORS, cross_origin
#from api.am.serializers import user
#from api.restplus import api
import settings


app = Flask(__name__)                  #  Create a Flask WSGI appliction
CORS(app)
api = Api(app,version='1.0', title='School Activity Monitor API',
          description='Provides a set of operations to track suspicious behaviour and notify the appropriate people')                         #  Create a Flask-RESTPlus API

user = api.model('User', {
    'username': fields.String(required=True, description='Usenname of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'name': fields.String(required=True, description='Name of the user'),
    'user_type': fields.Integer(required=True,description='Type of user.  The value can be 0 for student, 1 for staff, 2 for principal'),
    'grade_level': fields.Integer(required=True,min=6,description='Only required for students.  Put the grade level, which can be the values of 6-12. This means 6th grade to 12th grade'),
    'mobile': fields.String(description='Mobile Phone Number'),
    'school_id': fields.Integer(required=True,description='The unique identifier for a school'),
})

school = api.model('School',{
    'school_id': fields.String(required=True, description='School ID'),
    'name': fields.String(required=True, description='School Name'),
    'address': fields.String(required=True, description='School Address'),
    'city': fields.String(required=True, description='School City'),
    'state': fields.String(required=True, description='School State'),
    'zipcode': fields.String(required=True, description='School Zipcode'),
    'office_phone_number':fields.String(required=True, description='School Office Phone Number'),
    'district_id':fields.String(required=False, description='District the School belongs to'),
    'main_contact_id':fields.String(required=False, description='The main user attached to this school.  This user will get all notifications'),
})


activity = api.model('Activity',{
    'activity_id': fields.String(required=False, description='Activity ID'),
    'datetime': fields.String(required=True, description='Data and time the activity was reported'),
    'user_id': fields.String(required=True, description='User who reported the activity'),
    'activity_type': fields.String(required=True, description='The type of activity'),
    'description': fields.String(required=True, description='Description of the Activity'),
    'status': fields.String(required=False, description='Status of the activity: open, reviewing, valid, lockdown_triggered, lockdown_completed, closed'),
    'lockdown_triggered_by':fields.String(required=False, description='User who triggered the lockdown'),
    'lockdown_triggered_datetime':fields.String(required=False, description='The date and time the lockdown was triggered'),
})

auth = api.model('Auth', {
    'username': fields.String(required=True, description='Usenname of the user'),
    'password': fields.String(required=True, description='Password of the user'),
})

authResponse = api.model('AuthResponse', {
    'type': fields.Integer(required=True, description='The type of user: 0 for student, 1 for staff and 2 for principal'),
})


#@api.route('/hello')                   #  Create a URL route to this resource
#class HelloWorld(Resource):            #  Create a RESTful resource
#    def get(self):                     #  Create GET endpoint
#        return {'School Suspicious Activity Monitor': 'API'}

@api.route('/auth')
class Auth(Resource):
    @api.expect(auth)
    @api.response(201, 'User was authenticated.', authResponse)
    def post(self):
        """Authenticates a user."""
        auth_user(request.json)
        return '{type: 0}', 201


@api.route('/users')
class UsersCollection(Resource):
    def get(self):
        """Returns a list of users. Users can be a techer, student, principal, staff, parent"""
        return {'name':'Mack'}
    
    @api.expect(user)
    @api.response(201, 'User successfully created.')
    def post(self):
        """Creates a new user."""
        create_user(request.json)
        return None, 201

@api.route('/schools')
class SchoolsCollection(Resource):
    def get(self):
        """Returns a list of Schools"""
        return {'name':'Cass Tech'}

    @api.expect(school)
    @api.response(201, 'Schools successfully created.')
    def post(self):
        """Creates a new School."""
        create_school(request.json)
        return None, 201

@api.route('/activity')
class ActvityCollection(Resource):
    def get(self):
        """Returns a list of Suspicious Activities"""
        return {'name':'Cass Tech'}

    @api.expect(activity)
    @api.response(201, 'Activity successfully created.')
    def post(self):
        """Creates a new Activity"""
        create_activity(request.json)
        return None, 201



def configure_app(flask_app):
    #flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    #flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    #flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    #flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    #flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    #blueprint = Blueprint('api', __name__, url_prefix='/api')
    #api.init_app(blueprint)
    #api.add_namespace(schools_namespace)
    #flask_app.register_blueprint(blueprint)

    #db.init_app(flask_app)



def main():
    initialize_app(app)
    context = ('./certs/cert.pem', './certs/key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context, debug=True)                #  Start a development server


if  __name__ == '__main__':
    main()
