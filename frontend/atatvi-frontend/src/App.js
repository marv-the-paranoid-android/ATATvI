import React, {Component} from 'react';
import Graph from './components/graph.js';
import axios from 'axios';

require('dotenv').config()

class App extends Component{
  
  constructor(props){
    console.log('in constructor')
    super(props)
    this.state = {
      dataDem: [
      { x: 1, y: 0},
      { x: 2, y: 0},
      { x: 3, y: 0},
      { x: 4, y: 0},
      { x: 5, y: 0}, 
      { x: 6, y: 0}, 
      { x: 7, y: 0},
    ],
      dataRep: [ 
      { x: 1, y: 0},
      { x: 2, y: 0},
      { x: 3, y: 0},
      { x: 4, y: 0},
      { x: 5, y: 0}, 
      { x: 6, y: 0}, 
      { x: 7, y: 0}
    ],
      demTweetCounter: 0,
      repTweetCounter: 0,
      color: "#ccccff"
    }
  }

  setData(apiData){
    //console.log('IN SET DATA')
    apiData.forEach(tweet =>{ 
      console.log(tweet["party"])
      if (tweet["party"].toString() === "GOP"){
        this.state.repTweetCounter ++
        console.log(this.state.repTweetCounter)
        this.setState(
          this.state.dataRep = [
          { x: 1, y: ( this.state.dataRep[1] + tweet["tone_anger"])/this.repTweetCounter},
          { x: 2, y: (this.state.dataRep[2] + tweet["tone_fear"])/this.state.repTweetCounter},
          { x: 3, y: (this.state.dataRep[3] + tweet["tone_joy"]/ this.state.repTweetCounter)},
          { x: 4, y: (this.state.dataRep[4] + tweet["tone_sadness"])/ this.repTweetCounter},
          { x: 5, y: (this.state.dataRep[5] + tweet["tone_analytic"])/this.repTweetCounter}, 
          { x: 6, y: (this.state.dataRep[6] + tweet["tone_confident"])/ this.repTweetCounter}, 
          { x: 7, y: (this.state.dataRep[7] + tweet["tone_tentative"])/this.repTweetCounter}
        ])
        console.log(this.state.dataRep)
      }
        
      if (tweet["party"].toString() === "DEM"){
        this.state.demTweetCounter ++
        console.log(this.state.demTweetCounter)
        this.setState(
          this.state.dataDem = [
            { x: 1, y: ( this.state.dataDem[1] + tweet["tone_anger"])/this.state.demTweetCounter},
            { x: 2, y: (this.state.dataDem[2] + tweet["tone_fear"])/this.state.demTweetCounter},
            { x: 3, y: (this.state.dataDem[3] + tweet["tone_joy"]/ this.state.demTweetCounter)},
            { x: 4, y: (this.state.dataDem[4] + tweet["tone_sadness"])/ this.state.demTweetCounter},
            { x: 5, y: (this.state.dataDem[5] + tweet["tone_analytic"])/this.state.demTweetCounter}, 
            { x: 6, y: (this.state.dataDem[6] + tweet["tone_confident"])/ this.state.demTweetCounter}, 
            { x: 7, y: (this.state.dataDem[7] + tweet["tone_tentative"])/this.state.demTweetCounter}
          ])
          console.log(this.state.dataDem)
        }
      }
      );
    }     

 
  getData(){
    let self = this
    //TODO: refactor to env
    const url = 'http://localhost:5000'
    //'https://atatvi.onrender.com'
    //const axios = require('axios')
    
    axios.get(url+'/api/v1/report')
      .then(function (response){
        console.log('in getData above setData'+ JSON.stringify(response))
        console.log(response.data.parties)
        self.setData(response.data.parties)
       
       //console.log('under set data in get data'+ JSON.stringify(response))
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

  componentDidMount(){
    this.getData()
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
