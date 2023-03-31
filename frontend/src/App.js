import React from 'react';
import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route, Link, Routes, Redirect} from 'react-router-dom'
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TODOList from './components/TODO.js'
import axios from 'axios'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie';


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'TODOs': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }

    load_data() {
        axios.get('http://127.0.0.1:8000/api/users/')
        .then(response => {
            this.setState({authors: response.data})
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/')
        .then(response => {
            this.setState({authors: response.data})
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/TODOs/')
        .then(response => {
            this.setState({authors: response.data})
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    render () {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/users'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todos'>TODOs</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> :
<Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path='/users' component={() => <UserList items={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
                        <Route exact path='/todos' component={() => <TODOList items={this.state.TODOs} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route component={<NotFound404/>} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
