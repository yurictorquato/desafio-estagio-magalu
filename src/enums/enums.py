from enum import StrEnum, auto


class CanalComunicacao(StrEnum):
    EMAIL = auto()
    SMS = auto()
    PUSH = auto()
    WHATSAPP = auto()


class Status(StrEnum):
    AGENDADO = auto()
    ENVIADO = auto()
    ERRO = auto()
    CANCELADO = auto()
