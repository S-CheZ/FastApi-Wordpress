from tortoise import Model, fields


class ChatAiMessageSession(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField("models.User", on_delete=fields.CASCADE, related_name="messages_sessions")

class ChatAiMessage(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    is_Ai=fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    session=fields.ForeignKeyField("models.ChatAiMessageSession", on_delete=fields.CASCADE, related_name="messages")