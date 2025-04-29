from fastapi import APIRouter, Request
from fastapi.params import Body

from NoteList.models import NoteList,Category
from User.models import User

Note = APIRouter(tags=["文章管理"])


@Note.get("/NoteList",summary="获取全部文章")
async def index(request: Request):
    try:
        #获取全部
        all = await NoteList.all().prefetch_related("user")

        res=[]
        for note in all:
            category=await note.category.all()
            res.append({
                "id":note.id,
                "title": note.title,
                "content": note.content,
                "cover_img": note.cover_img,
                "create_time": note.create_time,
                "user": {
                    "id": note.user.id if note.user else None,
                    "username": note.user.username if note.user else None,
                    "avatar_img": note.user.avatar_img if note.user else None,
                },
                "category": {
                    "id": category.id,
                    "name": category.name,
                }
            })
        return {
            "status": "1",
            "data": res
        }
    except Exception as e:
        return {
            "status": "0",
            "error": str(e)
        }

@Note.post("/NoteList",summary="添加文章")
async def add(request: Request):
    try:
        data = await request.json()
        category=await Category.get(id=data["category"])
        user=await User.get(id=data["user"])
        note = await NoteList.create(title=data["title"],
                                     content=data["content"],
                                     cover_img=data["cover_img"],
                                     category=category,
                                     user=user,)
        await note.save()
        print(note)
        return {
            "status": "1",
            "id": note.id,
            "msg": "添加成功"
        }
    except Exception as e:
        return {
            "status": "0",
            "error": str(e)
        }
@Note.get("/NoteList/{note_id}",summary="获取单篇文章")
async def get(note_id):
    try:
        note=await NoteList.get(id=note_id).prefetch_related("user")
        # user=await User.get(id=note.user)
        return {
            "status": "1",
            "data": {
                "title": note.title,
                "content": note.content,
                "cover_img": note.cover_img,
                "create_time": note.create_time,
                "user":{
                    "id": note.user.id,
                    "username": note.user.username,
                    "avatar_img": note.user.avatar_img,
                }
            }
        }
    except Exception as e:
        return {
            "status": "0",
            "error": str(e)
        }


@Note.get("/Category",summary="获取分类")
async def get():
    try:
        category = await Category.all()
        return {
            "status": "1",
            "data": category
        }
    except Exception as e:
        return {
            "status": "0",
            "error": str(e)
        }

@Note.post("/Category",summary="添加分类")
async def add(request:Request,data:dict=Body(...)):
    pass