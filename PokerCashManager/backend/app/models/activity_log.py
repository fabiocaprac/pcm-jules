from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid # For IDs

@dataclass
class ActivityLog:
    IDLog: uuid.UUID
    DataHoraEvento: datetime = field(default_factory=datetime.utcnow)
    TipoEvento: str # "CriacaoSessao", "AddJogador", "RegistroBuyIn", etc.
    Descricao: str # Detalhado
    IDOrganizadorResponsavel: uuid.UUID
    IDSessao: Optional[uuid.UUID] = None
    IDTransacao: Optional[uuid.UUID] = None
    IDJogadorSessao: Optional[uuid.UUID] = None # Referencia ao JogadorNaSessao
    NomeJogadorLog: Optional[str] = None # Para manter referencia caso jogador seja excluido
    ValorLog: Optional[float] = None
    DetalhesAdicionais: Optional[str] = None # Formato livre ou estruturado
