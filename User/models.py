from tortoise.models import Model
from tortoise import fields

class User(Model):
    id=fields.IntField(pk=True)
    username=fields.CharField(max_length=50)
    password=fields.CharField(max_length=50)
    avatar_img=fields.CharField(max_length=50,null=True)
    create_time=fields.DatetimeField(auto_now_add=True)
