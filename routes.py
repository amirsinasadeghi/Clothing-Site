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
  cursor.execute("SELECT name FROM Brands WHERE id IN (SELECT brandid FROM ClothesBrand WHERE clothesid = (SELECT id FROM Clothes WHERE name = ?))", (clothing[1],))
  brand = cursor.fetchall() 
  conn.close()
  print(clothing)
  return render_template('clothing.html', clothing=clothing, brand=brand )


@app.route('/about')
def about():
  return render_template('about.html', title="about") 

if __name__ == "__main__" :
  app.run(debug=True)