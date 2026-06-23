document.addEventListener('DOMContentLoaded', function() {
    const burgerBtn = document.getElementById('burger-btn');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav a');

    if (burgerBtn && navMenu) {

        //  Открытие/Закрытие по клику на саму кнопку бургера
        burgerBtn.addEventListener('click', () => {
            burgerBtn.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.classList.toggle('no-scroll');
        });

        //  Закрытие при клике на ссылку
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                burgerBtn.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('no-scroll');
            });
        });

        console.log("Бургер-меню инициализировано успешно!");
    } else {
        console.error("Ошибка: Не найдены ID 'burger-btn' или 'nav-menu'. Проверь HTML!");
    }
});