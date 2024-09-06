import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './HomePage';  // Import your home page or other components
import ErrorPage from './ErrorPage';  // Import your error page

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        {/* Add other routes here */}
        <Route path="*" element={<ErrorPage />} /> {/* This will catch all undefined routes */}
      </Routes>
    </Router>
  );
};

export default App;