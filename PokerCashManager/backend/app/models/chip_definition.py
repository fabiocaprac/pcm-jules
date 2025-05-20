from dataclasses import dataclass
from typing import Optional
import uuid # For IDs

@dataclass
class ChipDefinition:
    IDFicha: uuid.UUID
    IDSessao: uuid.UUID # Part of Fichario da Sessao
    ValorUnitario: float
    Cor: Optional[str] = None
    QuantidadeInicial: int = 0
    QuantidadeAtual: Optional[int] = None # Pode ser gerenciado ou apenas usado para cálculo
