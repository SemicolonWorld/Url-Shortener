const container = document.querySelector(".container");
const toggle = document.querySelector(".modeToggleBox");
toggle.onclick = () => {
  container.classList.toggle("active");
};


