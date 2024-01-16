import os.path
from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.vectorstores import ElasticVectorSearch
from langchain.vectorstores import ElasticsearchStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


embeddings = OpenAIEmbeddings()

db = ElasticVectorSearch(
    elasticsearch_url="http://elasticsearch:9200",
    index_name="elastic-index",
    embedding=embeddings,
)
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    chain_type="stuff",
    retriever=db.as_retriever(),
    return_source_documents=True,
)

def ask_handler(query):
    response = qa(query)
    # Get the unique filenames as a list, to return to the user
    sources = list(set(os.path.basename(doc.metadata['source']) for doc in response['source_documents']))

    return {
        "response": response['result'],
        "sources": sources
    }
