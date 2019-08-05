import React, {Component} from 'react'; 
//import ReactDom from 'react-dom';
import {VictoryArea, VictoryPolarAxis,VictoryChart, VictoryTheme, VictoryLabel} from 'victory'; 

const testData = [
  {tone: "anger", percentage: 0.2},
  {tone: "fear", percentage: 0.15},
  {tone: "joy", percentage: 0.15},
  {tone: "sadness", percentage: 0.2},
  {tone: "analytic", percentage: 0.15},
  {tone: "confident", percentage: 0.1},
  {tone: "tentative", percentage: 0.05}
  
];

class Graph extends Component {
  render(){
    return(
      <VictoryChart polar
      theme={VictoryTheme.material}
      >
        <VictoryPolarAxis dependentAxis
        style={{axis: {stroke: "none"}}}
        tickFormat= {[0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1]}
        tickValues = {[0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1]}
        />
        <VictoryPolarAxis
         dependentAxis
        tickFormat= {[0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1]}
        tickValues = {[0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1]}
        />
        <VictoryPolarAxis
        tickFormat= {[0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1]}
        tickValues = {[0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1]}
        />

        <VictoryArea
        categories={{x: ["anger", "fear", "joy", "sadness", "analytic", "confident", "tentative"] }}
        data={testData}
        style = {{
          data: {fill: "#c43a31" }
        }}
        labels={["anger", "fear", "joy", "sadness", "analytic", "confident", "tentative"]}
        labelComponent={<VictoryLabel renderInPortal />}
        />
      </VictoryChart>  
    ); 
  }
}

export default Graph; 
