from dataclasses import dataclass, field
from typing import Optional
import uuid # For IDs

@dataclass
class PlayerProfile:
    IDPerfilJogador: uuid.UUID
    NomeCompleto: str
    IDOrganizador: uuid.UUID # Who registered this profile
    Apelido: Optional[str] = None
    ContatoWhatsApp: Optional[str] = None
    ChavePIX: Optional[str] = None
    LimiteCredito: float = 0.0
    SaldoGlobalAcumulado: float = 0.0 # Calculated
