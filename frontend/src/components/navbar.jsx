import React, { useState }from "react";

import NavItem from "./navItem";

export default function NavBar() {

  return (
    <nav className="flex">
      <ul className="flex w-auto space-x-8">
        <h1 className="">My Alpha</h1>
        <NavItem content="about" href="/about" />
        <a href="/signin">Sign In</a>
      </ul>
    </nav>
  );
}
