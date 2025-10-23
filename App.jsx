import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post("http://localhost:8000/upload/", formData);
  };

  const handleAsk = async () => {
    const res = await axios.post("http://localhost:8000/ask/", { question });
    setAnswer(res.data.answer);
  };

  return (
    <div className="p-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload PDF</button>
      <input value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask a question..." />
      <button onClick={handleAsk}>Ask</button>
      <p><strong>Answer:</strong> {answer}</p>
    </div>
  );
}

export default App;
