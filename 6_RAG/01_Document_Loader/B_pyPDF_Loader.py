from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Arpit_Mandhan.pdf')

docs = loader.load()

print(docs)
print(type(docs))
print(len(docs))

