"use strict";

function wordleLab(target, value) {
  if (target.length != 5 || value.length != 5) {
    alert("Enter a 5 letter word");
  } else {
    let first = target;
    let second = value;
    let answer = [];

    let track = 0;
    for (let x of first) {
      let track2 = 0;
      for (let y of second) {
        if (x == y && track == track2) {
          answer.push(2);
          break;
        } else if (x == y && track != track2) {
          answer.push(1);
          break;
        }
        if (track2 == 4) {
          answer.push(0);
          break;
        }
        track2 += 1;
      }
      track += 1;
    }
    document.getElementById("demo").innerHTML = answer.toString();

    function getOccurrence(array, value) {
      var count = 0;
      array.split().forEach((v) => v == value && count++ && console.log(v));
      return count;
    }
    console.log(getOccurrence(first,'e'));
    return answer;
  }
}

$(window).on("load", () => {
  document.getElementById("target").value = "trees";
  document.getElementById("guess").value = "craze";
});
