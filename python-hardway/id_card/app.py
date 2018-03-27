from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/idcard", methods=['POST', 'GET'])

def index():
    ''' school_name = "Awesome University"
    name = "Tuyen Tram"
    id = "123456789"
    email = "ttram@au.edu" '''

    if request.method == "POST":
        my_school_name = request.form['school_name']
        my_name = request.form['name']
        my_id = request.form['id']
        my_email = request.form['email']
        school_name = f"{my_school_name}"
        name = f"{my_name}"
        id = f"{my_id}"
        email = f"{my_email}"
        return render_template("index.html", school_name=school_name, name=name, id=id, email=email)
    else:
        return render_template("id_card_form.html")

if __name__ == "__main__":
    app.run()