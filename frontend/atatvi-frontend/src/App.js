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
      color: "#ccccff",
      set: 0,

      dummyData: [
       { x: 1, y: 2},
       { x: 2, y: 3},
       { x: 3, y: 5},
       { x: 4, y: 4},
       { x: 5, y: 6}, 
       { x: 6, y: 6}, 
       { x: 7, y: 1}
      ]
    }


  }

  setData(apiData){
    //console.log('IN SET DATA')
    var curstate = this.state
    apiData.forEach(tweet =>{ 
      console.log(tweet["party"])
      if (tweet["party"].toString() === "GOP"){
        curstate.repTweetCounter ++
        
        
          curstate.dataRep = [
          { x: 1, y: ( curstate.dataRep[0]["y"] + tweet["anger"])/curstate.repTweetCounter},
          { x: 2, y: (curstate.dataRep[1]["y"] + tweet["fear"])/curstate.repTweetCounter},
          { x: 3, y: (curstate.dataRep[2]["y"] + tweet["joy"]/ curstate.repTweetCounter)},
          { x: 4, y: (curstate.dataRep[3]["y"] + tweet["sadness"])/ curstate.repTweetCounter},
          { x: 5, y: (curstate.dataRep[4]["y"] + tweet["analytic"])/curstate.repTweetCounter}, 
          { x: 6, y: (curstate.dataRep[5]["y"] + tweet["confident"])/ curstate.repTweetCounter}, 
          { x: 7, y: (curstate.dataRep[6]["y"] + tweet["tentative"])/curstate.repTweetCounter}
        ]
        //console.log("whole object"+ curstate.dataRep)
        //console.log("one line of obj"+ curstate.dataRep[1]["y"])
        console.log("one line from the tweet data" + tweet["anger"])
        console.log("tweet counter" + curstate.repTweetCounter)
      }
        
      if (tweet["party"].toString() === "DEM"){
        curstate.demTweetCounter ++
       
          curstate.dataDem = [
            { x: 1, y: ((curstate.dataDem[0]["y"] + tweet["anger"])/curstate.demTweetCounter)*100},
            { x: 2, y: ((curstate.dataDem[1]["y"] + tweet["fear"])/curstate.demTweetCounter)*100},
            { x: 3, y: ((curstate.dataDem[2]["y"] + tweet["joy"])/ curstate.demTweetCounter)*100},
            { x: 4, y: ((curstate.dataDem[3]["y"] + tweet["sadness"])/ curstate.demTweetCounter)*100},
            { x: 5, y: ((curstate.dataDem[4]["y"] + tweet["analytic"])/curstate.demTweetCounter)*100}, 
            { x: 6, y: ((curstate.dataDem[5]["y"] + tweet["confident"])/ curstate.demTweetCounter)*100},
            { x: 7, y: ((curstate.dataDem[6]["y"] + tweet["tentative"])/curstate.demTweetCounter)*100}
          ]
        }
      }
      );

      this.setState(curstate)
      console.log(curstate)
    }     

 
  getData(){
    //let self = this
    //TODO: refactor to env
    const url = 'http://localhost:5000'
    //'https://atatvi.onrender.com'
    //const axios = require('axios')
    
    axios.get(url+'/api/v1/report')
      .then((response => {
        console.log('in getData above setData'+ JSON.stringify(response))
        // console.log(response.data.parties)
        this.setData(response.data.parties)
       console.log(this.state)
       //console.log('under set data in get data'+ JSON.stringify(response))
      })
      )
      .catch(function(error){
        console.log(error)
      })
      
      }

  setColor(){


  }

  componentDidMount(){
    // this.getData()
    console.log('in did mount')
  }

  render(){
    if(this.state.set === 0){
      this.getData()
      this.setState({set : 1})
    }
    
    return (
     <div className="App">
        <Graph data={this.state.dataDem} color={this.state.color}/>
        <Graph data={this.state.dataRep} color={this.state.color}/>
        <Graph data={this.state.dummyData} color={this.state.color}/>
        
     </div>
   );
  }
}

export default App;
