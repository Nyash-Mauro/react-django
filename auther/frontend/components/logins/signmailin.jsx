import React from 'react'

function signMailIn(loginSubmit, otpSubmit, viewOtpForm) {
    return (
      <div className="wrapper">
        <h1 className="main-heading">Sign in</h1>
        <p className="sub-text">Sign in using your email.</p>
        {!viewOtpForm ? (
          <div className="form-wrapper">
            <form id="loginForm" onSubmit={loginSubmit}>
              <div className="input-field">
                <label>Email</label>
                <input
                  type="text"
                  placeholder="Phone"
                  name="phone"
                  autoComplete="false"
                />
              </div>
              <button className="main-button" type="submit" id="sign-in-button">
                Sign in
              </button>
            </form>
          </div>
        ) : (
          <div className="form-wrapper" onSubmit={otpSubmit}>
            <form id="otpForm">
              <div className="input-field">
                <label>Enter OTP</label>
                <input
                  type="number"
                  placeholder="One time password"
                  name="otp_value"
                  autoComplete="false"
                />
              </div>
              <button className="main-button" type="submit">
                Verify OTP
              </button>
            </form>
          </div>
        )}
      </div>
    )
  }
export default signMailIn