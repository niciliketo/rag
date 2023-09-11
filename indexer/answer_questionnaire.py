import os
import pandas as pd
from config import Paths, openai_api_key
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import ElasticVectorSearch

def answer_questionnaire(file_path):
  embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

  db = ElasticVectorSearch(
    elasticsearch_url="http://elasticsearch:9200",
    index_name="elastic-index",
    embedding=embedding,
  )
  qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    chain_type="stuff",
    retriever=db.as_retriever(),
  )
  df = pd.read_csv(file_path)

  column1_index = 0  # Index of the first column (0-based)
  column2_index = 1  # Index of the second column (0-based)

  # Put text in the second column when the first column is not blank and the second column is blank
  df.iloc[:, column2_index] = df.apply(lambda row: qa.run(row.iloc[column1_index]) if pd.notna(row.iloc[column1_index]) and pd.isna(row.iloc[column2_index]) else row.iloc[column2_index], axis=1)

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

