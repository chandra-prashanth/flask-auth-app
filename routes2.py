from flask import render_template,session,request,url_for,redirect
from flask_login import login_user,logout_user,current_user,login_required
from models1 import User

def register_routes1(app,db,bcrypt):
    
    @app.route('/')
    def index():
       return render_template('index.html')
    
    @app.route('/signup',methods=['GET','POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            user = User(username=username,password=hashed_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(User.username==username).first()

            if bcrypt.check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'Failed'
    
    @app.route('/secret')
    @login_required
    def secret():
        return 'Secret message'
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))