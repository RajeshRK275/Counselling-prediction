from enum import unique
from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import pickle
import numpy as np

app = Flask(__name__)
cit_eee_model_1 = pickle.load(open('cit_eee_model.pkl','rb'))
gct_eee_model_1 = pickle.load(open('gct_eee_model.pkl','rb'))
kct_eee_model_1 = pickle.load(open('kct_eee_model.pkl','rb'))
psg_eee_model_1 = pickle.load(open('psg_eee_model.pkl','rb'))
cit_it_model_1 = pickle.load(open('cit_it_model.pkl','rb'))
gct_it_model_1 = pickle.load(open('gct_it_model.pkl','rb'))
kct_it_model_1 = pickle.load(open('kct_it_model.pkl','rb'))
psg_it_model_1 = pickle.load(open('psg_it_model.pkl','rb'))
cit_ece_model_1 = pickle.load(open('cit_ece_model.pkl','rb'))
gct_ece_model_1 = pickle.load(open('gct_ece_model.pkl','rb'))
kct_ece_model_1 = pickle.load(open('kct_ece_model.pkl','rb'))
psg_ece_model_1 = pickle.load(open('psg_ece_model.pkl','rb'))
cit_mech_model_1 = pickle.load(open('cit_mech_model.pkl','rb'))
gct_mech_model_1 = pickle.load(open('gct_mech_model.pkl','rb'))
kct_mech_model_1 = pickle.load(open('kct_mech_model.pkl','rb'))
psg_mech_model_1 = pickle.load(open('psg_mech_model.pkl','rb'))
cit_civil_model_1 = pickle.load(open('cit_civil_model.pkl','rb'))
gct_civil_model_1 = pickle.load(open('gct_civil_model.pkl','rb'))
kct_civil_model_1 = pickle.load(open('kct_civil_model.pkl','rb'))
psg_civil_model_1 = pickle.load(open('psg_civil_model.pkl','rb'))

bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password, 12)


@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('result.html', result1="0%", result2="0%", result3="0%", result4="0%")
    else:
        return render_template('index.html', message="College Admission Prediction System")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(name=request.form['name'],
                                email=request.form['email'],
                                password=request.form['password']))
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        n = request.form['name']
        p = request.form['password']
        data = User.query.filter_by(name=n).first()
        if data is not None and bcrypt.check_password_hash(
            data.password, p):
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        course = request.form['course']
        marks = request.form['marks']
        cutoff = request.form['cutoff']
        cur_year = 2022
        if cutoff == 200:
            return render_template('result.html', result1= "100 %", result2="100 %", result3="100 %", result4="100 %")


        if course == "it":
            cit_it_result = cit_it_model_1.predict([[marks,cutoff,cur_year,197,184.75]])
            converted_1 = float(cit_it_result[0])
            if converted_1 > 100:
                converted_1 = 100
            converted_1=("%.2f" % round(converted_1, 2))
            converted_1 = str(converted_1)+" %"
            gct_it_result = gct_it_model_1.predict([[marks,cutoff,cur_year,194.75,178.5]])
            converted_2 = float(gct_it_result[0])
            if converted_2 > 100:
                converted_2 = 100
            converted_2=("%.2f" % round(converted_2, 2))
            converted_2 = str(converted_2)+" %"
            kct_it_result = kct_it_model_1.predict([[marks,cutoff,cur_year,193,162.75]])
            converted_3 = float(kct_it_result[0])
            if converted_3 > 100:
                converted_3 = 100
            converted_3=("%.2f" % round(converted_3, 2))
            converted_3 = str(converted_3)+" %"
            psg_it_result = psg_it_model_1.predict([[marks,cutoff,cur_year,197,189]])
            converted_4 = float(psg_it_result[0])
            if converted_4 > 100:
                converted_4 = 100
            converted_4=("%.2f" % round(converted_4, 2))
            converted_4 = str(converted_4)+" %"
            return render_template('result.html', result1= converted_1, result2=converted_4, result3=converted_3, result4=converted_2)


        if course == "eee":
            cit_eee_result = cit_eee_model_1.predict([[marks,cutoff,cur_year,198,191]])
            converted_1 = float(cit_eee_result[0])
            if converted_1 > 100:
                converted_1 = 100
            converted_1=("%.2f" % round(converted_1, 2))
            converted_1 = str(converted_1)+" %"
            gct_eee_result = gct_eee_model_1.predict([[marks,cutoff,cur_year,195,180]])
            converted_2 = float(gct_eee_result[0])
            if converted_2 > 100:
                converted_2 = 100
            converted_2=("%.2f" % round(converted_2, 2))
            converted_2 = str(converted_2)+" %"
            kct_eee_result = kct_eee_model_1.predict([[marks,cutoff,cur_year,196,177]])
            converted_3 = float(kct_eee_result[0])
            if converted_3 > 100:
                converted_3 = 100
            converted_3=("%.2f" % round(converted_3, 2))
            converted_3 = str(converted_3)+" %"
            psg_eee_result = psg_eee_model_1.predict([[marks,cutoff,cur_year,198.25,186.25]])
            converted_4 = float(psg_eee_result[0])
            if converted_4 > 100:
                converted_4 = 100
            converted_4=("%.2f" % round(converted_4, 2))
            converted_4 = str(converted_4)+" %"
            return render_template('result.html', result1= converted_1, result2=converted_4, result3=converted_3, result4=converted_2)

        if course == "ece":
            cit_ece_result = cit_ece_model_1.predict([[marks,cutoff,cur_year,198.25,189.75]])
            converted_1 = float(cit_ece_result[0])
            if converted_1 > 100:
                converted_1 = 100
            converted_1=("%.2f" % round(converted_1, 2))
            converted_1 = str(converted_1)+" %"
            gct_ece_result = gct_ece_model_1.predict([[marks,cutoff,cur_year,196.25,185.5]])
            converted_2 = float(gct_ece_result[0])
            if converted_2 > 100:
                converted_2 = 100
            converted_2=("%.2f" % round(converted_2, 2))
            converted_2 = str(converted_2)+" %"
            kct_ece_result = kct_ece_model_1.predict([[marks,cutoff,cur_year,193.25,180]])
            converted_3 = float(kct_ece_result[0])
            if converted_3 > 100:
                converted_3 = 100
            converted_3=("%.2f" % round(converted_3, 2))
            converted_3 = str(converted_3)+" %"
            psg_ece_result = psg_ece_model_1.predict([[marks,cutoff,cur_year,199.25,193]])
            converted_4 = float(psg_ece_result[0])
            if converted_4 > 100:
                converted_4 = 100
            converted_4=("%.2f" % round(converted_4, 2))
            converted_4 = str(converted_4)+" %"
            return render_template('result.html', result1= converted_1, result2=converted_4, result3=converted_3, result4=converted_2)

        if course == "mech":
            cit_mech_result = cit_mech_model_1.predict([[marks,cutoff,cur_year,195.33,178.25]])
            converted_1 = float(cit_mech_result[0])
            if converted_1 > 100:
                converted_1 = 100
            converted_1=("%.2f" % round(converted_1, 2))
            converted_1 = str(converted_1)+" %"
            gct_mech_result = gct_mech_model_1.predict([[marks,cutoff,cur_year,194.75,178.5]])
            converted_2 = float(gct_mech_result[0])
            if converted_2 > 100:
                converted_2 = 100
            converted_2=("%.2f" % round(converted_2, 2))
            converted_2 = str(converted_2)+" %"
            kct_mech_result = kct_mech_model_1.predict([[marks,cutoff,cur_year,190.25,184.75]])
            converted_3 = float(kct_mech_result[0])
            if converted_3 > 100:
                converted_3 = 100
            converted_3=("%.2f" % round(converted_3, 2))
            converted_3 = str(converted_3)+" %"
            psg_mech_result = psg_mech_model_1.predict([[marks,cutoff,cur_year,197,180]])
            converted_4 = float(psg_mech_result[0])
            if converted_4 > 100:
                converted_4 = 100
            converted_4=("%.2f" % round(converted_4, 2))
            converted_4 = str(converted_4)+" %"
            return render_template('result.html', result1= converted_1, result2=converted_4, result3=converted_3, result4=converted_2)

        if course == "civil":
            cit_civil_result = cit_civil_model_1.predict([[marks,cutoff,cur_year,193.5,169.25]])
            converted_1 = float(cit_civil_result[0])
            if converted_1 > 100:
                converted_1 = 100
            converted_1=("%.2f" % round(converted_1, 2))
            converted_1 = str(converted_1)+" %"
            gct_civil_result = gct_civil_model_1.predict([[marks,cutoff,cur_year,191,188]])
            converted_2 = float(gct_civil_result[0])
            if converted_2 > 100:
                converted_2 = 100
            converted_2=("%.2f" % round(converted_2, 2))
            converted_2 = str(converted_2)+" %"
            kct_civil_result = kct_civil_model_1.predict([[marks,cutoff,cur_year,186.25,177.5]])
            converted_3 = float(kct_civil_result[0])
            if converted_3 > 100:
                converted_3 = 100
            converted_3=("%.2f" % round(converted_3, 2))
            converted_3 = str(converted_3)+" %"
            psg_civil_result = psg_civil_model_1.predict([[marks,cutoff,cur_year,199,189.25]])
            converted_4 = float(psg_civil_result[0])
            if converted_4 > 100:
                converted_4 = 100
            converted_4=("%.2f" % round(converted_4, 2))
            converted_4 = str(converted_4)+" %"
            return render_template('result.html', result1= converted_1, result2=converted_4, result3=converted_3, result4=converted_2)



@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))


if(__name__ == '__main__'):
    app.secret_key = "NarutoUzumaki"
    db.create_all()
    app.run()
