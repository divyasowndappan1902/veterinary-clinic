document.addEventListener('DOMContentLoaded', () => {
    // Sticky Header
    const header = document.querySelector('.main-header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
            header.style.padding = '15px 0';
        } else {
            header.style.boxShadow = '0 5px 15px rgba(0,0,0,0.05)';
            header.style.padding = '20px 0';
        }
    });

    // Mobile Menu Toggle (Enhanced)
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (mobileToggle && mainNav) {
        mobileToggle.addEventListener('click', () => {
            mainNav.classList.toggle('active');
            
            // Toggle icon
            const icon = mobileToggle.querySelector('i');
            if (icon) {
                if (mainNav.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-xmark');
                } else {
                    icon.classList.remove('fa-xmark');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }

    // FAQ Accordion
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const body = header.nextElementSibling;
            const isOpen = body.style.display === 'block';
            
            // Close all
            document.querySelectorAll('.accordion-body').forEach(b => b.style.display = 'none');
            
            if (!isOpen) {
                body.style.display = 'block';
            }
        });
    });
});
