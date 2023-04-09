# Standard Libraries
import logging
from typing import Optional

import strawberry

logger = logging.getLogger(__name__)


@strawberry.type
class CoreNode:
    success: bool
    message: str
    error: Optional[str] = None
