from dataclasses import dataclass
from typing import Optional

from selectionsystem.selectionapp.domain.models.point import Point


@dataclass
class Target:
    selected_point: Optional[Point] = None
    value: int = 0
