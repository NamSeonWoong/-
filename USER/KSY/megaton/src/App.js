import React from 'react';
import './App.css';
import { Route, Link } from 'react-router-dom'
import Home from "./pages/Home"
import About from "./pages/About"
import Search from "./pages/Search"
import { Button } from 'react-bootstrap'

function App() {
  return (
    <div>
      <div style= {{margin: "2% 2% 5% 2%", display: "flex", justifyContent: "flex-end"}}>
        <Link to="/">
          <Button>홈</Button>
        </Link>
      
        <Link to={"/about"}>
          <Button>소개</Button>
        </Link>
      </div>
    
      <Route path="/" component={Home} exact={true}/>
      <Route path="/about" component={About} exact={true}/>
      <Route path="/search" component={Search} exact={true}/>



      <footer
        style={{
          backgroundColor: "#eceff1",
          color: "#757575",
          marginTop: "2%",
          paddingLeft: "10%",
          paddingRight: "10%",
          paddingTop: "2%",
          paddingBottom: "2%"
        }}
      >
        <hr style={{ marginBottom: "2%" }} />
        {/* <div
          container
          direction="row"
          justify="space-between"
          alignItems="center"
        > */}
          <div>
            copyright® Cat Ltd. All rights Reserved.
            <br />
            대표 : CAT
            <br />
            대표연락처 : vxda7@naver.com
            <br />
          </div>
          <div>
            {/* <img src={javalogo} alt="javalogo" style={{ height: "50px" }} />
            <img src={springlogo} alt="springlogo" style={{ height: "50px" }} />
            <img src={reactlogo} alt="reactlogo" style={{ height: "50px" }} />
            <img src={dockerlogo} alt="dockerlogo" style={{ height: "50px" }} /> */}
          </div>
        {/* </div> */}
      </footer>
    </div>
  );
}

export default App;

