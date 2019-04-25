import json
import falcon
import jsend
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from falcon_autocrud.resource import CollectionResource, SingleResource

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_account'
    id = sa.Column('id', UUID(), primary_key=True)
    email = sa.Column('email', sa.String(255))
    is_admin = sa.Column('is_admin', sa.Boolean())


class UserCollectionResource(CollectionResource):
    model = User
    methods = ['GET', 'POST']
    """Users class"""
    # def on_get(self, _req, resp):
    #     """on get request
    #     return Welcome message
    #     """
    #     msg = {'message': 'Welcome'}
    #     resp.body = json.dumps(jsend.success(msg))
    #     resp.status = falcon.HTTP_200

class UserResource(SingleResource):
    model = User