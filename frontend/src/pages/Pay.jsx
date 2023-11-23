import React, { useEffect, useState } from "react";

export default function Pay() {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("http://127.0.0.1:5000/salary").then(
            res => res.json()
        ).then (
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

    return (
        <div>
            <h1>{data}</h1>
        </div>
    ); 
}