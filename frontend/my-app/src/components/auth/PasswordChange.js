import React, { Component } from "react";
// import PropTypes from "prop-types";
import { reduxForm, Field, propTypes } from "redux-form";
import { required } from "redux-form-validators"
import { changePassword } from "../../actions/authActions";
import { renderField, renderError } from "../../utils/renderUtils";

class PasswordChange extends Component {

    static propTypes = {
        ...propTypes
    };

    render() {
        const { handleSubmit, error } = this.props;

        return (
            <div className="row justify-content-center">
                <form
                    className="col col-sm-4 card mt-5 p-2"
                    onSubmit={handleSubmit}
                >
                    <h4 className="text-md-center">Change Password</h4>
                    <hr/>

                    <fieldset className="form-group">
                        <Field name="old_password" label="Old Password" component={renderField}
                               type="password" validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
                        <Field name="password" label="Password" component={renderField}
                               type="password" validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
                        <Field name="password_confirm" label="Password Confirm" component={renderField}
                               type="password" validate={[required({message: "This field is required."})]}
                        />
                    </fieldset>

                    <fieldset className="form-group">
                        {renderError(error)}
                        <button action="submit" className="btn btn-primary">Submit</button>
                    </fieldset>
                </form>
            </div>
        );
    }
}

// Sync field level validation for password match
const validateForm = values => {
    const errors = {};
    const { password, password_confirm } = values;
    if (password !== password_confirm) {
        errors.password_confirm = "Password does not match."
    }
    return errors;
};

export default reduxForm({
    form: "change_password",
    onSubmit: changePassword,
    validate: validateForm
})(PasswordChange);