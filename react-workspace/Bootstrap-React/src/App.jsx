import React from 'react'; 
import { Button } from 'react-bootstrap'; 
import './App.css';

const StartShopping = () => {
    return(
        <div className="main">
            <div className="card">
                <h1>Crypto Market</h1>
                <p>Find new crypto coins in our directory.</p>
                <img className="image" src="/crypto.jpg" alt="Crypto" />
                <Button className="custom-button mb-2">
                    Shop Now
                </Button>
            </div>
        </div>
    );
};

export default StartShopping;
