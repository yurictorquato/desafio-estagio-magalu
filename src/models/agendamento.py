import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Enum, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from enums import CanalComunicacao, Status


class Base(DeclarativeBase):
    pass


class Agendamento(Base):
    __tablename__ = "agendamento"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    destinatario: Mapped[str] = mapped_column(String(100), nullable=False)
    mensagem: Mapped[str] = mapped_column(String(500), nullable=False)
    data_envio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    canal_comunicacao: Mapped[CanalComunicacao] = mapped_column(Enum(CanalComunicacao), nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False, default=Status.AGENDADO)
