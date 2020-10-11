(() => {

    const identifyPage = () => {
        const pageURL = (document.querySelector('#url_page')) ? document.querySelector('#url_page').value : '';
        const navbarsList = document.querySelectorAll('#navbar');


        for (const navbar of navbarsList) {
            const navLinks = navbar.querySelectorAll('.nav-link');
            for (const navLink of navLinks) {
                if (navLink.id == pageURL) {
                    navLink.classList.add('active-link');
                }
                else {
                    navLink.classList.remove('active-link');
                }
            }
        }
    };

    const init = () => {
        identifyPage();
    };


    init();


})();