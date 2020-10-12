import React, { Component } from "react";
import { render } from "react-dom";

class SequenceForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      sequence: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({sequence: event.target.value});
  }

  handleSubmit(event) {
    const postBody = {
      user: this.props.user,
      sequence: this.state.sequence
    };
    fetch('api/requests/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(postBody)
    });

  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Sequence:
          <input type="text" value={this.state.sequence} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default SequenceForm;