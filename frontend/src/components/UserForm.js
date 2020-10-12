import React, { Component } from "react";
import { render } from "react-dom";

class UserForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({name: event.target.value});
  }

  handleSubmit(event) {
    localStorage.setItem('user', this.state.name);
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Please enter a name we can associate these jobs with:
          <input type="text" value={this.state.name} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default UserForm;

