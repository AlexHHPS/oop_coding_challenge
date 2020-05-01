from unittest import TestCase

from selectionsystem.selectionapp.domain.models.coordinate import Coordinate
from selectionsystem.selectionapp.domain.models.point import Point


class TestCoordinate(TestCase):
    def test_to_dict(self):
        coords = [
            {"x1": 0, "y1": 0},
            {"x1": 10, "y1": 0},
            {"x1": 0, "y1": 20},
            {"x1": 5, "y1": 40},
            {"x1": 0, "y1": 0},
            {"x1": 34, "y1": 4},
        ]

        for coord in coords:
            with self.subTest():
                data = dict(x=coord.get("x1"), y=coord.get("y1"))
                coord = Coordinate(data)
                self.assertDictEqual(
                    data,
                    coord.to_dict()
                )
