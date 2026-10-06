from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from configs.database import obter_secao
from models import Agendamento
from schemas import AgendamentoCreate, AgendamentoOut

router = APIRouter()


@router.post(path="", summary="Cria um novo agendamento.", status_code=status.HTTP_201_CREATED,
             response_model=AgendamentoOut)
def criar_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(obter_secao)):
    dados = Agendamento(**agendamento.model_dump())

    db.add(dados)
    db.commit()
    db.refresh(dados)

    return dados


@router.get(path="", summary="Consulta todos os agendamentos existentes.", status_code=status.HTTP_200_OK,
            response_model=list[AgendamentoOut])
def listar_agendamentos(db: Session = Depends(obter_secao)) -> list[AgendamentoOut]:
    return db.execute(select(Agendamento)).scalars().all()


@router.get(path="/{id_agendamento}", summary="Consulta um agendamento existente pelo ID.",
            status_code=status.HTTP_200_OK,
            response_model=AgendamentoOut)
def obter_agendamento_pelo_id(id_agendamento: UUID, db: Session = Depends(obter_secao)) -> AgendamentoOut:
    resultado = db.get(Agendamento, id_agendamento)

    if not resultado:
        raise HTTPException(status_code=404, detail=f"Agendamento com ID {id_agendamento} não encontrado.")

    return resultado
