// Main JavaScript for Glow Beauty Salon and Spa
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Mobile menu toggle (if needed)
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Contact form submission
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const data = {
                name: formData.get('name'),
                phone: formData.get('phone'),
                email: formData.get('email'),
                message: formData.get('message')
            };

            // Here you would normally send to a server
            // For now, we'll just show an alert
            alert('Thank you for your message! We will get back to you soon.');
            this.reset();
        });
    }

    // Gallery lightbox (simple implementation)
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const img = this.querySelector('img');
            if (img && img.src) {
                // Simple lightbox - can be enhanced
                window.open(img.src, '_blank');
            }
        });
    });

    // Optimized scroll fade-in animation (only observe when needed)
    const observerOptions = {
        threshold: 0.05,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Stop observing after animation
            }
        });
    }, observerOptions);

    // Observe only visible elements initially
    const scrollElements = document.querySelectorAll('.scroll-fade-in');
    scrollElements.forEach((el, index) => {
        // Delay observing to reduce initial load
        setTimeout(() => {
            observer.observe(el);
        }, index * 50);
    });

    // Throttled scroll handler
    let ticking = false;
    function handleScroll() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                // Only essential scroll effects here
                ticking = false;
            });
            ticking = true;
        }
    }
    
    // Use passive scroll listener for better performance
    window.addEventListener('scroll', handleScroll, { passive: true });

    // iPhone-Style Dynamic Island Navbar (Header)
    const islandNav = document.getElementById('dynamic-island-nav');
    const islandToggle = document.getElementById('island-toggle');
    
    if (islandToggle && islandNav) {
        islandToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            islandNav.classList.toggle('active');
            islandToggle.classList.toggle('active');
        });

        // Close on outside click
        document.addEventListener('click', function(e) {
            if (!islandNav.contains(e.target) && islandNav.classList.contains('active')) {
                islandNav.classList.remove('active');
                islandToggle.classList.remove('active');
            }
        });

        // Close on link click
        const islandLinks = islandNav.querySelectorAll('.island-link-header');
        islandLinks.forEach(link => {
            link.addEventListener('click', function() {
                islandNav.classList.remove('active');
                islandToggle.classList.remove('active');
            });
        });
    }

    // Hero Slider
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const indicators = document.querySelectorAll('.indicator');
    const totalSlides = slides.length;
    let autoSlideInterval;

    function showSlide(index) {
        // Remove active class from all slides and indicators
        slides.forEach(slide => slide.classList.remove('active'));
        indicators.forEach(indicator => indicator.classList.remove('active'));

        // Add active class to current slide and indicator
        if (slides[index]) {
            slides[index].classList.add('active');
        }
        if (indicators[index]) {
            indicators[index].classList.add('active');
        }
        
        currentSlide = index;
    }

    function nextSlide() {
        const next = (currentSlide + 1) % totalSlides;
        showSlide(next);
    }

    function prevSlide() {
        const prev = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(prev);
    }

    // Auto-slide functionality
    function startAutoSlide() {
        // Clear any existing interval
        stopAutoSlide();
        // Start new interval - change slide every 5 seconds
        autoSlideInterval = setInterval(nextSlide, 5000);
    }

    function stopAutoSlide() {
        if (autoSlideInterval) {
            clearInterval(autoSlideInterval);
            autoSlideInterval = null;
        }
    }

    // Slider controls
    const prevBtn = document.querySelector('.slider-prev');
    const nextBtn = document.querySelector('.slider-next');

    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            prevSlide();
            stopAutoSlide();
            startAutoSlide(); // Restart auto-slide after manual navigation
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            nextSlide();
            stopAutoSlide();
            startAutoSlide(); // Restart auto-slide after manual navigation
        });
    }

    // Indicator clicks
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', function() {
            showSlide(index);
            stopAutoSlide();
            startAutoSlide(); // Restart auto-slide after manual navigation
        });
    });

    // Pause auto-slide on hover, resume on mouse leave
    const heroSlider = document.querySelector('.hero-slider');
    if (heroSlider) {
        heroSlider.addEventListener('mouseenter', stopAutoSlide);
        heroSlider.addEventListener('mouseleave', startAutoSlide);
    }

    // Start auto-slide when page loads
    if (totalSlides > 0) {
        startAutoSlide();
    }

    // Update icons only when needed (no MutationObserver for better performance)
    if (typeof lucide !== 'undefined' && islandToggle) {
        islandToggle.addEventListener('click', function() {
            setTimeout(() => {
                lucide.createIcons();
            }, 100);
        });
    }
});

