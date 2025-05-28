from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nitin@123",
        database="password"
    )
    cursor = db.cursor()
except Exception as e:
    print(f"MySQL connection failed: {e}")
    exit(1)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return redirect(url_for('index'))

    user_id      = request.form['id']
    old_password = request.form['old_password']
    new_password = request.form['new_password']

    sql = "INSERT INTO users (user_id, old_password, new_password) VALUES (%s, %s, %s)"
    val = (user_id, old_password, new_password)
    try:
        cursor.execute(sql, val)
        db.commit()
        return """
            <h3>Password Changed Successfully!</h3>
        """
    except Exception as e:
        return f"""
            <h3>Error: {e}</h3>
        """

if __name__ == '__main__':
    app.run(debug=True)
