from flask import Flask, render_template, request, redirect, url_for, session, flash 
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash 
import secrets 
 
app = Flask(__name__) 
app.secret_key = secrets.token_hex(16) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' 
db = SQLAlchemy(app) 
 
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(50), unique=True, nullable=False) 
    password = db.Column(db.String(256), nullable=False) 
 
with app.app_context(): 
    db.create_all() 
@app.route("/") 
def home(): 
    return render_template("karn.html") 
 
@app.route('/register', methods=['GET', 'POST']) 
def register(): 
    if request.method == 'POST': 
        username = request.form['username'] 
        password = request.form['password'] 
 
        if User.query.filter_by(username=username).first(): 
            flash('Username already taken. Please choose another.', 'error') 
        else: 
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256') 
            new_user = User(username=username, password=hashed_password) 
            db.session.add(new_user)
 
            db.session.commit() 
            flash('Registration successful. You can now log in.', 'success') 
            return redirect(url_for('login')) 
 
    return render_template('register.html') 
 
@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST': 
        username = request.form['username'] 
        password = request.form['password'] 
 
        user = User.query.filter_by(username=username).first() 
 
        if user and check_password_hash(user.password, password): 
            session['username'] = username 
            flash('Login successful!', 'success') 
            return redirect(url_for('dashboard')) 
        else: 
            flash('Invalid username or password. Please try again.', 'error') 
 
    return render_template('login.html') 
 
@app.route('/dashboard') 
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        flash('Please log in to access the dashboard.', 'info')
        return redirect(url_for('login'))
@app.route('/karn')
def karn():
    return render_template("karn1.html")

@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template("FAQs.html")

@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route('/message-us', methods=['GET', 'POST'])
def contact():
    return render_template('message-us.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profilesetting.html')



#Dashboard

@app.route('/organdonar', methods=['GET', 'POST'])
def organdonar():
    return render_template('organdonor.html')

@app.route('/blooddonar', methods=['GET', 'POST'])
def blooddonar():
    return render_template('blooddonor.html')

@app.route('/bloodbank', methods=['GET', 'POST'])
def bloodbank():
    return render_template('bloodbank.html')

@app.route('/organbankcards', methods=['GET', 'POST'])
def organbankcards():
    return render_template('organbankcards.html')

@app.route('/organbankinfo', methods=['GET', 'POST'])
def organbankinfo():
    return render_template('organbankinfo.html')


#

@app.route('/logout') 
def logout(): 
    session.pop('username', None) 
    flash('You have been logged out.', 'info') 
    return redirect(url_for('karn')) 
 
if __name__ == '__main__': 
    app.run(debug=True) 

