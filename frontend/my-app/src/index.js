import React from "react";
import ReactDOM from "react-dom";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import Landing from "./components/auth/Landing";
import Login from "./components/auth/Login";

ReactDOM.render(
    <BrowserRouter>
        <Switch>
            <Route exact path="/" component={Landing}/>
            <Route path="/login" component={Login}/>
        </Switch>
    </BrowserRouter>

, document.getElementById("root"));