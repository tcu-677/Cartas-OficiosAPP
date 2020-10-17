(() => {
    const btnSpinner = document.querySelector('#btn-spinner');
    const activeSpinner = document.querySelector('#active-spinner');
    const inputCodigoOficio = document.querySelector('#id_codigo_de_oficio');
    const oficiosTable = $('#oficios-table');


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

    const eventsAndActions = () => {

        if (oficiosTable.length > 0) {

            oficiosTable.DataTable({
                "lengthMenu": [6, 10, 15, 20, 25],
                "order": [[0, "desc"]],
                "language": {
                    "lengthMenu": "Mostrar _MENU_ oficios por página",
                    "search": "Busca un oficio: _INPUT_",
                    "infoEmpty": "No hay oficios disponibles",
                    "zeroRecords": "<p class='my-table-text mt-2'>No hay oficios que coincidan con la búsqueda</p>",
                    "info": "<p class='my-table-text mt-2'>Página _PAGE_ de _PAGES_</p>",
                    "paginate": {
                        "previous": "<i class='fas fa-arrow-left'></i>",
                        "next": "<i class='fas fa-arrow-right'></i>"
                    },
                    "infoFiltered": ""
                },
            });

        }

        if (inputCodigoOficio) {
            inputCodigoOficio.readOnly = true;
        }
        if (activeSpinner) {
            activeSpinner.style.display = 'none';
            btnSpinner.addEventListener('click', () => {
                activeSpinner.style.display = 'inline-block';
            });
        }


    };

    const init = () => {
        identifyPage();
        eventsAndActions();
    };


    init();
    // btn.style.display = 'none'

})();