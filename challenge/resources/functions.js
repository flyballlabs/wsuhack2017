// Define login variables and functions

const apiURL = "https://wsuhack.flyballlabs.com"

/*
 * Creates a new user in the realtime database
 */
function createUser() {
  console.log("Creating user: " + username);

  const username = document.getElementById("register-form").elements["username"].value;
  const password = document.getElementById("register-form").elements["password"].value;
  const name = document.getElementById("register-form").elements["name"].value;
  const email = document.getElementById("register-form").elements["email"].value;
  const mobile = document.getElementById("register-form").elements["mobile"].value;
  const grade_level = document.getElementById("register-form").elements["grade_level"].value;
  const school_id = document.getElementById("register-form").elements["school_id"].value;

  if (document.getElementById("role-staff").checked === true) {
    const user_type = "staff";
  }
  else if (document.getElementById("role-security").checked === true) {
    const user_type = "security";
  }
  else if (document.getElementById("role-principal").checked === true) {
    const user_type = "principal";
  }
  // default to student (should never reach this)
  else {
    const user_type = "student";
  }

  postData = {
    "username": username,
    "password": password,
    "name": name,
    "email": email,
    "mobile": mobile,
    "user_type": user_type,
    "grade_level": grade_level,
    "school_id": school_id
  };

  // Send POST request with user data to api
  $.post(apiURL + "/users", postData, function(data,status,xhr) {
      console.log(data);
      console.log(status);
      console.log(xhr);
    }).done(function() {console.log("No Error");})
      .fail(function() {console.log("Error occurred");});
  }

/*
 * Logins a user in using the realtime database
 */
function loginUser() {
  // Grab vales from Form
  const username = document.getElementById("login-form").elements["username"].value;
  const password = document.getElementById("login-form").elements["password"].value;

  console.log("Logging in user: " + username);

  postData = {
    "username": username,
    "password": password
  };

  // Grab password from api
  $.ajax({
      type: "POST",
      url: "https://wsuhack.flyballlabs.com/auth",
      data: JSON.stringify(postData),
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      dataType: 'json',
      success: function(data) {
        console.log("Auth Succeeded");
        console.info(data);

          if (data['type'] === 0) {
            window.location.href = "homepage/report-threat.html";
          }
          else if (data['type'] > 0) {
            window.location.href = "homepage/index.html";
          }
          else {
            window.location.href = "index.html";
          }

      },
      error: function(data){
        console.log("Auth Failed");
      }
  });

}

/*
 * Functions for grabbing values from Forms
 */
function passRegisterVals() {
  console.log("Passing vals to create func");


  const args = [ user, name, email, phone, role ];
  console.log(args);
  return args;
}

