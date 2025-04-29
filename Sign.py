
import hashlib
from fastapi import  Request


#判断是否能通过加密
async def is_Sign(request:Request):
    # 获取密文
    X_sign = request.headers.get("X-sign")
    # 获取传入的事件戳
    t = request.query_params.get("t")
    # 获取Data
    body = await request.body()
    # 需要加密的文本进行拼接
    sign_str = body.decode("utf-8") + "&" + str(t)
    # 初始化加密算法
    MD5 = hashlib.md5()
    # 加密
    MD5.update(sign_str.encode())
    # 判断加密后的内容是否一样
    if X_sign == MD5.hexdigest():
        # print("签名一样")
        return True
    else:
        # print("签名不一样")
        return False
