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
    const [nextdata, setNextdata] = React.useState([]); // 미리 다음페이지 로딩
    const [data, setData] = React.useState("");
    const [inputdata, setInputdata] = React.useState("")
    const [page, setPage] = React.useState(1)
    const [loading, setLoading] = React.useState(false)
    const handleChange = (e) => {
        setInputdata(e.target.value)
    }
    const inputstyle = {
        justifyContent: "center",
        width: "80%"
    }
    const Search = () => {
        setLoading(true)
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
        // 다음페이지 미리 로딩
        axios.get(`http://i02c102.p.ssafy.io:5000/search/${inputdata}/${page + 1}`)
        .then(
            (res)=>{
                setPage(page + 1)
                console.log(res.data)
                setNextdata(res.data)
                setLoading(false)
            }
        ).catch(
            (e)=>{console.log(e)}
        )
    }
    const handleKeyPress = (e) => {
        if (e.key === "Enter"){
            Search()
        }
    }

    const Morepage = () => {
        setLoading(true)
        setRealdata(realdata.concat(nextdata))
        setNextdata([])
        axios.get(`http://i02c102.p.ssafy.io:5000/search/${inputdata}/${page + 1}`)
            .then((res)=>{
                console.log(res.data)
                setNextdata(res.data)
                setPage(page + 1)
                setLoading(false)
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
                            <Board realdata={realdata}/>
                            {/* {LoadingButton()} */}
                            {loading ? (
                                <Button disabled>로딩중...</Button>
                            ):(
                                <Button onClick={Morepage}>더보기</Button>
                            )}
                            
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