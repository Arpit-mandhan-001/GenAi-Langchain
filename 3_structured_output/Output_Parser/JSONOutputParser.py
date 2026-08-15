from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv();

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task= "text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="give me top 10 movies \n {format_instruction}",
    input_variables=[],
    partial_variables= {'format_instruction': parser.get_format_instructions()} # this add text {return JSON object}
)

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)