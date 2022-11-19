from mod.login import app_login, error_login
from mod.scrap import scrap_lang, scrap_level, scrap_question, scrap_read
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cH@c~nE9C=MxUfBQ7M,J:=K^ABJfdn8kMXZJv}>aCGoKY9UG>&?-51*s"HeJX@'

error = ""
level = []
t_question = []
t_read = []
code = ""
compilers = ""
question = ""
source_code = "source.html"
logins = '/login'


@app.route('/')
def login():  # put application's code here
    return render_template('login.html', error=error)


@app.route(logins, methods=['POST', 'GET'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        global session
        session, u = app_login(username, password)
        check = 'window.location.href = "http://buildit.iare.ac.in/"'
        if check in u:
            global compilers
            compilers = scrap_lang(session)
            return render_template(source_code, compilers=compilers, code=code, question=question, level=level,
                                   t_question=t_question, t_read=t_read)
        else:
            global error
            error = error_login(u)
            return redirect('/')
    else:
        return render_template(source_code, compilers=compilers, code=code, question=question, level=level,
                               t_question=t_question, t_read=t_read)


@app.route('/source', methods=['POST'])
def source():
    source = request.form.get('source')
    print(source)
    return render_template('source.html')


@app.route('/tutorials/<al_lan>', methods=['GET'])
def levels_t(al_lan):
    global level, t_question, t_read
    t_question = []
    t_read = []
    level = scrap_level(session, al_lan)
    return redirect(logins)


@app.route('/tutorials/<al_lan>/<path:al_ques>', methods=['GET'])
def levels_q(al_ques, al_lan):
    global t_question
    t_question = scrap_question(session, al_lan + '/' + al_ques)
    return redirect(logins)


@app.route('/tutorials/questions/<path:al_read>', methods=['GET'])
def reads(al_read):
    global t_read, question
    question = al_read[4:]
    t_read = scrap_read(session, al_read)
    return redirect(logins)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('err_404.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
