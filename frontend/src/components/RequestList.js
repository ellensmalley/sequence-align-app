import React, { Component } from "react";
import { render } from "react-dom";
import RequestResult from "./RequestResult";

class RequestList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  fetchUserRequests(user) {
    fetch(`api/requests/${user}/`)
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  componentDidMount() {
    const user = this.props.user;
    if (user !== undefined && user !== null) {
      this.fetchUserRequests(user);
    }
  
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.user !== this.props.user) {
      if (user !== undefined && user !== null) {
        this.fetchUserRequests(user);
      }
    }
  }

  render() {
    return (
      <ul>
        {this.state.data.reverse().map(result => {
          return (
            <li key={result.id}>
              <RequestResult {...result} />
            </li>
          );
        })}
      </ul>
    );
  }
}

export default RequestList;
