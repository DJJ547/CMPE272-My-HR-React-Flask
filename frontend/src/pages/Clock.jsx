import React, { useEffect, useState } from "react";
import { Number } from "../components/clock/Number";
import { Word } from "../components/clock/Word";

const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];

export default function Clock(h24 = true) {
  const months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const [month, setMonth] = useState(0);
  const [date, setDate] = useState(0);
  const [year, setYear] = useState(0);
  const [hour, setHour] = useState(0);
  const [minute, setMinute] = useState(0);
  const [second, setSecond] = useState(0);
  const [day, setDay] = useState(0);
  const [pm, setPm] = useState(false);
  const [output, setOutput] = useState("");

  function handlePunch(punchType) {
    console.log(punchType)
    // fetch("http://127.0.0.1:5000/test")
    //   .then((response) => response.json())
    //   .then((data) => {
    //     console.log(data);
    //     setOutput(data);
    //   })
    //   .catch((error) => console.error(error));
    const time = new Date();
    const currentTime = time.getTime();
    console.log(currentTime)

    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        type: punchType,
        time: currentTime,
      }),
    };
    fetch("http://127.0.0.1:5000/clock", options)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setOutput(data.message);
      })
      .catch((error) => console.error(error));
  }

  useEffect(() => {
    const update = () => {
      const datetime = new Date();
      let hour = datetime.getHours();
      if (!h24) {
        hour = hour % 12 || 12;
      }
      setMonth(datetime.getMonth());
      setDate(datetime.getDate());
      setYear(datetime.getFullYear());
      setHour(hour);
      setMinute(datetime.getMinutes());
      setSecond(datetime.getSeconds());
      setDay(datetime.getDay());
      setPm(datetime.getHours() >= 12);
    };

    update();

    const interval = setInterval(() => {
      update();
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <div className="m-[10px] rounded-[10px] bg-[#0d1621] flex flex-col items-center overflow-hidden pl-[20px] pr-[20px] py-[20px]">
        <div className="space-x-3 text-[3rem]">
          <Word value={months[month - 1]} />
          <Number value={date} />
          <Word value={","} />
          <Number value={year} />
        </div>
        <div className="text-[2rem] flex flex-row items-center justify-center gap-[33px] px-[10px] py-[0] pt-[10px]">
          {days.map((value, index) => (
            <Word key={value} value={value} hidden={index != day} />
          ))}
        </div>
        <div className="flex flex-row gap-[10px]">
          <div className="flex-[1] text-[5rem] m-0 p-0 top-[0]">
            <Number value={hour} />
            <Word value={":"} />
            <Number value={minute} />
            <Word value={":"} />
            <Number value={second} />
          </div>
          <div className="self-end text-[2.5rem] flex gap-[10px] mb-[25px]">
            <Word value={"AM"} hidden={pm} />
            <Word value={"PM"} hidden={!pm} />
          </div>
        </div>
      </div>
      <div className="flex justify-center space-x-10 text-white font-bold m-10">
        <button
          onClick={() => handlePunch("start_shift")}
          className="rounded-[10px] bg-[#0d1621] p-5"
        >
          Start Shift
        </button>
        <button
          onClick={() => handlePunch("start_lunch")}
          className="rounded-[10px] bg-[#0d1621] p-5"
        >
          Start Lunch
        </button>
        <button
          onClick={() => handlePunch("end_lunch")}
          className="rounded-[10px] bg-[#0d1621] p-5"
        >
          End Lunch
        </button>
        <button
          onClick={() => handlePunch("end_shift")}
          className="rounded-[10px] bg-[#0d1621] p-5"
        >
          End Shift
        </button>
      </div>
      <div className="flex w-full h-100 overflow-y-scroll bg-gray-200">
        <h1>{output}</h1>
      </div>
    </div>
  );
}
