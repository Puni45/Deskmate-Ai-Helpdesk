import { useState } from "react";
import axios from "axios";

function App() {

  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {

    if (!message.trim()) return;

    const userMessage = {
      sender: "You",
      text: message
    };

    setChat((prev) => [...prev, userMessage]);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          user: "puneeth",
          message: message
        }
      );

      const botMessage = {
        sender: "DeskMate",
        text: response.data.response
      };

      setChat((prev) => [...prev, botMessage]);

    } catch (error) {

      const errorMessage = {
        sender: "DeskMate",
        text: "Error connecting to backend."
      };

      setChat((prev) => [...prev, errorMessage]);
    }

    setMessage("");
  };

  return (

    <div
      style={{
        maxWidth: "800px",
        margin: "40px auto",
        fontFamily: "Arial"
      }}
    >

      <h1>DeskMate AI Helpdesk</h1>

      <div
        style={{
          border: "1px solid gray",
          borderRadius: "10px",
          padding: "20px",
          minHeight: "400px",
          marginBottom: "20px",
          overflowY: "auto"
        }}
      >

        {chat.map((msg, index) => (

          <div
            key={index}
            style={{
              marginBottom: "15px"
            }}
          >

            <strong>{msg.sender}:</strong>

            <div>{msg.text}</div>

          </div>
        ))}

      </div>

      <div
        style={{
          display: "flex",
          gap: "10px"
        }}
      >

        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask DeskMate..."
          style={{
            flex: 1,
            padding: "12px",
            fontSize: "16px"
          }}
        />

        <button
          onClick={sendMessage}
          style={{
            padding: "12px 20px",
            fontSize: "16px",
            cursor: "pointer"
          }}
        >
          Send
        </button>

      </div>

    </div>
  );
}

export default App;