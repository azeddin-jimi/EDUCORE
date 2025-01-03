from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form('email')  
    password = request.form('password') 
    remember = request.form('remember') 

    if not email or not password:
        return "<h1>Erreur !</h1><p>Email ou mot de passe manquant.</p>", 400

    print(f"Email: {email}, Password: {password}, Remember me: {remember}")

    return f"<h1>Merci !</h1><p>Nous avons bien reçu votre email : {email}</p>"

if __name__ == '__main__':
    app.run(debug=True)
