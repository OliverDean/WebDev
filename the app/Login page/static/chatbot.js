
// Chatbot functionality start
$(function() {
  var INDEX = 0;

  function generate_message(msg, type, buttons = []) {
    INDEX++;
    if (type==='self') {
      var str = '<div class="messages_item messages_item_self">' + msg + "</div>";
    }
    if (type==='user') {
      var str = '<div class="messages_item messages_item_user">' + msg + "</div>";
    }
    if (type==='image') {
      var str = '<div class="messages_item_image"><img src="/static/images/Alicecat.png"></div>';
    }
    if (type==='button' && buttons.length > 0) {
      str += "<div class='button-group'>";
      for (var i = 0; i < buttons.length; i++) {
        str += "<button class='button' data-value='" + buttons[i] + "'>" + buttons[i] + "</button>";
      }
      str += "</div>";
    }
    
    $(".chat-logs").append(str);
    $("#cm-msg-"+INDEX).hide().fadeIn(300);
    $(".chat-box-body").animate({ scrollTop: $(".chat-box-body")[0].scrollHeight}, 2500);

  }
  

  $("#chat-submit").click(function(e) {
    e.preventDefault();
    var msg = $("#chat-input").val();
    if(msg.trim() === ''){
      return false;
    }
    generate_message(msg, 'user');
    $("#chat-input").val('');
    // Send user's message to the server and get response
    $.ajax({
      type: "POST",
      url: "/chat",
      contentType: "application/json",
      data: JSON.stringify({ message: msg }),
      dataType: "json",
      success: function(data) {
        console.log("Response received: " + data.message);
        generate_message(data.message, 'self', data.buttons);
        handleDragDropArea(data.showDropArea);
        $(".chat-box-body").stop().animate({ scrollTop: $(".chat-box-body")[0].scrollHeight}, 1500);
      },
      error: function() {
        console.log("Error occurred while sending request");
      }
    });
  });

  // Fetch initial message from the server
  $.get("/start")
    .done(function(data) {

      console.log("Initial message received: " + data.message);

      generate_message(data.message, 'image', data.buttons);
      generate_message(data.message, 'self', data.buttons);
      handleDragDropArea(data.showDropArea);

      $(".chat-box-body").stop().animate({ scrollTop: $(".chat-box-body")[0].scrollHeight}, 10000);
    })
    .fail(function() {
      console.log("Error occurred while fetching initial message");
    });

  // Handle button clicks
  $(document).on("click", ".button", function() {
    var msg = $(this).data('value');
    generate_message(msg, 'user');
    // Send user's message to the server and get response
    $.post("/chat", {message: msg})
      .done(function(data) {
        if (data.buttons.length === 0) {
          // No buttons in the response, display the response only
          generate_message(data.message, 'self');
        } else {
          // Buttons in the response, display the response and buttons
          generate_message(data.message, 'self', data.buttons);
        }
        handleDragDropArea(data.showDropArea);

        // Check if the user's response should prompt for age
        if (msg.toLowerCase() === "yes" && data.message.toLowerCase().includes("what is your age")) {
          // Display an input field for the user to enter their age
          var ageInput = "<input type='text' id='age-input' placeholder='Enter your age'>";
          $(".chat-logs").append(ageInput);
          $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);
        }
      });
  });

// Handle age input submission
$(document).on("click", "#age-input-submit", function() {
  var age = $("#age-input").val();
  generate_message(age, 'user');
  // Send user's age to the server and get response
  $.post("/chat", {message: age})
    .done(function(data) {
      // Remove the age input field
      $("#age-input").remove();

      // Display the response
      generate_message(data.message, 'self', data.buttons);
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);
    });
});
});

// Chatbot functionality end

// Sidebar functionality start
const toggleBtn = document.querySelector(".sidebar-toggle");
const closeBtn = document.querySelector(".close-btn");
const sidebar = document.querySelector(".sidebar");

toggleBtn.addEventListener("click", function () {
  // // if (sidebar.classList.contains("show-sidebar")) {
  // //   sidebar.classList.remove("show-sidebar");
  // // } else {
  // //   sidebar.classList.add("show-sidebar");
  // // }
  sidebar.classList.toggle("show-sidebar");
});

closeBtn.addEventListener("click", function () {
  sidebar.classList.remove("show-sidebar");
});
// Sidebar functionality end

function handleDragDropArea(showDropArea) {
  // TODO: implement functionality for drag-drop area
  console.log('Called handleDragDropArea with', showDropArea);
}