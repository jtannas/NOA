function checkPasswordMatch() {
  var password1 = $("#password1").val();
  var password2 = $("#password2").val();

  if (password1 != password2) {
    $("#divCheckPasswordMatch").html("Passwords do not match!");
    $("#divCheckPasswordMatch").attr("class","text-danger");
  } else {
    $("#divCheckPasswordMatch").html("Passwords match");
    $("#divCheckPasswordMatch").attr("class","text-success");
  }
}

$(document).ready(function() {
  $("#password1, #password2").keyup(checkPasswordMatch);
});