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
    '''Select language, social media, target group and the product name from the boxes below. 
       **click Run** to receive a **suggestions for a social media ad** from the ChatGPT
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
model_engine = "text-davinci-003"
openai.api_key = "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" 

def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    query = "Write a creative ad, in",language,"for the following product to run on",media,"aimed at", target,".Product:", product
    user_query = st.text_input("Enter query here, to click Run :q", query)
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query)
        w4 = st.button("Run")
        return st.write(w4,f"{user_query} {response}")
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