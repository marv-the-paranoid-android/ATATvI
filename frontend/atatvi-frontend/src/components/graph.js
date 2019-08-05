import React from 'react'; 
import ReactDom from 'react-dom';
import {VictoryBar, VictoryChart, VictoryAxis} from 'victory'; 

const data2012 = [
  {quarter: 1, earnings: 13000},
  {quarter: 2, earnings: 16500},
  {quarter: 3, earnings: 14250},
  {quarter: 4, earnings: 19000}
];

export class Graph extends React.Component {
  render(){
    return(
      <VictoryChart>
        <VictoryBar
        data={data2012}
        x="quarter" 
        y="earnings"
        />
      </VictoryChart>  
    ); 
  }
}

