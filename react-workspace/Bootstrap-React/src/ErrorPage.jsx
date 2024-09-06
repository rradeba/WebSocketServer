import React from 'react';
import { Link } from 'react-router-dom';  // if using React Router for navigation
import './ErrorPage.css';  // Optional: for custom styling

const ErrorPage = () => {
    return (
        <div className="error-container">
            <h1>Oops!</h1>
            <p>Something went wrong or this page doesn't exist.</p>
            <Link to="/">Go back to Home</Link>
        </div>
    );
};

export default ErrorPage;