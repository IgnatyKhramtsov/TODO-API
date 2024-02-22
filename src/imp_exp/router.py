import json
from json import JSONDecodeError

from fastapi import APIRouter, Depends, UploadFile, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse

from database import get_session
from tasks.models import TasksORM
from tasks.router import get_all_tasks
from tasks.schemas import TaskBase, TaskCreate

router = APIRouter(
    prefix="/download",
    tags=["Download Upload"]
)

def convert_to_DTO(data: TaskBase) -> TaskBase:
    return data

@router.post("/import_tasks")
def add_tasks_in_upload_file(file: UploadFile, session=Depends(get_session)):
    if file.content_type != "application/json":
        raise HTTPException(status_code=400, detail="Invalid document type")
    else:
        datas = json.loads(file.file.read())
    for data in datas:
        print(data)
        session.add(TasksORM(**data))
    session.commit()


@router.get("/export_tasks")
def download_tasks(query=Depends(get_all_tasks)):
    res_dto = [TaskBase.model_validate(row, from_attributes=True) for row in query["tasks"]]
    json_data = [jsonable_encoder(res, exclude={"id"}) for res in res_dto]
    file_name = "your_tasks.json"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2, ensure_ascii=False)

    return FileResponse(file_name, media_type="application/octet-stream", filename=file_name)

