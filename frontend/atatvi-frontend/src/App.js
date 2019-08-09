import React, {Component} from 'react';
import Graph from './components/graph.js';
import Header from './components/header.js';
import './scss/core.scss';
import './App.css';

require('dotenv').config()

class App extends Component{

render(){
    return (
      <>
      <div className="App">
        <Header />
        <section className="grid-container">
          <article className="graph">
            <Graph className="gop" party='GOP' color='red' />
          </article>
          <article className="graph-two">
            <Graph party='DEM' color='blue' />
          </article>
          </section>
        <div className="rep">Republican</div>
          <div className="dem">Democrat</div>
     </div>
    
     </>
     
    );
}
}

export default App;