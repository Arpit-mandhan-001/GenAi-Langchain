from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv();

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash");

st.header("Research tool");

# static prompt
# user_input = st.text_input("Enter your prompt here");

# dynamic prompt
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# prompt template 
template = load_prompt("template.json")

# step 1. template making
# prompt = template.invoke({
#     'paper_input' : paper_input,
#     'style_input' : style_input,
#     'length_input' : length_input,
# })

if st.button("summarize"):
    # step 2. calling model
    # result = model.invoke(prompt)

    # we can do this in one step by forming chain this is feature of langchain
    chain = template | model
    result = chain.invoke({
     'paper_input' : paper_input,
     'style_input' : style_input,
     'length_input' : length_input,
    })
    st.write(result.content[0]["text"])
