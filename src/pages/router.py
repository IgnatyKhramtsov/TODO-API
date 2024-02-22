from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from tasks.router import get_all_tasks, search_task

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/base")
def get_base_pages(request: Request, all_task=Depends(get_all_tasks)):
    return templates.TemplateResponse("task.html", {"request": request, "tasks": all_task["tasks"]})


@router.get("/search/{word}")
def get_base_pages(request: Request, search_task=Depends(search_task)):
    return templates.TemplateResponse("task.html", {"request": request, "tasks": search_task})
