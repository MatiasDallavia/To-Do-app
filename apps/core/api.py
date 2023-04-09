# Standard Libraries
from typing import Optional

import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry.tools import merge_types

from apps.core.schema.queries.tasks import TasksMutation, TasksQuery

queries = merge_types(
    "Queries",
    (TasksQuery,),
)

mutations = merge_types(
    "Mutations",
    (TasksMutation,),
)


class RootQuery(queries):
    _service: Optional[str]


class RootMutation(mutations):
    _service: Optional[str]


schema = strawberry.federation.Schema(
    query=RootQuery,
    mutation=RootMutation,
    config=StrawberryConfig(auto_camel_case=False),
)
