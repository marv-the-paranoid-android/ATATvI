import React, {Component} from 'react';
import Graph from './components/graph.js';
import axios from 'axios';

require('dotenv').config()

class App extends Component{
  
  constructor(props){
    console.log('in constructor')
    super(props)
    this.state = {
      dataDem:  [{ x: 1, y: anger},
      { x: 2, y: fear},
      { x: 3, y: joy},
      { x: 4, y: sadness},
      { x: 5, y: analytic}, 
      { x: 6, y: confident}, 
      { x: 7, y: tentative},
    ],
      dataRep: [ 
      { x: 1, y: anger},
      { x: 2, y: fear},
      { x: 3, y: joy},
      { x: 4, y: sadness},
      { x: 5, y: analytic}, 
      { x: 6, y: confident}, 
      { x: 7, y: tentative}
    ],
      demTweetCounter: 0,
      repTweetCounter: 0,
      color: "#ccccff"
    }
  }

  setData(apiData){
    //console.log('IN SET DATA')
    apiData.forEach(tweet => 
      console.log(tweet["party"])
      if (tweet["party"] === "GOP"){
        this.demTweetCounter ++
        this.setState(
          this.dataRep = [
          { x: 1, y: ( anger + tweet["tone_anger"])/this.demTweetCounter},
          { x: 2, y: (fear + tweet["tone_fear"])/demTweetCounter},
          { x: 3, y: (joy + tweet["tone_joy"]/ demTweetCounter)},
          { x: 4, y: (sadness + tweet["tone_sadness"])/ demTweetCounter},
          { x: 5, y: (analytic + tweet["tone_analytic"])/demTweetCounter}, 
          { x: 6, y: (confident + tweet["tone_confident"])/ demTweetCounter}, 
          { x: 7, y: (tentative + tweet["tone_tentative"])/demTweetCounter}
        ])
      }
        console.log("REP DATA 🦅🦅🦏🦏🦏🦏🇺🇸🇺🇸🇺🇸🇺🇸**********************************************************************************", this.dataRep)
      if (tweet["party"] === "DEM"){
        this.repTweetCounter ++
        this.setState(
          this.dataDem = [
          { x: 1, y: tweet["tone_anger"]},
          { x: 2, y: tweet["tone_fear"]},
          { x: 3, y: tweet["tone_joy"]},
          { x: 4, y: tweet["tone_sadness"]},
          { x: 5, y: tweet["tone_analytic"]}, 
          { x: 6, y: tweet["tone_confident"]}, 
          { x: 7, y: tweet["tone_tentative"]}
          ]
        )
        console.log("DEM DATA 🦅🦅🐐🐐🐐🐐🇺🇸🇺🇸🇺🇸🇺🇸**********************************************************************************", this.dataDem)

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
