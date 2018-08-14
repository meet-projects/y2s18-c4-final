# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
# from databases import add_student, get_all_students 
import databases

# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '34gsss7s'

# App routing code here
@app.route('/' , methods = ['GET','POST'])
def login_page():
    if request.method == 'POST':
        user = databases.query_by_name(request.form["name"])
        print(request.form['name'])
        if user is not None:
            if user.password == request.form["password"]:
                session['username'] = user.name
                return redirect(url_for("profile_page", username = user.name))

            else:
                error = 'password does not match'
                return render_template('home.html', error = error)
        else:

            error = 'username does not exist'
            return render_template('home.html', error = error)

    else:

        return render_template('home.html')


# Running the Flask app

@app.route('/profile/<string:username>')
def profile_page(username):

    user = databases.query_by_name(username)
    if user is not None:
        return render_template('profile.html', user = user)
    else:
        return redirect(url_for('login_page'))

@app.route('/signup', methods = ['GET' ,'POST'])
def sign_up_page():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        name = request.form['name']
        password = request.form['password']
        number = request.form['phonenum']

        print("hthr")
        
        databases.add_user(name , password, 0 , number)
        return redirect(url_for("login_page"))
@app.route('/noor', methods=['GET' ,'POST'])
def noor():
    if request.method == 'GET':
        return render_template("noor.html")
@app.route('/thank_you', methods=['GET' ,'POST'])
def thanks():
    if request.method == 'GET':
        return render_template("thank_you.html")


@app.route('/categories')
def categories():
    return render_template("categories.html")


@app.route('/categories/phones')
def phones():
    phoneposts = databases.query_by_category("phones")
    return render_template("phones.html",phones =phoneposts )

@app.route('/bags')
def bags():
    return render_template("bags.html")
@app.route('/lostorfound' , methods=['POST','GET'])
def lostorfound():
    return render_template('noor.html')


@app.route('/other')
def other():
    return render_template("other.html")
@app.route('/post' , methods=['GET' ,'POST'] )
def makepost():
     if request.method == 'GET':
         return render_template('makepost.html')
     else:
         describe = request.form['describe']
         category = request.form['category']
         title = request.form['title']

         databases.add_post(title,describe,category)


         return redirect(url_for("profile_page", username = session['username']))


    

# @app.route('/search', methods['GET', 'POST'])
# def search():

    
if __name__ == "__main__":
    app.run(debug=True)