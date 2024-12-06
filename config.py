

# 数据库配置

# 主机地址
Hostname='127.0.0.1'
# 端口号
Port=3306
# 数据库名称
Database='sxy'
# 用户名
Username='root'
# 密码
Password='root'
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(Username,Password,Hostname,Port,Database)
SQLALCHEMY_DATABASE_URI = DB_URI