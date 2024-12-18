from flask import Flask, request, render_template, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = 'supersecretkey'

players = {}

@app.route('/')
def index():
    return render_template('index.html', players=players)

@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        player = request.form['player']
        word = request.form['word']
        score = calculate_score(word)

        if player not in players:
            players[player] = 0
        players[player] += score

        # Set cookie
        response = make_response(redirect(url_for('index')))
        response.set_cookie('player', player)
        return response

    player = request.cookies.get('player')
    return render_template('input.html', player=player)

def calculate_score(word):
    letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    return sum(letter_values.get(char, 0) for char in word.lower())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
