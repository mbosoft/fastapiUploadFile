
from database.db import Base
from sqlalchemy import Column, Integer, String


class FileModel(Base):
    __tablename__ = "FileModel"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)

    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
