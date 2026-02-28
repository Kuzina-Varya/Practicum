from htpy import html, head, meta, body, h1, h2, p, button, script
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

TOPIC = "Управление складом (WMS-lite)"
app = FastAPI()
app.mount("/static", StaticFiles(directory="client/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    page = html[
        head[
            meta(charset="utf-8"),
        ],
        body[
            h1[f"Была выбрана тема {TOPIC}"],
            h2(id="status"),            
            p(id="msg"),                
            button(id="btn", disabled=True)["Классная тема!"],
            script[f'window.WS_URL = "ws://127.0.0.1:8002/ws";'],#кладем адрес в переменную
            script(src="/static/app.js")  
        ],
    ]
    return HTMLResponse(content="<!doctype html>\n" + str(page))