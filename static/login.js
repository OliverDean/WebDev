// uses jquery to handle click events and animations for toggling between the login and registration forms.

$(document).ready(function() {
  var panelOne = $('.form-panel.two').height(),
    panelTwo = $('.form-panel.two')[0].scrollHeight;
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
            window.location.href = "/login";
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

  $('.form-panel.two').not('.form-panel.two.active').on('click', function(e) {
    e.preventDefault();

    $('.form-toggle').addClass('visible');
    $('.form-panel.one').addClass('hidden');
    $('.form-panel.two').addClass('active');
    $('.form').animate({
      'height': panelTwo
    }, 200);
  });

  $('.form-toggle').on('click', function(e) {
    e.preventDefault();
    $(this).removeClass('visible');
    $('.form-panel.one').removeClass('hidden');
    $('.form-panel.two').removeClass('active');
    $('.form').animate({
      'height': panelOne
    }, 200);
  });

  $("#login-form").on("submit", function(e) {
    e.preventDefault();
    const formData = $(this).serialize();
    $.post("/login", formData, function(response) {
      if (response.status === "success") {
        window.location.href = "/dashboard";
      } else {
        console.log('incorrect login')
        alert(response.message);
      }
    });
  });

  $(document).on("submit", "#register-form", function(e) {
    
  });
  });
  

