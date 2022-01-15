import json
from datetime import datetime
import sys
import pendulum
import pyrebase
import datetime
import smtplib
import os
from twilio.rest import Client

firebaseConfig = {
    "apiKey": "AIzaSyCVRu69_Bg7MsVgq-Ti1mZUhj-NrUT6PwU",
    "authDomain": "covidmonitoring-a3d96.firebaseapp.com",
    "databaseURL": "https://covidmonitoring-a3d96-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "covidmonitoring-a3d96",
    "storageBucket": "covidmonitoring-a3d96.appspot.com",
    "messagingSenderId": "977720035469",
    "appId": "1:977720035469:web:3f85edf7b64bbc6b557ac4",
    "measurementId": "G-9YWD4QEL7X"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

database = {'admin': 'admin123', 'rhuadmin': 'rhu123', 'rhuKalayaan': 'kalayaan123'}


@app.route('/')
def system():
    return render_template('login.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    name1 = request.form['username']
    pwd = request.form['password']
    if request.method == 'POST':
        if name1 not in database:
            flash("Invalid Credentials. Try again!", "danger")
        elif database[name1] != pwd:
            flash("Invalid Credentials. Try again!", "danger")
        else:
            flash('Successfully logged in!', "success")
            return redirect(url_for('dashboard'))

    return render_template('login.html', error=error)


@app.route('/home', methods=('GET', 'POST'))
def home():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    error = None
    result = db.child("Patients").get()
    if result.val() == None:
        result2 = 0;
    else:
        result2 = db.child("Patients").get()
    return render_template('index.html', t=result2, a=date, b=date1, c=date2, d=date3, e=date4, error=error)


@app.route('/dashboard')
def dashboard():
    res = db.child("Recovered").get()
    res2 = db.child("Deceased").get()
    res3 = db.child("Active").get()
    res4 = db.child("Close Contact").get()
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    dateee = db.child("Patients").get()
    if res.val() == None:
        result2 = 0;
        result5 = 0;
    else:
        result2 = len(db.child('Recovered').get().val());
        result5 = db.child("Recovered").get();

    if res2.val() == None:
        result = 0;
        result6 = 0;

    else:
        result = len(db.child('Deceased').get().val())
        result6 = db.child("Deceased").get();
    if res3.val() == None:
        result3 = 0;
        result7 = 0;
    else:
        result3 = len(db.child('Active').get().val())
        result7 = db.child("Active").get();

    if dateee.val() == None:
        result4 = 0;
    else:
        result4 = db.child("Patients").get()
    if res4.val() == None:
        result8 = 0;
        res9 = 0;
    else:
        result8 = len(db.child('Close Contact').get().val())
        res9 = db.child("Close Contact").get()

    return render_template('dashboard.html', t1=result, t5=result3, t2=result2, t3=result5, t4=result6, ta=result4,
                           t6=result7, a=date, b=date1, c=date2, d=date3, e=date4, t7=result8, t8=res9)


@app.route('/Positive')
def Positive():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    dateee = db.child("Patients").get()
    res3 = db.child("Active").get()
    if res3.val() == None:
        result5 = 0;
    else:
        result5 = db.child("Active").get();
    if dateee.val() == None:
        result6 = 0;
    else:
        result6 = db.child("Patients").get();
    return render_template('Positive.html', t=result5, t1=result6, a=date, b=date1, c=date2, d=date3, e=date4, )


@app.route('/CloseContact')
def CloseContact():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    dateee = db.child("Patients").get()
    error = None
    res3 = db.child("Close Contact").get()
    if res3.val() == None:
        result5 = 0;
    else:
        result5 = db.child("Close Contact").get();
    if dateee.val() == None:
        result6 = 0;
    else:
        result6 = db.child("Patients").get();
    return render_template('CloseContact.html', t=result5, t1=result6, a=date, b=date1, c=date2, d=date3, e=date4,error=error )


@app.route('/Recovered')
def Recovered():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    dateee = db.child("Patients").get()
    res3 = db.child("Recovered").get()
    if dateee.val() == None:
        result6 = 0;
    else:
        result6 = db.child("Patients").get();
    if res3.val() == None:
        result7 = 0;
    else:
        result7 = db.child("Recovered").get();
    return render_template('recovered.html', t=result7, t1=result6, a=date, b=date1, c=date2, d=date3, e=date4, )


@app.route('/Deceased')
def Deceased():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    dateee = db.child("Patients").get()
    res3 = db.child("Deceased").get()
    if dateee.val() == None:
        result7 = 0;
    else:
        result7 = db.child("Patients").get();
    if res3.val() == None:
        result6 = 0;
    else:
        result6 = db.child("Deceased").get();
    return render_template('Deceased.html', t=result6, t1=result7, a=date, b=date1, c=date2, d=date3, e=date4, )


@app.route('/Monitoring')
def Monitoring():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    dateee = db.child("Patients").get()
    result = db.child("Patient Monitoring").get()
    if result.val() == None:
        result2 = 0;
    else:
        result2 = db.child("Patient Monitoring").get()
    return render_template('monitoringrecord.html', t=result2, t1=dateee, a=date, b=date1, c=date2, d=date3, e=date4, )


@app.route('/Swab')
def Swab():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    date = today.strftime('%d %B %Y')
    today1 = datetime.datetime.now() + datetime.timedelta(days=2)
    date1 = today1.strftime('%d %B %Y')
    today2 = datetime.datetime.now() + datetime.timedelta(days=3)
    date2 = today2.strftime('%d %B %Y')
    today3 = datetime.datetime.now() + datetime.timedelta(days=4)
    date3 = today3.strftime('%d %B %Y')
    today4 = datetime.datetime.now() + datetime.timedelta(days=5)
    date4 = today4.strftime('%d %B %Y')
    dateee = db.child("Patients").get()
    result = db.child("Patients").get()
    result2 = db.child("Close Contact").get()
    if result.val() == None:
        res = 0;
        if result2.val() == None:
            res1 = 0;
        else:
            res1 = db.child("Close Contact").get()
        return render_template('swab.html', t=res, t1=dateee, a=date, b=date1, c=date2, d=date3, e=date4, t2=res1)
    else:
        res = db.child("Patients").get();
        if result2.val() == None:
            res1 = 0;
        else:
            res1 = db.child("Close Contact").get()
        return render_template('swab.html', t=res, t1=dateee, a=date, b=date1, c=date2, d=date3, e=date4, t2=res1)


@app.route('/edit/<username>', methods=('GET', 'POST'))
def edit(username):
    from datetime import datetime
    error = None

    if request.method == 'POST':
        swabdate = request.form['date']
        today = datetime.today().strftime('%Y-%m-%d')
        swabtime = request.form['time']
        result = request.form['result']
        Mobile_num = request.form['mobile_num']
        if swabdate == "" or swabtime == "":
            flash("Please input date and time!", "danger")
        elif swabdate < today:
            flash("cannot input previous date!", "warning")
        else:
            if result == "Close Contact":
                db.child("Close Contact").child(username).update({
                    "swabSchedule": swabdate + " " + swabtime,
                })
                ccount_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(ccount_sid, token)

                message = client.messages.create(
                    to=Mobile_num,
                    messaging_service_sid='MG4d0dca8117cc86d69359a45a251af1ba',
                    body="Text Notification!  "
                         "RHU Kalayaan has set a date for your swab test! \n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
                )
            elif result == "Active":
                db.child("Patients").child(username).update({
                    "swabSchedule": swabdate + " " + swabtime,
                })
                ccount_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(ccount_sid, token)

                message = client.messages.create(
                    to=Mobile_num,
                    messaging_service_sid='MG4d0dca8117cc86d69359a45a251af1ba',
                    body="Text Notification!  "
                         "RHU Kalayaan has set a date for your swab test! \n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
                )
            flash("Schedule successfully added!")


            return redirect(url_for('Swab'))

    orderedDict = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()

    return render_template("UpdateSwab.html", data=orderedDict, error=error)
@app.route('/CCswab/<username>', methods=('GET', 'POST'))
def CCswab(username):
    from datetime import datetime
    error = None

    if request.method == 'POST':
        swabdate = request.form['date']
        today = datetime.today().strftime('%Y-%m-%d')
        swabtime = request.form['time']
        Mobile_num = request.form['mobile_num']
        if swabdate == "" or swabtime == "":
            flash("Please input date and time!", "danger")
        elif swabdate < today:
            flash("cannot input previous date!", "warning")
        else:

            db.child("Close Contact").child(username).update({
                "swabSchedule": swabdate + " " + swabtime,
            })

            ccount_sid = 'ACd129dfc0753b6b00366bbcbfb09286cf'
            token = "ff52ef5cc8831a56791be7e878d90d6b"
            client = Client(ccount_sid, token)

            message = client.messages.create(
                to=Mobile_num,
                from_='+12058583568',
                body="Text Notification!  "
                     "RHU Kalayaan has set a date for your swab test! \n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
            )
            flash("Schedule successfully added!")
            return redirect(url_for('Swab'))

    orderedDict = db.child("Close Contact").order_by_key().equal_to(username).limit_to_first(1).get()

    return render_template("UpdateCCSwab.html", data=orderedDict, error=error)
@app.route('/view1/<username>', methods=('GET', 'POST'))
def view1(username):
    if request.method == 'POST':
        Pname = request.form['patientName']
        PatientID = request.form['PatientID']
        Birthday = request.form['birthday']
        Age = request.form['age']
        Sex = request.form['sex']
        Mobile_num = request.form['mobile_num']
        Address = request.form['address']
        Condition = request.form['condition']
        CaseStatus = request.form['caseStatus']
        OtherIllness = request.form['otherIllness']
        EmergencyCPerson = request.form['emergencyCPerson']
        EmergencyContactNo = request.form['emergencyContact']
        username = request.form['username']
        CivilStatus = request.form['civilStatus']
        result = request.form['result']

        db.child("Close Contact").child(username).update({
            "result": result,
            "patientName": Pname,
            "patientID": PatientID,
            "birthday": Birthday,
            "age": Age,
            "sex": Sex,
            "mobile_num": Mobile_num,
            "address": Address,
            "condition": Condition,
            "caseStatus": CaseStatus,
            "otherIllness": OtherIllness,
            "emergencyCPerson": EmergencyCPerson,
            "emergencyContact": EmergencyContactNo,
            "username": username,
            "civilStatus": CivilStatus,
        })
        return redirect(url_for('home'))

    orderedDict = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("ViewPatientInfo.html", data=orderedDict)
@app.route('/viewCC/<username>', methods=('GET', 'POST'))
def viewCC(username):
    if request.method == 'POST':
        Pname = request.form['patientName']
        PatientID = request.form['PatientID']
        Birthday = request.form['birthday']
        Age = request.form['age']
        Sex = request.form['sex']
        Mobile_num = request.form['mobile_num']
        Address = request.form['address']
        Condition = request.form['condition']
        CaseStatus = request.form['caseStatus']
        OtherIllness = request.form['otherIllness']
        EmergencyCPerson = request.form['emergencyCPerson']
        EmergencyContactNo = request.form['emergencyContact']
        username = request.form['username']
        CivilStatus = request.form['civilStatus']
        result = request.form['result']

        db.child("Close Contact").child(username).update({
            "result": result,
            "patientName": Pname,
            "patientID": PatientID,
            "birthday": Birthday,
            "age": Age,
            "sex": Sex,
            "mobile_num": Mobile_num,
            "address": Address,
            "condition": Condition,
            "caseStatus": CaseStatus,
            "otherIllness": OtherIllness,
            "emergencyCPerson": EmergencyCPerson,
            "emergencyContact": EmergencyContactNo,
            "username": username,
            "civilStatus": CivilStatus,
        })
        return redirect(url_for('home'))

    orderedDict = db.child("Close Contact").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("ViewCloseContact.html", data=orderedDict)


@app.route('/view/<username>', methods=('GET', 'POST'))
def view(username):
    if request.method == 'POST':
        pname = request.form['Pname']
        pID = request.form['PatientID']
        swab = request.form['swabSchedule']
        uname = request.form['username']

        db.child("Patients").child(uname).update({
            "patientName": pname,
            "patientID": pID,
            "swabSchedule": swab,
            "username": uname
        })
        return redirect(url_for('Swab'))

    orderedDict = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("ViewSwabTest.html", data=orderedDict)
@app.route('/viewCCswab/<username>', methods=('GET', 'POST'))
def viewCCswab(username):
    if request.method == 'POST':
        pname = request.form['Pname']
        pID = request.form['PatientID']
        swab = request.form['swabSchedule']
        uname = request.form['username']

        db.child("Patients").child(uname).update({
            "patientName": pname,
            "patientID": pID,
            "swabSchedule": swab,
            "username": uname
        })
        return redirect(url_for('Swab'))

    orderedDict = db.child("Close Contact").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("ViewCCSwab.html", data=orderedDict)


@app.route('/view2/<PatientID>', methods=('GET', 'POST'))
def view2(PatientID):
    res3 = db.child(PatientID).get()

    return render_template('ViewMonitoringRecord.html', t=res3)


@app.route('/edit1/<username>', methods=('GET', 'POST'))
def edit1(username):
    from datetime import datetime
    dt = datetime.today().strftime("%B %d, %Y %H:%M:%S")

    today = datetime.today().strftime('%d %B %Y ')
    today4 = datetime.today().strftime('%m/%d/%Y')
    today2 = datetime.today().strftime('%B %Y ')
    today1 = datetime.today().strftime('%Y-%m-%d')

    if request.method == 'POST':
        dayAdmitted = request.form['dayAdmitted']
        estimatedDateRecovery = request.form['estimatedDateRecovery']
        password = request.form['password']
        security = request.form['security']
        securityQues = request.form['securityQues']
        swabSchedule = "Your Swab schedule is not yet available"
        Pname = request.form['patientName']
        PatientID = request.form['patientID']
        Birthday = request.form['birthday']
        Age = request.form['age']
        Sex = request.form['sex']
        Mobile_num = request.form['mobile_num']
        Condition = request.form['condition']
        CaseStatus = request.form['caseStatus']
        OtherIllness = request.form['otherIllness']
        EmergencyCPerson = request.form['emergencyCPerson']
        emergencyContact = request.form['emergencyContact']
        username = request.form['username']
        CivilStatus = request.form['civilStatus']
        Address = request.form['address']
        dateAdmitted = request.form['dateAdmitted']
        housenum = request.form['housenum']
        city = request.form['city']
        province = request.form['province']
        PIcontact = request.form['PIcontact']
        NatureOfContact = request.form['NOcontact']

        SignAndSymp = request.form['SignAndSymp']
        doConsultation = request.form['doConsultation']
        result = request.form['result']

        if result == "Recovered":
            db.child(result).child(PatientID).set({"result": result,
                                                   "password": password,
                                                   "security": security,
                                                   "securityQues": securityQues,
                                                   "swabSchedule": swabSchedule,
                                                   "dayAdmitted": dayAdmitted,
                                                   "estimatedDateRecovery": estimatedDateRecovery,
                                                   "patientName": Pname,
                                                   "patientID": PatientID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                                   "sex": Sex,
                                                   "mobile_num": Mobile_num,
                                                   "address": Address,
                                                   "housenum": housenum,
                                                   "city": city,
                                                   "province": province,
                                                   "condition": Condition,
                                                   "caseStatus": CaseStatus,
                                                   "otherIllness": OtherIllness,
                                                   "emergencyCPerson": EmergencyCPerson,
                                                   "emergencyContact": emergencyContact,
                                                   "username": username,
                                                   "civilStatus": CivilStatus,
                                                   "dateAdmitted": dateAdmitted,
                                                   "dayRecovered": today4,
                                                   "PIncontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,
                                                    "dateRecovered":today,
                                                   })
            db.child("Active").child(PatientID).remove()
            db.child("Patients").child(username).update({
                "result": result,
                "password": password,
                "security": security,
                "securityQues": securityQues,
                "swabSchedule": swabSchedule,
                "dayAdmitted": dayAdmitted,
                "estimatedDateRecovery": estimatedDateRecovery,
                "patientName": Pname,
                "patientID": PatientID,
                "birthday": Birthday,
                "age": Age,
                "sex": Sex,
                "mobile_num": Mobile_num,
                "address": Address,
                "housenum": housenum,
                "city": city,
                "province": province,
                "condition": Condition,
                "caseStatus": CaseStatus,
                "otherIllness": OtherIllness,
                "emergencyCPerson": EmergencyCPerson,
                "emergencyContact": emergencyContact,
                "username": username,
                "civilStatus": CivilStatus,
                "dateAdmitted": dateAdmitted,
                "dayRecovered": today4,
                "PIncontact": PIcontact,
                "NatureOfContact": NatureOfContact,
                "SignAndSymp": SignAndSymp,
                "doConsultation": doConsultation,

            })

        elif result == "Deceased":
            COD = request.form['CauseofDeath']
            dateandtime = request.form['dateandtime']
            db.child(result).child(PatientID).set({"result": result,
                                                   "patientName": Pname,
                                                   "patientID": PatientID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                                   "sex": Sex,
                                                   "mobile_num": Mobile_num,
                                                   "address": Address,
                                                   "housenum": housenum,
                                                   "city": city,
                                                   "province": province,
                                                   "condition": Condition,
                                                   "caseStatus": CaseStatus,
                                                   "otherIllness": OtherIllness,
                                                   "emergencyCPerson": EmergencyCPerson,
                                                   "emergencyContact": emergencyContact,
                                                   "username": username,
                                                   "civilStatus": CivilStatus,
                                                   "dayDied": today4,
                                                   "dateAdmitted": dateAdmitted,
                                                   "dateDied": today,
                                                   "CauseOfDeath": COD,
                                                   "DTofDeath": dateandtime,
                                                   "PIcontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,

                                                   })
            db.child("Active").child(PatientID).remove()
            db.child("Patients").child(username).update({
                "result": result,
                "CauseOfDeath": COD,
                "patientName": Pname,
                "patientID": PatientID,
                "birthday": Birthday,
                "age": Age,
                "sex": Sex,
                "mobile_num": Mobile_num,
                "address": Address,
                "housenum": housenum,
                "city": city,
                "province": province,
                "condition": Condition,
                "caseStatus": CaseStatus,
                "otherIllness": OtherIllness,
                "emergencyCPerson": EmergencyCPerson,
                "emergencyContact": emergencyContact,
                "username": username,
                "civilStatus": CivilStatus,
                "dateAdmitted": dateAdmitted,
                "PIcontact": PIcontact,
                "SignAndSymp": SignAndSymp,
                "doConsultation": doConsultation,
                "NatureOfContact": NatureOfContact,
                "DTofDeath": dateandtime,
            })
        elif result == "Active":
            db.child(result).child(PatientID).set({"result": result,
                                                   "password": password,
                                                   "security": security,
                                                   "securityQues": securityQues,
                                                   "swabSchedule": swabSchedule,
                                                   "dayAdmitted": dayAdmitted,
                                                   "estimatedDateRecovery": estimatedDateRecovery,
                                                   "patientName": Pname,
                                                   "patientID": PatientID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                                   "sex": Sex,
                                                   "mobile_num": Mobile_num,
                                                   "address": Address,
                                                   "housenum": housenum,
                                                   "city": city,
                                                   "province": province,
                                                   "condition": Condition,
                                                   "caseStatus": CaseStatus,
                                                   "otherIllness": OtherIllness,
                                                   "emergencyCPerson": EmergencyCPerson,
                                                   "emergencyContact": emergencyContact,
                                                   "username": username,
                                                   "civilStatus": CivilStatus,
                                                   "dateAdmitted": dateAdmitted,
                                                   "dayRecovered": today4,
                                                   "PIncontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,


                                                   })
            db.child("Recovered").child(PatientID).remove()
            db.child("Close Contact").child(PatientID).remove()
            db.child("Patients").child(username).update({
                "result": result,
                "password": password,
                "security": security,
                "securityQues": securityQues,
                "swabSchedule": swabSchedule,
                "dayAdmitted": dayAdmitted,
                "estimatedDateRecovery": estimatedDateRecovery,
                "patientName": Pname,
                "patientID": PatientID,
                "birthday": Birthday,
                "age": Age,
                "sex": Sex,
                "mobile_num": Mobile_num,
                "address": Address,
                "housenum": housenum,
                "city": city,
                "province": province,
                "condition": Condition,
                "caseStatus": CaseStatus,
                "otherIllness": OtherIllness,
                "emergencyCPerson": EmergencyCPerson,
                "emergencyContact": emergencyContact,
                "username": username,
                "civilStatus": CivilStatus,
                "dateAdmitted": dateAdmitted,
                "dayRecovered": today4,
                "PIncontact": PIcontact,
                "NatureOfContact": NatureOfContact,
                "SignAndSymp": SignAndSymp,
                "doConsultation": doConsultation,

            })
        elif result == "Close Contact":
            db.child(result).child(PatientID).set({"result": result,
                                                   "patientName": Pname,
                                                   "patientID": PatientID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                                   "sex": Sex,
                                                   "mobile_num": Mobile_num,
                                                   "address": Address,
                                                   "housenum": housenum,
                                                   "city": city,
                                                   "province": province,
                                                   "condition": Condition,
                                                   "caseStatus": CaseStatus,
                                                   "otherIllness": OtherIllness,
                                                   "emergencyCPerson": EmergencyCPerson,
                                                   "emergencyContact": emergencyContact,
                                                   "username": username,
                                                   "civilStatus": CivilStatus,
                                                   "dateAdmitted": dateAdmitted,
                                                   "dayRecovered": today4,
                                                   "NatureOfContact": NatureOfContact,
                                                   "PIcontact": PIcontact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,

                                                   })
        flash("Patient Status Updated Successfully!")
        db.child("Patients").child(username).update({
            "result": result,
            "patientName": Pname,
            "patientID": PatientID,
            "birthday": Birthday,
            "age": Age,
            "sex": Sex,
            "mobile_num": Mobile_num,
            "address": Address,
            "housenum": housenum,
            "city": city,
            "province": province,
            "condition": Condition,
            "caseStatus": CaseStatus,
            "otherIllness": OtherIllness,
            "emergencyCPerson": EmergencyCPerson,
            "emergencyContact": emergencyContact,
            "username": username,
            "civilStatus": CivilStatus,
            "dateAdmitted": dateAdmitted,
            "PIcontact": PIcontact,
            "SignAndSymp": SignAndSymp,
            "doConsultation": doConsultation,
            "NatureOfContact": NatureOfContact,
        })
        return redirect(url_for('home'))

    orderedDict = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()

    return render_template("UpdatePatientInfo.html", data=orderedDict)


@app.route('/editCC/<username>', methods=('GET', 'POST'))
def editCC(username):
    from datetime import datetime
    dt = datetime.today().strftime("%B %d, %Y %H:%M:%S")

    today = datetime.today().strftime('%d %B %Y ')
    today4 = datetime.today().strftime('%m/%d/%Y')
    today2 = datetime.today().strftime('%B %Y ')
    today1 = datetime.today().strftime('%Y-%m-%d')
    res = db.child("Patients").get()
    if res.val() == None:
        res1 = 0;
    else:
        res1 = len(db.child('Patients').get().val())
    if request.method == 'POST':
        Pname = request.form['patientName']
        PatientID = request.form['patientID']
        Birthday = request.form['birthday']
        Age = request.form['age']
        Sex = request.form['sex']
        Mobile_num = request.form['mobile_num']
        Condition = request.form['condition']
        CaseStatus = request.form['caseStatus']
        OtherIllness = request.form['otherIllness']
        EmergencyCPerson = request.form['emergencyCPerson']
        emergencyContact = request.form['emergencyContact']
        username = request.form['username']
        CivilStatus = request.form['civilStatus']
        Address = request.form['address']
        dateAdmitted = request.form['dateAdmitted']
        housenum = request.form['housenum']
        city = request.form['city']
        province = request.form['province']
        PIcontact = request.form['PIcontact']
        NatureOfContact = request.form['NOcontact']
        SignAndSymp = request.form['SignAndSymp']
        doConsultation = request.form['doConsultation']
        result = request.form['result']
        dayAdmitted = request.form['dayAdmitted']
        estimatedDateRecovery = request.form['estimatedDateRecovery']
        password = request.form['password']
        security = request.form['security']
        securityQues = request.form['securityQues']
        res3=str(res1+1)
        pID = "KP-" + res3;
        swabSchedule = "Your Swab schedule is not yet available"

        if result == "Active":
            db.child(result).child(pID).set({"result": result,
                                                   "password": password,
                                                   "security": security,
                                                   "securityQues": securityQues,
                                                   "swabSchedule": swabSchedule,
                                                   "dayAdmitted": dayAdmitted,
                                                   "estimatedDateRecovery": estimatedDateRecovery,
                                                   "patientName": Pname,
                                                   "patientID": pID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                                   "sex": Sex,
                                                   "mobile_num": Mobile_num,
                                                   "address": Address,
                                                   "housenum": housenum,
                                                   "city": city,
                                                   "province": province,
                                                   "condition": Condition,
                                                   "caseStatus": CaseStatus,
                                                   "otherIllness": OtherIllness,
                                                   "emergencyCPerson": EmergencyCPerson,
                                                   "emergencyContact": emergencyContact,
                                                   "username": username,
                                                   "civilStatus": CivilStatus,
                                                   "dateAdmitted": dateAdmitted,
                                                   "dayRecovered": today4,
                                                   "PIncontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,
                                                   })
            db.child("Patients").child(username).set({"result": result,
                                                       "password": password,
                                                       "security": security,
                                                       "securityQues": securityQues,
                                                       "swabSchedule": swabSchedule,
                                                       "dayAdmitted": dayAdmitted,
                                                       "estimatedDateRecovery": estimatedDateRecovery,
                                                       "patientName": Pname,
                                                       "patientID": pID,
                                                       "birthday": Birthday,
                                                       "age": Age,
                                                       "sex": Sex,
                                                       "mobile_num": Mobile_num,
                                                       "address": Address,
                                                       "housenum": housenum,
                                                       "city": city,
                                                       "province": province,
                                                       "condition": Condition,
                                                       "caseStatus": CaseStatus,
                                                       "otherIllness": OtherIllness,
                                                       "emergencyCPerson": EmergencyCPerson,
                                                       "emergencyContact": emergencyContact,
                                                       "username": username,
                                                       "civilStatus": CivilStatus,
                                                       "dateAdmitted": dateAdmitted,
                                                       "dayRecovered": today4,
                                                       "PIncontact": PIcontact,
                                                       "NatureOfContact": NatureOfContact,
                                                       "SignAndSymp": SignAndSymp,
                                                       "doConsultation": doConsultation,

                                                       })
            db.child("Close Contact").child(username).remove()
            db.child("Patient Monitoring").child(PatientID).remove()
            flash('Successfully logged in!', "success")
        elif result == "Cleared":
            db.child("Close Contact").child(username).update({
                "result": result,
            })
            db.child("Patient Monitoring").child(PatientID).remove()
            flash('Successfully logged in!', "success")
        return redirect(url_for('CloseContact'))

    orderedDict = db.child("Close Contact").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("UpdateCloseContact.html", data=orderedDict)


@app.route('/logout')
def logout():
    flash('Successfully logged out!', "success")
    return redirect('/')


@app.route("/post/<username>")
def post(username):
    orderedDict = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()
    print(orderedDict, file=sys.stderr)

    return render_template("UpdateSwab.html", data=orderedDict)


@app.route("/post1/<username>")
def post1(username):
    orderedDict1 = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()
    print(orderedDict1, file=sys.stderr)

    return render_template("edit1.html", data=orderedDict1)


@app.route("/post2/<username>")
def post2(username):
    orderedDict1 = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()
    print(orderedDict1, file=sys.stderr)

    return render_template("ViewSwabTest.html", data=orderedDict1)


@app.route("/post3/<username>")
def post3(username):
    orderedDict = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()
    print(orderedDict, file=sys.stderr)

    return render_template("ViewPatientInfo.html", data=orderedDict)


if __name__ == '__main__':
    app.run()
from math import ceil


def week_of_month(dt):
    first_day = dt.replace(day=1)

    dom = dt.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom / 7.0))
