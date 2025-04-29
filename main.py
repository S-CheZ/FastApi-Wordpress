

import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import Response, JSONResponse
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from File.views import File
from Sign import is_Sign
from User.views import USER
from settings import TORTOISE_ORM
from NoteList.views import Note
from ChatAi.views import ChatAi


# 创建初始化函数
async def lifespan(app: FastAPI):
    # 初始化
    await Tortoise.init(TORTOISE_ORM)
    # 创建表
    await Tortoise.generate_schemas()
    yield
    # 关闭
    await Tortoise.close_connections()


# 创建程序
app = FastAPI(lifespan=lifespan)


# @app.middleware("http")
# async def interpret_request(request: Request, call_next):
#
#     # 排除不需要验证的路径
#     if request.method=="GET" or any(path in request.url.path for path in ["/docs", "/openapi.json", "/File", "/static","/Note/Category"]):
#         response = await call_next(request)
#         return response
#
#     # 是否存在加密
#     if not await is_Sign(request):
#         return JSONResponse(status_code=401,
#                             content={
#                                 "status":0,
#                                 "msg":"签名未通过"
#                             }
#                         )
#
#     response = await call_next(request)
#     return response


# 添加中间件
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_headers=["*"],
                   allow_methods=["*"],
                   )

# 添加路由
app.include_router(USER, prefix="/User", )
app.include_router(File, prefix="/File", )
app.include_router(Note, prefix="/Note", )
app.include_router(ChatAi, prefix="/Chat", )
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000,reload=True)
