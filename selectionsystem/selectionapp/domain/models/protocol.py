from abc import ABC, abstractmethod

from selectionsystem.selectionapp.domain.models.point import Point


class Protocol(ABC):
    pass


class FilterProtocol(Protocol, ABC):
    restrictive: bool

    @abstractmethod
    def check_applies(self, point: Point) -> bool:
        pass


class DistanceProtocol(Protocol, ABC):
    prev_distance: int

    @abstractmethod
    def check_distance(self, point: Point) -> bool:
        pass


class ClosestEnemiesProtocol(DistanceProtocol):
    def __init__(self):
        self.prev_distance = 1000

    def check_distance(self, point: Point) -> bool:
        new_distance = point.distance_from_me()

        if new_distance < self.prev_distance:
            self.prev_distance = new_distance
            return True


class FurthestEnemiesProtocol(DistanceProtocol):
    def __init__(self):
        self.prev_distance = 0

    def check_distance(self, point: Point) -> bool:
        new_distance = point.distance_from_me()

        if new_distance > self.prev_distance:
            self.prev_distance = new_distance
            return True


class AssistAlliesProtocol(FilterProtocol):
    def __init__(self):
        self.restrictive = False

    def check_applies(self, point: Point) -> int:
        return point.has_allies


class AvoidCrossfireProtocol(FilterProtocol):
    def __init__(self):
        self.restrictive = False

    def check_applies(self, point: Point) -> int:
        return not point.has_allies


class PrioritizeMechProtocol(FilterProtocol):
    def __init__(self):
        self.restrictive = False

    def check_applies(self, point: Point) -> int:
        return point.has_mech


class AvoidMechProtocol(FilterProtocol):
    def __init__(self):
        self.restrictive = True

    def check_applies(self, point: Point) -> int:
        return not point.has_mech


