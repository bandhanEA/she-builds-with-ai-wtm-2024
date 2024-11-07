import streamlit as st
import requests
from vertexai.generative_models import (
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Tool,
)

API_KEY = "AIzaSyDI9pkPlHBLlMYeKE6XFmncYP9vdNhY8eI"

def collect_user_input():
    with st.form(key='travel_form'):
        # Demographic Information
        age = st.slider("Age", min_value=18, max_value=100)
        # location = st.text_input("Departure Location")
        # preferred_destination = st.text_input("Preferred Travel Destination")
        # Google Places API for location suggestions
        location = st.text_input("Departure Location")
        # if location:
        #     api_key = API_KEY
        #     url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={location}&key={api_key}"
        #     response = requests.get(url)
        #     predictions = response.json().get("predictions", [])
        #     suggestions = [pred["description"] for pred in predictions]
        #     location = st.selectbox("Select Departure Location", suggestions) if suggestions else location

        preferred_destination = st.text_input("Preferred Travel Destination")
        # if preferred_destination:
        #     url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={preferred_destination}&key={api_key}"
        #     response = requests.get(url)
        #     predictions = response.json().get("predictions", [])
        #     suggestions = [pred["description"] for pred in predictions]
        #     preferred_destination = st.selectbox("Select Preferred Travel Destination", suggestions) if suggestions else preferred_destination

        # Travel Experience
        travel_experience = st.selectbox("Travel Experience", [
            "Newbie (never traveled before)",
            "Beginner (traveled only in a group before)",
            "Medium Solo Traveler (has traveled solo 1-2 times)",
            "Frequent solo traveler (travels solo every year)"
        ])

        # Interests
        interests = st.multiselect("Interests", [
            "Outdoors", "Indoors", "Shopping", "Musuems", "Beaches", "Hiking", "Cycling", "Sightseeing", "Parties"
        ]) or "Not specified by user"

        # Nationality
        nationality = st.text_input("Nationality") or "Not specified by user"

        # Budget Preferences
        budget = st.selectbox("Budget Preferences", [
            "Low (under $1k USD)", "Medium ($1k - 3k USD)", "High ($5k+ USD)"
        ]) or "Not specified by user"

        # Safety Preferences
        comfort_level = st.selectbox("Comfort Level with Solo Travel", [
            "Very Comfortable", "Somewhat Comfortable", "Not at all Comfortable"
        ]) or "Doesn't matter"
        accommodation_types = st.multiselect("Preferred Accommodation Types", [
             "Girls only hotels", "Co-ed Hostels", "Hotels", "Airbnb"
        ]) or "None"
        transportation_preferences = st.multiselect("Preferred Mode of Transportation", [
            "Ladies only transportation", "Lady drivers", "Public transportation", "Ride sharing"
        ]) or "None"
        sensitivity_preferences = st.multiselect("Sensitivity Preferences", [
            "Loud noise sensitivity", "Crowd fear", "No isolated place", "Low crime"
        ]) or "NONE"

        #checkbox for pets
        pets = st.checkbox("Traveling with pets?") or "NONE"

        #checkbox for disabilities
        disabilities = st.checkbox("Any Disabilities?") or "NONE"
        # if disabilities:
        #     disability_options = [
        #     "Visual Impairment", "Hearing Impairment", "Mobility Impairment",
        #     "Cognitive Impairment", "Speech Impairment", "Other"
        #     ]
        #     selected_disabilities = st.multiselect("Please specify your disabilities", disability_options)
        #     if "Other" in selected_disabilities:
        #         other_disability = st.text_input("Please specify your disability")

        additional_preferences = st.text_input("Anything else you'd like to share about your preferences?") or "NONE"

        # Communication Method
        communication_method = st.text_input("Email") or "Not specified by user"

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        user_data_str = f"""
        User's age is {age}.
        Departure Location is {location}.
        Arrival Destination is {preferred_destination}.
        User's nationality is {nationality}.
        User's travel experience is {travel_experience}.
        User's interests are {interests}.
        User's budget preference is {budget}.
        User's comfort level with solo travel is {comfort_level}.
        User's preferred accommodation types are {accommodation_types}.
        User's preferred mode of transportation is {transportation_preferences}.
        User's sensitivity preferences are {sensitivity_preferences}.
        User is travelling with pets: {pets}.
        User has disabilities: {disabilities}.
        User's additional preferences are {additional_preferences}.
        """

        return user_data_str
    return None

def generate_travel_plan(user_data):
    model = GenerativeModel(
        "gemini-1.5-pro",
        generation_config=GenerationConfig(temperature=0),
    )
    # Define a prompt that instructs the model to consider safety
    prompt = f"""
    You a travel guide for women. Based on the following information:
    {user_data}
    
    Create a detailed travel itinerary for a solo female traveler visiting 
    {user_data.preferred_destination} from {location}.

    Key Considerations:

    Safety: Prioritize user's safety as a woman and their accommodations, transportation, and activities that are known to be safe for solo female travelers.
    Costs under {budget}: Provide a day to day estimated cost in {location} rate and {preferred_destination} rate and total estimated cost range.
    Emergency Contacts: Include a list of emergency numbers for the destination and advise the user to save them on their phone.
    Share tips for solo travelers in {preferred_destination}.
    Additional Tips for the Model:
    
    Format the plan in a clear professional organized manner and a detailed itinerary with day-by-day activities and cost range with links for each location you are recommending. Format the plan to be easy to read and follow.
    """

    response = model.generate_content(prompt)
    return response.text

st.set_page_config(
    page_title="WTM Hackthon 2024 Chat",
    page_icon="vertex-ai.png",
    layout="wide",
)

if __name__ == "__main__":
    st.write("## Your Personalized Travel Plan, powered by Gemini")

    col1, col2 = st.columns([8, 1])
    with col1:
        st.title("She Builds With AI 2024")
    with col2:
        st.image("she_builds_with_ai_general_devpost.png")
    
    st.write("### Enter your travel preferences below to receive a personalized travel plan for a solo female traveler")
    user_data = collect_user_input()
    if user_data:
        travel_plan = generate_travel_plan(user_data)
        st.write(travel_plan)

