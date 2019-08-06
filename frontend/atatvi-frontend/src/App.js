import React, {Component} from 'react';
import Graph from './components/graph.js';
import axios from 'axios';

require('dotenv').config()

class App extends Component{
  
  constructor(props){
    console.log('in constructor')
    super(props)
    this.state = {
      dataDem: [],
      dataRep: [],
      color: "#ccccff"
    }
  }

  setData(apiData){
    console.log('IN SET DATA')
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
      console.log("REP DATA 🦅🦅🦏🦏🦏🦏🇺🇸🇺🇸🇺🇸🇺🇸**********************************************************************************", this.dataRep)
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
      console.log("REP DATA 🦅🦅🐐🐐🐐🐐🇺🇸🇺🇸🇺🇸🇺🇸**********************************************************************************",this.dataDem)
    }  
    }
   }
 
  getData(){
    let self = this
    //TODO: refactor to env
    const url = 'http://localhost:5000'
    //'https://atatvi.onrender.com'
    //const axios = require('axios')
    
    axios.get(url+'/api/v1/tweets')
      .then(function (response){
        console.log('in getData above setData'+ response)
       self.setData(response)
       console.log('under set data in get data'+response)
      })
      .catch(function(error){
        console.log(error)
      })
      .finally(function(){
        //TODO: DO we need a finally? 
      })
  }

  setColor(){

  }


  render(){
    this.getData()
    return (
     <div className="App">
        <Graph data={this.state.dataDem} color={this.state.color}/>
        
        <Graph data={this.state.dataRep} color={this.state.color}/>
        
     </div>
   );
  }
}

export default App;
