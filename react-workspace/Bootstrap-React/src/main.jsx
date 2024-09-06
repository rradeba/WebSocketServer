import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './HomePage';  // Import your home page or other components
import ErrorPage from './ErrorPage';  // Import your error page

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route component={ErrorPage} /> 
      </Switch>
    </Router>
  );
};

export default App;