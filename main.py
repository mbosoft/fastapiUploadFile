import uvicorn
from fastapi import FastAPI
from models import file
from database.db import engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.file import upload_router 

# instance 
app=FastAPI()

# config Database 
file.Base.metadata.create_all(bind=engine)

# config static and templates
app.mount("/static",StaticFiles(directory="static",html=True),name="static")
templates=Jinja2Templates(directory="templates/")

# config routes
app.include_router(upload_router)



if __name__=="__main__":
    uvicorn.run("main:app",reload=True)