from sqlalchemy import Column, String, create_engine, MetaData, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import hashlib

# 创建对象的基类:
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/flask')


# Model
# 用户
class User(Base):
	# 表名
	__tablename__ = 'tb_user'

	id = Column(Integer(), primary_key=True)
	name = Column(String(20))
	age = Column(Integer())
	password = Column(String(200))
	phone = Column(String(20))

# Base.metadata.create_all(engine)

# 创建DBSession类型和session对象
DBSession = sessionmaker(bind=engine)
session = DBSession()

# 添加新数据
# new_user = User(name='李四', age=22, password='123456', phone='18888888888')
# session.add(new_user)	# 添加到session
# session.commit()	# 提交保存到数据库
session.close()

#
# m = hashlib.sha256()
# m.update(b"123456")
# # 创建新User对象:
# new_pwd = Password(id='1', user_id='1', password=m.hexdigest())
# # 添加到session:
# session.add(new_pwd)
# # 提交即保存到数据库:
# session.commit()
