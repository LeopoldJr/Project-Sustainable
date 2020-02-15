import pyrebase

config = {"apiKey": "AIzaSyCXVfGjx0QfnSKFiBSFZ6jX1u8pLO_K4oM",
    "authDomain": "test-cedf0.firebaseapp.com",
    "databaseURL": "https://test-cedf0.firebaseio.com",
    "projectId": "test-cedf0",
    "storageBucket": "test-cedf0.appspot.com",
    "messagingSenderId": "703866193263",
    "appId": "1:703866193263:web:7c27817f991a689292949a",
    "measurementId": "G-W6E1V4C1XS"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name = request.form['name']
            db.child("todo").push(name)
            todo = db.child("todo").get()
            to = todo.val()
            return render_template('tutorial.html',t=to.values())
        elif request.form['submit'] == 'delete':
            db.child("todo").remove()
            return render_template('tutorial.html')
    return render_template('tutorial.html')
    
if __name__ =='__main__':
    app.run(debug=True)

#db.child("names").push({"name": "Jason"})
#db.child("names").child("name").update({"name":"Teets"})

#users=db.child("names").child("name").get()
#print(:users.val())

#db.child("names").child("name").remove()

#<form action="" method="post">
#	<input type="text" name="name">
#	<button type="submit">Submit</button>	        
#</form>
#{% for l in t%}
#	{{l}}
#{% endfor %}