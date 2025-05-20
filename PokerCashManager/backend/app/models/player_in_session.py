from dataclasses import dataclass
import uuid # For IDs

@dataclass
class PlayerInSession:
    IDJogadorSessao: uuid.UUID
    IDSessao: uuid.UUID
    IDPerfilJogador: uuid.UUID
    NomeJogadorExibicao: str # Nome ou apelido do perfil
    TotalBuyInsSessao: float = 0.0
    TotalCashoutsSessao: float = 0.0
    TotalPagamentosSessao: float = 0.0 # Pode ser negativo
    SaldoPendenteSessao: float = 0.0 # Calculado
    SaldoAtualEmJogo: float = 0.0 # Calculado: TotalBuyInsSessao - TotalCashoutsSessao
