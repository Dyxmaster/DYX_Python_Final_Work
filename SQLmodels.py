from exts import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # 将长度设置为 255
    email = db.Column(db.String(50), unique=True)
    created_time = db.Column(db.DateTime, default=datetime.now)


# 在终端中运行以下命令，完成迁移三部曲
# 1） flask db init  # 初始化迁移环境 只需执行一次
# 2） flask db migrate   # 生成迁移脚本
# 3） flask db upgrade  # 执行迁移脚本