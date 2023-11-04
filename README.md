# rag
Retrieval augmented generation

## Quick start
Put the documents you want to RAG into the data directory
Make sure docker compose is installed, then run
```bash
docker compose up
```

# Details
The docker compose file creates
1. An ElasticSearch container, for storing documents
2. A indexer container, for indexing documents
3. An app container, to serve the API

## Details on using
Put unstructured documents in the data directory
When docker starts, the indexer container will parse them using the langchain DirectoryLoader
Once started, visit http://127.0.0.1:8000/docs and use the ask endpoint to start asking questions
Alternatively, you can put a CSV of questions into the indexer/questionnaires folder, and call the appropriate endpoint to populate answers.
Note that the questions must be in column 1 and answers will be added to column 2 for all non-blank rows.


