import React from 'react'; 
import { Button } from 'react-bootstrap'; 
import './App.css';


const StartShopping = () => {
    return(
        <div className = "main">
            <div className = "card">
                <h1>Crypto Market</h1>
                <p>Find new crypto coins in our directory.</p>
                <img className ="image " src="crypto.jpg" alt="" />
                <Button className = "custom-button" variant="primary">
                    Shop Now
                </Button>
            </div>
        </div>
    )
};

export default StartShopping; 
