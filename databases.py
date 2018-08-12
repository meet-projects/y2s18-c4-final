# Database related imports
# Make sure to import your tables!
from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_user(name, password, points, picture):
	print("Added a user!")
	user = User(name = name, password = password, points = points, picture = picture)
	session.add(user)
	session.commit()

def query_all():
	students = session.query(User).all()
	return students

def query_by_name(name):
	return session.query(User).filter_by(name = name).all()

def query_by_status(status):
	return session.query(User).filter_by(fraud = status).all()

def delete_all():
	
	session.query(User).delete()
	session.commit()

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