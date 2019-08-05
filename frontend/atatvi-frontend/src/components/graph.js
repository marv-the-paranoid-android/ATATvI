import React, {Component} from 'react'; 
//import ReactDom from 'react-dom';
import {VictoryArea, VictoryChart, VictoryAxis, VictoryTheme} from 'victory'; 

const data2012 = [
  {quarter: 1, earnings: 13000},
  {quarter: 2, earnings: 16500},
  {quarter: 3, earnings: 14250},
  {quarter: 4, earnings: 19000}
];

class Graph extends Component {
  render(){
    return(
      <VictoryChart
      theme={VictoryTheme.material}
      domainPadding={20}
      >
        <VictoryAxis
        tickValues={[1,2,3,4]}
        tickFormat={["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"]}
        />
        <VictoryAxis
        dependentAxis
        tickFormat={(x)=>(`$${x/1000}k`)}
        />
        <VictoryArea
        data={data2012}
        x="quarter" 
        y="earnings"
        />
      </VictoryChart>  
    ); 
  }
}

export default Graph; 
