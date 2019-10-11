import React, {Component} from 'react';
import logo from '../logo.svg';
import 'bootstrap/dist/css/bootstrap.css';
import './App.css'
import {Table} from 'reactstrap';

const InfoTable =
    <Table bordered striped condensed hover>
        <thead>
        <tr>
            <th>1</th>
            <th>2</th>
        </tr>
        </thead>
        <tbody>

        </tbody>
    </Table>;

class App extends Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                    <h1>Welcome to BTC-LTH-ARB-SYSTEM</h1>
                </header>
                <br/><br/>
                <div>{InfoTable}</div>
            </div>
        );
    }
}

export default App;
