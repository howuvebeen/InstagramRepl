import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { getpostList } from "../../actions/authActions";

class Newsfeed extends Component {

    static propTypes = {
        getpostList: PropTypes.func.isRequired,
        post: PropTypes.object
    };

    componentWillMount() {
        this.props.getpostList();
    }

    renderPost() {
        const posts  = this.props.post;
        if (posts) {
            return (
                <div>
                  {posts.map(post => (
                    <div>
                        {post.owner}
                        {post.photo}
                        {post.description}
                    </div>
                  ))}
                </div>
            );
        }
        return null;
    }

    render() {
        return (
            <div>
                {this.renderPost()}
            </div>
        );
    }
}

function mapStateToProps(state) {
    return {
        post: state.auth.post
    }

}

export default connect(mapStateToProps, { getpostList } )( Newsfeed );