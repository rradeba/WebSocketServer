import React from 'react';
import { NavLink } from 'react-router-dom';
import { Button, Container, Row, Col, Image } from 'react-bootstrap';
import './ErrorPage.css';  

const ErrorPage = () => {
    return (
        <Container className="error-container">
            <Row className="text-center">
                <Col>
                    <Image className="img-fluid" src="\404.png" alt="404" />
                </Col>
            </Row>
            <Row className="text-center">
                <Col>
                    <h1>404: Page Not Found</h1>
                    <p>Something went wrong or this page doesn't exist.</p>
                    <NavLink to="/" className="btn btn-primary">Go back to Home</NavLink>
                </Col>
            </Row>
        </Container>
    );
};

export default ErrorPage;

