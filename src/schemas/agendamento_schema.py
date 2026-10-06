from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from enums import CanalComunicacao, Status


class AgendamentoCreate(BaseModel):
    destinatario: str
    mensagem: str
    data_envio: datetime
    canal_comunicacao: CanalComunicacao


class AgendamentoOut(BaseModel):
    id: UUID
    destinatario: str
    mensagem: str
    data_envio: datetime
    canal_comunicacao: CanalComunicacao
    status: Status

    model_config = ConfigDict(from_attributes=True)