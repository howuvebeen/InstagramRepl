import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import { connect } from "react-redux";

class Header extends Component {

    static propTypes = {
        authenticated: PropTypes.bool
    };
    //If authenticated, show Profile and Logout in nav-bar
    renderLinks() {
        if (this.props.authenticated) {
            return (
                [
                    <li className="nav-item" key="profile">
                        <Link className="nav-link" to="/profile">Profile</Link>
                    </li>,
                    <li className="nav-item" key="logout">
                        <Link className="nav-link" to="/logout">Logout</Link>
                    </li>
                ]
            );
        //If not authenticated, show Login and Sign up in nav-bar
        } else {
            return (
                [
                    <li className="nav-item" key="login">
                        <Link className="nav-link" to="/login">Login</Link>
                    </li>,
                    <li className="nav-item" key="signup">
                        <Link className="nav-link" to="/signup">Sign Up</Link>
                    </li>
                ]
            );
        }
    }

    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <Link to="/" className="navbar-brand">Instagram</Link>
                <ul className="navbar-nav">
                    {this.renderLinks()}
                </ul>
            </nav>
        )
    }
}

// we need authenticated data from state changed to prop 
function mapStateToProps(state) {
    return {
        authenticated: state.auth.authenticated
    }
}
/* to read data from the store, enable by calling connect with the mapStateToProps parameter, 
 a function describing which part of the data we need from the store.*/
export default connect(mapStateToProps)(Header);