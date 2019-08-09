import React, {Component} from 'react';
import Graph from './components/graph.js';
import Header from './components/header.js';
import Main from './components/Main.js';
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
        <div className="rep">Republican Tweet Tones:</div>
          <article className="graph">
            <Graph className="gop" party='GOP' color='red' />
          </article>
          <div className="dem">Democrat Tweet Tones:</div>
          <article className="graph-two">
            <Graph party='DEM' color='blue' />
          </article>
          <Main />
          </section>
     </div>
    
     </>
     
    );
}
}

export default App;