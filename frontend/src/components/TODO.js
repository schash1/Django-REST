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
        </tr>
    )
}

const TODOList = ({todos}) => {
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
            </th>
            {todos.map((todo) => <TODOItem todo={todo} />)}
        </table>
    )
}

export default TODOList