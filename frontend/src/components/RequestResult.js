import React, { Component } from "react";
import { render } from "react-dom";


class RequestResult extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id: 0,
      user: '',
      sequence: '',
      status: '',
      genome: '',
      location: '',
      protein: '',
      fetchNum: 0
    };
  }

  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  fetchRequest(id) {
    const fetchNum = this.state.fetchNum + 1;
    fetch(`api/requests/${id}/`)
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
            ...data,
            fetchNum
          };
        });
      });
  }



  componentDidMount() {
    this.setState({...this.props});
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.state.status === "RUNNING" && this.state.fetchNum <= 10) {
      this.sleep(1000).then(() => {
        this.fetchRequest(this.props.id)
      });
    }
  }

  render_data() {
    if (this.state.status === "RUNNING") {
      return (`Sequence: ${this.state.sequence}, Status: ${this.state.status}`);
    } else if (this.state.status === "ERROR") {
      return (`Error matching sequence ${this.state.sequence}`);
    } else if (this.state.status === "INVALID") {
      return (`Invalid sequence ${this.state.sequence}`);
    } else if (this.state.status === "NOT_FOUND") {
      return (`Sequence ${this.state.sequence} not found to encode any protein in list.`);
    } else {
      const genome_link = `https://www.ncbi.nlm.nih.gov/nuccore/${this.state.genome}`;
      return (<div>{`Sequence: ${this.state.sequence}, Result: This sequence was found in ${this.state.genome} at location ${this.state.location} encoding protein ${this.state.protein}. See genome `}<a href={genome_link}>here.</a></div>)
    }
  }

  render() {
    const data = this.render_data();
    return (
      <div>
      {data}
      </div>
    );
  }
}

export default RequestResult;
