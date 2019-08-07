import React, {Component} from 'react';
import Graph from './components/graph.js';


require('dotenv').config()


class App extends Component{

    render(){
        return (
            <div className="App">
                <Graph party='GOP' color='red' />
                <Graph party='DEM' color='blue' />
            </div>
        );
    }
}

export default App;
