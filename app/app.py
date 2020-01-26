from flask import Flask, render_template, redirect, request
from datetime import date
from message import Message

app = Flask(__name__)
messages = []

@app.route("/")
def hello():
    return render_template('test.html', messages=messages)
    
@app.route("/newpost", methods=['GET', 'POST'])
def new_post():
    if request.method == "POST":
        content = request.form.get('content')
        location = request.form.get('location')
        day = (date.today()).strftime("%m/%d/%Y")
        mess= Message(location,content,day)
        messages.append(mess)
        return redirect('/')
        
    return render_template("form.html")
	
	
if __name__ == '__main__':
	app.run()