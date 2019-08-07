import React, {Component} from 'react';
import Graph from './components/graph.js';
import axios from 'axios';

require('dotenv').config()

class App extends Component{
  
  constructor(props){
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
        
        this.setState(
          this.state.dataRep = [
          { x: 1, y: ( this.state.dataRep[0]["y"] + tweet["anger"])/this.repTweetCounter},
          { x: 2, y: (this.state.dataRep[1]["y"] + tweet["fear"])/this.state.repTweetCounter},
          { x: 3, y: (this.state.dataRep[2]["y"] + tweet["joy"]/ this.state.repTweetCounter)},
          { x: 4, y: (this.state.dataRep[3]["y"] + tweet["sadness"])/ this.repTweetCounter},
          { x: 5, y: (this.state.dataRep[4]["y"] + tweet["analytic"])/this.repTweetCounter}, 
          { x: 6, y: (this.state.dataRep[5]["y"] + tweet["confident"])/ this.repTweetCounter}, 
          { x: 7, y: (this.state.dataRep[6]["y"] + tweet["tentative"])/this.repTweetCounter}
        ])
        //console.log("whole object"+ this.state.dataRep)
        //console.log("one line of obj"+ this.state.dataRep[1]["y"])
        console.log("one line from the tweet data" + tweet["anger"])
        console.log("tweet counter" + this.state.repTweetCounter)
      }
        
      if (tweet["party"].toString() === "DEM"){
        this.state.demTweetCounter ++
        this.setState(
          this.state.dataDem = [
            { x: 1, y: ( this.state.dataDem[0]["y"] + tweet["anger"])/this.state.demTweetCounter},
            { x: 2, y: (this.state.dataDem[1]["y"] + tweet["fear"])/this.state.demTweetCounter},
            { x: 3, y: (this.state.dataDem[2]["y"] + tweet["joy"])/ this.state.demTweetCounter},
            { x: 4, y: (this.state.dataDem[3]["y"] + tweet["sadness"])/ this.state.demTweetCounter},
            { x: 5, y: (this.state.dataDem[4]["y"] + tweet["analytic"])/this.state.demTweetCounter}, 
            { x: 6, y: (this.state.dataDem[5]["y"] + tweet["confident"])/ this.state.demTweetCounter}, 
            { x: 7, y: (this.state.dataDem[6]["y"] + tweet["tentative"])/this.state.demTweetCounter}
          ])
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
        // console.log(response.data.parties)
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
