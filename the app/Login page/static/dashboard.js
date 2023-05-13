$(function() {
  var INDEX = 0;

  function generate_message(msg, type, buttons = []) {
    INDEX++;
    var str = "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
    str += "<span class=\"msg-avatar\">";
    str += "</span>";
    str += "<div class=\"cm-msg-text\">";
    str += msg;
    str += "</div>";
    if (type === 'self' && buttons.length > 0) {
        str += "<div class='button-group'>";
        for (var i = 0; i < buttons.length; i++) {
          str += "<button class='button'>" + buttons[i] + "</button>";
        }
        str += "</div>";
    }
    str += "</div>";
    $(".chat-logs").append(str);
    $("#cm-msg-"+INDEX).hide().fadeIn(300);
    $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);
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
      generate_message(data.message, 'self', data.buttons);
    })
    .fail(function() {
      console.log("Error occurred while fetching initial message");
    });

  // Handle button clicks
  $(document).on("click", ".button", function() {
    var msg = $(this).text();
    generate_message(msg, 'user');
    // Send user's message to the server and get response
    $.post("/chat", {message: msg})
      .done(function(data) {
        generate_message(data.message, 'self', data.buttons);
      });
  });

});
