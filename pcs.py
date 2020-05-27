from datetime import datetime
from functools import wraps

from flask import Flask, render_template, request, url_for, session, redirect

import config
from exts import db
from models import User, Prescription

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


#登录限制
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper

@app.route('/')
def index():
    context = {
        'prescriptions': Prescription.query.order_by(Prescription.pre_date.desc()).all()
    }
    return render_template('index.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = User.query.filter(User.phone == phone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            #如果31天内都不需要重新登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return "手机号码或密码错误，请重新登录！"



@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        phone = request.form.get('phone')
        username = request.form.get('username')
        password = request.form.get('password')
        pwd_confirm = request.form.get('pwd_confirm')

        #手机号码验证
        user = User.query.filter(User.phone == phone).first()
        if user:
            return "手机号码已被注册，请更换手机号码！"
        else:
            #验证两次输入的密码是否相同
            if password != pwd_confirm:
                return "两次输入的密码不一致，请重新输入，并保证两次输入密码相同！"
            else:
                user = User(phone=phone, username=username, password=password)
                db.session.add(user)
                db.session.commit()
                #注册成功之后，重定向到登录页面
                return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id')
    # del session['user_id']
    return redirect(url_for('index'))


@app.route('/precomment', methods=['GET', 'POST'])
@login_required
def pre_comment():
    if request.method == 'GET':
        return render_template('pre_comment.html')
    else:
        t_id = request.form.get('t_id')
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        pre_date = datetime.strptime(request.form.get('pre_date'), "%Y-%m-%d").date()
        diagnosis = request.form.get('diagnosis')
        first_page = request.form.get('first_page')
        second_page = request.form.get('second_page')
        third_page = request.form.get('third_page')
        injection = request.form.get('injection')
        pre_amount = request.form.get('pre_amount')
        prescriber = request.form.get('prescriber')
        section = request.form.get('section')
        reasonable = request.form.get('reasonable')
        comments = request.form.get('comments')
        pre_com = Prescription(t_id=t_id,name=name,gender=gender,age=age,pre_date=pre_date,diagnosis=diagnosis,
                               first_page=first_page,second_page=second_page,third_page=third_page,injection=injection,
                               pre_amount=pre_amount,prescriber=prescriber,section=section,reasonable=reasonable,
                               comments=comments)
        db.session.add(pre_com)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<pre_id>')
def detail(pre_id):
    pre_item = Prescription.query.filter(Prescription.id == pre_id).first()
    return render_template('detail.html', pre_item=pre_item)



@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == "__main__":
    app.run()