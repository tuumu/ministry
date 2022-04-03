
const mobileBtn = document.getElementById('mobile-menu');
const nav = document.querySelector('nav');
const mobileExit = document.getElementById('mobile-exit');

mobileBtn.addEventListener('click', () => {
    nav.classList.add('active');

})
mobileExit.addEventListener('click', () => {
    nav.classList.remove('active');

})

