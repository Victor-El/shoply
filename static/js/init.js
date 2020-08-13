document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var options = {};
    var instances = M.Sidenav.init(elems, options);

    var agreeCheck = document.querySelector("input[name=agree]");
    var signup = document.getElementById("sign-up");
    agreeCheck.addEventListener('change', e => {
      if (e.target.checked == true) {
        signup.disabled = false;
      } else {
        signup.disabled = true;
      }
    });
  });