import React from 'react';
import './App.css';
import { Route, Link } from 'react-router-dom'
import Home from "./pages/Home"
import About from "./pages/About"
import { Button } from 'react-bootstrap'

function App() {
  return (
    <div>
      <div style= {{marginBottom: "20%"}}>
        <Link to="/">
          <Button>홈</Button>
        </Link>
      
        <Link to="/about">
          <Button>소개</Button>
        </Link>
      </div>
    
      <Route path="/" component={Home} exact={true}/>
      <Route path="/about" component={About} exact={true}/>
    </div>
  );
}

export default App;

