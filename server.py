from htpy import html, head, meta, body, h1, p, h2
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, HTTPException

TOPIC =" Управление складом (WMS-lite)"
app = FastAPI()
@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    accept = request.headers.get("accept", "")
    if "text/html" not in accept:
        raise HTTPException(
            status_code=406,
            detail='Нужен заголовок Accept с "text/html"'
        )

    else: 
        html_text=html[
        head[
            meta(charset="utf-8"),
            ],
        body[
            h1["Тема:"],
            h2[TOPIC],
            p["ляляляляляля"],
            ],
                    ] 
        return HTMLResponse(content="<!doctype html>\n" + str(html_text))
