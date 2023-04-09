# Standard Libraries
import logging
import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_exercise.settings")

application = get_asgi_application()

from apps.core.api import schema

subgraph_path = "/tasks/"
subgraph_prefix = "/api/graph"

graphql_app = GraphQLRouter(schema, path=subgraph_path)

fastapp = FastAPI()
fastapp.include_router(graphql_app, prefix=subgraph_prefix)

logging.basicConfig(level=logging.DEBUG)
