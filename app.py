from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
  {
    'id': 1,
    'title': 'QR Code Generator',
    'description': 'Generates QR code for this current website',
  },
  {
    'id': 2,
    'title': 'Whatsapp Clone',
    'description': 'Whatsapp clone Version'
  },
  {
    'id': 3,
    'title': 'Credit score risk assessment application',
    'description': 'An application that assesses and comments on       the risk threshold of each user'
  },
  {
    'id': 4,
    'title': 'SQL database project',
    'description': 'A database project that tracks transactions        made by a customer'
  }
]

@app.route("/")
def hello_BigStepper():
    return render_template('home.html', projects=PROJECTS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)