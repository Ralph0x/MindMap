import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
  const linkStyle = {
    margin: '0 10px',
    textDecoration: 'none',
    color: 'blue',
  };

  const activeStyle = {
    fontWeight: 'bold',
    color: 'darkred',
  };

  return (
    <header>
      <nav aria-label="Main navigation">
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          <li style={{ display: 'inline-block' }}>
            <NavLink 
              to="/" 
              exact 
              style={linkStyle} 
              activeStyle={activeStyle}>
              Home
            </NavLink>
          </li>
          <li style={{ display: 'inline-block' }}>
            <NavLink 
              to="/about" 
              style={linkStyle} 
              activeStyle={activeStyle}>
              About
            </NavLink>
          </li>
          <li style={{ display: 'inline-block' }}>
            <NavLink 
              to="/features" 
              style={linkStyle} 
              activeStyle={activeStyle}>
              Features
            </NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;