import json
import falcon
import jsend
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from falcon_autocrud.resource import CollectionResource, SingleResource
from uuid import uuid4

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_account'
    id = sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4)
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