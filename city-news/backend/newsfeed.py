# newsfeed.py

NEWS = [
    {"id": 1, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 2, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 3, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 4, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 5, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 6, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 7, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 8, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 9, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 10, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 11, "title": "Autonomous Delivery Drones", "content": "Codetropolis launches a fleet of autonomous delivery drones to enhance logistics."},
    {"id": 12, "title": "Virtual Reality Education", "content": "Schools in Codetropolis will implement virtual reality for immersive learning experiences."},
    {"id": 13, "title": "AI Healthcare Assistants", "content": "Hospitals in Codetropolis will use AI assistants to improve patient care."},
    {"id": 14, "title": "Smart Waste Management", "content": "The city introduces smart waste management systems to optimize garbage collection."},
    {"id": 15, "title": "Electric Bus Fleet", "content": "Codetropolis will replace its public bus fleet with electric buses."},
    {"id": 16, "title": "Urban Farming Initiative", "content": "The city promotes urban farming to increase local food production."},
    {"id": 17, "title": "Smart Street Lighting", "content": "Codetropolis installs smart street lighting to improve energy efficiency."},
    {"id": 18, "title": "Digital Identity Cards", "content": "Residents will receive digital identity cards for secure access to city services."},
    {"id": 19, "title": "AI Crime Prediction", "content": "The police department will use AI to predict and prevent crimes."},
    {"id": 20, "title": "Smart Water Management", "content": "Codetropolis implements smart water management to reduce water waste."},
    {"id": 21, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 22, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 23, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 24, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 25, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 26, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 27, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 28, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 29, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 30, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 31, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 32, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 33, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 34, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 35, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 36, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 37, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 38, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 39, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 40, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 41, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 42, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 43, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 44, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 45, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 46, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 47, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 48, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 49, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 50, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 51, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 52, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 53, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 54, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 55, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 56, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 57, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 58, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 59, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 60, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 61, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 62, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 63, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 64, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 65, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 66, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 67, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 68, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 69, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 70, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 71, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 72, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 73, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 74, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 75, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 76, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 77, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 78, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 79, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 80, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 81, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 82, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 83, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 84, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 85, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 86, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 87, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 88, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 89, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 90, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
    {"id": 91, "title": "Hovercar Racing League Announced!", "content": "Codetropolis will host its first hovercar racing league this summer."},
    {"id": 92, "title": "Mayor Introduces Anti-Gravity Bike Subsidies", "content": "Citizens are encouraged to switch to anti-gravity bikes with new government subsidies."},
    {"id": 93, "title": "Robot Ban in Parks Sparks Debate", "content": "The controversial ban on robots in public parks continues to divide citizens."},
    {"id": 94, "title": "New AI-Powered Traffic System", "content": "Codetropolis introduces an AI-powered traffic system to reduce congestion."},
    {"id": 95, "title": "Green Energy Initiative", "content": "The city launches a new green energy initiative to promote sustainability."},
    {"id": 96, "title": "Public Wi-Fi Expansion", "content": "Free public Wi-Fi will be available in all parks and public spaces."},
    {"id": 97, "title": "New Recycling Program", "content": "A new recycling program aims to reduce waste and promote environmental responsibility."},
    {"id": 98, "title": "Community Garden Project", "content": "Residents are encouraged to participate in the new community garden project."},
    {"id": 99, "title": "Electric Vehicle Charging Stations", "content": "New electric vehicle charging stations will be installed throughout the city."},
    {"id": 100, "title": "Smart City Infrastructure", "content": "Codetropolis invests in smart city infrastructure to improve urban living."},
]

def fetch_news():
    """
    Fetch the latest news stories from the database.
    Note: This function intentionally duplicates news.
    """
    return NEWS + NEWS  # Intentional bug: duplicate entries


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
