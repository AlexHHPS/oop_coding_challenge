from unittest import mock, TestCase
from unittest.mock import MagicMock

from selectionsystem.selectionapp.domain.models.protocol import DistanceProtocol, FilterProtocol
from selectionsystem.selectionapp.domain.services.target_selector import SelectTargetService


class SelectTargetServiceTestCase(TestCase):
    def test_obtain_best_target_coordinates_with_no_entries(self):
        self.service = SelectTargetService(
            MagicMock(
                points=[]
            )
        )

        with self.assertRaises(IndexError):
            self.service.obtain_best_target_coordinates()

    def test_obtain_best_target_coordinates_with_distance_protocol(self):
        protocol = MagicMock(
            **{"check_distance.return_value": True},
            spec=DistanceProtocol
        )
        point1 = MagicMock(
            coordinates=(20, 10)
        )
        point2 = MagicMock(
            coordinates=(4, 3)
        )
        self.service = SelectTargetService(
            MagicMock(
                protocols=[protocol],
                points=[point1, point2]
            )
        )

        self.assertEqual(
            (4, 3),
            self.service.obtain_best_target_coordinates()
        )
        self.assertEqual(protocol.check_distance.call_count, 2)

    def test_obtain_best_target_coordinates_with_no_distance_protocol(self):
        protocol = MagicMock(
            restrictive=False,
            spec=FilterProtocol
        )
        point1 = MagicMock(
            coordinates=(10, 10)
        )
        point2 = MagicMock(
            coordinates=(4, 3)
        )
        self.service = SelectTargetService(
            MagicMock(
                protocols=[protocol],
                points=[point1, point2]
            )
        )

        self.assertEqual(
            (10, 10),
            self.service.obtain_best_target_coordinates()
        )
