from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from newsfeed import fetch_news, format_news

app = Flask(__name__, static_folder='static', template_folder='templates')

# Enable CORS for your API
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Serve the news API
@app.route("/api/news", methods=["GET"])
def get_news():
    """
    Serve the latest news stories to the frontend.
    """
    try:
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 5))
        news = fetch_news()
        start = (page - 1) * per_page
        end = start + per_page
        paginated_news = news[start:end]
        formatted = format_news(paginated_news)
        return jsonify(formatted)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve the main page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
