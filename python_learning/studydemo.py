#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
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

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
new_user = User(name='louuser1')
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
