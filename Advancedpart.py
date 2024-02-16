from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)




@app.route('/profile')
def y():
    rand=random.randint(1,100)
    #rand=request.args.get('a',200)
    return render_template('Profile.html',name=rand)


@app.route('/')
def index():
    return redirect(url_for('y')) 


if __name__ == "__main__":
    app.run(debug=True)
