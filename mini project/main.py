from flask import Flask,render_template,request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
import MySQLdb.cursors


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rabia123$@localhost/fyp'
app.config['SECRET_KEY'] = "Rabia"
db = SQLAlchemy(app)

class students(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    groupleader = db.Column(db.String(120), unique=False, nullable=False)
    institution = db.Column(db.String(120), unique=False, nullable=False)
    nameofdp = db.Column(db.String(120), unique=False, nullable=False)
    headofdp = db.Column(db.String(120), unique=False, nullable=False)
    psupervisor = db.Column(db.String(120), unique=False, nullable=False)
    npfgroupmembers = db.Column(db.String(120), unique=False, nullable=False)
    pgmofstudy = db.Column(db.String(120), unique=False, nullable=False)
    ptitle = db.Column(db.String(120), unique=False, nullable=False)
    pdiscription = db.Column(db.String(120), unique=False, nullable=False)


@app.route("/", methods=['GET'])
def index():
    return render_template("home.html")
@app.route("/newgroup", methods=['GET'])
def newgroup():
    data=students.query.order_by(students.sno).all()
    return render_template("newgroup.html",data=data)

@app.route("/form", methods=['POST','GET'])
def form():
    if request.method == 'POST':
        groupleader = request.form.get('groupleader')
        institution = request.form.get('institution')
        nameofdp = request.form.get('nameofdp')
        headofdp = request.form.get('headofdp')
        psupervisor = request.form.get('psupervisor')
        npfgroupmembers = request.form.get('npfgroupmembers')
        pgmofstudy = request.form.get('pgmofstudy')
        ptitle = request.form.get('ptitle')
        pdiscription = request.form.get('pdiscription')
        stud = students(groupleader=groupleader, institution=institution, nameofdp=nameofdp, headofdp=headofdp,
                     psupervisor=psupervisor, npfgroupmembers=npfgroupmembers, pgmofstudy=pgmofstudy,
                     ptitle=ptitle, pdiscription=pdiscription)
        db.session.add(stud)
        db.session.commit()
    
        return redirect("/newgroup")
    return render_template("form.html")
    


@app.route("/home", methods=['GET'])
def home():
    if session.get('username'):
        return render_template("index.html")
    else:
        return render_template("login.html")


@app.route("/login", methods=['POST','GET'])
def intro():
    msg = "Login first"
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "rabia" and password=="Rabia":
            session['username'] = "rabia"
            return render_template("index.html")
        else:
            msg = "Incorrect Usrname and Password"
        return render_template("login.html", msg = msg)
    else:
        return render_template("login.html", msg=msg)

@app.route("/update/<int:sno>/", methods=['POST','GET'])
def update(sno):
    if request.method == 'POST':
        groupleader = request.form.get('groupleader')
        institution = request.form.get('institution')
        nameofdp = request.form.get('nameofdp')
        headofdp = request.form.get('headofdp')
        psupervisor = request.form.get('psupervisor')
        npfgroupmembers = request.form.get('npfgroupmembers')
        pgmofstudy = request.form.get('pgmofstudy')
        ptitle = request.form.get('ptitle')
        pdiscription = request.form.get('pdiscription')

        stud = students.query.filter_by(sno = sno).first()
        stud.groupleader =groupleader
        stud.institution= institution
        stud.nameofdp = nameofdp
        stud.headofdp=headofdp
        stud.psupervisor = psupervisor
        stud.npfgroupmembers= npfgroupmembers
        stud.pgmofstudy= pgmofstudy
        stud.ptitle= ptitle
        stud.pdiscription= pdiscription
       
        
        db.session.commit()
        return redirect(url_for('newgroup'))
    else:
        stud = students.query.filter(students.sno == sno).first()
        return render_template("update.html", stud=stud, sno=sno)
@app.route("/delete/<int:sno>/", methods=['POST','GET'])
def delete(sno):
      
        group = students.query.get(sno)
        db.session.delete(group)
        db.session.commit()
        return redirect(url_for('newgroup'))       



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
