from mod.login import app_login, error_login
from mod.scrap import scrap_lang, scrap_level, scrap_question, scrap_read
from flask import Flask, render_template, request, redirect, url_for
from mod.submit import submit_code
from mod.script_variable import c_id
from mod.answers import get_answers
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cH@c~nE9C=MxUfBQ7M,J:=K^ABJfdn8kMXZJv}>aCGoKY9UG>&?-51*s"HeJX@'

error = ""
lin = ""
level = []
t_question = []
t_read = []
course = ""
code = ""
compilers = []
stance = "Not Submitted"
cm = ""
rs = [stance, stance, [stance]]
question = ""
source_code = "source.html"
logins = '/login'


@app.route('/')
def login():  # put application's code here
    global lin, level, t_question, t_read, course, code, compilers, cm, rs, question, error
    lin = ""
    level = []
    t_question = []
    t_read = []
    course = ""
    code = ""
    compilers = []
    cm = ""
    rs = [stance, stance, [stance]]
    question = ""
    if error == "":
        return render_template('login.html', error=error)
    else:
        a = ""
        a = error
        error = ""
        return render_template('login.html', error=a)


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
                                   t_question=t_question, t_read=t_read, rs=rs)
        else:
            global error
            error = error_login(u)
            return redirect('/')
    else:
        return render_template(source_code, compilers=compilers, code=code, question=question, level=level,
                               t_question=t_question, t_read=t_read, rs=rs)


@app.route('/tutorials/<al_lan>', methods=['GET'])
def levels_t(al_lan):
    global level, t_question, t_read, course
    t_question = []
    t_read = []
    course = al_lan
    level = scrap_level(session, al_lan)
    return redirect(logins)


@app.route('/tutorials/<al_lan>/<path:al_ques>', methods=['GET'])
def levels_q(al_ques, al_lan):
    global t_question, lin
    lin = al_lan + '/' + al_ques
    t_question = scrap_question(session, lin)
    global code, t_read
    t_read = []
    code = ""
    return redirect(logins)


@app.route('/tutorials/questions/<path:al_read>', methods=['GET'])
def reads(al_read):
    global t_read, question
    question = al_read[4:]
    code = get_answers(session, al_read)
    t_read = scrap_read(session, al_read)
    return redirect(logins)


@app.route('/code', methods=['POST'])
def score():
    global code, question, cm, rs, course
    code = request.form.get('code').strip()
    question = request.form.get('question')
    cm = request.form.get('compiler')
    if course == "":
        course = c_id(cm)
    rs = submit_code(session, code, question, cm, course)
    return redirect(logins)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('err_404.html')


# if __name__ == '__main__':
#    app.run(debug=False, port=os.getenv("PORT", default=5000))
