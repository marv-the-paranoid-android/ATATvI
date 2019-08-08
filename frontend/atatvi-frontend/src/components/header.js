import React, { Component } from 'react'


class Header extends Component {
    render() {
      return (
      <>
        <section className="Header">
        <link href="https://fonts.googleapis.com/css?family=Lora:400,700|Montserrat:300" rel="stylesheet"></link>
        <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed&display=swap" rel="stylesheet"></link>
        <h1 className='title'>ATATvI
        <p className="nlp"> <img className="nlp" src={require('../assets/atatvi-logo.png')} alt='logo flower'/></p>
        </h1>
        </section>
      </>
      );
    }
  }

export default Header