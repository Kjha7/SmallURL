from django.db import models
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine.management import sync_table
import base64
import hashlib


# Create your models here.
class User(DjangoCassandraModel):
    user_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    first_name = columns.Text()
    last_name = columns.Text()
    email = columns.Text()


class URLModels(DjangoCassandraModel):
    url_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    original_url = columns.Text()
    creation_date = columns.Date()
    expiration_date = columns.Date()
    user_id = columns.Text()
    hits = columns.Integer(default=0)

    def get_short_url(self):
        url_ = self.original_url
        result = base64.b64encode(hashlib.sha1(url_))
        return result

    def decode_url(self, str1):
        return base64.b64decode(str1)

