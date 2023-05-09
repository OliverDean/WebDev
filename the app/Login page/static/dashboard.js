$(function() {
  var INDEX = 0;

  function generate_message(msg, type) {
    INDEX++;
    var str = "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
    str += "<span class=\"msg-avatar\">";
    str += "<img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
    str += "</span>";
    str += "<div class=\"cm-msg-text\">";
    str += msg;
    str += "</div>";
    str += "</div>";
    $(".chat-logs").append(str);
    $("#cm-msg-"+INDEX).hide().fadeIn(300);
    $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);
  }

  $("#chat-submit").click(function(e) {
    e.preventDefault();
    var msg = $("#chat-input").val();
    if(msg.trim() == ''){
      return false;
    }
    generate_message(msg, 'user');
    $("#chat-input").val('');
    // Send user's message to the server and get response
    $.post("/chat", {message: msg})
      .done(function(data) {
        generate_message(data.message, 'self');
      });
  });

  // Fetch initial message from the server
  $.get("/start")
    .done(function(data) {
      generate_message(data.message, 'self');
    });
});
