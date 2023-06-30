/* Make an interactable dice roll generator */
var diceRoll = document.createElement('div');
diceRoll.innerHTML = '<input type="text" id="diceRollInput" value="1d6" /> <button id="diceRollButton">Roll</button> <span id="diceRollResult"></span>';
document.body.appendChild(diceRoll);
var diceRollInput = document.getElementById('diceRollInput');
var diceRollButton = document.getElementById('diceRollButton');
var diceRollResult = document.getElementById('diceRollResult');
diceRollButton.onclick = function() {
  var diceRollInputValue = diceRollInput.value;
  var diceRollInputValueSplit = diceRollInputValue.split('d');
  var diceRollInputValueSplit0 = parseInt(diceRollInputValueSplit[0]);
  var diceRollInputValueSplit1 = parseInt(diceRollInputValueSplit[1]);
  var diceRollResultValue = 0;
  for (var i = 0; i < diceRollInputValueSplit0; i++) {
    diceRollResultValue += Math.floor(Math.random() * diceRollInputValueSplit1) + 1;
  }
  diceRollResult.innerHTML = diceRollResultValue;
};
/* Make it so the higher the roll, the larger the font of the text that displays the result */
diceRollResult.style.fontSize = '1em';
diceRollButton.onclick = function() {
  var diceRollInputValue = diceRollInput.value;
  var diceRollInputValueSplit = diceRollInputValue.split('d');
  var diceRollInputValueSplit0 = parseInt(diceRollInputValueSplit[0]);
  var diceRollInputValueSplit1 = parseInt(diceRollInputValueSplit[1]);
  var diceRollResultValue = 0;
  for (var i = 0; i < diceRollInputValueSplit0; i++) {
    diceRollResultValue += Math.floor(Math.random() * diceRollInputValueSplit1) + 1;
  }
  diceRollResult.innerHTML = diceRollResultValue;
  diceRollResult.style.fontSize = diceRollResultValue + 'em';
};
diceRollResult.style.fontSize = '1em';
diceRollButton.onclick = function() {
  var diceRollInputValue = diceRollInput.value;
  var diceRollInputValueSplit = diceRollInputValue.split('d');
  var diceRollInputValueSplit0 = parseInt(diceRollInputValueSplit[0]);
  var diceRollInputValueSplit1 = parseInt(diceRollInputValueSplit[1]);
  var diceRollResultValue = 0;
  for (var i = 0; i < diceRollInputValueSplit0; i++) {
    diceRollResultValue += Math.floor(Math.random() * diceRollInputValueSplit1) + 1;
  }
  diceRollResult.innerHTML = diceRollResultValue;
  diceRollResult.style.fontSize = diceRollResultValue + 'em';
  diceRollResult.style.position = 'static'; // Change position to static
};
