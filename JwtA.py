from datetime import datetime,timedelta,timezone
import jwt

SECRET_KEY="866c44956921b6e2b141cf99a3d46354425a6d1758f106ccd382dff926907af7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

#获取token
def create_user_token(data:dict):
    #转出来变成字符串
    to_encode=data.copy()
    to_encode.update({'exp': datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    token=jwt.encode(
        to_encode,          #   传输的内容
        SECRET_KEY,         #jwt的签名密钥
        algorithm=ALGORITHM
    )
    print(token)
    return token

