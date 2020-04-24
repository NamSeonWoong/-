import React, {Component} from 'react';
import { Navbar, Nav, NavDropdown, Form,FormControl, Button } from 'react-bootstrap'
import CSVReader from 'react-csv-reader'
import {CSVLink} from "react-csv"
import './Navs.css';

class Navs extends Component {
    
papaparseOptions = {
    header: true,
    // transformHeader: header=> {
        
    // }
}
state = {
        data: [],
        headers: [
            {label: "TITLE", key:'title'},
            {label: "CONTENT", key:'content'},
            {label: "COMMERCIAL", key:'commercial'},
        ]
    }
    handleFile= (csvdata, fileInfo) => {
        csvdata[0].push('COMMERCIAL')
        csvdata.map((arr,idx)=>{
            if (idx > 0) 
                arr.push('1')
        })
        this.setState({
            data: csvdata,            
        })
        console.log(this.state.data)
    }
    render() {
        return (
            <Navbar bg="light" expand="lg">
                <Navbar.Brand href="#home">Preprocessor V ALPHA</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse  id="basic-navbar-nav">           
                    <Nav className="mx-auto justify-content-between">     
                        <NavDropdown title="import csv" id="import-csv-dropdown">
                            <CSVReader 
                                onFileLoaded={this.handleFile}
                                parseOptions={this.papaparseOptions}
                                fileEncoding="UTF-8"
                            />
                        </NavDropdown>
                        <NavDropdown title="export csv" id="export-csv-dropdown">
                            <CSVLink 
                                data={this.state.data} 
                                headers={this.state.headers}
                                filename="textoutput.csv"
                            >
                                Download
                            </CSVLink>
                        </NavDropdown>
                        <NavDropdown title="check data" id="basic-nav-dropdown">
                            <Form inline>
                                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                                <Button variant="outline-success">Search</Button>
                            </Form>
                            <NavDropdown.Divider />
                            {this.state.data.map((arr, idx)=>{
                                return <NavDropdown.Item href="#">{arr[0]} {arr[1]}</NavDropdown.Item>
                            })}
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
}

export default Navs;