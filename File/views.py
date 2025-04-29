import os.path
from typing import List

from fastapi import APIRouter, UploadFile,Request

File = APIRouter(tags=["文件管理"])
@File.post("/upload",summary="添加文件")
async def upload_file(request:Request,file: UploadFile):
    max_size = 3 * 1024 * 1024
    try:
        #限制大小
        if file.size > max_size:
            return {
                "status": 0,
                "msg":"文件不得大于3m"
            }
        path = os.path.join(os.getcwd(), "static/upload", file.filename)
        with open(path, "wb+",) as f:
            for line in file.file.readlines():
                f.write(line)
        return {
            "status": 1,
            "url":str(request.base_url)+"static/upload/"+file.filename,
            "filename":file.filename,
            "msg": "上传成功"
        }
    except Exception as e:
        return {
            "status": 0,
            "msg": str(e)
        }

@File.post("/uploads", summary="添加多个文件")
async def upload_file(files : List[UploadFile]):
    for file in files:
        print(file.filename)
    return files