import React from 'react';
import { createRoot } from 'react-dom/client';

import App from './App.jsx';  

console.log('Index.js is rendering');  

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Main />
  </React.StrictMode>
);
