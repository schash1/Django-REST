import React from 'react'


const TODOItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.date_created}
            </td>
            <td>
                {todo.date_update}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.on_off}
            </td>
            <td>
                <button onClick={()=>deleteTODO(item.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const TODOList = ({todos, deleteTODO}) => {
    return (
        <table>
            <th>
               Project
            </th>
            <th>
                Text
            </th>
            <th>
                Date created
            </th>
            <th>
                Date update
            </th>
            <th>
                User
            </th>
            <th>
                On Off
            <th></th>
            {todos.map((todo) => <TODOItem todo={todo} deleteTODO={deleteTODO} />)}
        </table>
        <Link to='/todos/create'>Create</Link>
    )
}

export default TODOList