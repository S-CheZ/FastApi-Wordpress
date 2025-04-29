from tortoise.fields import ForeignKeyField
from tortoise.models import Model
from tortoise import fields

#分类
class Category(Model):
    id =fields.IntField(pk=True)
    name =fields.TextField(max_length=100)

#文章
class NoteList(Model):
    id =fields.IntField(pk=True)
    title= fields.TextField(max_length=100)     #标题
    content =fields.TextField()                 #内容
    cover_img=fields.TextField(max_length=100)  #标题图片
    create_time=fields.DatetimeField(auto_now_add=True)
    #分类
    category= ForeignKeyField("models.Category", on_delete=fields.CASCADE,related_name="notes")

    #用户
    user=ForeignKeyField("models.User", on_delete=fields.CASCADE,related_name="notes")

class Carousel(Model):
    id =fields.IntField(pk=True)
    title= fields.TextField(max_length=100)
    img_url=fields.TextField(max_length=100)