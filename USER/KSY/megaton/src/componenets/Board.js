import React from 'react'
import {Table} from 'react-bootstrap'

const Board = ({data, setData}) => {
    const axiosdata = [
        {
            "articleid": "휴대폰 판매/매입",
            "title": "갤럭시 s10e 팝니다.",
            "user": "바삭한피자",
            "date": "2020.04.23",
            "url": "https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc"
        },
        {
            "articleid": "휴대폰 판매/매입",
            "title": "갤럭시 s10e 팝니다.",
            "user": "바삭한피자",
            "date": "2020.04.23",
            "url": "https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc"
        },
        {
            "articleid": "휴대폰 판매/매입",
            "title": "갤럭시 s10e 팝니다.",
            "user": "바삭한피자",
            "date": "2020.04.23",
            "url": "https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc"
        },
    ]
    return (
        <Table responsive>
            <thead>
            <tr>
                <th className="text-center">카테고리</th>
                <th className="text-center">제목</th>
                <th className="text-center">작성자</th>
                <th className="text-center">작성일</th>
            </tr>
            </thead>
            <tbody>
                {axiosdata.map(data => (
                    <tr>
                        <td className="text-center">{data.articleid}</td>
                        <td><a href={data.url}>{data.title}</a></td>    
                        <td className="text-center">{data.user}</td>
                        <td className="text-center">{data.date}</td>
                    </tr>
                ))}
                
            </tbody>
        </Table>
    )
}

export default Board