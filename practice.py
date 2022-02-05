from flask import Flask, render_template,  redirect, url_for, request
from flask_mysqldb import MySQL
import pymysql


app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'practice'

mysql = MySQL(app)

class Database:

#practice
    def __init__(self):
        host = "127.0.0.1"
        user = 'root'
        password = '12345'
        db = 'practice'
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def mancity(self):
                self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Manchester City' limit 0,10;")
                result = self.cur.fetchall()
                return result  

    def mancityscorers(self):
            self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Manchester City' limit 0,5;")
            goals = self.cur.fetchall()
            return goals


def get_data():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM MyUsers")
        rows = cur.fetchall()    
        return rows

#mancity
@app.route('/' , methods=['GET', 'POST'])
def mancity():
    def mancity1():
        db = Database()
        products = db.mancity()
        return products

    def mancityscorers1():
        db = Database()
        products = db.mancityscorers()
        return products

    def index():
        if request.method == "POST":
            details = request.form
            id = len(get_data())+1
            comment = details['comment']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO MyUsers(id, comment) VALUES (%s, %s)", (id, comment))
            mysql.connection.commit()
            cur.close()
        
        
        print("-->\n", all_text)

    all_text = get_data()  
    res = mancity1()
    win = mancityscorers1()
    value=index()

    return render_template("practice2.html" , value=value, all_text= all_text, result = res, winners= win, team="Manchester City") 



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#         details = request.form
#         id = details['id']
#         comment = details['comment']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO MyUsers(id, comment) VALUES (%s, %s)", ( id, comment))
#         mysql.connection.commit()
#         cur.close()
    
#     all_text = get_data()
#     print("-->\n", all_text)

#     return render_template('practice2.html', all_text = all_text)

