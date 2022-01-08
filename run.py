from flask import Flask,redirect,url_for,render_template,request,session
from datetime import timedelta

app= Flask(__name__)

app.secret_key= "sklfjsiafj248djs"
app.permanent_session_lifetime = timedelta(days=5) #man use minutes 5 ...# Even if you close the browswer window you will have the session data only when you logout will it be popped or deleted 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True # this will last 5 minutes now because that is what we defined in line 7
        user = request.form["nm"]
        session["user"] = user  # session stores the user into dictionary
        print(session["user"]) # print session data
        return redirect(url_for("user"))# dont pass ,user=user 
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

# retrieve session data after login
# if you close broswer and go back to this page it will be gone because it is in session!
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>This user name:(( {user} )). Was retrieved via session data it was not passed as a variable in render_template!!</h1>"
    else:
        return redirect(url_for("login"))

# if go to logout page then it will pop or remove the session data for user and redirect to the login
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
if __name__=="__main__":
    app.run(debug=True)
