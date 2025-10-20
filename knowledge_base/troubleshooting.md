# Troubleshooting Cheatsheet

- **403 / 429**: rotate proxies, reduce concurrency, add delays, randomize headers.
- **CAPTCHA**: try different pools, headless detection mitigation, human-in-the-loop vendors.
- **Selenium NoSuchElement**: add explicit waits, ensure correct iframe/window, stabilize selectors.
- **Render differences**: prefer `wait.until(EC.presence_of_element_located(...))` over fixed sleeps.
- **Parsing**: sanitize whitespace, fallback selectors, defensive defaults (`.get(default='')`).
