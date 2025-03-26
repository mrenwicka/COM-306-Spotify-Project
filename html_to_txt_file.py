from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Write login details to a text file
    with open('logins.txt', 'a') as file:
        file.write(f'Username: {username}, Password: {password}\n')
    
    return "Login information saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)