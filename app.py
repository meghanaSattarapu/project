from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    movies = [
        {"name": "Inception", "poster": "https://m.media-amazon.com/images/I/81xZ0hA+TjL._AC_UF894,1000_QL80_.jpg", "genre": "Action | Sci-Fi"},
        {"name": "Interstellar", "poster": "https://m.media-amazon.com/images/I/81ai6zx6IIL._AC_UF894,1000_QL80_.jpg", "genre": "Adventure | Drama | Sci-Fi"},
        {"name": "The Dark Knight", "poster": "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_UF894,1000_QL80_.jpg", "genre": "Action | Crime | Thriller"}
    ]
    return render_template('index.html', movies=movies)

@app.route('/book/<movie_name>')
def book(movie_name):
    return render_template('seats.html', movie=movie_name)

@app.route('/confirm', methods=['POST'])
def confirm():
    movie = request.form['movie']
    seats = request.form['selectedSeats']
    return f"<h2>🎉 Booking Confirmed!</h2><p>Movie: {movie}</p><p>Seats: {seats}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
