# Implementation Plan: SEO & Functionality Audit

## Goal Description
Perform a comprehensive SEO and functionality sweep across the entire Kitchen Hub project to ensure all pages meet best practices for search engine indexing and social sharing.

## Proposed Changes

### [MODIFY] `*.html`
- **Open Graph (OG) Tags**: Append `<meta property="og:title">`, `og:description`, `og:image`, and `og:url` across all 7 HTML files to ensure rich previews on social media (LinkedIn, WhatsApp, etc.).
- **Missing Meta Descriptions**: Add descriptive `<meta name="description">` tags to `terminos-y-condiciones.html`, `politica-de-privacidad.html`, and `publica-tu-cocina.html`.

### [MODIFY] `sitemap.xml`
- **Missing Pages**: Add the newly launched `/dark-kitchen-santiago.html` and `/publica-tu-cocina.html` to the sitemap tree to ensure Google indexes them immediately. Update the `lastmod` dates for other files explicitly.

### [NEW/MODIFY] `robots.txt`
- **Robots.txt**: Add a `robots.txt` file at the root to explicitly define `Allow: /` and point crawlers to the absolute URL of the sitemap.

## Verification Plan
### Local Verification
- Check the source code of the updated HTML files to ensure no duplicate `<title>` or `<meta>` tags were created during insertion.
- Validate `sitemap.xml` XML structure manually.
- Deploy the changes via Git so Vercel can reflect them in production.
