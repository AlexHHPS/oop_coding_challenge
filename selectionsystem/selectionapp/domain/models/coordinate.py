from selectionsystem.selectionapp.domain.models.model import Model
import json


class Coordinate(Model):
    x: int
    y: int

    def __init__(self, data):
        self.hydrate(data)

    def hydrate(self, data):
        self.x = data["x"]
        self.y = data["y"]

    def to_json(self):
        return dict(x=self.x, y=self.y)
