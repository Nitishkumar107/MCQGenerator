import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv

from src.MCQGenerotor.utils import read_file, get_table_data
from src.MCQGenerotor.logger import logging


from langchain_openai import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import PyPDF2 

# load the necessary packages from environment
load_dotenv()

# access th eenvironment variables just like you would with os.environ
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
#print(OPENAI_API_KEY)

# temperature is creativity parameters(0-2)
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name = "gpt-3.5-turbo", temperature=0.5)

TEMPLATE='''
Text:{text}
you are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number}. multiple choice questions for {subject} students
in {tone} tone. Make sure the questions are not repeated and check all the questions to be conforming the text as well. 
Make sure to format your response like RESPONSE_JSON below and use it as a guide.\
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
'''

# there are 2 types of prompts 1) zero-shot prompt and 2) one-shot prompt
# zero-shot prompt-: when question is asked directly from the LLM Model without giving any data
# one-shot prompt-: when question is asked from the model according to the givn data , here we need to trained the model by fine tuning
#          and hyperparameter tuning .


# thest variable will be passed by the user
quiz_generaton_prompt = PromptTemplate(input_variables=['text','number','subject','tone','response_json'],
                                    template=TEMPLATE
                                    )


# connecting LLM chain with prompt component
# quiz_chain is llm chain object, this is our 1st chain chreated here
quiz_chain = LLMChain(prompt=quiz_generaton_prompt,llm=llm, output_key="quiz", verbose=True)
# verbose -> want to see the execution or not in ternimal







