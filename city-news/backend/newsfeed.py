# newsfeed.py

NEWS = [
    {"id": 1, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 2, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 3, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
]

def fetch_news():
    """
    Fetch the latest news stories from the database.
    Note: This function intentionally duplicates news.
    """
    unique_news = {story['id']: story for story in NEWS}
    return list(unique_news.values())

def format_news(news):
    """
    Format news stories for the frontend.
    """
    formatted = []
    for story in news:
        formatted.append(f"{story['title']}: {story['content']}")
    return formatted


if __name__ == "__main__":
    print("Fetching news...")
    news = fetch_news()
    formatted_news = format_news(news)
    for item in formatted_news:
        print(item)
