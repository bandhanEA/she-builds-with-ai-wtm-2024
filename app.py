import time

from google.cloud import bigquery
import streamlit as st
from vertexai.generative_models import FunctionDeclaration, GenerativeModel, Part, Tool

BIGQUERY_DATASET_ID = "she_builds_with_ai_2024"

list_datasets_func = FunctionDeclaration(
    name="list_datasets",
    description="Get a list of datasets that will help answer the user's question",
    parameters={
        "type": "object",
        "properties": {},
    },
)

list_tables_func = FunctionDeclaration(
    name="list_tables",
    description="List tables in a dataset that will help answer the user's question",
    parameters={
        "type": "object",
        "properties": {
            "dataset_id": {
                "type": "string",
                "description": "Dataset ID to fetch tables from.",
            }
        },
        "required": [
            "dataset_id",
        ],
    },
)

get_table_func = FunctionDeclaration(
    name="get_table",
    description="Get information about a table, including the description, schema, and number of rows that will help answer the user's question. Always use the fully qualified dataset and table names.",
    parameters={
        "type": "object",
        "properties": {
            "table_id": {
                "type": "string",
                "description": "Fully qualified ID of the table to get information about",
            }
        },
        "required": [
            "table_id",
        ],
    },
)

sql_query_func = FunctionDeclaration(
    name="sql_query",
    description="Get information from data in BigQuery using SQL queries",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "SQL query on a single line that will help give quantitative answers to the user's question when run on a BigQuery dataset and table. In the SQL query, always use the fully qualified dataset and table names `eax-apps.she_builds_with_ai_2024.user-data` in the correct format with template strings.",
            }
        },
        "required": [
            "query",
        ],
    },
)

role_func = FunctionDeclaration(
    name="assign_role_to_model",
    description=""" You are a chatbot on giving recommendations to women experiencing menopause. Find ways they can improve their lifestyle to healthy based on the data recieved on BigQuery
    """,
    parameters={
        "type": "object",
        "properties": {
            "sleep": {
                "type": "string",
                "description": "The number of hours user slept most nights",
            },
            "night_sweats": {
                "type": "string",
                "description": "The number of nights the user's sleep was disrupted by night sweats",
            },
            "period_start": {  
                "type": "string",
                "description": "The date the user's period started",
            },
            "period_end": {
                "type": "string",
                "description": "The date the user's period ended",
            },
            "period_heaviness": {
                "type": "string",
                "description": "The heaviness of the user's period",
            },
            "spotting": {
                "type": "string",
                "description": "If the user experienced spotting",
            },
            "diet": {
                "type": "string",
                "description": "The user's diet type low, med, high",
            },
            "exercise": {
                "type": "string",
                "description": "The user's exercise level low, med, high",
            },
            "stress_levels": {
                "type": "string",
                "description": "The user's stress levels low, med, high",
            },
            "alcohol_consumption": {
                "type": "string",
                "description": "The user's alcohol consumption low, med, high",
            },
            "medications_supplements": {
                "type": "string",
                "description": "The user's medications or supplements",
            },
            "mood_swings": {
                "type": "string",
                "description": "The user's mood swings",
            },
            "anxiety": {
                "type": "string",
                "description": "The user's anxiety",
            },
            "depression": {
                "type": "string",
                "description": "The user's depression",
            },
            "hot_flashes": {
                "type": "string",
                "description": "The user's hot flashes",
            },
            "vaginal_dryness": {
                "type": "string",
                "description": "The user's vaginal dryness",
            },
            "joint_pain": {
                "type": "string",
                "description": "The user's joint pain",
            },
            "date_of_birth": {
                "type": "string",
                "description": "The user's year of birth",
            }
        },
        "required": [
            "sleep",
            "night_sweats",
            "period_start",
            "period_end",
            "period_heaviness",
            "spotting",
            "diet",
            "exercise",
            "stress_levels",
            "alcohol_consumption",
            "medications_supplements",
            "mood_swings",
            "anxiety",
            "depression",
            "hot_flashes",
            "vaginal_dryness",
            "joint_pain",
            "date_of_birth"
        ],
    },
)

sql_query_tool = Tool(
    function_declarations=[
        list_datasets_func,
        list_tables_func,
        get_table_func,
        sql_query_func,
        role_func,
    ],
)

model = GenerativeModel(
    "gemini-1.5-pro",
    generation_config={"temperature": 0},
    tools=[sql_query_tool],
)

st.set_page_config(
    page_title="WTM Hackthon 2024 Chat",
    page_icon="vertex-ai.png",
    layout="wide",
)

col1, col2 = st.columns([8, 1])
with col1:
    st.title("She Builds With AI 2024 Chat")
with col2:
    st.image("she_builds_with_ai_general_devpost.png")
    

st.subheader("In draft mode - only SQL queries logic implemented, no authentication or proper 'medical' recommendations yet.")

# st.markdown(
#     "[Source Code](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/function-calling/sql-talk-app/)   •   [Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/function-calling)   •   [Codelab](https://codelabs.developers.google.com/codelabs/gemini-function-calling)   •   [Sample Notebook](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb)"
# )

with st.expander("More information about this chat", expanded=False):
    st.write(
        """
        - Gemini API used with gemini-1.5-pro model
        - Google Library used: vertexai.generative_models
        - Database: Google Cloud BigQuery
        - Temporary UI made possible with Streamlit - https://streamlit.io/
        - This snipet of code deals with fetching data from BigQuery using Gemini API's function calling only. 
        - NOTE: authentication and health reccomendations are not implemented, only fetching data from BigQuery using natural language. 

        Questions tested so far - 
        - What kind of information is in this database?
        - What are all the periods start and end date for user 1234? 
        - What is the sleep duration for most nights for user 1234?
        - How many times did user 1234 experience joint pain as High?
    """
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"].replace("$", r"\$"))  # noqa: W605
        try:
            with st.expander("Function calls, parameters, and responses"):
                st.markdown(message["backend_details"])
        except KeyError:
            pass

if prompt := st.chat_input("Ask me about information in the database..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        chat = model.start_chat()
        client = bigquery.Client()
# about where the information in your response is
#             coming from in the database. Only use information that you learn
#             from BigQuery, do not make up information.
        prompt += """
            You are a doctor treating women experiencing menupause or going to experience menopause between the ages 45-90 years old. 
            Please give a high-level summary followed by detail in
            plain language. Use information available in the BigQuery with column names as: 
            Date - Date the user logged/inputted their data,	
            ID - User ID,
            Sleep_Quality - The Quality of user's sleep, 
            Sleep_Duration_Most_Nights_hours - the number of hours user slept most nights,
            Night_Sweats_Disruption - If the user experienced Night sweats and sleep disruption or not,
            Period_Start - Date the user's period started,
            Period_End - Date the user's period ended,	
            Period_Heaviness - If the user's period was heavy or not,	
            Spotting - If the user experienced spotting or not,
            Diet - What kind of a diet the user followed,
            Exercise - The user exercised low, med, high or not at all,
            Stress_Levels - The user expereinced stress levels low, med, high or not at all,
            Alcohol_Consumption	- The user consumed alcohol low, med, high or not at all,
            Medications_Supplements	- The user medications or supplements,
            Mood_Swings - The user experienced mood swings or not,
            Anxiety	- The user experienced anxiety or not,
            Depression- The user experienced depression or not,
            Hot_Flashes	- The user experienced hot flashes or not,
            Vaginal_Dryness	- The user experienced vaginal dryness or not,	
            Joint_Pain - The user experienced joint pain or not,	
            Date_of_birth - The user's year of birth. 

            Structure your responses with ways to improve their numbers given the user's data recieved from BigQuery.
            """

        try:
            response = chat.send_message(prompt)
            response = response.candidates[0].content.parts[0]

            print(response)

            api_requests_and_responses = []
            backend_details = ""

            function_calling_in_process = True
            while function_calling_in_process:
                try:
                    params = {}
                    for key, value in response.function_call.args.items():
                        params[key] = value

                    print(response.function_call.name)
                    print(params)

                    if response.function_call.name == "list_datasets":
                        api_response = client.list_datasets()
                        api_response = BIGQUERY_DATASET_ID
                        api_requests_and_responses.append(
                            [response.function_call.name, params, api_response]
                        )

                    if response.function_call.name == "list_tables":
                        api_response = client.list_tables(params["dataset_id"])
                        api_response = str([table.table_id for table in api_response])
                        api_requests_and_responses.append(
                            [response.function_call.name, params, api_response]
                        )

                    if response.function_call.name == "get_table":
                        api_response = client.get_table(params["table_id"])
                        api_response = api_response.to_api_repr()
                        api_requests_and_responses.append(
                            [
                                response.function_call.name,
                                params,
                                [
                                    str(api_response.get("description", "")),
                                    str(
                                        [
                                            column["name"]
                                            for column in api_response["schema"][
                                                "fields"
                                            ]
                                        ]
                                    ),
                                ],
                            ]
                        )
                        api_response = str(api_response)

                    if response.function_call.name == "sql_query":
                        job_config = bigquery.QueryJobConfig(
                            maximum_bytes_billed=100000000
                        )  # Data limit per query job
                        try:
                            cleaned_query = (
                                params["query"]
                                .replace("\\n", " ")
                                .replace("\n", "")
                                .replace("\\", "")
                            )
                            query_job = client.query(
                                cleaned_query, job_config=job_config
                            )
                            api_response = query_job.result()
                            api_response = str([dict(row) for row in api_response])
                            api_response = api_response.replace("\\", "").replace(
                                "\n", ""
                            )
                            api_requests_and_responses.append(
                                [response.function_call.name, params, api_response]
                            )
                        except Exception as e:
                            error_message = f"""
                            Trouble fetching user details from BigQuery. 
                            Please try rephrasing your question. Details:

                            {str(e)}"""
                            st.error(error_message)
                            api_response = error_message
                            api_requests_and_responses.append(
                                [response.function_call.name, params, api_response]
                            )
                            st.session_state.messages.append(
                                {
                                    "role": "assistant",
                                    "content": error_message,
                                }
                            )

                    print(api_response)

                    response = chat.send_message(
                        Part.from_function_response(
                            name=response.function_call.name,
                            response={
                                "content": api_response,
                            },
                        ),
                    )
                    response = response.candidates[0].content.parts[0]

                    backend_details += "- Function call:\n"
                    backend_details += (
                        "   - Function name: ```"
                        + str(api_requests_and_responses[-1][0])
                        + "```"
                    )
                    backend_details += "\n\n"
                    backend_details += (
                        "   - Function parameters: ```"
                        + str(api_requests_and_responses[-1][1])
                        + "```"
                    )
                    backend_details += "\n\n"
                    backend_details += (
                        "   - API response: ```"
                        + str(api_requests_and_responses[-1][2])
                        + "```"
                    )
                    backend_details += "\n\n"
                    with message_placeholder.container():
                        st.markdown(backend_details)

                except AttributeError:
                    function_calling_in_process = False

            time.sleep(3)

            full_response = response.text
            with message_placeholder.container():
                st.markdown(full_response.replace("$", r"\$"))  # noqa: W605
                with st.expander("Function calls, parameters, and responses:"):
                    st.markdown(backend_details)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response,
                    "backend_details": backend_details,
                }
            )
        except Exception as e:
            print(e)
            error_message = f"""
                Error in the try and catch. Details:

                {str(e)}"""
            st.error(error_message)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message,
                }
            )
