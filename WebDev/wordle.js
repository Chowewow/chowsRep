$(window).on("load", () => {
  $('#guess').val('craze');
  $('#btn').click(() => {
    let value = $('#guess').val();
    if (value.length != 5) {
      alert("Enter a 5 letter word");
    } else {
      $('#time').load('https://drtnf.net/wordle_time_left');
      $('#answer').load(`https://drtnf.net/wordle_guess?guess=${value}`);
    }

  });
});
