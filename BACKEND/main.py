import fastapi
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio

app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/first")
async def first():
    await asyncio.sleep(5)
    return "answer 1"


@app.get("/second")
async def second():
    await asyncio.sleep(1)
    return "answer 2"


uvicorn.run(app, host="127.0.0.1", port=8081)