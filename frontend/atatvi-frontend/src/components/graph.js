import React, {Component} from 'react';
import {VictoryArea, VictoryPolarAxis,VictoryChart, VictoryTheme} from 'victory';
import axios from 'axios';

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

    /**
     *
     */
    constructor(props){
        super(props);
        this.state = {

            party: props.party,
            color: props.color,
            set: 0,

            counter: 0,
            data: [
                { x: 1, y: 0},
                { x: 2, y: 0},
                { x: 3, y: 0},
                { x: 4, y: 0},
                { x: 5, y: 0},
                { x: 6, y: 0},
                { x: 7, y: 0},
            ],
        }
    }

    /**
     *
     */
    componentDidMount() {
        this.loadData();
    }

    /**
     *
     */
    parseData(data) {

        let curstate = this.state

        data.forEach(rec => {

            if (rec["party"].toString() === curstate.party) {
                curstate.counter ++

                curstate.data = [
                    { x: 1, y: ((curstate.data[0]["y"] + rec["anger"])     / curstate.counter)*100},
                    { x: 2, y: ((curstate.data[1]["y"] + rec["fear"])      / curstate.counter)*100},
                    { x: 3, y: ((curstate.data[2]["y"] + rec["joy"])       / curstate.counter)*100},
                    { x: 4, y: ((curstate.data[3]["y"] + rec["sadness"])   / curstate.counter)*100},
                    { x: 5, y: ((curstate.data[4]["y"] + rec["analytic"])  / curstate.counter)*100},
                    { x: 6, y: ((curstate.data[5]["y"] + rec["confident"]) / curstate.counter)*100},
                    { x: 7, y: ((curstate.data[6]["y"] + rec["tentative"]) / curstate.counter)*100}
                ]
            }
        });

        this.setState(curstate)
    }

    /**
     *
     */
    loadData() {

        // @TODO Turn into .ENV
        const url = 'http://localhost:5000/api/v1/report'

        axios.get(url)
            .then(response => {
                this.parseData(response.data.parties)
            })
            .catch(function(error){
                console.log(error)
            })
    }


    /**
     *
     */
    render(){
        return(
            <VictoryChart
                polar
                domain={{x: [0, 7]}}
                theme={VictoryTheme.material}
                height={200}
                width={200}
            >

                <VictoryPolarAxis
                    dependentAxis
                    style={{
                        axis: {stroke: "none"},
                        grid: { stroke: "grey", strokeDasharray: "4, 8" }
                    }}
                />

                <VictoryPolarAxis
                    tickValues = {["Anger", "Fear", "Joy", "Sadness", "Analytic", "Confident", "Tentative"]}
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
