import React, { Component } from "react";
import { render } from "react-dom";
import SequenceForm from "./SequenceForm.js";
import RequestList from "./RequestList.js";
import UserForm from "./UserForm.js";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      user: '',
      hasUser: false,
    };
  }

  componentDidMount() {
    const user = localStorage.getItem('user');
    if (user !== null && user !== undefined) {
      this.setState({ user , hasUser: true });
    }
  }

  render() {
    if (this.state.hasUser) {
      return (
        <div>
          <SequenceForm user={this.state.user} />
          <RequestList user={this.state.user} /> 
        </div>
      );
    } else {
      return (
        <UserForm />
      );
    }
    
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);