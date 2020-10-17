(() => {
    const btnSpinner = document.querySelector('#btn-spinner');
    const activeSpinner = document.querySelector('#active-spinner');
    const input_codigo_oficio = document.querySelector('#id_codigo_de_oficio')


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

    const events = () => {
        if (activeSpinner) {
            activeSpinner.style.display = 'none';
            btnSpinner.addEventListener('click', () => {
                activeSpinner.style.display = 'inline-block';
            });
        }


    };

    const init = () => {
        identifyPage();
        events();
    };


    init();
    // btn.style.display = 'none'

})();