import React, { Component } from "react";

class Signup extends Component{
    constructor(props){
        super(props);
        this.state = {
            email: "",
            password: "",
            email:""
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit(event) {
        alert('A email and password was submitted: ' + this.state.email + " " + this.state.password + " " + this.state.email);
        event.preventDefault();
    }

    render() {
        return (
            <div>
                Signup
                <form onSubmit={this.handleSubmit}>
                    <label>
                        email:
                        <input name="email" type="text" value={this.state.email} onChange={this.handleChange}/>
                    </label>

                    <label>
                        Password:
                        <input name="password" type="password" value={this.state.password} onChange={this.handleChange}/>
                    </label>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        )
    }
}
export default Signup;