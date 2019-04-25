from .resources.welcome import Welcome
from .resources import user

def addRoutes(falcon_api, db_engine):
    falcon_api.add_route('/welcome', Welcome())
    falcon_api.add_route('/users', user.UserCollectionResource(db_engine))
    falcon_api.add_route('/users/{id}', user.UserResource(db_engine))