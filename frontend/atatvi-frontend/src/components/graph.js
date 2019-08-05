import React, {Component} from 'react'; 
//import ReactDom from 'react-dom';
import {VictoryArea, VictoryPolarAxis,VictoryChart, VictoryTheme, VictoryLabel} from 'victory'; 

const data2012 = [
  {quarter: 1, earnings: 13000},
  {quarter: 2, earnings: 16500},
  {quarter: 3, earnings: 14250},
  {quarter: 4, earnings: 19000}
];

class Graph extends Component {
  render(){
    return(
      <VictoryChart polar
      theme={VictoryTheme.material}
      
      >
        <VictoryPolarAxis dependentAxis
        //style={{axis: {stroke: "black"}}}
        //tickValues={[1,2,3,4]}
        //tickFormat={["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"]}
        />
        <VictoryPolarAxis
        // dependentAxis
        // tickFormat={(x)=>(`$${x/1000}k`)}
        />
        <VictoryArea
        //categories={{x: ["anger", "fear", "joy", "sadness", "analytic", "confident", "tentative"] }}
        data={data2012}
        style = {{
          data: {fill: "#c43a31" }
        }}
        //labels={["anger", "fear", "joy", "sadness", "analytic", "confident", "tentative"]}
        //labelComponent={<VictoryLabel renderInPortal />}
        x="quarter" 
        y="earnings"
        />
      </VictoryChart>  
    ); 
  }
}

export default Graph; 
