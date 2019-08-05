import React, {Component} from 'react'; 
//import ReactDom from 'react-dom';
import {VictoryArea, VictoryPolarAxis,VictoryChart, VictoryTheme} from 'victory'; 

const testData = [
  { x: 1, y: 2},
  { x: 2, y: 3},
  { x: 3, y: 5},
  { x: 4, y: 4},
  { x: 5, y: 6}, 
  { x: 6, y: 8}, 
  { x: 7, y: 1}
  
];

class Graph extends Component {
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
        grid: { stroke: "grey", strokeDasharray: "4, 8" }}}
      />

      <VictoryPolarAxis
        tickValues = {["Anger", "Fear", "Joy", "Sadness", "Analytic","Confident", "Tentative"]}
      />

      <VictoryArea
        data={testData}
        style={{data: {width: 1}}}
        
  
      />
      </VictoryChart>  
    ); 
  }
}

export default Graph; 
