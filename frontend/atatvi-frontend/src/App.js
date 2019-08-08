import React, {Component} from 'react';
import Graph from './components/graph.js';
import './App.css';

require('dotenv').config()


class App extends Component{

    render(){
        return (
            <div className="App">

                <div className="row">
                    <div class="column"><Graph party='GOP' color='red' /></div>
                    <div class="column"><Graph party='DEM' color='blue' /></div>
                </div>
            </div>
        );
    }

}

export default App;
