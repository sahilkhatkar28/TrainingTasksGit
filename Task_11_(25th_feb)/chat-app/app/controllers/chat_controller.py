from flask import session, redirect, url_for, render_template

def chat():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('chat.html')
