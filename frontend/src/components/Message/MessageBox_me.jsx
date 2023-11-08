import React, { useState } from "react";

export default function MessageBox({ User, messages }) {
  return (
    <div className="flex justify-end">
      <div className="mb-4 w-40">
        <div className="font-semibold text-right p-1">{User}</div>
        <div className="text-sm text-gray-600 shadow p-2 round">{messages}</div>
      </div>
    </div>
  );
}
