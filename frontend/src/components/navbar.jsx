import React, { useState }from "react";

import NavItem from "./navItem";

export default function NavBar() {

  return (
    <nav className="flex">
      <ul className="flex w-auto space-x-8">
        <h1 className="">My Alpha</h1>
        <NavItem content="about" href="/about" />
        <NavItem content="Register" href="/register" />
        <NavItem content="Log In" href="/login" />
      </ul>
    </nav>
  );
}
