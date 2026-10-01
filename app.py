from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "senha secreta"

@app.route('/')
def index():
    if 'lista' not in session:
        session['lista'] = []
    return render_template('tarefas.html', lista=session['lista'])

if __name__ == "__main__":
    app.run(debug=True)