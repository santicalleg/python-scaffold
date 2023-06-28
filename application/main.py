# from infrastructure.entry_point.api import app as api
from infrastructure.entry_point.graphql import app as api

app = api.create_app()