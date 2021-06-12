from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'somekey'


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    visits = session['visits']
    return render_template("index.html", visits=visits)


@app.route('/add2', methods=['POST'])
def add2():
    session['visits'] += 1
    visits = session['visits']
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['visits'] = 0
    visits = session['visits']
    return redirect("/",)


@app.route('/destroy_session')
def delete():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
