import datetime
from peewee import *

database_proxy = Proxy()

class BaseModel(Model):
  class Meta:
    database = database_proxy


class User(BaseModel):
  name = CharField(null=False, max_length=255)
  email = CharField(null=False, default='')
  username = CharField(null=False)
  joined_at = DateField(default=datetime.datetime.now)
  somone_joined_at = CharField(default='')

  class Meta:
    db_table = 'users'


class Tweet(BaseModel):
  text = CharField()
  user = ForeignKeyField(User, to_field=User.id, db_column="user_id", null=True)

  class Meta:
    db_table = 'tweet'


class UserMeta(BaseModel):
  user = ForeignKeyField(User, to_field=User.id, db_column="user_id", null=True)
  avatar_url = CharField(default='')

def create_tables():
  User.create_table(True)
  Tweet.create_table(True)
