from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for users, scores, and leaderboard
users = {}
leaderboard = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username not in users:
        users[username] = {'password': password, 'score': 0}
    elif users[username]['password'] != password:
        return "Invalid credentials", 401
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET'])
def quiz():
    return render_template('quiz.html')

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    score = data['score']
    username = request.args.get('username')
    if username in users:
        users[username]['score'] = score
        leaderboard.append({'username': username, 'score': score})
        leaderboard.sort(key=lambda x: x['score'], reverse=True)  # Sort leaderboard in descending order
    return jsonify({"message": "Score submitted successfully"}), 200

@app.route('/leaderboard', methods=['GET'])
def leaderboard_page():
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    return render_template('leaderboard.html', scores=[entry['score'] for entry in sorted_leaderboard])

if __name__ == '__main__':
    app.run(debug=True)



# PS C:\Users\ADITYA\desktop> cd "D:\C TUTORIAL COURSE\SIH_2024_WyvernS\QUIZ"
# PS D:\C TUTORIAL COURSE\SIH_2024_WyvernS\QUIZ> python app.py
#  * Serving Flask app 'app'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 120-287-772

