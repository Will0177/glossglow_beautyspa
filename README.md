# Glow Beauty Salon & Spa - Website

A complete, modern multi-page website for Glow Beauty Salon & Spa featuring elegant design, comprehensive services, and interactive features.

## Website Structure

### Pages
- **index.html** - Home page with hero section, services overview, testimonials, and 8-second video section
- **about.html** - About us page with company story, values, and team information
- **services.html** - Detailed services page with all treatments and services offered
- **portfolio.html** - Portfolio/gallery page showcasing work results with filtering
- **contact.html** - Contact page with contact form and business information

## Features

### ✅ Mandatory Features Implemented

1. **8-Second Video Section**
   - Located on the home page
   - Section titled "Watch Our 8-Second Story"
   - Video placeholder ready for `assets/videos/8-second-story.mp4`
   - See `VIDEO_SCRIPT.md` for complete script

2. **Live Chat Widget**
   - Interactive chat widget on all pages
   - Automated bot messages:
     - "Hello! 👋 How can we help you today?"
     - "Are you interested in our services?"
     - "We'll reply in under 2 minutes."
     - "Would you like a free consultation?"
   - Fixed position button in bottom-right corner
   - Fully functional chat interface

3. **Contact Form**
   - Fields: Full Name, Phone Number, Email, Message
   - Form validation
   - Submissions configured for: hello@crownect.com
   - Located on contact.html page

## Design

- **Color Scheme:** Elegant neutrals with accent color #BCAAA4 (soft taupe)
- **Typography:** Cormorant Garamond (serif) for headings, Inter (sans-serif) for body
- **Style:** Modern, elegant, professional beauty salon aesthetic
- **Responsive:** Fully responsive design for all device sizes

## File Structure

```
/
├── index.html
├── about.html
├── services.html
├── portfolio.html
├── contact.html
├── css/
│   └── style.css
├── js/
│   ├── main.js
│   └── chat.js
├── assets/
│   ├── images/
│   │   └── (see REQUIRED_ASSETS.md for complete list)
│   └── videos/
│       └── 8-second-story.mp4 (to be added)
├── VIDEO_SCRIPT.md
├── RESEARCH_SUMMARY.md
├── LOGO_PROMPT.md
├── REQUIRED_ASSETS.md
└── README.md
```

## Setup Instructions

1. **Add Images:**
   - Place all images in `assets/images/` folder
   - See `REQUIRED_ASSETS.md` for complete list and naming conventions

2. **Add Video:**
   - Place 8-second video in `assets/videos/8-second-story.mp4`
   - Uncomment video tag in index.html when ready
   - See `VIDEO_SCRIPT.md` for script details

3. **Update Contact Information:**
   - Update phone numbers, addresses, and email addresses throughout all pages
   - Update contact form action if using a different email service

4. **Add Logo:**
   - Place logo files in `assets/images/` or root directory
   - Update logo references in HTML files
   - See `LOGO_PROMPT.md` for logo design specifications

5. **Configure Contact Form:**
   - Update form action in contact.html
   - Set up backend form handling if needed
   - Currently configured for mailto:hello@crownect.com

## Technologies Used

- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework (via CDN)
- **Lucide Icons** - Modern icon library
- **Vanilla JavaScript** - No frameworks, pure JS
- **Google Fonts** - Cormorant Garamond & Inter

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile responsive
- Progressive enhancement

## Customization

### Colors
Main color scheme can be customized in:
- Tailwind classes throughout HTML
- CSS custom properties in `css/style.css`

### Content
- All content is easily editable in HTML files
- Services, testimonials, and team info can be updated directly

### Features
- Live chat can be connected to a real chat service
- Contact form can be integrated with form handling services
- Video section can be enhanced with custom video player

## Documentation Files

- **VIDEO_SCRIPT.md** - Complete 8-second video script and production notes
- **RESEARCH_SUMMARY.md** - Business research findings and information
- **LOGO_PROMPT.md** - Logo design specifications and requirements
- **REQUIRED_ASSETS.md** - Complete list of all images and videos needed

## Next Steps

1. Add all required images (see REQUIRED_ASSETS.md)
2. Create and add 8-second promotional video
3. Design and add logo files
4. Update all contact information with actual business details
5. Set up form handling for contact form
6. Connect live chat to actual chat service (optional)
7. Add Google Maps embed to contact page
8. Test all functionality across devices
9. Optimize images for web
10. Set up hosting and domain

## Notes

- All images currently have placeholder fallbacks to Unsplash
- Contact information uses placeholder values - update before launch
- Social media links are placeholders - update with actual accounts
- Form submission currently uses mailto - set up proper backend for production

## Support

For questions or customization needs, refer to the documentation files or update the HTML/CSS/JS files directly.

---

**Built for Glow Beauty Salon & Spa**
*Where beauty meets wellness*

# glossglow_beautyspa
# glossglow_beautyspa
