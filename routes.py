from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

# this is the route for my home page.
@app.route('/')
def home ():
  return render_template('home.html', title="home")

@app.route('/about')
def about():
  return render_template('about.html', title="about") 

#this simplifies any query that im doing so that I dont need to rewrite the thing out all the time.
def do_query (query, data=None, fetchone=False):
  conn = sqlite3.connect("clothing.db")
  cur = conn.cursor()
  if data is None:
    cur.execute(query)
  else:
    cur.execute(query, data)
  results = cur.fetchone() if fetchone else cur.fetchall()
  conn.close()
  return results

#This query grabs all the data from anything that classifies as a shirt (id of 2) and displays it, after this users can select on one specific shirt name and it will take them to the link of the ID of the shirt.
@app.route ('/shirts')
def shirts ():
  shirts = do_query ('SELECT id,name,price,photo FROM Clothes WHERE typeid="2"')
  return render_template('shirts.html', shirts=shirts )


@app.route ('/pants')
def pants ():
  pants = do_query ('SELECT id,name,price,photo FROM Clothes WHERE typeid="1"')
  return render_template('pants.html', pants=pants )


@app.route ('/sweaters')
def sweaters ():
  sweaters = do_query ('SELECT id,name,price,photo FROM Clothes WHERE typeid="3"')
  return render_template('sweaters.html', sweaters=sweaters )




#This grabs all the info for one specific clothing item and displays it onto the screen.
@app.route ('/clothingitem/<int:id>')
def clothingitem (id):
  clothingitem = do_query (" SELECT * FROM Clothes WHERE id=?;", (id,), fetchone=True)
  color = do_query('SELECT * FROM Color WHERE id IN (SELECT colorid FROM ClothesColor WHERE clothesid=?)',(id,), fetchone = False) 
  return render_template('clothingitem.html',clothingitem=clothingitem,color=color )



  
  
if __name__ == "__main__" :
  app.run(debug=True)