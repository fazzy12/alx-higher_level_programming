$(document).ready(function () {
  $('#toggle_header').click(function () {
    const header = $('header');

    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    } else {
      // Default case, in case header has no class
      header.addClass('red');
    }
  });
});
