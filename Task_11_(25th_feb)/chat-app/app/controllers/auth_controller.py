from flask import request, session, redirect, url_for, render_template
from app.services.auth_service import AuthService

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = AuthService.authenticate_user(username, password)
        if user:
            session['username'] = username
            return redirect(url_for('chat.chat'))
    return render_template('index.html')

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not AuthService.register_user(username, password):
            return "User already exists!", 400
        return redirect(url_for('auth.login'))
    return render_template('register.html')
