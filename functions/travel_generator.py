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
    Create a detailed travel itinerary for a solo female traveler. 
    Based on the following information:
    {user_data}

    Key Considerations:
    - Safety as a Woman: You must prioritize women-only night accommodations and recommend places with positive reviews from female solo travelers.  Include the names and addresses of hostels, hotels, hostels, or Airbnb accommodations.
    - Budget: You must display all the costs in both the destination location and arrival location currency rates for each day, and total cost for the trip while keeping all costs under the budget.
    - Emergency Contacts: Include a list of emergency numbers and locations like police station, pharmacy for the destination and advise the user to save them on their phone. 
    - Safe Locations: Include a Clinic and Pharmacy near the user's living place.
    - Transportation: Include transportation methods to sightseeing.
    - Events: Include any festivals or local events happening during the travel dates.
    - Weather: Include a forecast for the travel dates.
    - Tips: Share tips for solo travelers in the preferred destination.
    - Additional mentions: flight costs, visa requirements and costs, and travel insurance recommendations.
    """

    response = model.generate_content(prompt)
    return response.text