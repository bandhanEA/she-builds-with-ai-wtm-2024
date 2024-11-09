from vertexai.generative_models import (
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Tool,
)

def generate_travel_plan(user_data):
    model = GenerativeModel(
        "gemini-1.5-pro",
        generation_config=GenerationConfig(temperature=0),
    )
    # Define a prompt that instructs the model to consider safety
    prompt = f"""
    You are a travel guide for women that prioritizes safety for women. 
    Create a detailed travel itinerary for a solo female traveler while giving the best travel recommendations in the destination location.
    Based on the following information:
    {user_data}

    Key Considerations:
    - Safety as a Woman: You must prioritize women-only night accommodations and recommend places with positive reviews from female solo travelers.  Include the names and addresses of hostels, hotels, hostels, or Airbnb accommodations.
    - Budget: You must display all the costs in both the destination location and arrival location currency rates for each day, and total cost for the trip while keeping all costs under the budget.
    - Emergency Contacts: Include a list of emergency numbers and locations for the destination and advise the user to save them on their phone. Locations should include closest pharamacies, hospitals, police stations, and their nationality embassy to the accommodations recommended.
    - Tips: Share tips for solo travelers in the preferred destination.
    - You must include domain website links and addresses of recommended places.

    Please ensure the itinerary includes:
    - Keep in mind if user has a disability or not while recommending activities.
    - Clinics and pharmacies near the accommodations.
    - Transportation  to sightseeing options and schedules.
    - Any cultural or local events happening during the travel dates.
    - Weather forecast for the travel dates.
    - Local events and festivals happening during the travel dates.
    - Additional mention that this agenda: flight costs, visa requirements and costs, and travel insurance recommendations.
    """

    response = model.generate_content(prompt)
    return response.text