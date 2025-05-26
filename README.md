# 🧠 CAPTCHA Mind Game

Um CAPTCHA em formato de mini-jogo lógico, feito com FastAPI e frontend visual imersivo.

## 🚀 Demonstração
![screenshot](screenshot.png)

## 🎯 Objetivo
Desafiar o usuário com enigmas mentais e proteger sua aplicação contra bots com estilo.

---

## 📦 Estrutura do projeto
```
captcha-mind-game/
├── app/
│   ├── main.py              # Entry point da aplicação
│   ├── logic.py             # Lógica dos desafios
│   ├── templates/           # HTMLs do jogo
│   └── static/              # Estilo visual
├── tests/
│   └── test_logic.py        # Testes unitários
├── requirements.txt         # Dependências
├── uvicorn.sh               # Script para rodar local
├── .gitignore               # Boas práticas
└── README.md
```

## 🛠️ Como rodar localmente
```bash
git clone https://github.com/seunome/captcha-mind-game.git
cd captcha-mind-game
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
bash uvicorn.sh
```
Acesse: [http://localhost:8000](http://localhost:8000)

## 🌐 Deploy gratuito na Render
- Crie uma conta em [https://render.com](https://render.com)
- Crie um novo web service com:
  - Build command: `pip install -r requirements.txt`
  - Start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`

## 🔐 Integração com Google reCAPTCHA (v2 ou v3)
1. Crie uma chave de site em https://www.google.com/recaptcha/admin
2. Adicione o script no HTML `captcha.html`
```html
<script src="https://www.google.com/recaptcha/api.js" async defer></script>
```
3. No botão:
```html
<button class="g-recaptcha"
        data-sitekey="SUA_CHAVE_SITE"
        data-callback='onSubmit'>Verificar</button>
```
4. No backend: valide o token reCAPTCHA com a API Google antes de aceitar a resposta.

## 🧪 Testes
```bash
pytest
```

## ✨ Inspiração
Mistura de lógica proposicional + design sci-fi + criatividade para desafiar bots e humanos.
