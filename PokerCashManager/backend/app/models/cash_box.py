from dataclasses import dataclass
from typing import Optional
import uuid # For IDCaixa

@dataclass
class CashBox:
    IDCaixa: uuid.UUID
    NomeCaixa: str
    IDSessaoAtiva: Optional[uuid.UUID] # Assuming Session ID is UUID
    IDOrganizador: uuid.UUID # Assuming Organizer ID is UUID
