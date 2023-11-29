import dayjs from "dayjs";
import React, { useState } from "react";
import { generateDate, months } from "../static/schedule/calendar";
import cn from "../static/schedule/cn";
import { GrFormNext, GrFormPrevious } from "react-icons/gr";

const schedule = [
  {
    shift_start: "2023-11-13T17:00:00",
    lunch_Start: "2023-11-13T21:00:00",
    lunch_end: "2023-11-13T21:30:00",
    shift_end: "2023-11-13T23:00:00",
  },
  {
    shift_start: "2023-11-15T17:00:00",
    lunch_Start: "2023-11-15T21:00:00",
    lunch_end: "2023-11-15T21:30:00",
    shift_end: "2023-11-15T23:00:00",
  },
  {
    shift_start: "2023-11-18T05:30:00",
    lunch_Start: "2023-11-18T09:30:00",
    lunch_end: "2023-11-18T10:30:00",
    shift_end: "2023-11-18T14:30:00",
  },
  {
    shift_start: "2023-11-19T06:30:00",
    lunch_Start: "2023-11-19T10:30:00",
    lunch_end: "2023-11-19T11:30:00",
    shift_end: "2023-11-19T15:30:00",
  },
];

export default function Scheduling() {
  const days = ["S", "M", "T", "W", "T", "F", "S"];
  const currentDate = dayjs();
  const [today, setToday] = useState(currentDate);
  const [selectDate, setSelectDate] = useState(currentDate);
  const [schedules, setSchedules] = useState(schedule);
  return (
    <div className="flex gap-10 sm:divide-x justify-center mx-auto h-screen items-center sm:flex-row flex-col p-10">
      <div className="w-full h-full">
        <div className="flex justify-between items-center">
          <h1 className="select-none font-semibold">
            {months[today.month()]}, {today.year()}
          </h1>
          <div className="flex items-center ">
            <GrFormPrevious
              className="w-5 h-5 cursor-pointer hover:scale-105 transition-all"
              onClick={() => {
                setToday(today.month(today.month() - 1));
              }}
            />
            <h1
              className=" cursor-pointer hover:scale-105 transition-all"
              onClick={() => {
                setToday(currentDate);
              }}
            >
              Today
            </h1>
            <GrFormNext
              className="w-5 h-5 cursor-pointer hover:scale-105 transition-all"
              onClick={() => {
                setToday(today.month(today.month() + 1));
              }}
            />
          </div>
        </div>
        <div className="grid grid-cols-7">
          {days.map((day, index) => {
            return (
              <h1
                key={index}
                className="text-sm text-center h-14 w-14 grid place-content-center text-black font-bold select-none"
              >
                {day}
              </h1>
            );
          })}
        </div>

        <div className=" grid grid-cols-7">
          {generateDate(today.month(), today.year()).map(
            ({ date, currentMonth, today }, index) => {
              return (
                <div
                  key={index}
                  className={cn(currentMonth ? "" : "text-gray-400", today ? "bg-gray-500 text-white" : "", "transition ease-in-out delay-50 hover:bg-gray-500 hover:text-white cursor-pointer file:p-1 text-center h-32 grid place-content-start text-sm border-solid border-2 border-gray-400")}
                >
                  <h1
                    className={cn(
                      
                      selectDate.toDate().toDateString() ===
                        date.toDate().toDateString()
                        ? "bg-black text-white"
                        : "",
                      "h-10 w-10 rounded-full grid place-content-center transition-all select-none"
                    )}
                    onClick={() => {
                      setSelectDate(date);
                    }}
                  >
                    {date.date()}
                  </h1>
                </div>
              );
            }
          )}
        </div>
      </div>
      {/* <div className="h-96 w-96 sm:px-5">
				<h1 className=" font-semibold">
					Schedule for {selectDate.toDate().toDateString()}
				</h1>
				<p className="text-gray-400">No meetings for today.</p>
			</div> */}
    </div>
  );
}
