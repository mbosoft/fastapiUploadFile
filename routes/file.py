from fastapi import APIRouter, Request, UploadFile,Form
from fastapi.templating import Jinja2Templates
from repository import file as repo
from fastapi.responses import JSONResponse

templates = Jinja2Templates(directory="templates/")
upload_router = APIRouter()


@upload_router.get("/")
def main(request: Request):
    list_name=repo.fetch_all()
    contexts = {
        "request": request,
        "list_name":list_name,

    }
    return templates.TemplateResponse("index.html", contexts)


@upload_router.post("/")
def insert(request: Request, file: UploadFile = Form(...)):

    list_name=repo.upload_file(file)
    contexts = {
        "list_name":list_name,
        "request": request,
    }
    return templates.TemplateResponse("index.html", contexts)


@upload_router.delete("/{id}")
def deleteItem(id:int):
    repo.deleteItem(id)
    return JSONResponse(status_code=200,content={"Message":"Item deleted"})