from fastapi import APIRouter
from starlette_graphene3 import GraphQLApp
from infrastructure.entry_point.graphql.schemas.schema import schema

router = APIRouter()

router.add_route("/graphql", GraphQLApp(schema=schema))