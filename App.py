from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #root
def index():
    return render_template('index.html', title="Emmarher")

@app.route('/contact')#contact frame
def contact():
    return 'Contact Frame'


if __name__ == '__main__':
    app.run(debug=True)