# Discover the world, your way! 

- This application allows you to create a personalized plan for travelling solo. Created for womxn by womxn. The meaning behind NomadNari comes from, `Nari` means for "woman" in Hindi, and in Japaese it means to succeed. In Korean, `Ri` stands for "beauty and grace". NomadNari aims to provide women with a travel guide that will help them succeed as a traveler. 

### Inspiration behind NomadNari
- As an elder sister and a best friend, I have two very close womxn to me who travel solo, but only once a year because it takens months to even plan the trip, hours of reading reviews, and hours of double checking each and every location, route, and accomodation. Why? As you know,because of the research behind it. There are currently apps that help women travel together and help other solo travelers but there is currently nothing out there that creates safe trip trips for womxn. 
- NomadNari aims to elimate the time it takes to research and provide womxn with a list of safe locations they can follow up on and choose from instead of thousands of options which lead to time wasting and headaches. 
- A survey of 400 U.S. women found that two in five had experienced sexual harassment while traveling alone. Sexual harassment is the most common gender risk for solo female travelers. ([https://www.researchgate.net/publication/344631063_The_Dark_Side_of_Solo_Female_Travel_Negative_Encounters_with_Male_Strangers])

### Why should we support NomadNari? 
- Research shows that traveling alone can offer several pros, including: increased self-confidence, personal growth through self-reflection, greater flexibility to tailor your itinerary, deeper immersion in local culture, opportunities to meet new people, improved decision-making skills, and a sense of empowerment by taking charge of your own experiences; essentially allowing you to discover more about yourself and your capabilities in a new environment. ([https://www.tandfonline.com/doi/full/10.1080/13683500.2024.2362380#:~:text=Exploring%20the%20benefits%20of%20solo,et%20al.%2C%202017).])

- The gender equity category this project is break barriers towards 
    - `Women and girl’s safety`
- This project aims to combat United Nation's Sustainabilty goals
    - `5.2 - Eliminate all forms of violence against all women and girls in the public and private spheres, including trafficking and sexual and other types of exploitation.`
    - `5.B - Enhance the use of enabling technology, in particular information and communications technology, to promote the empowerment of women.`

### How we built it? 
- We started with a survey, we asked our friends and family that travel solo, how would they like to be helped while planning their solo trip and what resources they would like to see. 
- We used the `google-cloud-aiplatform` Python package, and used the `vertexai` SDK, that allowed us to Gemini through the `gemini-1.5-pro` model. 
- We then picked `Streamlit` to support the front-end 

### How does NomadNari currently work? 
- The user inputs their prefernces on travel including location, dates, accomodations, travel, etc. 
- This data is then fed into the Gemini model along with some Prompts to generate a travel guide for the user

### Challenges we ran into?
- As a millenial woman who graduated high school a couple of plenty years ago, Im only used to in-person hackathons. NomadNari faced difficulties with securely a team that was not going to give up, we had 3 instances of where we thought had a team but time after time everyone back out due to their own personal reasons or time constraints and NomadNari understands, because life happens to all of us. 

### Accomplishments we're proud of? 
- We were able to get back up and keep on trying to achieve our mission of providing a trip guide even after facing several challenges. 
- Deploying to production

##### Future plans include: 
- Account Sign Up/Sign In
- A Community Discussion Board
- Ability to Edit the Travel Guide and Save it to their Profile
- Ability to support folx with disabilities and pets
- Firebase Authentication
- Firebase Firestore
- Cloud Functions 

## Overview
This app demonstrates the power of
- Generative AI on Vextex AI - The `google-cloud-aiplatform` Python package, `vertexai` SDK, and Gemini's Generative Model `gemini-1.5-pro`. 
- Streamlit `streamlit` for UI
- Cloud Run for deploying

## Prerequisites

- A Google Cloud project with billing enabled
- APIs for Vertex AI, and Cloud Run enabled

## To run the app on your local machine: 
- Authenticate your local machine with your project name
`gcloud config set project your-project-id`
- Run `bash setup.sh`

This script will:

- Connect to the Vertex AI API
- Install Python and packages
- Start the app

#### We are working on updating this project after the hackathon is over and publish this project to create a safer travel experience for every women