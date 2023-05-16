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
    // type == yes_no
    if (type === 'self' && buttons.length > 0) {
      str += "<div class='button-group'>";
      for (var i = 0; i < buttons.length; i++) {
        str += "<button class='button' data-value='" + buttons[i] + "'>" + buttons[i] + "</button>";
      }
      str += "</div>";
    }
    str += "</div>";
    $(".chat-logs").append(str);
    $("#cm-msg-"+INDEX).hide().fadeIn(300);
    $(".chat-logs").animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, "fast");

  }