from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from database.connection import connect_to_db
from database.server import router

config = dotenv_values()

app = FastAPI()

#include routes
app.include_router(router)



#connection
@app.on_event("startup")
async def startup():
    connect_to_db(app)

