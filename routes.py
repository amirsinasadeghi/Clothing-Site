from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def home ():
  return render_template('home.html', title="home")


def do_query (query):
  conn = sqlite3.connect("clothing2.db")
  cur = conn.cursor()
  cur.execute(query)
  results = cur.fetchall()
  conn.close()
  return results


@app.route ('/shirts')
def shirts ():
  shirts = do_query ('SELECT Name,Price,Photo FROM Shirts')
  return render_template('shirts.html', shirts=shirts )


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