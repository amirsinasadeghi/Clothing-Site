from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

# this is the route for my home page.
@app.route('/')
def home ():
  return render_template('home.html', title="home")

#this simplifies any query that im doing so that I dont need to rewrite the thing out all the time.
def do_query (query): 
  conn = sqlite3.connect("clothing2.db")
  cur = conn.cursor()
  cur.execute(query)
  results = cur.fetchall()
  conn.close()
  return results

#This query grabs all the data from shirts and displays it, after this users can select on one specific shirt name and it will take them to the link of the ID of the shirt.
@app.route ('/shirts')
def shirts ():
  shirts = do_query ('SELECT Name,Price,Photo FROM Shirts')
  return render_template('shirts.html', shirts=shirts )

#This grabs all the info for one specific shirt and displays it onto the screen.
@app.route ('/shirts/<int:id>')
def singleshirt (id):
  conn = sqlite3.connect("clothing2.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Shirts WHERE id=?;", (id,))
  singleshirt = cursor.fetchone()
  conn.close()
  print(singleshirt)
  return render_template('singleshirt.html', singleshirt=singleshirt )

@app.route('/about')
def about():
  return render_template('about.html', title="about") 

if __name__ == "__main__" :
  app.run(debug=True)