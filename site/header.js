const masthead = document.querySelector(".paper-masthead");
const compact = document.querySelector(".compact-header");
const compactHeight = compact.getBoundingClientRect().height;

const observer = new IntersectionObserver(([entry]) => {
  compact.classList.toggle("is-visible", entry.boundingClientRect.bottom <= compactHeight);
}, { rootMargin: `-${compactHeight}px 0px 0px` });

observer.observe(masthead);
