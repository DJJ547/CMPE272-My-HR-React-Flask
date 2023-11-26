import React, { useState } from "react";

export default function MessageBox({ User, messages }) {
  return (
    <div className="flex justify-start">
      <div className="mb-4">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" className="rounded-full h-16 w-16 inline-block p-2" />
      </div>
      <div className="mb-4 w-40">
        <div className="font-semibold text-left p-1">{User}</div>
        <div className="text-sm text-gray-600 shadow p-2 round">{messages}</div>
      </div>
    </div>
  );
}
