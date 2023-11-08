import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import MessageBox from "../components/Message/MessageBox";
import MessageBox_me from "../components/Message/MessageBox_me";

export default function Message() {
  const socket = io("http://localhost:5000");
  const [otherUser, setotherUser] = useState("Other user");
  const me = "Me";

  const [components, setComponents] = useState([]);
  const handleSend = (e) => {
    e.preventDefault();
    const newComponent = React.createElement(MessageBox_me, {
      User: me,
      messages: e.target[0].value,
    });
    setComponents([...components, newComponent]);
    e.target[0].value = "";
  };
  return (
    <div className="p-12">
      <div className="flex flex-col h-full bg-white rounded-md shadow-md w-[60%] mx-auto">
        <div className="p-4 bg-indigo-500 text-white font-semibold rounded-t-md">
          Chatting with {otherUser}
        </div>
        <div className="flex-grow overflow-auto p-6" id="message_Box">
          {/* Messages go here */}
          <MessageBox User={otherUser} messages="Hello" />
          <MessageBox_me
            User={me}
            messages="Hi i like your t shirt, so i bought one too"
          />
          {components.map((Component, index) => (
            <div key={10}>{Component}</div>
          ))}
          {/* More messages... */}
        </div>

        <div className="p-4 border-t border-gray-200">
          <form className="flex" onSubmit={handleSend}>
            <input
              className="flex-grow rounded-l-md border-gray-300 border p-2 outline-none"
              placeholder="Type a message"
            />
            <button className="bg-indigo-500 text-white rounded-r-md px-4">
              Send
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
