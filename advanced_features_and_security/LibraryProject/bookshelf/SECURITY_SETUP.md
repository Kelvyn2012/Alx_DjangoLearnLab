# HTTPS and Security Configuration for Alx_DjangoLearnLab

## Django Settings
- Enforced HTTPS with `SECURE_SSL_REDIRECT = True`
- Enabled HSTS for 1 year with preload and subdomain support
- Secured cookies via `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`
- Added browser-level headers to prevent clickjacking and XSS

## Nginx HTTPS Setup
- Configured redirection from HTTP to HTTPS
- Integrated Let's Encrypt SSL certificates
- Applied best-practice TLS parameters and security headers

## Review Notes
- All HTTP traffic is now redirected to HTTPS
- Cookies are encrypted and protected from MITM
- Web app now denies iframe embedding and MIME sniffing
- Production `DEBUG` is disabled to prevent sensitive info leak

## Recommendations
- Monitor certificate expiry using Certbot auto-renew
- Regularly audit security headers via tools like [securityheaders.com](https://securityheaders.com)
- Review app code for secure form handling, CSRF protection, and SQL injection risks
