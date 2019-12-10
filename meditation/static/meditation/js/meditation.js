function toggleInstructions() {
    var x = document.getElementById("instructions");
    if (x.style.visibility === "hidden") {
      x.style.visibility = "visible";
      document.querySelector('#btnToggle').textContent = 'Hide Instructions';
    } else {
      x.style.visibility = "hidden";
      document.querySelector('#btnToggle').textContent = 'Show Instructions';
    }
  } 