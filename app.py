# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
# from databases import add_student, get_all_students 
import databases

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/' , methods=['GET','POST'])
def login_page():
    if request.method == 'POST':
        user = databases.query_by_name(request.form["name"])
        print(request.form['name'])
        if user is not None:
            if user.password == request.form["password"]:
                return redirect(url_for("profilepage"))

            else:
                error = 'password does not match'
                return render_template('home.html', error=error)
        else:

            error = 'username does not exist'
            return render_template('home.html', error=error)

    else:

        return render_template('home.html')


# Running the Flask app

@app.route('/profile')
def profile_page():
    pass

@app.route('/signup', methods=['GET' ,'POST'])
def sign_up_page():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        name = request.form['name']
        password = request.form['password']


        
        databases.add_user(name , password, 0)
        return render_template("home.html")

@app.route('/categories')
def categories():
    return render_template("categories.html")

@app.route('/phones')
def phones():
    return render_template("phones.html")
@app.route('/bags')
def bags():
    return render_template("bags.html")
@app.route('/other')
def other():
    return render_template("other.html")

# @app.route('/search', methods['GET', 'POST'])
# def search():

    
if __name__ == "__main__":
    app.run(debug=True)