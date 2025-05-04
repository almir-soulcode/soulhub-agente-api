from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Requisicao(BaseModel):
    pergunta: str
    nome: Optional[str] = "Aluno"
    nivel: Optional[str] = "auto"
    tipo: Optional[str] = "auto"
    exemplos: Optional[str] = "auto"

class Resposta(BaseModel):
    resposta: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat", response_model=Resposta)
def chat(req: Requisicao):
    markdown_responses = [
        f"# Resposta Genérica\n\nVocê perguntou: **{req.pergunta}**\n\n> \"A dúvida é o princípio da sabedoria.\" — Aristóteles",
        f"## Detalhes Técnicos\n\n- Pergunta: `{req.pergunta}`\n- Status: ✅ Respondido\n\n```python\nprint('Simulação completa!')\n```",
        f"### Resposta poética\n\n*\"Palavras lançadas ao vento digital...\"*\n\n**Pergunta:** {req.pergunta}\n\nResposta: _A brisa responde com silêncio e código._",
        f"# 🎲 Resposta aleatória\n\nVocê disse: **{req.pergunta}**\n\nAqui vai um fato curioso:\n\n- A Lua está se afastando da Terra a 3,8 cm por ano.",
        f"## Simulação com tabela\n\n| Entrada | Tipo |\n|--------|------|\n| {req.pergunta} | Pergunta |\n\n_Aguardando confirmação..._",
    ]

    response = random.choice(markdown_responses)

    return Resposta(resposta=response)