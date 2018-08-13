from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class User(Base):
	__tablename__ = "users"
	user_id = Column(Integer, primary_key = True)
	name = Column(String)
	password = Column(String)
	points = Column(Integer)
	#picture = Column(String)

	def __repr__(self):
		return ("user name:{}, user pass:{}, user points:{}".format(self.name, self.password, self.points))

class Post(Base):
	__tablename__ = "posts"
	post_id = Column(Integer, primary_key = True)
	title = Column(String)
	description = Column(String)

	def __repr__(self):
		return ("Post title: {}, Post description: {}".format(self.title, self.description))