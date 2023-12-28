from flask import Flask, render_template, redirect, url_for, request
import mysql.connector
import json

app = Flask(__name__)
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="qwerty@123",
        database="user"
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    print(f"Failed to connect to the database: {err}")

@app.route('/')
def index():
    return render_template('sign_login.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user[0]
            password = password
            print(password)
            print(stored_password)

            if password== stored_password:
                return redirect(url_for('show_book_information'))
            else:
                return "Wrong password"
        else:
            return "User does not exist"

    return render_template('sign_in.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        values = (username, password, email)

        try:
            cursor.execute(query, values)
            db.commit()
            return redirect('/p')  
        except mysql.connector.Error as err:
            db.rollback()
            return f"Failed: {err}"

    return render_template('sign_up.html')

@app.route('/p')
def show_book_information():
    return render_template('p.html')

@app.route('/test.json')
def get_book_information():
    with open('test.json') as user_file:
        file_contents = user_file.read()
        return file_contents


@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    return render_template('borrow.html')



@app.route('/index', methods=['GET', 'POST'])
def return_book():
        return render_template('./index.html')




@app.route('/return', methods=['GET', 'POST'])
def return_book_page():    
    return render_template('return.html')


if __name__ == '__main__':
    app.run(debug=True) 

