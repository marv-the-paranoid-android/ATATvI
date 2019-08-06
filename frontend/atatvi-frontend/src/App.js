import React, {Component} from 'react';
import Graph from './components/graph.js';
import axios from "axios";
// import './App.css';


class App extends Component{

  constructor(props){
    super(props)
    this.state = {
      dataDem: [],
      dataRep: [],
      color: "#ccccff"
    }
  }
 
  getData(){
    const url = 'BACKEND-URL'
    
    

  }

  setColor(){

  }

  // setData(){

  //   if (apiData.party = "GOP"){
  //     setState(
  //       dataRep : [
  //       { x: 1, y: apiData.party["GOP"].anger},
  //       { x: 2, y: apiData.party["GOP"].fear},
  //       { x: 3, y: apiData.party["GOP"].joy},
  //       { x: 4, y: apiData.party["GOP"].sadness},
  //       { x: 5, y: apiData.party["GOP"].analytic}, 
  //       { x: 6, y: apiData.party["GOP"].confident}, 
  //       { x: 7, y: apiData.party["GOP"].tentative}
  //     ])
  //   if (apiData.party = "DEM"){
  //     this.setState(
  //       dataDem : [
  //       { x: 1, y: .4},
  //       { x: 2, y: .9},
  //       { x: 3, y: .2},
  //       { x: 4, y: .6},
  //       { x: 5, y: .1}, 
  //       { x: 6, y: .8}, 
  //       { x: 7, y: .1}
  //       ]
  //     )
  //   }  
  //   }

  

  // }

  render(){
    return (
     <div className="App">
        <Graph data={this.state.dataDem} color={this.state.color}/>
        <Graph data={this.state.dataRep} color={this.state.color}/>
     </div>
   );
  }
}

export default App;
