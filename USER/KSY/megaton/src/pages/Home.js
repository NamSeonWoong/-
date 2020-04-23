import React from 'react';
import {InputGroup, Button, FormControl, Container, Row} from 'react-bootstrap';
import catswim from "../images/catswim2.png"
import Board from "../componenets/Board"
// import axios from 'axios';

const Home = ({history}) => {
    const [data, setData] = React.useState("");
    const [inputdata, setInputdata] = React.useState("")
    const handleChange = (e) => {
        setInputdata(e.target.value)
    }
    const inputstyle = {
        justifyContent: "center",
        width: "80%"
    }
    const Search = () => {
        setData(inputdata);
        setInputdata("");
        // history.push("/about");
    }
    const handleKeyPress = (e) => {
        if (e.key === "Enter"){
            Search()
        }
    }

    return (
        <div>
            <Container>
                <Row className="justify-content-center mb-5">
                    <a href="/">
                        <img src={catswim} alt="title"/>
                    </a>
                </Row>
                <Row className="justify-content-center">
                    <InputGroup className="mb-3" style={inputstyle}>
                        <FormControl
                        aria-describedby="basic-addon2"
                        onChange={handleChange}
                        onKeyPress={handleKeyPress}
                        value = {inputdata}
                        />
                        <InputGroup.Append>
                        <Button variant="outline-secondary" onClick={Search}>검색</Button>
                        </InputGroup.Append>
                    </InputGroup>
                </Row>
                <Row>
                    {data ? (
                        <Board data={data} setData={setData}/>
                    ) : (
                        <></>
                    )}
                </Row>
            </Container>
            <h1>{inputdata}</h1>
        </div>
    )
}

export default Home;