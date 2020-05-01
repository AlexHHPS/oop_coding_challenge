from selectionsystem.selectionapp.domain.models.protocol import (
    ClosestEnemiesProtocol,
    FurthestEnemiesProtocol,
    AssistAlliesProtocol,
    AvoidCrossfireProtocol,
    PrioritizeMechProtocol,
    AvoidMechProtocol,
    Protocol
)


class ProtocolFactory:
    protocols = {
        "closest-enemies": ClosestEnemiesProtocol,
        "furthest-enemies": FurthestEnemiesProtocol,
        "assist-allies": AssistAlliesProtocol,
        "avoid-crossfire": AvoidCrossfireProtocol,
        "prioritize-mech": PrioritizeMechProtocol,
        "avoid-mech": AvoidMechProtocol
    }

    def create(self, protocol: str) -> Protocol:
        return self.protocols.get(protocol)()
