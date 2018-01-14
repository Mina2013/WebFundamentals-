from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def landing():
    return render_template('index.html')
app.run(debug=True)
@app.route('/ninja')
def ninja():
    return render_template('ninja.html')
app.run(debug=True)
