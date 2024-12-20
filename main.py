from flask import Flask, render_template, request, redirect, url_for, session

strona = Flask(__name__)
strona.secret_key = 'logins'

#User data for testing
users = {
    'sitter': {'password': 'Spassword', 'type': 'sitter'},
    'owner': {'password': 'Opassword', 'type': 'owner'}
}

@strona.route('/')
def home():
    return render_template('index.html')

@strona.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            session['user_type'] = user['type']
            return redirect(url_for('account'))
        
        return "Invalid credentials", 401
    return render_template('login.html')

@strona.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@strona.route('/signup')
def signup():
    return render_template('signup.html')

@strona.route('/signup/owner', methods=['GET', 'POST'])
def signup_owner():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        username = request.form['username']
        return redirect(url_for('account'))
    return render_template('POsignup.html')

@strona.route('/signup/sitter', methods=['GET', 'POST'])
def signup_sitter():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        username = request.form['username']
        dob = request.form.get('dob')
        experience = request.form['experience']

        session['username'] = username
        session['user_type'] = 'sitter'

        return redirect(url_for('account'))
    return render_template('PSsignup.html')

@strona.route('/home', methods=['GET', 'POST'])
def Home():
    if request.method == 'POST':
        petno = request.form.get('petno') #Selection not required
        service = request.form.get('service')
        duration = request.form.get('duration')
        return redirect(url_for('results')) 
    return render_template('home.html')

@strona.route('/account')
def account():
    user_type = session.get('user_type')

    if user_type == 'sitter':
        return render_template('PSaccount.html', username=session.get('username'))
    elif user_type == 'owner':
        return render_template('POaccount.html', username=session.get('username'))
    else:
        return "Access Denied", 403

@strona.route('/results')
def results():
    return render_template('results.html')

@strona.route('/sitter1')
def sitter1():
    return render_template('sitter1.html')

@strona.route('/sitter2')
def sitter2():
    return render_template('sitter2.html')

@strona.route('/sitter3')
def sitter3():
    return render_template('sitter3.html')

@strona.route('/sitter4')
def sitter4():
    return render_template('sitter4.html')

@strona.route('/favourites')
def favourites():
    return render_template('favourites.html')

@strona.route('/booking')
def booking():
    return render_template('booking.html')

@strona.route('/OGenAdv')
def OGenAdv():
    return render_template('OGenAdv.html')

@strona.route('/SGenAdv')
def SGenAdv():
    return render_template('SGenAdv.html')

if __name__ == '__main__':
    strona.run(debug=True)

