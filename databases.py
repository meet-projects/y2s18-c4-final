# Database related imports
# Make sure to import your tables!
from model import Base, User, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_user(name, password, points, phone_number):
	
	print("Added a user!")
	user = User(name = name, password = password, points = points, phone_number = phone_number)
	session.add(user)
	session.commit()

def add_post(title, description, category):

	print("Added a post!")
	post = Post(title = title, description = description, category = category)
	session.add(post)
	session.commit()

def query_all_users():

	return session.query(User).all()

def query_all_posts():

	return session.query(Post).all()

def query_by_name(name):

	return session.query(User).filter_by(name = name).all()

def query_by_title(title):

	return session.query(Post).filter_by(title = title).all()

def delete_all_users():
	
	session.query(User).delete()
	session.commit()

def delete_all_posts():
	
	session.query(Posts).delete()
	session.commit()

def query_by_category(category):
	return session.query(Post).filter_by(category = category).all()

def delete_duplicates():

	names = []
	
	for i in query_all_articles():
	
		names.append(i.name)
	
	names = set(names)
	names = list(names)
	temp = []

	for i in names:
		
		#l = query_by_name(i)
		temp.append(query_by_name(i)[0])
	
	delete_all()

	for i in temp:
		add(i.name, i.password, i.points, i.picture)
		#for j in range(len(l)-1):

			#delete_article_by_name(i)
	session.commit()