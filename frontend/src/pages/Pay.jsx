import React, { useEffect, useState } from "react";
import { Card, Typography } from "@material-tailwind/react";

const TABLE_HEAD = ["Past Salaries"]

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
        /* <div className="">
            {text.map((data) => (
                <div>
                    Salary:  {data}
                </div>
            )
            )}
        </div> */
        <Card className="h-full w-full overflow-scroll">
            <table className="w-full min-w-max table-auto text-left">
                <thead>
                    <tr>
                        {TABLE_HEAD.map((head) => (
                        <th key={head} className="border-b border-blue-gray-100 bg-blue-gray-50 p-4">
                            <Typography
                            variant="small"
                            color="blue-gray"
                            className="font-normal leading-none opacity-70"
                            >
                            {head}
                            </Typography>
                        </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {text.map((data) => (
                        <tr key={data} className="even:bg-blue-gray-50/50">
                            <td className="p-4">
                                <Typography variant="small" color="blue-gray" className="font-normal">
                                ${data}
                                </Typography>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </Card>
    ); 
}