from alchemy.ormdemo import *


engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/oldculture')
Session = sessionmaker(bind=engine)

session = Session()

print("%r" % session.query(User).get(1))
#filter_by按某一字段过滤
print("%r" % session.query(User).filter_by(username='M').first())
#filter可以按多个字段过滤
print("%r" % session.query(User).filter(User.username=='Ann Steele').first())

print("%r" % session.query(User).all())
#按id查询
a = session.query(Article).get(10)

##更新一个字段
a.title = "my test blog"
session.add(a)
session.commit()
#删除
session.delete(a)
session.commit()
