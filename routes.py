from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def home ():
  return render_template('home.html', title="home")


@app.route ('/clothing/<int:id>')
def clothing (id):
  conn = sqlite3.connect("clothing.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Clothes WHERE id=?;", (id,))
  clothing = cursor.fetchone()
  conn.close()
  print(clothing)
  return render_template('clothing.html', clothing=clothing )


@app.route('/about')
def about():
  return render_template('about.html', title="about") 


if __name__ == "__main__" :
  app.run(debug=True)