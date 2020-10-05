document.addEventListener("DOMContentLoaded", () => {
  console.log("Loaded!");
  document.querySelector("#login").style.display = "none";
  document.querySelector("#registration").style.display = "none";

  document.querySelector("#loginbtn").addEventListener("click", () => {
    document.querySelector("#login").style.display = "block";
    document.querySelector("#registration").style.display = "none";
    document.querySelector(".message").style.display = "none";
  });

  document.querySelector("#registrationbtn").addEventListener("click", () => {
    document.querySelector("#registration").style.display = "block";
    document.querySelector("#login").style.display = "none";
    document.querySelector(".message").style.display = "none";
  });

  $("#registration").on("submit", function (e) {
    e.preventDefault();
    console.log("Register!");

    let csrfToken = $("input[name=csrfmiddlewaretoken]").val();
    console.log(csrfToken);

    $.ajax({
      type: "POST",
      url: "/api/v1/users/new",
      data: {
        first_name: $("#fname").val(),
        last_name: $("#lname").val(),
        username: $("#username").val(),
        email: $("#email").val(),
        password: $("#password").val(),
        password2: $("#password2").val(),
        csrfmiddlewaretoken: csrfToken,
        credentials: "include",
      },

      success: function (response) {
        console.log(response);
        document.querySelector("#registration").style.display = "none";
        document.querySelector("#login").style.display = "block";
        let message = document.querySelector(".message");
        message.innerHTML = `<h3 class="alert alert-info">Registration Success!</h3>`;
        message.style.display = "block";
      },

      error: function (err) {
        console.log(JSON.stringify(err));
      },
    });
  });
});
