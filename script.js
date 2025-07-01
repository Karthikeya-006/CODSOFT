const display = document.querySelector('.display');
const keys = document.querySelectorAll('.keys,.keysop');
let currentInput = '';
keys.forEach(key => {
  key.addEventListener('click', () => {
    const keyValue = key.textContent;

    if (key.classList.contains('c')) {
      currentInput = '';
      display.value= '';
    }
    else if(key.classList.contains(AC))
        {
            display.value = display.value.slice(0, -1);
        } 
    else if (key.classList.contains('=')) {
      try {
        const expression = currentInput.replace(/x/g, '*').replace(/÷/g, '/');
        const result = eval(expression);
        display.value = result;
        currentInput = result.toString();
      } catch {
        display.value = 'Error';
        currentInput = '';
      }
    } else {
      currentInput += keyValue;
      display.value= currentInput;
    }
  });
});
