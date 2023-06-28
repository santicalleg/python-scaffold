from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return "Hello from graphene and fastapi!"

schema = Schema(query=Query)