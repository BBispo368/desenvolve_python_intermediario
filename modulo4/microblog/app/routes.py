from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app import alquimias
from datetime import datetime

@app.route('/')
@login_required
def index():
    posts = []
    if current_user.is_authenticated:
        # Update last login timestamp when they visit index
        current_user.last_login = datetime.utcnow()
        db.session.commit()
        posts = alquimias.get_timeline()
    return render_template('index.html', user=current_user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()
        
        user = alquimias.validate_user_password(username, password)
        if user:
            print("\nLogin bem sucedido!\n")
            login_user(user, remember=True)  # or remember=user.remember? In their slide: login_user(user, remember=user.remember) but wait, user doesn't have a remember attribute in db. Let's use remember=True.
            return redirect(url_for('index'))
        else:
            print("\nUsuário ou senha inválidos\n")
            flash('Usuário ou senha inválidos')
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        if alquimias.user_exists(username):
            print("\nUsuário já existe!\n")
            flash('Usuário já existe!')
            return redirect(url_for('login'))
        else:
            password = request.form['password'].lower()
            foto = request.form.get('foto', '')
            bio = request.form.get('bio', '')
            remember = True if request.form.get('remember') == 'on' else False
            
            user = alquimias.create_user(username, password, foto=foto, bio=bio)
            print("\nLogin bem sucedido!\n")
            login_user(user, remember=remember)
            return redirect(url_for('index'))
            
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form.get('body', '')
        if body:
            alquimias.create_post(body, current_user)
        return redirect(url_for('index'))
    return render_template('post.html')
