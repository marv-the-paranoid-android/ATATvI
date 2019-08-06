import React, {Component} from 'react'; 
//import ReactDom from 'react-dom';
import {VictoryArea, VictoryPolarAxis,VictoryChart, VictoryTheme} from 'victory'; 

// const testData = [
//   { x: 1, y: .4},
//   { x: 2, y: .9},
//   { x: 3, y: .2},
//   { x: 4, y: .6},
//   { x: 5, y: .1}, 
//   { x: 6, y: .8}, 
//   { x: 7, y: .1}
  
// ];

class Graph extends Component {

  constructor(props){
    super(props); 
    this.state = {
      data: props.data,
      color: props.color
    }
  }

  render(){
    return(
      <VictoryChart polar
      domain={{x: [0, 7]}}
      theme={VictoryTheme.material}
      
      //height={400} width={400}
      >
      <VictoryPolarAxis dependentAxis
        style={{
        axis: {stroke: "none"},
        grid: { stroke: "grey", strokeDasharray: "4, 8" }
      }}
      />

      <VictoryPolarAxis
        tickValues = {["Anger", "Fear", "Joy", "Sadness", "Analytic","Confident", "Tentative"]}
      />

      <VictoryArea
        data={this.state.data}
        style={{data: {fill: this.state.color, width: 1}}}
      />
      </VictoryChart>  
    ); 
  }
}

export default Graph; 
