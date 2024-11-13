# Welcome to NomadNari!

NomadNari allows you to create an anonymous personalized travel guide for solo traveling keeping women's safety first. The meaning behind NomadNari comes from, `Nari` meaning `woman` in Hindi, and in Japanese meaning to succeed. In Korean, `Ri` means `beauty and grace`. Created for women by women.

- The gender equity category this project is breaking barriers towards:
  - `Women and girl’s safety`
- This project aims to combat United Nation's Sustainabilty goals
  - `5.2 - Eliminate all forms of violence against all women and girls in the public and private spheres, including trafficking and sexual and other types of exploitation.`
  - `5.B - Enhance the use of enabling technology, in particular information and communications technology, to promote the empowerment of women.`

### Inspiration behind NomadNari

- As an elder sister and a best friend, I have two very close single women in my life who travel solo, but rarely because it has takes months to even plan a single trip, hours of reading reviews, and hours of double checking each and every location, route, and accommodation.
- There are currently apps that help women travel together and help other solo travelers when they think they might be in danger but there is currently nothing out there that creates a safe trip guide for women.
- A survey of 400 U.S. women found that two in five had experienced sexual harassment while traveling alone. Sexual harassment is the most common gender risk for solo female travelers. ([https://www.researchgate.net/publication/344631063_The_Dark_Side_of_Solo_Female_Travel_Negative_Encounters_with_Male_Strangers])
- NomadNari aims to eliminate the time it takes to research and provide women with a list of safe locations they can follow up on and choose from instead of thousands of options which lead to time wasting, headaches, and fear.

### Why should we support NomadNari?

- Research shows that traveling alone can offer several pros, including: increased self-confidence, personal growth through self-reflection, greater flexibility to tailor your itinerary, deeper immersion in local culture, opportunities to meet new people, improved decision-making skills, and a sense of empowerment by taking charge of your own experiences; essentially allowing you to discover more about yourself and your capabilities in a new environment. ([https://www.tandfonline.com/doi/full/10.1080/13683500.2024.2362380#:~:text=Exploring%20the%20benefits%20of%20solo,et%20al.%2C%202017).])

##### Visit NomadNari > [(https://she-builds-with-ai-2024-18051056880.us-central1.run.app/)]

### What does NomadNari currently do?

- The user inputs their preferences into the form including location, travel dates, accommodations, transportation, previous experiences, travel, etc.
- Based on the data user inputted and prompt engineering, the Gemini model generates a personalized travel guide for the user

### How we built it?

- We started with a survey, we asked our friends and family that travel solo, how would they like to be helped while planning their solo trip and what resources would they like to see.
- The most suggested answer was a condensed list of safe places for them to travel to, so they dont have to waste hours reading up reviews. Hence, the travel guide - NomadNari.
- NomadNari is currently built with Python.
- We used the `google-cloud-aiplatform` Python package, and enabled the `Vertex AI API` and used the `vertexai` SDK, that allowed us to use Gemini through the `gemini-1.5-pro` model.
- We then picked `Streamlit` to support the front-end.
- After through testing and updates, we deployed the application to Google Cloud Cloud Run.

### How does NomadNari currently work?

- The user inputs their preferences on the form including location, dates, accommodations, travel, etc.
- This data is fed into the Gemini model along with some Prompts to generate a travel guide for the user

### Challenges we ran into?

- As a millennial woman who graduated high school a couple of plenty years ago, Im only used to in-person hackathons. I personally faced difficulties with securely a team at first by going ghosted and then when I finally got into a team 3 times time after time with folx of complete opposite timezones on different topics but unfortunately everyone happened to back out due to their own personal reasons or time constraints which I understand, because life happens to all of us.
- November 6th, when the last team didn't work out, I decided to roll up my sleeves and found the right opportunity to do this project for my loved ones.

### What we learned?

- We learned how conveniently we were able to use the `google-cloud-aiplatform` package to utilize Gemini while giving a specific data!
- We also learned about the open-source Python Streamlit where we can turn Python scripts to web apps, as a full-time back-end engineer, I found this framework very convenient to work with as well. And I hope to contribute to this open-source package as well.
- We learned that if we keep on going, no matter what, it is possible to reach to your goal.

### Accomplishments we're proud of?

- Utilizing AI to do good and try to make this world a safer place for women.
- Utlizing AI to give women the confidence they need to travel solo.
- Utilizing Google Cloud Run to deploy the application.
- Testing pre-production and post-production.
- Being able to get back up and keep on trying to achieve our mission of providing a trip guide even after facing challenges.

##### Future plans include:

- A new design for UI/UX
- Account Sign Up/Sign In
- A Community Discussion Board
- Ability to Edit the Travel Guide and Save it to their Profile
- Ability to support folx with disabilities and pets
- Firebase Authentication
- Firebase Firestore
- Cloud Functions

##### Visit NomadNari > [(https://she-builds-with-ai-2024-18051056880.us-central1.run.app/)]

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
