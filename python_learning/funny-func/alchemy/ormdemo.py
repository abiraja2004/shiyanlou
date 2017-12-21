# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, SmallInteger, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from sqlalchemy.orm import sessionmaker
#导入faker工厂对象 构造测试数据
from faker import Factory
import random


engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/oldculture')
Base = declarative_base()


class User(Base):
    #__tablename__用于设置数据库中表的名字
    __tablename__ = 'users'

    #常用的数据库字段类型 Text, Boolean, SmallInteger, DateTime
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='author')
    #一对一关系
    userinfo = relationship('UserInfo', backref='user', uselist=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


class UserInfo(Base):
    __tablename__ = 'userinfos'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(11))
    link = Column(String(64))
    user_id = Column(Integer, ForeignKey('users.id'))


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    cate_id = Column(Integer, ForeignKey('categories.id'))
    #多对多通过一个辅表关联
    tags = relationship('Tag', secondary='article_tag', backref='articles')

    def __repr__(self):
        """
        %s调用 __str__()
        %r调用 __rper__()
        :return:
        """
        return '%s(%r)' % (self.__class__.__name__, self.title)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='category')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


article_tag = Table(
    #第一个参数为表名称，第二个参数是metadata，这两个是必须的
    'article_tag', Base.metadata,
    #多对多关系，辅助表，一般存储要关联的两个表的id，并设置为外键
    Column('article_id', Integer, ForeignKey('articles.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)

#删除表
Base.metadata.drop_all(engine)
#创建表
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

faker = Factory.create()
session = Session()

faker_users = [User(
    username=faker.name(),
    password=faker.word(),
    email=faker.email(),
) for i in range(10)
]

session.add_all(faker_users)

faker_categories = [Category(name=faker.word()) for i in range(5)]
session.add_all(faker_categories)

#生成20个标签
faker_tags = [Tag(name=faker.word()) for i in range(20)]
session.add_all(faker_tags)

#生成100篇文章
for i in range(100):
    article = Article(
        title=faker.sentence(),
        content=" ".join(faker.sentences(nb=random.randint(10, 20))),
        author=random.choice(faker_users)
    )
    for tag in random.sample(faker_tags, random.randint(2, 5)):
        article.tags.append(tag)
    session.add(article)

session.commit()


