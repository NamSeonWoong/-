import React from 'react';
import {InputGroup, Button, FormControl, Container, Row} from 'react-bootstrap';
import catswim from "../images/catswim2.png"
import Board from "../componenets/Board"
import axios from 'axios';

// function simulateNetworkRequest() {
//     return new Promise((resolve) => setTimeout(resolve, 2000));
//   }
  
// function LoadingButton() {
//     const [isLoading, setLoading] = React.useState(false);

//     React.useEffect(() => {
//         if (isLoading) {
//         simulateNetworkRequest().then(() => {
//             setLoading(false);
//         });
//         }
//     }, [isLoading]);

//     const handleClick = () => setLoading(true);

//     return (
//         <Button
//         variant="primary"
//         disabled={isLoading}
//         onClick={!isLoading ? handleClick : null}
//         >
//         {isLoading ? 'Loading…' : 'Click to load'}
//         </Button>
//     );
// }


const Home = ({history}) => {
    const [realdata, setRealdata] = React.useState([]);
    const [data, setData] = React.useState("");
    const [inputdata, setInputdata] = React.useState("")
    let page = 1;
    const handleChange = (e) => {
        setInputdata(e.target.value)
    }
    const inputstyle = {
        justifyContent: "center",
        width: "80%"
    }
    const Search = () => {
        setData(inputdata);
        // setInputdata("");
        axios.get(`http://i02c102.p.ssafy.io:5000/search/${inputdata}/${page}`)
        .then(
            (res)=>{
                console.log(res.data)
                setRealdata(res.data)
            }
        ).catch((e)=>{
            console.log(e)
        })
    }
    const handleKeyPress = (e) => {
        if (e.key === "Enter"){
            Search()
        }
    }

    const Morepage = () => {
        axios.get(`http://i02c102.p.ssafy.io:5000/search/${inputdata}/${page + 1}`)
            .then((res)=>{
                console.log(res.data)
                setRealdata(realdata.concat(res.data))
                page += 1;
            })
            .catch((e)=>{
                console.log(e)
            })
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
                <Row className="justify-content-center">
                    {data ? (
                        <>
                            <Board data={data} setData={setData} realdata={realdata}/>
                            {/* {LoadingButton()} */}
                            <Button onClick={Morepage}>더보기</Button>
                        </>
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