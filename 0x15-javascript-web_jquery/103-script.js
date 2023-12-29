$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();

    // Fetch the translation from the API
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // Fetch translation when the button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation when ENTER is pressed on the language code input
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the ENTER key code
      fetchTranslation();
    }
  });
});
