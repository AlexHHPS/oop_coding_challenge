from selectionsystem.selectionapp.domain.models.model import Model


class Enemy(Model):
    type: str
    number: int

    def __init__(self, data):
        self.hydrate(data)

    def hydrate(self, data):
        self.type = data["type"]
        self.number = data["number"]
