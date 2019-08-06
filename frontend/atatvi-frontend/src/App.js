import React, {Component} from 'react';
import Graph from './components/graph.js';
// import './App.css';


class App extends Component{

  constructor(props){
    super(props)
    this.state = {
      data: [],
      color: "#ccccff"
    }
  }

  

  render(){
    return (
     <div className="App">
        <Graph data={this.data} color={this.color}/>
     </div>
   );
  }
}

export default App;
