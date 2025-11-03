from flask import Flask, request , render_template , session 
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.secret_key = "Admin"


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ayushaggarwal@09'
app.config['MYSQL_DB'] = 'Students'


mysql = MySQL(app)




@app.route('/')
def home():
# Yha bss login ho rha h 
    name = session.get('username')
    return render_template('index.html' , name = name)



@app.route('/profile' , methods = ['GET' , 'POST'])
def admin_profile():

# Yha jo login info match kr rhe h 
    if request.method == "POST": 
        admin_name = "admin"
        admin_pass = "admin@123"

        user_name = request.form['username']
        user_pass = request.form['password']

        session['username'] = user_name

        if admin_name == user_name and admin_pass == user_pass: 
            #age match hui to admin panel open hoga 
            name = session.get('username')
            return render_template('admin_pr.html' , name = name)
        else : 
            # nhi to login page hi open hoga 
            return render_template('index.html')
        
    else: 
        name = session.get('username')
        return render_template("admin_pr.html" , name = name)



@app.route('/show_students')
def show_students():
    name = session.get('username')
    cur = mysql.connection.cursor()

    cur.execute('SELECT * FROM student_data')

    cur.close()
    return render_template('show_students.html' , name = name)


@app.route('/add_stud' )
def add_students():



    return render_template('add_student.html')


@app.route('/suces_add', methods=["GET", "POST"])
def success_add():
    if request.method == "POST":


        
        student_name = request.form.get('studentName')
        student_number = request.form.get('rollNumber')
        student_branch = request.form.get('branch')
        student_section = request.form.get('section')


        cur = mysql.connection.cursor()

        cur.execute( """INSERT INTO student_data (roll_no , name , branch , sec)
                    VALUES (%s , %s , %s , %s) """, (student_number , student_name ,student_branch , student_section , ) )

        mysql.connection.commit()

        cur.close()
            # process form data here
        return render_template('suces_add.html')
    else:
        return render_template('add_students')
    


@app.route('/upd_stud')
def upd_stud():
    name = session.get('username')
    return render_template('update_stud.html' , name = name)



@app.route('/edit_info')
def edit_info():
    return render_template('edit_detail.html')



if __name__ == "__main__":
    app.run(debug = True)