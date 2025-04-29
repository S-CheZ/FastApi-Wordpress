from tortoise import Tortoise

# 配置 MySQL 数据库
TORTOISE_ORM = {
    "connections": {
        "default": {
            # "engine": "tortoise.backends.asyncpg",   # 数据库引擎 PostgresQL
            "engine": "tortoise.backends.mysql",  # 数据库引擎 Mysql or Mariadb
            "credentials": {
                "host": "127.0.0.1",    # 地址
                "port": "3306",         # 端口
                "user": "root",         # 用户名
                "password": "!Shizichen2003",     # 密码
                "database": "admin",  # 数据库名称（需要提前创建数据库）
                "minsize": 1,           # 最少连接
                "maxsize": 5,           # 最大连接
                "charset": "utf8mb4",   # 编码
                "echo": True            # 是否反馈SQL语句
            }
        }
    },
    "apps": {
        "models": {
            "models": ['aerich.models',"User.models","NoteList.models","ChatAi.models"],   # models数据模型迁移
            "default_connection": "default"
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}


