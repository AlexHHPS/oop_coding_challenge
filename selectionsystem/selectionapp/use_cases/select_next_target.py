from selectionsystem.selectionapp.domain.models.order import Order
from selectionsystem.selectionapp.domain.services.target_selector import SelectTargetService
from selectionsystem.selectionapp.interfaces import Command


class SelectNextTargetUseCase(Command):
    def __init__(self, data: dict):
        self.order = Order(data)

    def execute(self):
        targeting_service = SelectTargetService(self.order)
        return targeting_service.obtain_best_target_coordinates()
