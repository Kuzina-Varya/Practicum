import asyncio      
import random       
from fastapi import FastAPI, WebSocket  
from starlette.websockets import WebSocketDisconnect  

app = FastAPI()
@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
    except Exception as e:
         print(f"Рукопожатие не удалось:{e}") 
         return 

    sender_task = asyncio.create_task(sender_loop(websocket))
    try:
        await receiver_loop(websocket)
    except WebSocketDisconnect:
        pass
    finally:
        sender_task.cancel()
        try:
            await sender_task
        except asyncio.CancelledError:
            pass
            
            
async def sender_loop(websocket: WebSocket):
    while True:
        try:
            await asyncio.sleep(random.uniform(2,5))

            if (random.random() < 0.65):
                await websocket.send_text("Это лучшая тема, что есть. Хотя…")
            else:
                await websocket.send_text("Надо менять тему…")
        except WebSocketDisconnect:
            break


async def receiver_loop(websocket: WebSocket):
    seen = set()
    try:
        while True:
            msg = await websocket.receive_text()
            if msg not in seen:
                seen.add(msg)
                await websocket.send_text("Да? Хорошо. Спасибо за поддержку!")
    except WebSocketDisconnect:
        return  

    
    
