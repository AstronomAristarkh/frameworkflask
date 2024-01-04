from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/base/')
def html_base():
    return render_template('base.html')

@app.route('/clothes/')
def html_clothes():
    return render_template('clothes.html')

@app.route('/jacket/')
def html_jacket():
    return render_template('jacket.html')

@app.route('/shoes/')
def html_shoes():
    return render_template('shoes.html')

@app.route('/whiteshirt/')
def html_whiteshirt():
    return render_template('whiteshirt.html')

if __name__ == '__main__':
    app.run()

