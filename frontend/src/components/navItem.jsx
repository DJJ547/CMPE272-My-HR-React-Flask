import { NavLink } from "react-router-dom";

export default function NavItem({ content, href }) {

  return (
    <li className="">
      <NavLink
        className=""
        to={href}
      >
        <h1 className="" >
          {content}
        </h1>
      </NavLink>
    </li>
  );
}