import os
from datetime import datetime  # get current date
from models.file import FileModel
from sqlalchemy.orm import Session
from database.db import engine
from fastapi import HTTPException,status

now = datetime.now()
session = Session(bind=engine, expire_on_commit=False)


def deletePathFile(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error : %s %s" % (file_path, e.strerror))    


def deleteItem(id):
    itemObject=session.query(FileModel).filter(FileModel.id==id).first()
    if itemObject:
        session.delete(itemObject)
        session.commit()
        session.close()
        deletePathFile(itemObject.file_path)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"file with id {id} not found")


def upload_file(file):
    try:
        dir = createPathFile()
        contents = file.file.read()
        path = dir+'/'+file.filename
        with open(path, "wb") as f:
            if not (os.path.isfile(file.filename)):
                f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    new_file = FileModel(file_name=file.filename, file_path=path)

    file_exist = session.query(FileModel.id).filter_by(
        file_path=path).first() is not None

    if not file_exist:
        session.add(new_file)
        session.commit()
        session.close()
    else:
        print("exist")

    return fetch_all()


def fetch_all():
    return session.query(FileModel).all()


def createPathFile():
    date_now = now.strftime("%Y.%m.%d")
    path = "file/"+date_now
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    return path
