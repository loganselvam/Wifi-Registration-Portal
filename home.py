import os

from flask import Flask, render_template,request,session
from werkzeug.utils import secure_filename

import ar_master

app=Flask(__name__,static_folder='static')
app.config.from_object(__name__)
app.config['SECRET_KEY']='1a2s3d4f5g6h'
mm=ar_master.master_flask_code()


@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html')
@app.route("/user_home")
def user_home():
    return render_template('user_home.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/admin_log", methods = ['GET', 'POST'])
def admin_log():
    error = None
    if request.method == 'POST':
        un = request.form['uname']
        pa = request.form['pass']
        print(un)
        print(pa)
        pa = pa.strip()
        un = un.strip()
        if un == "admin" and pa == "admin":

            return render_template('admin_home.html', error=error)
        else:
            return render_template('admin_log.html', error=error)
    return render_template('admin_log.html')


@app.route("/user_log", methods = ['GET', 'POST'])
def user_log():
    msg = None
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['pass']

        n1 = str(n)
        g1 = str(g)

        q = ("SELECT * from user_details where register_no='" + str(n1) + "' and password='" + str(g1) + "'")
        data = mm.select_direct_query(q)
        data = len(data)
        if data == 0:
            return render_template('user_login.html', flash_message=True, data="Failed")
        else:
            msg = 'Success'
            session['user'] = n
            return render_template('student_details.html', sid=n)
    return render_template('user_login.html')

@app.route("/user_register", methods = ['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        registerno = request.form['registerno']
        email = request.form['email']
        gender = request.form['gender']
        password = request.form['password']

        maxin = mm.find_max_id("user_details")
        qry = ("insert into user_details values('" + str(maxin) + "','" + str(registerno) + "','" + str(email) + "','" + str(gender) + "','" + str(password) + "')")
        result = mm.insert_query(qry)
        print(result)
        return render_template('user_login.html',flash_message=True,data="Success")
    return render_template('user_register.html')



@app.route("/staff_register", methods = ['GET', 'POST'])
def staff_register():
    if request.method == 'POST':

        email = request.form['email']
        gender = request.form['gender']
        password = request.form['password']

        maxin = mm.find_max_id("staff_register")
        qry = ("insert into staff_register values('" + str(maxin) + "','" + str(email) + "','" + str(gender) + "','" + str(password) + "')")
        result = mm.insert_query(qry)
        print(result)
        return render_template('staff_login.html',flash_message=True,data="Success")
    return render_template('staff_register.html')



@app.route("/admin_view_user")
def admin_view_user():
    data = mm.select_direct_query("select register_no,name,depart,contact,device,email,date,mac,hostel from student_wifi_details")
    return render_template('admin_view_user.html',items=data)





@app.route("/staff_login", methods = ['GET', 'POST'])
def staff_login():
    msg = None
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['pass']

        n1 = str(n)
        g1 = str(g)

        q = ("SELECT * from staff_register where email='" + str(n1) + "' and password='" + str(g1) + "'")
        data = mm.select_direct_query(q)
        data = len(data)
        if data == 0:
            return render_template('user_login.html', flash_message=True, data="Failed")
        else:
            msg = 'Success'
            session['user'] = n
            return render_template('staff_details.html', sid=n)
    return render_template('staff_login.html')


@app.route("/staff_details", methods = ['GET', 'POST'])
def staff_details():
    if request.method == 'POST':

        register_no = request.form['register_no']
        name = request.form['name']
        depart = request.form['depart']
        contact = request.form['contact']
        device = request.form['device']
        email = request.form['email']
        date = request.form['date']
        mac = request.form['mac']
        designation = request.form['designation']



        maxin = mm.find_max_id("staff_wifi_details")
        qry = ("insert into staff_wifi_details values('" + str(maxin) + "','" + str(register_no) + "','" + str(name) + "','" + str(depart) + "','" + str(contact) + "','" + str(device) + "','" + str(email) + "','" + str(date) + "','" + str(mac) + "','" + str(designation) + "')")
        result = mm.insert_query(qry)
        print(result)
        return render_template('staff_details.html',flash_message=True,data="Success")
    return render_template('staff_details.html')

@app.route("/student_details", methods = ['GET', 'POST'])
def student_details():
    if request.method == 'POST':

        register_no = request.form['register_no']
        name = request.form['name']
        depart = request.form['depart']
        contact = request.form['contact']
        device = request.form['device']
        email = request.form['email']
        date = request.form['date']
        mac = request.form['mac']
        hostel = request.form['hostel']



        maxin = mm.find_max_id("student_wifi_details")
        qry = ("insert into student_wifi_details values('" + str(maxin) + "','" + str(register_no) + "','" + str(name) + "','" + str(depart) + "','" + str(contact) + "','" + str(device) + "','" + str(email) + "','" + str(date) + "','" + str(mac) + "','" + str(hostel) + "')")
        result = mm.insert_query(qry)
        print(result)
        return render_template('student_details.html',flash_message=True,data="Success")
    return render_template('student_details.html')


@app.route("/admin_view_staff")
def admin_view_staff():
    data = mm.select_direct_query("select register_no,name,depart,contact,device,email,date,mac,designation from staff_wifi_details")
    return render_template('admin_view_staff.html',items=data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)