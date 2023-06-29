from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

from .entity import Entity

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FilaAtendimento(Entity):
    def __init__(self, id, pedido_id, recebido_em, finalizado_em, created_at):
        super().__init__(id, created_at)
        self.pedido_id = pedido_id
        self.recebido_em = recebido_em
        self.finalizado_em = finalizado_em
        self.created_at = created_at