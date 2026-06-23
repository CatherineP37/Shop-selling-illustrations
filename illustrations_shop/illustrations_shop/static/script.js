const mobileMenu = document.getElementById('mobileMenu');
const opened = document.getElementById('opened');
const closed = document.getElementById('closed');
const filter = document.querySelector('.filter');

function openMobileMenu() {    
    mobileMenu.style.display = "flex";
    mobileMenu.style.flexDirection = "column";
    mobileMenu.style.justifyContent = "center";
    mobileMenu.style.alignItems = "center";    
    closed.style.display = "none";
    opened.style.display = "block";
}

function closeMobileMenu() {
    mobileMenu.style.display = "none";
    closed.style.display = "flex";
    opened.style.display = "none";
}

function toggleFilter() {
    filter.classList.toggle('filter-open');
}