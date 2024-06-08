import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.MCQGenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.MCQGenerator.MCQGenerator1 import generate_evaluate_chain
from src.MCQGenerator.logger import logging

# streamlit is uded to create a rapid simple web app for testing

# loading json files
with open('C:\Users\hp26\Documents\MCQGenerator\response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)


# creating a title for the app
st.title('MCQ Creator Application with Langchain')

# Create a form using st.form
with st.form('user_inputs'):
    #file upload
    uploaded_file = st.file_uploader('upload a PDF or txt file')

    # input Fields
    mcq_count = st.number_input('no. of MCQs', min_value=3, max_value=50)

    # subject
    subject = st.text_input('Inser Subject', max_chars=20)

    # Quiz Tone
    tone = st.text_input('Complexity level of Questions', max_chars=20, placeholder='simple')

    # Add Button 
    button = st.form_submit_button('Create MCQS')

    # check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and to:
        with st.write('Generating MCQ...')
        try:
            text = read_file(uploaded_file)
            # count tokens and the cost of API call
            with get_openai_callback() as cb:
                response = generate_evaluate_chain.run(
                    text=text,
                    number=mcq_count,
                    subject=subject,
                    tone=tone,
                    response_json=json.dump(RESPONSE_JSON)
                )
        except Exception as e:
                st.write(f'Error: {e}')
                traceback.print_exc()
                st.stop()
        else:
                print(f'Total Token: {cb.total_token}')
                print(f'Prompt Token: {cb.prompt_token}')
                print(f'Completion Token: {cb.completion_token}')
                print(f'Total Cost: {cb.total_cost}')

                if isinstance(response, dict):
                    # Extract the quiz from the response
                    quiz = response.get('quiz',None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        df = pd.DataFrame(table_data)
                        df.index = df.index+1
                        st.table(df)
                        #display results in a text box as well
                        st.text_area(label="Review", value=response['review'])
                    else:
                        st.error('Error in the table data')
                else:
                    st.write(response)
