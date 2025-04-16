from flask import Flask, request, render_template

app = Flask(__name__)

# Dummy user database
database = {
    'nachi': '123',
    'james': 'aac',
    'faisal': 'faisal@123'
    
}

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1] != pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name1)
        
    @app.route('/')
    def project_list():
         data = [
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 28}
    ]
    return render_template('table.html', people=data)

if __name__ == '__main__':
    app.run(debug=True)
