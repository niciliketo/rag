<script type="text/babel">
      const { useState } = React;
      const API_URL = 'http://localhost:8000';  // Replace with your API URL

      function App() {
        const [query, setQuery] = useState('');
        const [response, setResponse] = useState(null);

        const askQuestion = async () => {
          setResponse({response: "loading...", sources: []});
          try {
            const res = await axios.post(`${API_URL}/ask?query=${query}`, {});
            setResponse(res.data);
          } catch (err) {
            console.error(err);
            setResponse(null);
          }
        };

        return (
          <div>
            <h1>RAG GUI</h1>
            <div>
              <input
                type="text"
                value={query}
                onChange={e => setQuery(e.target.value)}
                onKeyDown={e => {
                  if (e.key === 'Enter') {
                    askQuestion();
                  }
                }}
              />
              <button onClick={askQuestion}>Ask</button>
            </div>
            {response && (
              <div>
                <h2>Response:</h2>
                <p className='response'>{response.response}</p>
                <hr/>
                <h2>Sources:</h2>
                <ul>
                  {response.sources.map((source, index) => (
                    <li key={index}>{source}</li>
                  ))}
                </ul>
                <hr/>
                <h2>Debug:</h2>
                <pre>{JSON.stringify(response, null, 2)}</pre>
              </div>
            )}
          </div>
        );
      }
      ReactDOM.render(<App />, document.getElementById('root'));
