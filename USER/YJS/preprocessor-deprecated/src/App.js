import React from 'react';
// import logo from './logo.svg';
import {Container, Row, Col} from 'react-bootstrap'
import './App.css';
import Navs from './Navs.js'

function App() {
  const style = {
   height : '2000px' 
  }
  return ( 
    <div className="App">
      <Navs/>
      <Container fluid>
        <Row className="justify-content-center">
          <Col xs={6}>
            <h1 className="text-center">
              Preprocessor V ALPHA
            </h1>
          </Col>
        </Row>
        <Row>
          <div style={style}>
          </div>
        </Row>
      </Container>
    </div>
  );
}

export default App;
