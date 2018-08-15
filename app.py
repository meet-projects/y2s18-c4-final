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



@app.route('/categories')
def categories():
    return render_template("categories.html")


@app.route('/phones')
def phones():
    phoneposts = databases.query_by_category("phones")
    return render_template("phones.html",phones = phoneposts )

@app.route('/bags')
def bags():
    bagsposts = databases.query_by_category("bags")
    return render_template("bags.html",bags =bagsposts)
@app.route('/lostorfound' , methods=['POST','GET'])
def lostorfound():
    return render_template('noor.html')


@app.route('/other')
def other():
    otherposts = databases.query_by_category("other")
    return render_template("other.html" ,others = otherposts)
@app.route('/thanyou')
def thanku():
    return render_template("thank_you.html")
@app.route('/sunglasses')
def sunglasses():
    sunglassesposts = databases.query_by_category("sunglases")
    return render_template("sunglasses.html" ,sunglasses = sunglassesposts)

@app.route('/wallets')
def wallets():
    walletsposts = databases.query_by_category("wallets")
    return render_template("wallets.html",wallets = walletsposts)
@app.route('/books')
def books():
    booksposts = databases.query_by_category("books")
    return render_template("books.html" , books=booksposts)
@app.route('/keys')
def keys():
    keysposts = databases.query_by_category('keys')
    return render_template("keys.html", keys=keysposts)
@app.route('/clothes')
def clothes():
    clothesposts = databases.query_by_category("clothes")
    return render_template("clothes.html", clothes=clothesposts)
@app.route('/jewerly')
def jewerly():
    jewerlyposts = databases.query_by_category("jewelry")
    return render_template("jewerly.html", jewerly = jewerlyposts)
    
    

    
    
@app.route('/post' , methods=['GET' ,'POST'] )
def makepost():
     if request.method == 'GET':
         return render_template('makepost.html')
     else:
         describe = request.form['describe']
         category = request.form['category']
         title = request.form['title']
         contact = request.form['contact_info']
         username = request.form['username']

         databases.add_post(title,describe,category,username,contact)
         userpoints = databases.get_points(name = username)
         databases.update_points(amount = 10, name = username)
         
         return redirect(url_for('thanku'))

  
if __name__ == "__main__":
    app.run(debug=True)