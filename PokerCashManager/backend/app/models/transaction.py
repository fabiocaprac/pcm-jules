from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid # For IDs

@dataclass
class Transaction:
    IDTransacao: uuid.UUID
    IDSessao: uuid.UUID
    IDJogadorSessao: uuid.UUID # Referencia JogadorNaSessao
    TipoTransacao: str # "BuyIn", "Cashout", "Pagamento"
    Valor: float
    MetodoPagamento: str # "Dinheiro", "PIX", "CartaoCredito", "CartaoDebito", "Nenhum/Pendente"
    StatusPagamento: str # "Pago", "Pendente"
    DataHoraTransacao: datetime = field(default_factory=datetime.utcnow)
    IDOrganizadorExecutor: uuid.UUID
    # DirecaoPagamento is only relevant for "Pagamento" type.
    # For simplicity in the dataclass, this can be handled by logic or a separate field.
    # Adding it here for completeness as per document.
    DirecaoPagamento: Optional[str] = None # "EntradaCaixa", "SaidaCaixa"
