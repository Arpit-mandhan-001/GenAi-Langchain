from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task= "text-generation",
)

llm2 = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro-0813",
    task="text-generation",
)

model1 = ChatHuggingFace(llm=llm)
model2 = ChatHuggingFace(llm=llm2)
model3 = ChatGoogleGenerativeAI(model="gemini-3.5-flash")


prompt1 = PromptTemplate(
    template="give me short 20 points notes on text \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="give me 10 Quiz question on topic \n {topic}",
    input_variables=['topic']
)
prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single document \n {notes} and {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model3 | parser

chain = parallel_chain | merge_chain


result = chain.invoke({'topic' : 'Solar system'})

print(result)
chain.get_graph().print_ascii()

