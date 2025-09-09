// Hamburger Toggle
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("nav-links");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
  hamburger.classList.toggle("open");
});

// Parallax Effect for Background Pyramid
const pyramid = document.querySelector(".background-pyramid");
window.addEventListener("scroll", () => {
  let offset = window.scrollY;
  pyramid.style.transform = `translate(-50%, calc(-50% + ${offset * 0.2}px)) scale(1.05)`;
});
