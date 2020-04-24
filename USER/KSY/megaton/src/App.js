import React from 'react';
import './App.css';
import { Route, Link } from 'react-router-dom'
import Home from "./pages/Home"
import About from "./pages/About"
import Search from "./pages/Search"
import { Button } from 'react-bootstrap'

function App() {
  return (
    <div style={{}}>
      <body style={{minHeihgt: "100%", margin: "0 0 -200px 0"}}>
        <div style= {{margin: "2% 2% 5% 2%", display: "flex", justifyContent: "flex-end"}}>
          <Link to="/">
            <Button variant="outline-primary">홈</Button>
          </Link>
        
          <Link to={"/about"}>
            <Button variant="outline-primary">소개</Button>
          </Link>
        </div>
        <Route path="/" component={Home} exact={true}/>
        <Route path="/about" component={About} exact={true}/>
        <Route path="/search" component={Search} exact={true}/>
      </body>
      {/* <footer
        style={{
          position: "absolute",
          bottom: "0",
          width: "100%",
          height: "200px",
          backgroundColor: "#eceff1",
          color: "#757575",
          paddingLeft: "10%",
          paddingRight: "10%",
          paddingTop: "2%",
          paddingBottom: "2%"
        }}
      >
        <hr style={{ marginBottom: "2%" }} />
          <div>
            copyright® Cat Ltd. All rights Reserved.
            <br />
            대표 : CAT
            <br />
            대표연락처 : vxda7@naver.com
            <br />
          </div>
      </footer> */}
    </div>
  );
}

export default App;