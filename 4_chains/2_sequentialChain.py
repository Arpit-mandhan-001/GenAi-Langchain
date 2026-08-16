from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task= "text-generation",
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Give me deatiled report for this {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="from this detailed report give me 5 most important point {report}",
    input_variables=['report']
)

parser = StrOutputParser()

chain : RunnableSequence = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({'topic' : 'child marraige in india'})

print(result)
chain.get_graph().print_ascii()

