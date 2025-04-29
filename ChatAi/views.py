from fastapi import APIRouter, Request, HTTPException
from tortoise.exceptions import DoesNotExist

from ChatAi.ChatAiInterface import getChatAiMessage
from ChatAi.models import ChatAiMessageSession, ChatAiMessage
from User.models import User

ChatAi = APIRouter(tags=["Ai接口"])


@ChatAi.post("/chat", summary="获取ai返回")
async def get_chat(request: Request):
    try:
        json_data = await request.json()
        uid = int(json_data["uid"])
        message = json_data["message"]
        is_create = bool(json_data["is_create"])
        user = await User.get(id=uid)

        # 检查数据是否有误

        if uid is None or message is None:
            raise HTTPException(status_code=400, detail="数据传输有误1")

        # 逻辑运行
        if is_create:
            # 创建
            session = await ChatAiMessageSession.create(user_id=user.id)
            await session.save()
            # 创建消息
            userMessage = await ChatAiMessage.create(content=message, session_id=session.id, user_id=user.id)
            await userMessage.save()

            msgs = [
                {
                    "role": "user",
                    "content": message
                }
            ]
            #通过ai网站获取
            res = await getChatAiMessage(messages=msgs, user=userMessage.id)
            for item in res:
                AiMessage = await ChatAiMessage.create(content=item["message"]["content"], session_id=session.id,
                                                       user_id=user.id, is_Ai=True)
                await AiMessage.save()
            return {
                "status": "1",
                "sid": session.id,
                "data": res
            }
        else:  # 不创建

            sid = int(json_data["sid"])
            session = await ChatAiMessageSession.get(id=sid)
            # 获取对应Session会话数据
            record = await ChatAiMessageSession.get(id=sid, user_id=user.id)
            # 获取对应消息数据
            messages =await ChatAiMessage.filter(session_id=record.id)
            # 创建消息
            userMessage = await ChatAiMessage.create(content=message, session_id=session.id, user_id=user.id)
            await userMessage.save()
            #消息集合
            msgs = [
            ]
            #添加之前的聊天记录
            for item in messages:
                msgs.append({
                    "role": "assistant"  if item.is_Ai==True else "user",
                    "content": item.content
                })
            #添加现在的聊天记录
            msgs.append({
                "role":"user",
                "content": message
            })
            #获取聊天记录
            res=await getChatAiMessage(messages=msgs, user=user.id)
            for item in res:
                #添加到数据库
                AiMessage = await ChatAiMessage.create(content=item["message"]["content"], session_id=session.id,
                                                       user_id=user.id, is_Ai=True)
                await AiMessage.save()
            #返回数据
            return {
                "status": "1",
                "sid": session.id,
                "data": res
            }
        return message
    except DoesNotExist:
        return HTTPException(status_code=400, detail="未存在当前session")
    # except TypeError:
    #     return  HTTPException(status_code=400,detail="数据传输错误")


@ChatAi.get("/sessions", summary="获取会话列表")
async def get_sessions(request: Request):
    try:
        json_data = request.query_params
        uid = json_data["uid"]
        user = await User.get(id=uid)
        sessions = await ChatAiMessageSession.filter(user_id=user.id).all()
        # sessions_data=[ print(session) for session in sessions]
        sessions_data = []
        for session in sessions:
            content = await ChatAiMessage.filter(session_id=session.id, is_Ai=False).last()
            sessions_data.append({
                "sid": session.id,
                "content": content.content,
            })
        return {"status": "1", "data": sessions_data}
    except DoesNotExist:
        return HTTPException(status_code=400, detail="未查询到")

@ChatAi.get("/ChatList",summary="获取聊天记录列表")
async def get_chatMessage_list(request: Request):
    try:
        json_data = request.query_params
        sid = json_data["sid"]
        uid = json_data["uid"]
        user = await User.get(id=uid)
        session = await ChatAiMessageSession.get(id=sid,user_id=user.id)
        messages= await ChatAiMessage.filter(session_id=session.id).all()
        megs=[]
        for message in messages:
            megs.append({
                "sid": session.id,
                "content": message.content,
                "is_Ai": message.is_Ai,
            })
        return {"status": "1", "data": megs}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))