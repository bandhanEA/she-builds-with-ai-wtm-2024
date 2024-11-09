import streamlit as st
from functions.travel_generator import generate_travel_plan
from functions.form import collect_user_input

st.set_page_config(
    page_title="NomadNari - WTM",
    page_icon="vertex-ai.png",
    layout="wide",
)

if __name__ == "__main__":

    col1, col2, col3 = st.columns([4, 0.5, 0.5])
    with col1:
        st.write("## Welcome to NomadNari")
        st.write("#### This project is part of Women Techmakers She Builds With AI 2024 Hackathon")
    with col2:
        st.image("she_builds_with_ai_general_devpost.png")
    with col3:
        st.image("vertex-ai.png")

    st.write("NomadNari allows you to create an anonymous personlized solo trip guide with the focus on safety for womxn by womxn, while creating possibilities for all. `Nari` means for `woman` in Hindi, and in Japaese it means to succeed. In Korean, `Ri` stands for `beauty and grace`. This trip is powered by Google gemini-1.5-pro model and Google Cloud Run. So, let's get started!") 
    
    user_data = collect_user_input()
    #Create a submit button to generate the travel plan
    if user_data:
        with st.spinner('Generating your travel plan...'):
            travel_plan = generate_travel_plan(user_data)
            st.write(travel_plan)
            st.session_state.travel_plan = travel_plan
            st.write("#### At this launch, we ask you copy the travel plan to your local file or preferably a Google Doc. Our next update will allow you to save the travel plan to your account along with have discussions with fellow solo womxn travellers.")

            
