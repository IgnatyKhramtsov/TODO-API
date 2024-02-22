from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, sync_engine, session_factory

import os
import sys

from tasks.models import PriorityORM
# from users.router import router as router_users
from tasks.router import router as router_tasks
from pages.router import router as router_pages
from imp_exp.router import router as router_download

# sys.path.insert(1, os.path.join(sys.path[0], '..'))

app = FastAPI(
    title="TODO_API",
    docs_url="/"
)

@app.on_event("startup")
def startup_event():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    priorities_data = ['Low', 'Normal', 'High']
    with session_factory() as session:
        for priority_name in priorities_data:
            priority = PriorityORM(name=priority_name)
            session.add(priority)
        session.commit()


app.include_router(router_tasks)
app.include_router(router_pages)
app.include_router(router_download)

origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)