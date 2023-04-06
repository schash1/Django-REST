import React from 'react'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.link}
            </td>
            <td>
                {project.users}
            </td>
            <td>
                <button onClick={()=>deleteProject(item.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, deleteProject}) => {
    return (
        <table>
            <th>
               Project name
            </th>
            <th>
                Link
            </th>
            <th>
                User
            </th>
            <th></th>
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} />)}
        </table>
        <Link to='/projects/create'>Create</Link>
    )
}

export default ProjectList