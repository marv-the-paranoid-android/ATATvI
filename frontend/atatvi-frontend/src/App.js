import React, {Component} from 'react';
import Graph from './components/graph.js';
import Header from './components/header.js';
import Modal from './components/Modal/Modal';
import './scss/core.scss';
import './App.css';

require('dotenv').config()

class App extends Component{

  constructor() {
    super();

    this.state = {
        isShowing: false
    }
  }

  openModalHandler = () => {
    this.setState({
      isShowing: true
    });
  }
  
  closeModalHandler = () => {
    this.setState({
      isShowing: false
    });
  }

render(){
    return (
      <>
      <div className="App">
        <Header />
        <section className="grid-container">
        <div className="rep">Republican:</div>
          <article className="graph">
            <Graph className="gop" party='GOP' color='red' />
          </article>
          <div className="dem">Democrat:</div>
          <article className="graph-two">
            <Graph party='DEM' color='blue' />
          </article>
          </section>
          { this.state.isShowing ? <div onClick={this.closeModalHandler} className="back-drop"></div> : null }

        <button className="open-modal-btn" onClick={this.openModalHandler}>Open Modal</button>

        <Modal
            className="modal"
            show={this.state.isShowing}
            close={this.closeModalHandler}>
                Democrat or Republican Name. Content of Tweets.
        </Modal>

        <div className="rep">Republican</div>
          <div className="dem">Democrat</div>

     </div>
    
     </>
     
    );
  }
}

export default App;