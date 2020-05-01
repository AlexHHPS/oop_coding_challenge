from selectionsystem.selectionapp.domain.factories.protocol import ProtocolFactory
from selectionsystem.selectionapp.domain.models.model import Model
from selectionsystem.selectionapp.domain.models.point import Point


class Order(Model):
    protocols: list
    points: list

    def __init__(self, data):
        self.protocols = list()
        self.points = list()
        self.hydrate(data)

    def hydrate(self, data):
        for protocol in data["protocols"]:
            self.protocols.append(ProtocolFactory().create(protocol))

        for point in data["scan"]:
            new_point = Point(point)

            if new_point.distance_from_me() <= 100:
                self.points.append(Point(point))
