import React from 'react'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import './navbar.css'; 
import { Navbar, Nav, Container } from 'react-bootstrap';

function MyNavbar() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Container>
        <Navbar.Brand href="/">MyWebsite</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/about">Customers</Nav.Link>
            <Nav.Link href="/services">Products</Nav.Link>
            <Nav.Link href="/contact">Contact</Nav.Link> 
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default MyNavbar;