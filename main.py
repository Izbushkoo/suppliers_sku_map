import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv

load_dotenv()


# Replace the placeholder with your Atlas connection string
uri = os.getenv("MONGO_URL")
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

database = client.list_databases()

for i in database:
    print(i)


# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

app = FastAPI()


# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8900)
