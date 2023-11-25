import React, { useEffect, useState } from "react";

export default function Pay() {

    const [text, setText] = useState([])

    useEffect(() => {
        fetch("http://127.0.0.1:5000/pay")
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
            setText(data)
        })
        .catch((error) => {
            console.error(error);
        });
    }, []);

    return (
        <div className="">
            {text.map((data) => (
                <div>
                    Salary:  {data}
                </div>
            )
            )}
        </div>
    ); 
}