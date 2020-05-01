import math
from typing import Optional

from selectionsystem.selectionapp.domain.models.coordinate import Coordinate
from selectionsystem.selectionapp.domain.models.enemy import Enemy
from selectionsystem.selectionapp.domain.models.model import Model


class Point(Model):
    coordinates: Coordinate
    enemies: Enemy
    allies: Optional[str]

    def __init__(self, data):
        self.hydrate(data)

    def hydrate(self, data):
        self.coordinates = Coordinate(data["coordinates"])
        self.enemies = Enemy(data["enemies"])
        self.allies = data.get("allies")

    @property
    def has_mech(self):
        return self.enemies.type == "mech"

    @property
    def has_allies(self):
        return self.allies is not None

    @property
    def distance_from_me(self):
        return math.sqrt(
            self.coordinates.x ** 2 + self.coordinates.y ** 2
        )
