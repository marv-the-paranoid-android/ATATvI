import React, {Component} from 'react'; 
//import ReactDom from 'react-dom';
import {VictoryArea, VictoryPolarAxis,VictoryChart, VictoryTheme, VictoryLabel} from 'victory'; 

const testData = [
  {tone: "anger", percentage: 20},
  {tone: "fear", percentage: 15},
  {tone: "joy", percentage: 20},
  {tone: "sadness", percentage: 20},
  {tone: "analytic", percentage: 15},
  {tone: "confident", percentage: 10},
  {tone: "tentative", percentage: 5}
  
];

class Graph extends Component {
  render(){
    return(
      <VictoryChart polar
      theme={VictoryTheme.material}
      //domain={{x: [0, 1]}}
      height={400} width={400}
      >
        <VictoryPolarAxis dependentAxis
          style={{
          axis: {stroke: "none"},
          tickLabels: { fill: "none"},
           grid: { stroke: "grey", strokeDasharray: "4, 8" }}}
        />

        <VictoryPolarAxis
        tickValues = {["Anger", "Fear", "Joy", "Sadness", "Analytic", "Confident", "Tentative"]}
        />

        <VictoryArea
      
        data={testData}
        style = {{
          data: {fill: "#c43a31" }
        }}
  
        />
      </VictoryChart>  
    ); 
  }
}

export default Graph; 
