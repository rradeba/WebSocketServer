import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Container, Row, Col, Image} from 'react-bootstrap';
import './ErrorPage.css';  

const ErrorPage = () => {
    return (
        <div className="error-container Container"> 
            <img class = "img Row" src="\404.png" alt="404" />
            <div class = "row">
                <h1>404: Page Not Found</h1>
                <p>Something went wrong or this page doesn't exist.</p>
                <Link to="/">Go back to Home</Link>
            </div> 
        </div>
    );
};

export default ErrorPage;