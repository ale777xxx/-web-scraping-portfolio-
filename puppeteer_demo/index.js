import puppeteer from 'puppeteer-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';

puppeteer.use(StealthPlugin());

const PROXY = process.env.HTTP_PROXY || process.env.HTTPS_PROXY; // e.g. http://user:pass@host:port

(async () => {
  const launchArgs = ['--no-sandbox', '--disable-setuid-sandbox'];
  if (PROXY) launchArgs.push(`--proxy-server=${PROXY}`);

  const browser = await puppeteer.launch({
    headless: 'new',
    args: launchArgs
  });
  const page = await browser.newPage();

  await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome Safari');
  await page.goto('https://httpbin.org/ip', { waitUntil: 'domcontentloaded', timeout: 60000 });

  const content = await page.content();
  console.log(content);
  await browser.close();
})().catch(err => {
  console.error(err);
  process.exit(1);
});
