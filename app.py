# import libraries
from flask import Flask,request,render_template,jsonify
from DES_Manager.encryption import encryption
from DES_Manager.decryption import decryption

# Initialize flask
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process',methods = ['POST'])
def process():
  # Get message and the key value
  message = request.form['message']
  key = request.form['key']

  # Check for request message
  if(request.form['func']=="encryption"):
    output = encryption(message,key)
  else:
    output = decryption(message,key)

  return output

if __name__ == '__main__':
    app.run(debug=True)