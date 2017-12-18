#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#创建一个基类 
Base = declarative_base()
#相对路径当前目录下的shiyanlou.db文件
#'sqlite:////shiyanlou.db'表示绝对路径/shiyanlou.db
engine = create_engine('sqlite:///shiyanlou.db')
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    usercourses = relationship('UserCourse', backref='user')
 
class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    usercourses = relationship('UserCourse', backref='course')
 
class UserCourse(Base):
    __tablename__ = 'usercourse'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
#    user = relationship('User', foreign_keys=[user_id])
    course_id = Column(Integer, ForeignKey('course.id'))
#    course = relationship('Course', backref='usercourses')
    study_time = Column(Integer)

#删除表
Base.metadata.drop_all(engine)
#创建表
Base.metadata.create_all(engine)
#创建会话类
DBSession = sessionmaker(bind=engine)
#创建会话实例
session = DBSession()
 
new_user = User(name='louuser1')
#插入一条记录
session.add(new_user)
 
new_course = Course(name='loucourse1')
session.add(new_course)

new_usercourse = UserCourse(user_id=new_user.id,
                            course_id=new_course.id,
                            study_time=10)
session.add(new_usercourse)
session.commit()

print '%s - %s - %d minutes' \
      % (new_user.name, new_course.name, new_usercourse.study_time)
