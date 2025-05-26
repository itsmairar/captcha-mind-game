from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.logic import get_random_challenge, validate_choice
import time

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def escolher_modo(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})


@app.get("/jogo", response_class=HTMLResponse)
def get_captcha(request: Request, mode: str = Query("easy")):
    if mode not in ("easy", "hard"):
        return RedirectResponse(url="/", status_code=302)

    desafio = get_random_challenge(dificuldade=mode)
    return templates.TemplateResponse("captcha.html", {
        "request": request,
        "desafio": desafio["desafio"],
        "portas": desafio["portas"],
        "resposta": desafio["resposta_correta"]
    })


@app.post("/validar", response_class=HTMLResponse)
async def validar(
    request: Request,
    escolha: int = Form(...),
    resposta: int = Form(...),
    criado_em: float = Form(...)
):
    tempo_limite = 40
    tempo_agora = time.time()
    expirado = tempo_agora - criado_em > tempo_limite

    if expirado:
        return templates.TemplateResponse("resultado.html", {
            "request": request,
            "sucesso": False,
            "mensagem": "Tempo esgotado para responder."
        })

    sucesso = validate_choice(escolha, resposta)
    return templates.TemplateResponse("resultado.html", {
        "request": request,
        "sucesso": sucesso
    })
