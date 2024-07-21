from flask import Flask, render_template
from flask_cors import CORS 
app = Flask(_name_)
CORS(app)
@app.router('/')
def home():
  return render_template('index.html)
if _name_ == '_main_':
       app.run(debug=True)            
