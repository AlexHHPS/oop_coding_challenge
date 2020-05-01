from typing import Optional

from selectionsystem.selectionapp.domain.models.order import Order
from selectionsystem.selectionapp.domain.models.protocol import FilterProtocol, DistanceProtocol
from selectionsystem.selectionapp.domain.models.target import Target


class SelectTargetService:
    def __init__(self, order: Order):
        self.order = order
        self.target = Target(
            None,
            0
        )

    def obtain_best_target_coordinates(self):
        restrictive_protocols, filter_protocols, distance_protocol = self.__split_protocols()
        battlefield = self.order.points

        for battle_position in battlefield:
            for protocol in restrictive_protocols:
                if not protocol.check_applies(battle_position):
                    break

            value = self.__calculate_value_filters(battle_position, filter_protocols)
            if value > self.target.value:
                self.target = Target(
                    battle_position,
                    value
                )

            if value == self.target.value:
                if distance_protocol is not None:
                    if distance_protocol.check_distance(battle_position):
                        self.target = Target(
                            battle_position,
                            value
                        )

        if self.target.selected_point is None:
            return battlefield[0].coordinates

        return self.target.selected_point.coordinates

    def __calculate_value_filters(self, battle_position, filter_protocols):
        value = 0

        for filter_protocol in filter_protocols:
            if filter_protocol.check_applies(battle_position):
                value += 1

        return value

    def __split_protocols(self):
        restrictive_protocols = list()
        filter_protocols = list()
        distance_protocol: Optional[DistanceProtocol] = None

        for protocol in self.order.protocols:
            if isinstance(protocol, FilterProtocol):
                if protocol.restrictive:
                    restrictive_protocols.append(protocol)
                    break

                filter_protocols.append(protocol)

            distance_protocol = protocol

        return restrictive_protocols, filter_protocols, distance_protocol
