from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
  return render_template('login.html')

@app.route('/loggedin')
def logged_successfull():
  return render_template('loggedin.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
