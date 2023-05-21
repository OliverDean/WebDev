// Uses jQuery to handle click events and animations for toggling between the login, registration, and forgot password forms.
$(document).ready(function () {
  var panelOne = $('.form-panel.two').height(),
    panelTwo = $('.form-panel.two')[0].scrollHeight,
    panelThree = $('.form-panel.three')[0].scrollHeight,
    panelFour = $(".form-panel.four")[0].scrollHeight;

  function handleRegisterFormSubmit(e) {
    console.log("Submit event triggered");
    e.preventDefault();
    const formData = $("#register-form").serialize();
    console.log("Submitting form data:", formData);

    $.ajax({
      type: "POST",
      url: "/register",
      data: formData,
      success: function (response) {
        console.log("Received response:", response);
        if (response.status === "success") {
          alert("Registration successful!");
          window.location.href = "/";
        } else {
          alert(response.message);
        }
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.error("Error in AJAX request:", textStatus, errorThrown);
      },
    });
  }

  $("#register-button").on("click", function (e) {
    e.preventDefault();
    handleRegisterFormSubmit(e);
  });

  $('.form-panel.two').not('.form-panel.two.active').on('click', function (e) {
    e.preventDefault();

    $('.form-toggle').addClass('visible');
    $('.form-panel.one').addClass('hidden');
    $('.form-panel.two').addClass('active');
    $('.form').animate({
      'height': panelTwo
    }, 200);
  });

  $('.form-toggle').on('click', function (e) {
    e.preventDefault();
    $(this).removeClass('visible');
    $('.form-panel.one').removeClass('hidden');
    $('.form-panel.two').removeClass('active');
    $('.form').animate({
      'height': panelOne
    }, 200);
  });

  $(".form-recovery").on("click", function (e) {
    e.preventDefault();
    $('.form-panel.one').addClass('hidden');
    $('.form-panel.two').removeClass('active');
    $('.form-panel.three').addClass('active');
    $('.form').animate({
      'height': panelThree
    }, 200);
  });
  
  $(".form-back-to-login").on("click", function (e) {
    e.preventDefault();
    $('.form-panel.one').removeClass('hidden');
    $('.form-panel.three').removeClass('active');
    $('.form').animate({
      'height': panelOne
    }, 200);
  });

  $("#forgot-password-form").on("submit", function (e) {
    e.preventDefault();
    const formData = $(this).serialize();
    $.post("/forgot_password", formData, function (response) {
      if (response.status === "success") {
        alert("Password reset email has been sent!");
      } else {
        alert(response.message);
      }
    });
  });
  
  $("#login-form").on("submit", function (e) {
    e.preventDefault();
    const formData = $(this).serialize();
    $.post("/login", formData, function (response) {
      if (response.status === "success") {
        window.location.href = "/chatbot";
      } else {
        console.log('incorrect login');
        // Show the login error message
        $('#login-error').show();
        // Optionally, hide the error message after a few seconds:
        setTimeout(function() {
          $('#login-error').hide();
        }, 5000); // Hide after 5 seconds
      }
    });
  });
});

