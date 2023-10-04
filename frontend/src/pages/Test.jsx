import React, { useState, useEffect } from "react";

export default function Test() {
  const [text, setText] = useState('')
  //send a GET request to backend server
  useEffect(() => {
    fetch("http://127.0.0.1:5000/test")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setText(data)
      })
      .catch((err) => {
        console.log(err.message);
      });
  }, []);

  return (
  <div className="">
    <h1>{text}</h1>
  </div>
  );
}
