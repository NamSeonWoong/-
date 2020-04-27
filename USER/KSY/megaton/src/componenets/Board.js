import React from 'react'
import {Table} from 'react-bootstrap'


const Board = ({realdata}) => {
    return (
        <>
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
                    
                        {realdata.map(data => (
                            <tr>
                                <td className="text-center">{data.category}</td>
                                <td><a href={data.url}>{data.title}</a></td>    
                                <td className="text-center">{data.user}</td>
                                <td className="text-center">{data.date}</td>
                            </tr>
                        ))}
                    
                </tbody>
            </Table>
        </>
    )
}

export default Board