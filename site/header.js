const masthead = document.querySelector(".paper-masthead");
const compact = document.querySelector(".compact-header");
const menu = compact.querySelector(".compact-menu");
const menuToggle = menu.querySelector("summary");

const observer = new IntersectionObserver(([entry]) => {
  const mastheadHasScrolledPast = !entry.isIntersecting && entry.boundingClientRect.bottom <= 0;
  compact.classList.toggle("is-visible", mastheadHasScrolledPast);
  if (!mastheadHasScrolledPast) menu.open = false;
});

observer.observe(masthead);

menu.querySelector("nav").addEventListener("click", (event) => {
  if (event.target.closest("a")) menu.open = false;
});

document.addEventListener("click", (event) => {
  if (menu.open && !menu.contains(event.target)) menu.open = false;
});

compact.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && menu.open) {
    menu.open = false;
    menuToggle.focus();
  }
});
