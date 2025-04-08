import React, { useState, useRef, useEffect } from 'react';

const API_KEY = 'sk-42715b03250c4ddebfe62c263f8e97b9';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const chatEndRef = useRef(null);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    try {
      const res = await fetch('https://api.deepseek.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'deepseek-chat',
          messages: [
            {
              role: 'user',
              content: input,
            },
          ],
        }),
      });

      const data = await res.json();

      if (res.ok && data.choices && data.choices.length > 0) {
        const aiMessage = {
          sender: 'ai',
          text: data.choices[0].message.content.trim(),
        };
        setMessages((prev) => [...prev, aiMessage]);
      } else {
        setMessages((prev) => [
          ...prev,
          { sender: 'ai', text: 'No response from AI.' },
        ]);
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'ai', text: 'Error contacting AI.' },
      ]);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') sendMessage();
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div style={styles.container}>
      <div style={styles.chatContainer}>
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              ...styles.message,
              alignSelf: msg.sender === 'user' ? 'flex-end' : 'flex-start',
              backgroundColor: msg.sender === 'user' ? '#4f46e5' : '#e5e7eb',
              color: msg.sender === 'user' ? '#fff' : '#111827',
            }}
          >
            {msg.text}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      <div style={styles.inputBar}>
        <input
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          style={styles.input}
        />
        <button onClick={sendMessage} style={styles.sendButton}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: '100vh',
    display: 'flex',
    flexDirection: 'column',
    backgroundColor: '#1f2937',
    fontFamily: 'system-ui, sans-serif',
  },
  chatContainer: {
    flex: 1,
    padding: '1rem',
    display: 'flex',
    flexDirection: 'column',
    overflowY: 'auto',
  },
  message: {
    maxWidth: '75%',
    padding: '0.75rem 1rem',
    marginBottom: '0.5rem',
    borderRadius: '18px',
    fontSize: '1rem',
    lineHeight: '1.4',
  },
  inputBar: {
    display: 'flex',
    padding: '1rem',
    borderTop: '1px solid #374151',
    backgroundColor: '#111827',
  },
  input: {
    flex: 1,
    padding: '0.75rem 1rem',
    fontSize: '1rem',
    borderRadius: '12px',
    border: 'none',
    outline: 'none',
    marginRight: '0.75rem',
  },
  sendButton: {
    padding: '0.75rem 1.5rem',
    fontSize: '1rem',
    backgroundColor: '#4f46e5',
    color: '#fff',
    border: 'none',
    borderRadius: '12px',
    cursor: 'pointer',
  },
};

export default App;
