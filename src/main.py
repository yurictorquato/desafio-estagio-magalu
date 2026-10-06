import uvicorn
from fastapi import FastAPI

from configs import engine
from models import Base
from routers import router

app = FastAPI(title="API de Agendamentos")

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/agendamentos", tags=["Agendamentos"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
