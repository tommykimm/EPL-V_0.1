from flask import Flask, render_template,  redirect, url_for, request
from flask_mysqldb import MySQL
import pymysql

app= Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'practice'

mysql = MySQL(app)


#hellotesting!

#outside comment data
def get_data():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM MyUsers")
        rows = cur.fetchall()    
        return rows


class Database:
#main
    def __init__(self):
        host = "127.0.0.1"
        user = 'root'
        password = '12345'
        db = 'practice'
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    

# season8
    def list_products8(self):
        self.cur.execute("SELECT practice.standings.id, practice.teams.teams, practice.points.points_8, practice.seasons.years,row_number() over(order by points_8 desc) AS standings FROM practice.standings JOIN practice.teams ON practice.standings.teams = practice.teams.id JOIN practice.points ON practice.standings.points = practice.points.id JOIN practice.seasons ON practice.standings.seasons = practice.seasons.id where practice.seasons.years = '20/21' order by practice.points.points_8 desc;")                            
        result = self.cur.fetchall()
        return result

    def list_winners8(self):
        self.cur.execute("SELECT practice.winners.seasons, practice.seasons.years, practice.teams.teams FROM practice.winners JOIN practice.seasons ON practice.winners.seasons = practice.seasons.id JOIN practice.teams ON practice.winners.winners = practice.teams.id ORDER BY practice.winners.seasons DESC LIMIT 0,3;")
        winner = self.cur.fetchall()
        return winner


#season7
    def list_products7(self):
        self.cur.execute("SELECT practice.standings.id, practice.teams.teams, practice.points.points_7, practice.seasons.years, row_number() over(order by points_7 desc) AS standings FROM practice.standings JOIN practice.teams ON practice.standings.teams = practice.teams.id JOIN practice.points ON practice.standings.points = practice.points.id JOIN practice.seasons ON practice.standings.seasons = practice.seasons.id where practice.seasons.years = '19/20' order by practice.points.points_7 desc;")
        result = self.cur.fetchall()
        return result

    def list_winners7(self):
        self.cur.execute("SELECT practice.winners.seasons, practice.seasons.years, practice.teams.teams FROM practice.winners JOIN practice.seasons ON practice.winners.seasons = practice.seasons.id JOIN practice.teams ON practice.winners.winners = practice.teams.id ORDER BY practice.winners.seasons DESC LIMIT 1,3;")
        winner = self.cur.fetchall()
        return winner

#season6 
    def list_products6(self):
        self.cur.execute("SELECT practice.standings.id, practice.teams.teams, practice.points.points_6, practice.seasons.years, row_number() over(order by points_6 desc) AS standings FROM practice.standings JOIN practice.teams ON practice.standings.teams = practice.teams.id JOIN practice.points ON practice.standings.points = practice.points.id JOIN practice.seasons ON practice.standings.seasons = practice.seasons.id where practice.seasons.years = '18/19' order by practice.points.points_6 desc;")
        result = self.cur.fetchall()
        return result   

    def list_winners6(self):
        self.cur.execute("SELECT practice.winners.seasons, practice.seasons.years, practice.teams.teams FROM practice.winners JOIN practice.seasons ON practice.winners.seasons = practice.seasons.id JOIN practice.teams ON practice.winners.winners = practice.teams.id ORDER BY practice.winners.seasons DESC LIMIT 2,3;")
        winner = self.cur.fetchall()
        return winner

#season5
    def list_products5(self):
        self.cur.execute("SELECT practice.standings.id, practice.teams.teams, practice.points.points_5, practice.seasons.years, row_number() over(order by points_5 desc) AS standings FROM practice.standings JOIN practice.teams ON practice.standings.teams = practice.teams.id JOIN practice.points ON practice.standings.points = practice.points.id JOIN practice.seasons ON practice.standings.seasons = practice.seasons.id where practice.seasons.years = '17/18' order by practice.points.points_5 desc;")
        result = self.cur.fetchall()
        return result  

   


    def list_winners5(self):
        self.cur.execute("SELECT practice.winners.seasons, practice.seasons.years, practice.teams.teams FROM practice.winners JOIN practice.seasons ON practice.winners.seasons = practice.seasons.id JOIN practice.teams ON practice.winners.winners = practice.teams.id ORDER BY practice.winners.seasons DESC LIMIT 3,3;")
        winner = self.cur.fetchall()
        return winner

#season4
    def list_products4(self):
        self.cur.execute("SELECT practice.standings.id, practice.teams.teams, practice.points.points_4, practice.seasons.years, row_number() over(order by points_4 desc) AS standings FROM practice.standings JOIN practice.teams ON practice.standings.teams = practice.teams.id JOIN practice.points ON practice.standings.points = practice.points.id JOIN practice.seasons ON practice.standings.seasons = practice.seasons.id where practice.seasons.years = '16/17' order by practice.points.points_4 desc;")
        result = self.cur.fetchall()
        return result  

    def list_winners4(self):
        self.cur.execute("SELECT practice.winners.seasons, practice.seasons.years, practice.teams.teams FROM practice.winners JOIN practice.seasons ON practice.winners.seasons = practice.seasons.id JOIN practice.teams ON practice.winners.winners = practice.teams.id ORDER BY practice.winners.seasons DESC LIMIT 4,3;")
        winner = self.cur.fetchall()
        return winner
#arsenal
    def arsenal(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Arsenal' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def arsenalscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Arsenal' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#astonvilla
    def astonvilla(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Aston Villa' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def astonvillascorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Aston Villa' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#fulham
    def fulham(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Fulham' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def fulhamscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Fulham' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#brighton
    def brighton(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Brighton' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def brightonscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Brighton' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#burnley
    def burnley(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Burnley' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def burnleyscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Burnley' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#chelsea
    def chelsea(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Chelsea' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def chelseascorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Chelsea' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#crystalpalace
    def crystalpalace(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Crystal Palace' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def crystalpalacescorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Crystal Palace' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#everton
    def everton(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Everton ' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def evertonscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Everton ' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#leeds
    def leeds(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Leeds United' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def leedsscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Leeds United' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#leicester
    def leicester(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Leciester City' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def leicesterscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Leciester City' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#liverpool
    def liverpool(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Liverpool' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def liverpoolscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Liverpool' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#mancity
    def mancity(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Manchester City' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def mancityscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Manchester City' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#manu
    def manu(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Manchester United' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def manuscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Manchester United' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#newcastle
    def newcastle(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Newcastle United' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def newcastlescorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Newcastle United' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#norwich
    def norwich(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Norwich City' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def norwichscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Norwich City' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#southampton
    def southampton(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Southampton' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def southamptonscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Southampton' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#spurs
    def spurs(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Tottenham' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def spursscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Tottenham' limit 0,5;")
        goals = self.cur.fetchall()
        return goals


#sheffield
    def sheffield(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Sheffield' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def sheffieldscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Sheffield' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#westham
    def westham(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Westham' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def westhamscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Westham' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#wolves
    def wolves(self):
            self.cur.execute("SELECT practice.results.id, practice.dates.dates, practice.teams.teams, practice.scores.scores, practice.teams2.teams2, outcomes.outcomes FROM practice.results Join practice.dates on practice.results.dates = practice.dates.id JOIN practice.teams on practice.results.team1 = practice.teams.id join practice.scores on practice.results.scores= practice.scores.id join practice.teams2 on practice.results.team2 = practice.teams2.id join practice.outcomes on practice.results.outcomes = practice.outcomes.id where practice.teams.teams = 'Wolverhampton' limit 0,10;")
            result = self.cur.fetchall()
            return result  

    def wolvesscorers(self):
        self.cur.execute("select practice.topscorers.id , practice.players.player, practice.topscorers.goals, practice.teams.teams from practice.topscorers join practice.players on practice.topscorers.player = practice.players.id join practice.teams on practice.topscorers.club = practice.teams.id where practice.teams.teams ='Wolverhampton' limit 0,5;")
        goals = self.cur.fetchall()
        return goals

#arsenal
@app.route('/arsenal')
def arsenal():
    def arsenal1():
        db = Database()
        products = db.arsenal()
        return products

    def arsenalscorers1():
        db = Database()
        products = db.arsenalscorers()
        return products

  
    res = arsenal1()
    win = arsenalscorers1()
    return render_template("arsenal.html" , result = res, winners= win, team="Arsenal") 

#astonvilla
@app.route('/astonvilla')
def astonvilla():
    def astonvilla1():
        db = Database()
        products = db.astonvilla()
        return products

    def astonvillascorers1():
        db = Database()
        products = db.astonvillascorers()
        return products

  
    res = astonvilla1()
    win = astonvillascorers1()
    return render_template("astonvilla.html" , result = res, winners= win, team="Aston Villa")     


#fulham
@app.route('/fulham')
def fulham():
    def fulham1():
        db = Database()
        products = db.fulham()
        return products

    def fulhamscorers1():
        db = Database()
        products = db.fulhamscorers()
        return products

  
    res = fulham1()
    win = fulhamscorers1()
    return render_template("fulham.html" , result = res, winners= win, team="Fulham") 

#brighton
@app.route('/brighton')
def brighton():
    def brighton1():
        db = Database()
        products = db.brighton()
        return products

    def brightonscorers1():
        db = Database()
        products = db.brightonscorers()
        return products

  
    res = brighton1()
    win = brightonscorers1()
    return render_template("brighton.html" , result = res, winners= win, team="Brighton") 


#burnley
@app.route('/burnley')
def burnley():
    def burnley1():
        db = Database()
        products = db.burnley()
        return products

    def burnleyscorers1():
        db = Database()
        products = db.burnleyscorers()
        return products

  
    res = burnley1()
    win = burnleyscorers1()
    return render_template("burnley.html" , result = res, winners= win, team="Burnley") 


#chelsea
@app.route('/chelsea')
def chelsea():
    def chelsea1():
        db = Database()
        products = db.chelsea()
        return products

    def chelseascorers1():
        db = Database()
        products = db.chelseascorers()
        return products

  
    res = chelsea1()
    win = chelseascorers1()
    return render_template("chelsea.html" , result = res, winners= win, team="Chelsea") 


#crystalpalace
@app.route('/crystalpalace')
def crystalpalace():
    def crystalpalace1():
        db = Database()
        products = db.chelsea()
        return products

    def crystalpalacescorers1():
        db = Database()
        products = db.crystalpalacescorers()
        return products

  
    res = crystalpalace1()
    win = crystalpalacescorers1()
    return render_template("crystalpalace.html" , result = res, winners= win, team="Crystal Palace") 

#everton
@app.route('/everton')
def everton():
    def everton1():
        db = Database()
        products = db.everton()
        return products

    def evertonscorers1():
        db = Database()
        products = db.evertonscorers()
        return products

  
    res = everton1()
    win = evertonscorers1()
    return render_template("everton.html" , result = res, winners= win, team="Everton") 

#leeds
@app.route('/leeds')
def leeds():
    def leeds1():
        db = Database()
        products = db.leeds()
        return products

    def leedsscorers1():
        db = Database()
        products = db.leedsscorers()
        return products

  
    res = leeds1()
    win = leedsscorers1()
    return render_template("leeds.html" , result = res, winners= win, team="Leeds United") 


#leicester
@app.route('/leicester')
def leicester():
    def leicester1():
        db = Database()
        products = db.leicester()
        return products

    def leicesterscorers1():
        db = Database()
        products = db.leicesterscorers()
        return products

  
    res = leicester1()
    win = leicesterscorers1()
    return render_template("leicester.html" , result = res, winners= win, team="Leicester City") 


#liverpool
@app.route('/liverpool')
def liverpool():
    def liverpool1():
        db = Database()
        products = db.liverpool()
        return products

    def liverpoolscorers1():
        db = Database()
        products = db.liverpoolscorers()
        return products

  
    res = liverpool1()
    win = liverpoolscorers1()
    return render_template("liverpool.html" , result = res, winners= win, team="Liverpool") 



#mancity
@app.route('/mancity' , methods=['GET', 'POST'])
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

    return render_template("mancity.html" , value=value, all_text= all_text, result = res, winners= win, team="Manchester City") 



#manchesterunited
@app.route('/manu')
def manu():
    def manu1():
        db = Database()
        products = db.manu()
        return products

    def manuscorers1():
        db = Database()
        products = db.manuscorers()
        return products

  
    res = manu1()
    win = manuscorers1()
    return render_template("manu.html" , result = res, winners= win, team="Manchester United") 


#newcastleunited
@app.route('/newcastle')
def newcastle():
    def newcastle1():
        db = Database()
        products = db.newcastle()
        return products

    def newcastlescorers1():
        db = Database()
        products = db.newcastlescorers()
        return products

  
    res = newcastle1()
    win = newcastlescorers1()
    return render_template("newcastle.html" , result = res, winners= win, team="Newcastle United") 


#norwich
@app.route('/norwich')
def norwich():
    def norwich1():
        db = Database()
        products = db.norwich()
        return products

    def norwichscorers1():
        db = Database()
        products = db.norwichscorers()
        return products

  
    res = norwich1()
    win = norwichscorers1()
    return render_template("norwich.html" , result = res, winners= win, team="Norwich City") 


#southampton
@app.route('/southampton')
def southampton():
    def southampton1():
        db = Database()
        products = db.southampton()
        return products

    def southamptonscorers1():
        db = Database()
        products = db.southamptonscorers()
        return products

  
    res = southampton1()
    win = southamptonscorers1()
    return render_template("southampton.html" , result = res, winners= win, team="Southampton") 


#spurs
@app.route('/spurs')
def spurs():
    def spurs1():
        db = Database()
        products = db.spurs()
        return products

    def spursscorers1():
        db = Database()
        products = db.spursscorers()
        return products

  
    res = spurs1()
    win = spursscorers1()
    return render_template("spurs.html" , result = res, winners= win, team="Tottenham") 


#sheffield
@app.route('/sheffield')
def sheffield():
    def sheffield1():
        db = Database()
        products = db.sheffield()
        return products

    def sheffieldscorers1():
        db = Database()
        products = db.sheffieldscorers()
        return products

  
    res = sheffield1()
    win = sheffieldscorers1()
    return render_template("sheffield.html" , result = res, winners= win, team="Sheffield") 


#westham
@app.route('/westham')
def westham():
    def westham1():
        db = Database()
        products = db.westham()
        return products

    def westhamscorers1():
        db = Database()
        products = db.westhamscorers()
        return products

  
    res = westham1()
    win = westhamscorers1()
    return render_template("westham.html" , result = res, winners= win, team="West Ham") 
    
#wolves
@app.route('/wolves')
def wolves():
    def wolves1():
        db = Database()
        products = db.wolves()
        return products

    def wolvesscorers1():
        db = Database()
        products = db.wolvesscorers()
        return products

  
    res = wolves1()
    win = wolvesscorers1()
    return render_template("wolves.html" , result = res, winners= win, team="Wolverhampton") 


@app.route('/')
def index():
    return redirect(url_for('product8'))

if __name__ == '__main__':
    app.run(debug=True)



#season8
@app.route('/index8')
def product8():
    def db_query8():
        db = Database()
        products = db.list_products8()
        return products

    def db_query8_1():
        db = Database()
        products = db.list_winners8()
        return products

    res = db_query8()
    win = db_query8_1()
    return render_template("homepage8.html" , result = res, winner = win, seasons='20/21', ) 



#season7
@app.route('/index7')
def product7():
    def db_query7():
        db = Database()
        products = db.list_products7()
        return products

    def db_query7_1():
        db = Database()
        products = db.list_winners7()
        return products

    res = db_query7()
    win = db_query7_1()
    return render_template("homepage7.html" ,result= res, winner= win ,seasons='19/20')


#season6
@app.route('/index6')
def product6():
    def db_query6():
        db = Database()
        products = db.list_products6()
        return products

    def db_query6_1():
        db = Database()
        products = db.list_winners6()
        return products

    res = db_query6()
    win = db_query6_1()
    return render_template("homepage6.html" ,result= res, winner= win , seasons='18/19')

#season5
@app.route('/index5')
def product5():
    def db_query5():
        db = Database()
        products = db.list_products5()
        return products

    def db_query5_1():
        db = Database()
        products = db.list_winners5()
        return products

    res = db_query5()
    win = db_query5_1()
    return render_template("homepage5.html" ,result= res, winner= win, seasons='17/18')


#season4
@app.route('/index4')
def product4():
    def db_query4():
        db = Database()
        products = db.list_products4()
        return products

    def db_query4_1():
        db = Database()
        products = db.list_winners4()
        return products

    res = db_query4()
    win = db_query4_1()
    return render_template("homepage4.html" ,result= res, winner= win, seasons='16/17')





