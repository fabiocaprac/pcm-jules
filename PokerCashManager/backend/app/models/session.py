from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid # For IDs

@dataclass
class Session:
    IDSessao: uuid.UUID
    IDCaixa: uuid.UUID
    NomeSessao: str
    DataHoraInicio: datetime = field(default_factory=datetime.utcnow)
    DataHoraFim: Optional[datetime] = None
    Status: str = "Ativa"  # "Ativa", "Finalizada"
    IDOrganizadorCriador: uuid.UUID
    IDOrganizadorFinalizador: Optional[uuid.UUID] = None
    # Implicitly contains a list of JogadoresNaSessao and Transações
