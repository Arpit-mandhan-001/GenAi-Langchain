from langchain_community.document_loaders import WebBaseLoader


url = "https://www.youtube.com/watch?v=bL92ALSZ2Cg&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=12"
loader = WebBaseLoader(url)

docs = loader.load()

print(docs)
print(len(docs))