from flask import Flask, render_template, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, logout_user, login_user, login_required

import DataBase
import Forms

# initializing the login manager
login_manager = LoginManager()

# initializing Flask app
app = Flask(__name__)

# Configuring flask database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = "PIFANMOPWAINFOANWOFIKNAOFKNAOWFNMO"

#linking database to the app
DataBase.db.init_app(app)
login_manager.init_app(app)

#Creating database tables
with app.app_context():
    DataBase.db.create_all()

#Creating a userloader function
@login_manager.user_loader
def load_user(user_id):
    return DataBase.User.query.get(user_id)

### website routes ###

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('index_page'))

#Index page
@app.route("/")
@app.route("/index")
def index_page():
    user = DataBase.User
    searchbar = Forms.user_search_form()
    return render_template('index.html',
                            searchbar = searchbar,
                            user = user)

@app.route("/signup", methods =['GET','POST'])
def signup_page():
    user = DataBase.User
    form = Forms.Sign_up_form()

    if form.validate_on_submit():
        #adding a user to the database
        new_user = DataBase.User(username=form.username.data, email = form.email.data, password=form.password.data)
        try:
            DataBase.db.session.add(new_user)
            DataBase.db.session.commit()

            #signin the user and redirect to the homepage
            login_user(new_user)
            return redirect(url_for('home_page'))
        except(Exception):
            flash("That email is already registered please sign in")

    return render_template(
        'sign_up.html',
        searchbar = Forms.user_search_form(),
        form = form,
        user = user
        )

@app.route("/signin", methods =['GET','POST'])
def signin_page():
    form = Forms.Sign_in_form()

    if form.validate_on_submit():
        #search for matching credentials
        user = DataBase.User.query.filter_by(username=form.username.data, email = form.email.data, password=form.password.data).first()

        if user == None: # if user not found
            return render_template(
                'sign_in.html',
                form = form,
                user = DataBase.User,
                message = "Error: Provided username email or password was incorrect please try again"
            )
        #if user found log them in and redirect
        login_user(user)
        return redirect(url_for('home_page'))

    return render_template(
        'sign_in.html',
        form = form,
        user = DataBase.User,
        message = None
    )


@app.route("/home", methods =['GET','POST'])
@login_required
def home_page():
    user = DataBase.User
    form = Forms.Postform()
    searchbar = Forms.user_search_form()
    # pull all of the content out of the content table to show on the page
    data = DataBase.Content.query.all()
    if searchbar.validate_on_submit():
        user = DataBase.User.query.filter_by(username=form.username.data).first()
    if form.validate_on_submit():
        post = DataBase.Content(poster_id = 1, title=form.Title.data,content=form.Content.data)
        DataBase.db.session.add(post)
        DataBase.db.session.commit()

        #signin the user and redirect to the homepage
        return redirect(url_for('home_page'))
    return render_template(
        'home.html',
        searchbar = searchbar,
        form = form,
        user = user,
        data = data
    )

@app.route("/profile")
@login_required
def profile_page():
    user = DataBase.User
    searchbar = Forms.user_search_form()
    return render_template(
        'profile.html',
        searchbar = searchbar,
        user = user
    )

@app.route("/account/<Username>")
@login_required
def User_page(Username):
    user = DataBase.User
    searchbar = Forms.user_search_form()

    return render_template(
        'other_account.html',
        searchbar = searchbar,
        user = user
    )
@app.route("/signout")
@login_required
def signout():
    #log out user with flask login and redirect to the index page
    logout_user()
    return(redirect(url_for("index_page")))

if __name__ == '__main__':
    app.run(debug=True)