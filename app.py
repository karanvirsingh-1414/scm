from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Basic server-side validation
    if not email or not password:
        return 'Please enter both email and password.'

    # You can add your authentication logic here
    # For demonstration purposes, redirect to a dashboard page
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the Dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
