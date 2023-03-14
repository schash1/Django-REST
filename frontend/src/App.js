import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        const users = [
            {
                'user_name': 'Ivanov2000',
                'first_name': 'Фёдор',
                'last_name': 'Иванов',
                'email': 'ivanov2000@mail.ru'
            },
            {
                'user_name': 'Sidorov2000',
                'first_name': 'Женя',
                'last_name': 'Сидоров',
                'email': 'sidorov2000@mail.ru'
            },
        ]
        this.setState(
            {
                'users': users
            }
        )
    }
    render () {
        return (
            <div>
                <UserList users={this.state.users} />
            </div>
        )
    }
}

export default App;
