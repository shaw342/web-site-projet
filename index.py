from  flask import Flask,render_template,request,url_for,redirect,g
import hashlib
import sqlite3

app = Flask(__name__)
pageAcceuill = "index.html"
pageSIGNUP = "signup.html"
DATABASE = "auth.db"

@app.route("/")
def index():
    return render_template(pageAcceuill)

@app.route("/signup", methods=["GET","POST"])
def signup():
    username = request.form.get("nom")
    password = request.form.get("password")
    email = request.form.get("email")
    
    # Définir la variable user
    user = {
        'nom': username,
        'email': email,
        'mot_de_passe': password
    }

    return render_template(pageSIGNUP, user=user)

def hash_mdp(mdp):
    return hashlib.sha256(str(mdp).encode('utf-8')).hexdigest()


def get_db():
    db =  getattr(g,"_database",None)
    if db is None:
        conn =  g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_con():
    db  = getattr(g,'_database',None)
    db.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)    
