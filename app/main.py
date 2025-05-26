from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.logic import get_random_challenge, validate_choice
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def get_captcha(request: Request):
    desafio = get_random_challenge()
    return templates.TemplateResponse("captcha.html", {
        "request": request,
        "desafio": desafio["desafio"],
        "portas": desafio["portas"],
        "resposta": desafio["resposta_correta"]
    })


@app.post("/validar", response_class=HTMLResponse)
async def validar(request: Request, escolha: int = Form(...), resposta: int = Form(...)):
    sucesso = validate_choice(escolha, resposta)
    return templates.TemplateResponse("resultado.html", {
        "request": request,
        "sucesso": sucesso
    })
