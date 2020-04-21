import React from 'react';
import {InputGroup, Button, FormControl} from 'react-bootstrap'

const Home = () => {
    const inputstyle = {
        justifyContent: "center",
        width: "80%"
    }
    return (
        <div>
            <InputGroup className="mb-3" style={inputstyle}>
                <FormControl
                aria-describedby="basic-addon2"
                />
                <InputGroup.Append>
                <Button variant="outline-secondary">Button</Button>
                </InputGroup.Append>
            </InputGroup>
        </div>
    )
}

export default Home;