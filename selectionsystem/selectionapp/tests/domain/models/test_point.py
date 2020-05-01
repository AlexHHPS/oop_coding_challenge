from unittest import TestCase

from selectionsystem.selectionapp.domain.models.point import Point


class TestPoint(TestCase):
    def test_distance_from_me(self):
        scenarios = [
            {"x1": 0, "y1": 0, "distance": 0},
            {"x1": 10, "y1": 0, "distance": 10},
            {"x1": 0, "y1": 20, "distance": 20},
            {"x1": 5, "y1": 40, "distance": 40.311288741492746},
            {"x1": 0, "y1": 0, "distance": 0},
            {"x1": 34, "y1": 4, "distance": 34.23448553724738},
        ]

        for scenario in scenarios:
            with self.subTest():
                point = Point(dict(
                    coordinates=dict(x=scenario.get("x1"), y=scenario.get("y1")),
                    enemies=dict(type="soldier", number=10)
                ))
                self.assertEqual(scenario.get("distance"), point.distance_from_me())