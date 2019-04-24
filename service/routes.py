from .resources.welcome import Welcome
from .resources import users

def addRoutes(falcon_api, db_engine):
    falcon_api.add_route('/welcome', Welcome())
    falcon_api.add_route('/users', users.UserCollectionResource(db_engine))
    falcon_api.add_route('/users/{id}', users.UserResource(db_engine))