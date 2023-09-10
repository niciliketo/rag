import os
from langchain.document_loaders import BSHTMLLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from langchain.vectorstores import ElasticsearchStore
from langchain.document_loaders import DirectoryLoader
from config import Paths, openai_api_key
from config import openai_api_key

def index_handler():
    loader = DirectoryLoader(Paths.data)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=0
    )

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    documents = text_splitter.split_documents(data)
    db = ElasticVectorSearch.from_documents(
        documents,
        embeddings,
        elasticsearch_url="http://elasticsearch:9200",
        index_name="elastic-index",
    )
    return(db.client.info())


# if __name__ == "__main__":
#    main()
