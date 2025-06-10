from flask import Flask  # Import Flask framework
import random           # Import random module

app = Flask(__name__)   # Create Flask app instance

# List of interesting facts
facts_list = [
    "Honey never spoils.",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts.",
    "Wombat poop is cube-shaped.",
]

# Define routes for the Flask app

@app.route("/")  # Define route for the homepage
def home():
    # Return a simple HTML page with a welcome message
    return "<h1>Welcome to the Random Facts App!</h1>"

@app.route("/fact")  # Define route for the random fact
def random_fact():
    # Return a random fact from the list
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/about")  # Define route for the about page
def about():
    # Return a simple HTML page with information about the app
    return "<h1>About This App</h1><p>This app provides random interesting facts.</p>"

@app.route("/coin")  # Define route for the coin flip
def flip_coin():
    # Simulate a coin flip and return the result
    result = random.choice(["Heads", "Tails"])
    return f"<h1>Coin Flip Result</h1><p>{result}</p>"

@app.route("/password")  # Define route for the password generator
def generate_password():
    # Generate a random password of length 12
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(12))
    return f"<h1>Generated Password</h1><p>{password}</p>"

@app.route("/pictures")  # Define route for the random pictures page
def random_pictures():
    # List of image URLs
    image_urls = [
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "https://images.unsplash.com/photo-1465101046530-73398c7f28ca",
        "https://images.unsplash.com/photo-1518717758536-85ae29035b6d",
        "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
        "https://images.unsplash.com/photo-1465101178521-c1a9136a3b41"
    ]
    # Choose a random image
    img_url = random.choice(image_urls)
    # Return HTML with the random image
    return f'<h1>Random Picture</h1><img src="{img_url}" alt="Random Picture" style="max-width:400px;"><p>Refresh to see another!</p>'

# Run the app in debug mode
# pipenv run python main.py = To run this type of python idk
if __name__ == "__main__":
    app.run(debug=True)

