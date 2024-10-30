import React from 'react'; 
import MyNavbar from './navbar.jsx'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'; 
import { Button } from 'react-bootstrap';  

function App() { 
  return (
    <div className="mainPage">
      <MyNavbar />  
      <div className="card">
        <h1>Reid's Book Market</h1>
        <p>Management App For Reid's Books</p>
        <img className="image img-fluid" src="/book.png" alt="Crypto" />
        <Button className="custom-button mb-2">
          Shop Now
        </Button>
      </div>
    </div>
  );
}

export default App;