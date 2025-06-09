const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto("https://portfoliowebsite-deven.streamlit.app/", {
    waitUntil: "networkidle2",
    timeout: 60000,
  });
  console.log("✅ Streamlit site pinged successfully");
  await browser.close();
})();
