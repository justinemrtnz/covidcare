import json
from datetime import datetime
import sys
import pyrebase
import datetime
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
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
    res5 = db.child("probable").get()
    res6 = db.child("Suspected").get()

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
    if res5.val() == None:
        result10=0;
        result11 = 0;
    else:
        result10 = len(db.child('probable').get().val());
        result11 = db.child("probable").get();
    if res6.val() == None:
        result12 = 0;
        result13 = 0;
    else:
        result12 = len(db.child('Suspected').get().val());
        result13 = db.child("Suspected").get();
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
                           t6=result7, a=date, b=date1, c=date2, d=date3, e=date4, t7=result8, t8=res9, t9 = result10,t10 = result11, t11 = result12 , t12 = result13)


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
@app.route('/Probable')
def Probable():
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
    res3 = db.child("probable").get()
    if res3.val() == None:
        result5 = 0;
    else:
        result5 = db.child("probable").get();
    if dateee.val() == None:
        result6 = 0;
    else:
        result6 = db.child("Patients").get();
    return render_template('Probable.html', t=result5, t1=result6, a=date, b=date1, c=date2, d=date3, e=date4,error=error )
@app.route('/Suspected')
def Suspected():
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
    res3 = db.child("Suspected").get()
    if res3.val() == None:
        result5 = 0;
    else:
        result5 = db.child("Suspected").get();
    if dateee.val() == None:
        result6 = 0;
    else:
        result6 = db.child("Patients").get();
    return render_template('Suspected.html', t=result5, t1=result6, a=date, b=date1, c=date2, d=date3, e=date4,error=error )

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
    result3 = db.child("probable").get()
    result4 = db.child("Suspected").get()
    if result3.val() == None:
        res3 = 0;
    else:
        res3 = db.child("probable").get()
    if result4.val() == None:
        res4 = 0;
    else:
        res4 = db.child("Suspected").get()


    if result.val() == None:
        res = 0;
        if result2.val() == None:
            res1 = 0;
        else:
            res1 = db.child("Close Contact").get()
        return render_template('swab.html', t=res, t1=dateee, a=date, b=date1, c=date2, d=date3, e=date4, t2=res1 , t3 = res3, t4 = res4)
    else:
        res = db.child("Patients").get();
        if result2.val() == None:
            res1 = 0;
        else:
            res1 = db.child("Close Contact").get()
        return render_template('swab.html', t=res, t1=dateee, a=date, b=date1, c=date2, d=date3, e=date4, t2=res1 , t3 = res3 ,t4 = res4)


@app.route('/edit/<username>', methods=('GET', 'POST'))
def edit(username):
    import datetime

    error = None

    if request.method == 'POST':
        swabdate = request.form['date']
        today = datetime.datetime.now() + datetime.timedelta(days=1)
        date = today.strftime('%Y-%m-%d')
        swabtime = request.form['time']
        result = request.form['result']
        Mobile_num = request.form['mobile_num']
        from datetime import datetime
        ate_time_obj1 = datetime.strptime(swabtime, '%H:%M').strftime('%I:%M %p')

        if swabdate == "" or swabtime == "":
            flash("Please input date and time!", "danger")
        elif swabdate < date:
            flash("cannot input previous date!", "warning")
        else:
            if result == "Close Contact":
                db.child("Close Contact").child(username).update({
                    "swabSchedule": swabdate + " Time: " + ate_time_obj1,
                })
                count_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(count_sid, token)

                count_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(count_sid, token)

                message = client.messages.create(
                    from_='+19034939890',
                    to=Mobile_num,
                    body="Text Notification!  \n"
                             "RHU Kalayaan has set a date for your swab test!\n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
                )
                flash("Schedule successfully added!")
                return redirect(url_for('Swab'))

            elif result == "Active":
                db.child("Patients").child(username).update({
                    "swabSchedule": swabdate + " Time: " + ate_time_obj1,
                })
                count_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(count_sid, token)


                count_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(count_sid, token)

                message = client.messages.create(
                     from_='+19034939890',
                    to=Mobile_num,
                    body="Text Notification!  \n"
                             "RHU Kalayaan has set a date for your swab test!\n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
                )
                flash("Schedule successfully added!")
                return redirect(url_for('Swab'))

    orderedDict = db.child("Patients").order_by_key().equal_to(username).limit_to_first(1).get()

    return render_template("UpdateSwab.html", data=orderedDict, error=error)

@app.route('/CCswab/<username>', methods=('GET', 'POST'))
def CCswab(username):
    import datetime
    error = None

    if request.method == 'POST':
        today = datetime.datetime.now() + datetime.timedelta(days=1)
        date = today.strftime('%Y-%m-%d')
        swabdate = request.form['date']
        from datetime import datetime

        today = datetime.today().strftime('%Y-%m-%d')
        swabtime = request.form['time']
        Mobile_num = request.form['mobile_num']
        ate_time_obj1 = datetime.strptime(swabtime, '%H:%M').strftime('%I:%M %p')

        if swabdate == "" or swabtime == "":
            flash("Please input date and time!", "danger")
        elif swabdate < date:
            flash("cannot input previous date!", "warning")
        else:

            db.child("Close Contact").child(username).update({
                "swabSchedule": swabdate + " Time: " + ate_time_obj1,
            })

            try:
                count_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(count_sid, token)

                message = client.messages.create(
                    from_='+19034939890',
                    to=Mobile_num,
                    body="Text Notification!  \n"
                         "RHU Kalayaan has set a date for your swab test!\n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
                )
                flash("Schedule successfully added!")
                return redirect(url_for('Swab'))
            except TwilioRestException as e:
                flash("Phone Number Cannot reach", "danger")

    orderedDict = db.child("Close Contact").order_by_key().equal_to(username).limit_to_first(1).get()

    return render_template("UpdateCCSwab.html", data=orderedDict, error=error)
@app.route('/Pswab/<username>', methods=('GET', 'POST'))
def Pswab(username):
    import datetime
    error = None

    if request.method == 'POST':
        today = datetime.datetime.now() + datetime.timedelta(days=1)
        date = today.strftime('%Y-%m-%d')
        swabdate = request.form['date']
        from datetime import datetime

        today = datetime.today().strftime('%Y-%m-%d')
        swabtime = request.form['time']
        Mobile_num = request.form['mobile_num']
        ate_time_obj1 = datetime.strptime(swabtime, '%H:%M').strftime('%I:%M %p')

        if swabdate == "" or swabtime == "":
            flash("Please input date and time!", "danger")
        elif swabdate < date:
            flash("cannot input previous date!", "warning")
        else:

            db.child("probable").child(username).update({
                "swabSchedule": swabdate + " Time: " + ate_time_obj1,
            })

            try:
                count_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(count_sid, token)

                message = client.messages.create(
                    from_='+19034939890',
                    to=Mobile_num,
                    body="Text Notification!  \n"
                         "RHU Kalayaan has set a date for your swab test!\n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
                )
                flash("Schedule successfully added!")
                return redirect(url_for('Swab'))
            except TwilioRestException as e:
                flash("Phone Number Cannot reach", "danger")

    orderedDict = db.child("probable").order_by_key().equal_to(username).limit_to_first(1).get()

    return render_template("UpdateCCSwab.html", data=orderedDict, error=error)
@app.route('/Sswab/<username>', methods=('GET', 'POST'))
def Sswab(username):
    import datetime
    error = None

    if request.method == 'POST':
        today = datetime.datetime.now() + datetime.timedelta(days=1)
        date = today.strftime('%Y-%m-%d')
        swabdate = request.form['date']
        today = datetime.today().strftime('%Y-%m-%d')
        swabtime = request.form['time']
        Mobile_num = request.form['mobile_num']
        from datetime import datetime
        ate_time_obj1 = datetime.strptime(swabtime, '%H:%M').strftime('%I:%M %p')

        if swabdate == "" or swabtime == "":
            flash("Please input date and time!", "danger")
        elif swabdate < date:
            flash("cannot input previous date!", "warning")
        else:

            db.child("Suspected").child(username).update({
                "swabSchedule": swabdate + " Time: " + ate_time_obj1,
            })

            try:
                count_sid = 'ACc026937f5ed784bc4e05c210c1c00b77'
                token = "f91d6a88ac84a1f2834b340c67d7fa4c"
                client = Client(count_sid, token)

                message = client.messages.create(
                    from_='+19034939890',
                    to=Mobile_num,
                    body="Text Notification!  \n"
                         "RHU Kalayaan has set a date for your swab test!\n Please check it on the COVID CARE Kalayaan mobile application to see the schedule. Thank you, and be safe!",
                )
                flash("Schedule successfully added!")
                return redirect(url_for('Swab'))
            except TwilioRestException as e:
                flash("Phone Number Cannot reach", "danger")
    orderedDict = db.child("Suspected").order_by_key().equal_to(username).limit_to_first(1).get()

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

@app.route('/viewP/<username>', methods=('GET', 'POST'))
def viewP(username):
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

        db.child("probable").child(username).update({
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

    orderedDict = db.child("probable").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("viewP.html", data=orderedDict)

@app.route('/viewS/<username>', methods=('GET', 'POST'))
def viewS(username):
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

        db.child("Suspected").child(username).update({
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

    orderedDict = db.child("Suspected").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("viewS.html", data=orderedDict)

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
    res3 = db.child("Self-Monitoring").child(PatientID).get()

    return render_template('ViewMonitoringRecord.html', t=res3)


@app.route('/edit1/<username>', methods=('GET', 'POST'))
def edit1(username):
    from datetime import datetime, timedelta
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
        antigenres = request.form['antigenres']
        Dantigen = request.form['Dantigen']
        if result == "Recovered":
            db.child(result).child(PatientID).set({"result": result,
                                                   "antigenres": antigenres,
                                                   "Dantigen": Dantigen,

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
                "antigenres": antigenres,
                "Dantigen": Dantigen,
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
            today0 = datetime.today().strftime('%m/%d/%Y')
            COD = request.form['CauseofDeath']
            dateandtime = request.form['date']

            dateandtime1 = request.form['time']
            ate_time_obj = datetime.strptime(dateandtime,  '%Y-%m-%d').strftime('%d %B %Y ')
            ate_time_obj2 = datetime.strptime(dateandtime,  '%Y-%m-%d').strftime('%m/%B/%Y')
            ate_time_obj1 = datetime.strptime(dateandtime1,  '%H:%M').strftime('%I:%M %p')

            db.child(result).child(PatientID).set({"result": result,
                                                   "antigenres": antigenres,
                                                   "Dantigen": Dantigen,
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
                                                   "dateDied": ate_time_obj,
                                                   "dayDied": ate_time_obj2,
                                                   "CauseOfDeath": COD,
                                                   "DTofDeath": dateandtime + "Time: " + ate_time_obj1,
                                                   "PIcontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,

                                                   })
            db.child("Active").child(PatientID).remove()
            db.child("Patients").child(username).update({
                "result": result,
                "dateDied": ate_time_obj,
                "dayDied": ate_time_obj2,
                "antigenres": antigenres,
                "Dantigen": Dantigen,
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
                "DTofDeath": dateandtime + "Time: " + dateandtime1,
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
                                                   "antigenres": antigenres,
                                                   "Dantigen": Dantigen,
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
                "antigenres": antigenres,
                "Dantigen": Dantigen,
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
    from datetime import datetime, timedelta,date
    date = date.today() + timedelta(days=14)

    date = date.strftime('%d %B %Y')
    today = datetime.today().strftime('%d %B %Y ')
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
        antigenres = request.form['antigenres']
        Dantigen = request.form['Dantigen']
        if result == "Active":
            db.child(result).child(pID).set({"result": result,
                                                   "password": password,
                                                   "security": security,
                                                   "securityQues": securityQues,
                                                   "swabSchedule": swabSchedule,
                                                   "dayAdmitted": dayAdmitted,
                                                   "patientName": Pname,
                                                   "patientID": pID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                             "antigenres": antigenres,
                                             "Dantigen": Dantigen,
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
                                                   "dateAdmitted": today,
                                                   "PIncontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,
                                                "estimatedDateRecovery": date,

                                             })
            db.child("Patients").child(username).set({"result": result,
                                                       "password": password,
                                                       "security": security,
                                                       "securityQues": securityQues,
                                                       "swabSchedule": swabSchedule,
                                                       "dayAdmitted": dayAdmitted,
                                                       "patientName": Pname,
                                                       "patientID": pID,
                                                       "birthday": Birthday,
                                                       "age": Age,
                                                       "sex": Sex,
                                                      "antigenres": antigenres,
                                                      "Dantigen": Dantigen,
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
                                                       "dateAdmitted": today,
                                                       "PIncontact": PIcontact,
                                                       "NatureOfContact": NatureOfContact,
                                                       "SignAndSymp": SignAndSymp,
                                                       "doConsultation": doConsultation,
                                                      "estimatedDateRecovery": date,

                                                       })
            db.child("Close Contact").child(username).remove()
            db.child("Self-Monitoring").child(PatientID).remove()
            db.child("Patient Monitoring").child(PatientID).remove()
            flash('Successfully logged in!', "success")
        elif result == "Cleared":
            db.child("Close Contact").child(username).set({"result": result,
                                                           "password": password,
                                                           "security": security,
                                                           "securityQues": securityQues,
                                                           "swabSchedule": swabSchedule,
                                                           "dayAdmitted": dayAdmitted,
                                                           "patientName": Pname,
                                                           "patientID": PatientID,
                                                           "birthday": Birthday,
                                                           "age": Age,
                                                           "antigenres": antigenres,
                                                            "Dantigen": Dantigen,
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
                                                           "dateAdmitted": today,
                                                           "PIncontact": PIcontact,
                                                           "NatureOfContact": NatureOfContact,
                                                           "SignAndSymp": SignAndSymp,
                                                           "doConsultation": doConsultation,
                                                           "estimatedDateRecovery": date,

                                                           })

            db.child("Patient Monitoring").child(PatientID).remove()
            db.child("Self-Monitoring").child(PatientID).remove()
            db.child(PatientID).remove()
            flash('Successfully ', "success")
        return redirect(url_for('CloseContact'))

    orderedDict = db.child("Close Contact").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("UpdateCloseContact.html", data=orderedDict)
@app.route('/editS/<username>', methods=('GET', 'POST'))
def editS(username):
    from datetime import datetime, timedelta,date
    date = date.today() + timedelta(days=14)

    date = date.strftime('%d %B %Y')
    today = datetime.today().strftime('%d %B %Y ')
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
        antigenres = request.form['antigenres']
        Dantigen = request.form['Dantigen']
        swabSchedule = "Your Swab schedule is not yet available"

        if result == "Active":
            db.child(result).child(pID).set({"result": result,
                                                   "password": password,
                                                   "security": security,
                                                   "securityQues": securityQues,
                                                   "swabSchedule": swabSchedule,
                                                   "dayAdmitted": dayAdmitted,
                                                   "patientName": Pname,
                                                   "patientID": pID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                                   "sex": Sex,
                                             "antigenres": antigenres,
                                             "Dantigen": Dantigen,
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
                                                   "dateAdmitted": today,
                                                   "PIncontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,
                                                "estimatedDateRecovery": date,

                                             })
            db.child("Patients").child(username).set({"result": result,
                                                       "password": password,
                                                       "security": security,
                                                       "securityQues": securityQues,
                                                       "swabSchedule": swabSchedule,
                                                       "dayAdmitted": dayAdmitted,
                                                       "patientName": Pname,
                                                       "patientID": pID,
                                                       "birthday": Birthday,
                                                       "age": Age,
                                                       "sex": Sex,
                                                      "antigenres": antigenres,
                                                      "Dantigen": Dantigen,
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
                                                       "dateAdmitted": today,
                                                       "PIncontact": PIcontact,
                                                       "NatureOfContact": NatureOfContact,
                                                       "SignAndSymp": SignAndSymp,
                                                       "doConsultation": doConsultation,
                                                      "estimatedDateRecovery": date,

                                                       })
            db.child("Suspected").child(username).remove()
            db.child("Self-Monitoring").child(PatientID).remove()
            db.child("Patient Monitoring").child(PatientID).remove()
            flash('Successfully logged in!', "success")
        elif result == "Cleared":
            db.child("Suspected").child(username).set({"result": result,
                                                      "password": password,
                                                      "security": security,
                                                      "securityQues": securityQues,
                                                      "swabSchedule": swabSchedule,
                                                      "dayAdmitted": dayAdmitted,
                                                      "patientName": Pname,
                                                      "patientID": pID,
                                                      "birthday": Birthday,
                                                      "age": Age,
                                                      "sex": Sex,
                                                      "antigenres": antigenres,
                                                      "Dantigen": Dantigen,
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
                                                      "dateAdmitted": today,
                                                      "PIncontact": PIcontact,
                                                      "NatureOfContact": NatureOfContact,
                                                      "SignAndSymp": SignAndSymp,
                                                      "doConsultation": doConsultation,
                                                      "estimatedDateRecovery": date,

                                                      })

            db.child("Patient Monitoring").child(PatientID).remove()
            db.child("Self-Monitoring").child(PatientID).remove()
            db.child(PatientID).remove()
            flash('Successfully logged in!', "success")
        return redirect(url_for('Suspected'))

    orderedDict = db.child("Suspected").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("UpdateS.html", data=orderedDict)

@app.route('/editP/<username>', methods=('GET', 'POST'))
def editP(username):
    from datetime import datetime, timedelta,date
    date = date.today() + timedelta(days=14)

    date = date.strftime('%d %B %Y')
    today = datetime.today().strftime('%d %B %Y ')
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
        antigenres = request.form['antigenres']
        Dantigen = request.form['Dantigen']
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
                                                   "patientName": Pname,
                                                   "patientID": pID,
                                                   "birthday": Birthday,
                                                   "age": Age,
                                                   "sex": Sex,
                                                   "mobile_num": Mobile_num,
                                                   "address": Address,
                                                   "housenum": housenum,
                                                   "city": city,
                                             "antigenres": antigenres,
                                             "Dantigen": Dantigen,
                                                   "province": province,
                                                   "condition": Condition,
                                                   "caseStatus": CaseStatus,
                                                   "otherIllness": OtherIllness,
                                                   "emergencyCPerson": EmergencyCPerson,
                                                   "emergencyContact": emergencyContact,
                                                   "username": username,
                                                   "civilStatus": CivilStatus,
                                                   "dateAdmitted": today,
                                                   "PIncontact": PIcontact,
                                                   "NatureOfContact": NatureOfContact,
                                                   "SignAndSymp": SignAndSymp,
                                                   "doConsultation": doConsultation,
                                                "estimatedDateRecovery": date,

                                             })
            db.child("Patients").child(username).set({"result": result,
                                                       "password": password,
                                                       "security": security,
                                                       "securityQues": securityQues,
                                                       "swabSchedule": swabSchedule,
                                                       "dayAdmitted": dayAdmitted,
                                                       "patientName": Pname,
                                                       "patientID": pID,
                                                       "birthday": Birthday,
                                                       "age": Age,
                                                       "sex": Sex,
                                                      "antigenres": antigenres,
                                                      "Dantigen": Dantigen,
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
                                                       "dateAdmitted": today,
                                                       "PIncontact": PIcontact,
                                                       "NatureOfContact": NatureOfContact,
                                                       "SignAndSymp": SignAndSymp,
                                                       "doConsultation": doConsultation,
                                                      "estimatedDateRecovery": date,

                                                       })
            db.child("probable").child(username).remove()
            db.child("Self-Monitoring").child(PatientID).remove()
            db.child("Patient Monitoring").child(PatientID).remove()
            flash('Successfully logged in!', "success")
        elif result == "Cleared":
            db.child("probable").child(username).set({"result": result,
                                                      "password": password,
                                                      "security": security,
                                                      "securityQues": securityQues,
                                                      "swabSchedule": swabSchedule,
                                                      "dayAdmitted": dayAdmitted,
                                                      "patientName": Pname,
                                                      "patientID": pID,
                                                      "birthday": Birthday,
                                                      "age": Age,
                                                      "antigenres": antigenres,
                                                      "Dantigen": Dantigen,
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
                                                      "dateAdmitted": today,
                                                      "PIncontact": PIcontact,
                                                      "NatureOfContact": NatureOfContact,
                                                      "SignAndSymp": SignAndSymp,
                                                      "doConsultation": doConsultation,
                                                      "estimatedDateRecovery": date,
                                                      })
            db.child("Patient Monitoring").child(PatientID).remove()
            db.child("Self-Monitoring").child(PatientID).remove()
            db.child(PatientID).remove()
            flash('Successfully logged in!', "success")
        return redirect(url_for('Probable'))

    orderedDict = db.child("probable").order_by_key().equal_to(username).limit_to_first(1).get()
    return render_template("UpdateP.html", data=orderedDict)

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
