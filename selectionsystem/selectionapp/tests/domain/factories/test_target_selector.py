from unittest import TestCase

from selectionsystem.selectionapp.domain.factories.protocol import ProtocolFactory
from selectionsystem.selectionapp.domain.models.protocol import ClosestEnemiesProtocol, AssistAlliesProtocol


class ProtocolFactoryTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = ProtocolFactory()

    def test_create_valid(self):
        self.assertIsInstance(
            self.factory.create("closest-enemies"),
            ClosestEnemiesProtocol
        )

    def test_create_invalid(self):
        self.assertNotIsInstance(
            self.factory.create("closest-enemies"),
            AssistAlliesProtocol
        )

