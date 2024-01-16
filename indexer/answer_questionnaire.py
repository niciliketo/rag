import os
import pandas as pd
from config import Paths
from langchain.chains import RetrievalQA
from langchain.vectorstores import ElasticVectorSearch
from langchain.vectorstores import ElasticsearchStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

def process_row(row, qa):
    column1_index = 0  # Index of the first column (0-based)
    column2_index = 1  # Index of the second column (0-based)
    column3_index = 2  # Index of the third column (0-based)

    if pd.notna(row.iloc[column1_index]):
        response = qa(row.iloc[column1_index])
        # Get the unique filenames as a list, to return to the user
        sources = list(set(os.path.basename(doc.metadata['source']) for doc in response['source_documents']))

        row.iloc[column2_index] = response['result']
        row.iloc[column3_index] = sources
    return row

def answer_questionnaire(file_path):
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
  df = pd.read_csv(file_path)

  df = df.apply(process_row, args=(qa,), axis=1)

  # Save the updated DataFrame back to a CSV file
  output_file_path = file_path + '_updated.csv'
  df.to_csv(output_file_path, index=False)
  return(output_file_path)

def answer_questionnaire_handler():
  result = ''
  for filename in os.listdir(Paths.questionnaires):
      if filename.endswith('.csv'):
        file_path = os.path.join(Paths.questionnaires, filename)
        result = answer_questionnaire(file_path)

  return result

