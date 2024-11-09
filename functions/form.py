import streamlit as st
import datetime

def collect_user_input():
    with st.form(key='travel_form'):
        col1, col2  = st.columns([2,1])

        with col1:
            location = st.text_input("Departure City, Country")

        with col2:
            departure_date = st.date_input("Departure Date", datetime.date.today())

        col3, col4 = st.columns([2,1])

        with col3: 
            preferred_destination = st.text_input("Arrival City, Country")

        with col4:
            arrival_date = st.date_input("Return Date", datetime.date.today() + datetime.timedelta(days=7))

        # Calculate number of days
        if departure_date and arrival_date:
            number_of_days = (arrival_date - departure_date).days
        else:
            number_of_days = 0

        bugCol1, bugCol2, bugCol3 = st.columns([1,1,1])
        
        with bugCol1:
            # Budget Preferences
            budget = st.selectbox("Budget", [
                "Low (under $1k USD)", "Medium ($1k - 3k USD)", "High ($5k+ USD)"
            ]) or "Not specified by user"

        with bugCol2:
            # Accommodation Preferences
            accommodation_types = st.multiselect("Accommodations", [
                "Girls only Hostels", "Co-ed Hostels", "Hotels", "Airbnb"
            ]) or "None"

        with bugCol3:
            # Transportation Preferences
            transportation_preferences = st.multiselect("Transportation", [
                "Ladies-only Transportation", "Lady drivers", "Public Transportation", "Ride Sharing"
            ]) or "None"
        
        col5, col6, colReason = st.columns([1,1,1])
        
        with col5:
            # Demographic Information
            current_year = datetime.datetime.now().year
            age_options = ["Select your birth year"] + list(range(current_year - 17, current_year - 100, -1))
            birth_year = st.selectbox("Age", age_options)
            
            if birth_year != "Select your birth year":
                age = current_year - int(birth_year)
            else:
                age = "Not specified by user" 
        
        with col6:
            # Nationality
            nationality = st.text_input("Nationality") or "Not specified by user"
        
        with colReason: 
            # Reason for Travel
            reason_for_travel = st.multiselect("Reason for Travel", [
                "Business", "Vacation", "Family Visit", "Study", "Possibly Relocation and Work"
            ]) or "Not specified by user"

        col7, col8, col9 = st.columns([1,1,1])
        with col7:
            # Travel Experience
            travel_experience = st.selectbox("Solo Travel Experience", [
                "Never (Never traveled before)",
                "Beginner (Travels only in a group)",
                "Intermediate (Travels 1-2 solo times)",
                "Experienced (Travels solo every year)"
            ])

        with col8:    
            # Safety Preferences
            comfort_level = st.selectbox("Comfort with Solo Travel", [
                "Very Comfortable", "Somewhat Comfortable", "Not at all Comfortable"
            ]) or "Doesn't matter"

        with col9:
            # Interests
            interests = st.multiselect("Interests", [
                "Arts and Culture", "History and Heritage", "Nature and Wildlife", "Health and Wellness", "Education", "Food and Drinks"
            ]) or "Not specified by user"

        sensitivity_preferences = st.multiselect("Sensitivity Preferences", [
            "Loud noise sensitivity", "Crowd fear", "No isolated place", "Low crime"
        ]) or "NONE"

        #checkbox for pets
        # pets = st.checkbox("Traveling with pets?") or "NONE"

        #checkbox for disabilities
        # disabilities = st.checkbox("Any Disabilities?") or "NONE"
        # if disabilities:
        #     disability_options = [
        #     "Visual Impairment", "Hearing Impairment", "Mobility Impairment",
        #     "Cognitive Impairment", "Speech Impairment", "Other"
        #     ]
        #     selected_disabilities = st.multiselect("Please specify your disabilities", disability_options)
        #     if "Other" in selected_disabilities:
        #         other_disability = st.text_input("Please specify your disability")


        additional_preferences = st.text_input("Anything else you'd like to share about your trip? Example, visit a university, or spend a day at the financial district or any another additional prefernce.") or "NONE"

        st.write("Please note this guide is created using AI. Please review it carefully. Currently, this guide does not cater to disabilities and pets. We are working on adding these features and more!")

        submit_button = st.form_submit_button(label='Create Travel Plan')

    if submit_button:
        user_data_str = f"""
        Departure Location is {location} with departure date {departure_date}.
        Arrival Destination is {preferred_destination} with return date {arrival_date}.
        User wants to travel for {number_of_days} days.
        The reason for user's travel is {reason_for_travel}.
        User was born in {age}.
        User's nationality is {nationality}.
        User's travel experience is {travel_experience}.
        User's interests are {interests}.
        User's budget preference is {budget}.
        User's comfort level with solo travel is {comfort_level}.
        User's preferred accommodation types are {accommodation_types}.
        User's preferred mode of transportation is {transportation_preferences}.
        User's sensitivity preferences are {sensitivity_preferences}.
        User's additional preferences are {additional_preferences}.
        """

        return user_data_str
    return None
