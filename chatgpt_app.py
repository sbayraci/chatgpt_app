# Importing required packages
import streamlit as st
import openai

st.title("CX Social Media Helper ")
st.info(
    '''This is a Chat-GPT application that allows CX social media specialists to interact with 
       the OpenAI API's implementation of the ChatGPT model and generate creative ad suggestions for social media campaigns.
       '''
    )
st.sidebar.header("Instructions")
st.sidebar.info(
    '''Enter language, social media, target group and the product name from the input boxes. 
       **Click Run** to receive a **suggestions for a social media ad** from the ChatGPT
       '''
    )

language = st.sidebar.selectbox(
    'Language',
    ('English', 'Turkish', 'German'))

media = st.sidebar.selectbox(
    'Social Media',
    ('Instagram', 'Facebook', 'Twitter','TikTok','LinkedIn'))

target = st.sidebar.text_input('Target Group :q','Company Executives')

product = st.sidebar.text_input('Product :q','BMW 7 Series')




# Set the model engine and your OpenAI API key
openai.api_type='azure'
openai.api_base='https://oai-bo-azwe-prod-csr.openai.azure.com/'
openai.api_key='f8ce8085901b45c4992f16b31a44071b'
openai.api_version='2022-12-01'
model_engine ='oai-bo-davinci003'

def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    query = "Write a creative ad, in",language,"for the following product to run on",media,"aimed at", target,".Product:", product
    user_query = st.text_input("Click Run to generate output:q", query)
    
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query)
        result = st.button("Run")
        if result:
            return st.write(f"{user_query} {response}")
    
def ChatGPT(user_query):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0].text
    return response
# call the main function
main()
