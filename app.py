from flask import Flask, render_template, request, url_for, flash, redirect
import pyodbc 

from entities import *
from models import *


# DAO satup
database_settings = {"Server" : "127.0.0.1:1433",
                        "Database" : "quera_prj1",
                        "UID" : "sa",
                        "PWD" : "Qwer22@@"}                      
b_model = BaseModel()
b_model.set_connection(database_settings)

user_dao = SiteUserDAO(tb_name="SiteUser", PK="email")
jpdao = JobOppDAO("JobOpp", "ID")

# flask setup:
app = Flask(__name__)
app.config['SECRET_KEY'] = '4!@#wqweER1oIUp'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/')
def user():
    return render_template('user.html')


@app.route('/user/add/', methods=('GET', 'POST'))
def user_add():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        
        if not email or not password or not fname or not lname:
            flash('all inputs are required!')
        else:
            user = SiteUser(email, password, fname, lname)
            user_dao.save(user)
            return redirect(url_for('user'))
    
    return render_template('user_add.html')


@app.route('/user/search/', methods=('GET', 'POST'))
def user_search():
    if request.method == 'POST':
        email = request.form['email']

        if not email:
            flash('enter an email!')
        else:
            u = user_dao.find_by_id(email)
            global q_result
            q_result = [{'email': u.email, 'pass': u.password, 'fname': u.fname, 'lname': u.lname }]
            return render_template('user_search.html', parent_list=q_result)
    return render_template('user_search.html')#, parent_list=q_result)


@app.route('/user/all/')
def user_all():
    results = []
    us = user_dao.find_all()
    for u in us:
        results.append({'email': u.email, 'pass': u.password, 'fname': u.fname, 'lname': u.lname })
    return render_template('user_all.html', parent_list=results)


@app.route('/job_opp/')
def job_opp():
    results = []
    jobs = jpdao.find_all()
    # print(jobs)
    for j in jobs:
        results.append({'title': j.title, 'reg date': j.reg_date, 'company(id)': j.comp_id})

    return render_template('job_opp.html', job_opps=results)
