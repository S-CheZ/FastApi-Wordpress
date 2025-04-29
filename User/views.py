import json

from fastapi.params import Query, Body
from pydantic import BaseModel

from JwtA import create_user_token
from Sign import is_Sign
import uuid
from fastapi import APIRouter,Request
from .models import User

USER = APIRouter(tags=["用户管理"])

#模型
class LoginRequest(BaseModel):
    username: str
    password: str  # 假设需要密码字段


@USER.get("/{id}",summary="用户查询")
async def get_user():
    return {
        "id": str(uuid.uuid4()),
    }


@USER.post("",summary="用户添加")
async def post_user(request:Request):
    try:
        # 获取请求体
        body = await request.body()
        # json转字典
        data = json.loads(body)
        #检测传入数据是否正常
        if data["username"] == "" and data["password"] == "":
            return {
                "status": 0,
                "msg":"账号或密码为空"
            }
        if await User.filter(username=data["username"]).exists():
            return {
                "status": 0,
                "msg": "账户以存在"
            }
        # 获取数据库数据
        user=await User.create(username=data["username"], password=data["password"])
        await user.save()
        response=await get_login(request)
        # return {
        #     "status": 1,
        #     "msg": "添加成功"
        # }
        return response
    except Exception as e:
        print(e)
        return {
            "status": 0,
            "msg": str(e)
        }

@USER.delete("/delete",summary="用户删除")
async def delete_user():
    return {
        "id":str(uuid.uuid4()),
        "msg":"删除成功"
    }


@USER.post("/login",summary="登陆")
async def get_login(request:Request):
    try:
        #获取请求体
        body=await request.body()
        #json转字典
        data=json.loads(body)
        #获取数据库数据
        user=await User.get_or_none(username=data["username"])
        #判断是否存在
        if user is None:
            return {
                "status": "0",
                "msg":"用户未注册"
            }
        #获取token
        token=create_user_token({
            "username": user.username,
        })
        return {
            "status": "1",
            "msg":"登陆成功",
            "id":user.id,
            "username":user.username,
            "token":token,
        }
    except Exception as e:
        return {
            "status":"0",
            "msg":str(e)}
