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

  setData(apiData){

    if (apiData.party === "GOP"){
      this.setState(
        this.dataRep = [
        { x: 1, y: apiData.tone_anger},
        { x: 2, y: apiData.tone_fear},
        { x: 3, y: apiData.tone_joy},
        { x: 4, y: apiData.tone_sadness},
        { x: 5, y: apiData.tone_analytic}, 
        { x: 6, y: apiData.tone_confident}, 
        { x: 7, y: apiData.tone_tentative}
      ])
    if (apiData.party === "DEM"){
      this.setState(
        this.dataDem = [
        { x: 1, y: apiData.tone_anger},
        { x: 2, y: apiData.tone_fear},
        { x: 3, y: apiData.tone_joy},
        { x: 4, y: apiData.tone_sadness},
        { x: 5, y: apiData.tone_analytic}, 
        { x: 6, y: apiData.tone_confident}, 
        { x: 7, y: apiData.tone_tentative}
        ]
      )
    }  
    }
   }
 
  getData(){
    const url = 'BACKEND-URL'
    const axios = require('axios')

    axios.get(url+'/api/v1/tweets')
      .then(function (response){
       setData(response)
      })
      .catch(function(error){
        //TODO: Error handling
      })
      .finally(function(){
        //TODO: DO we need a finally? 
      })
  }

  setColor(){

  }

 

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
