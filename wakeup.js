const puppeteer = require("puppeteer");

(async () => {
  try {
    const browser = await puppeteer.launch({
      headless: true,
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });

    const page = await browser.newPage();
    await page.goto("https://portfoliowebsite-deven.streamlit.app/", {
      waitUntil: "networkidle2",
      timeout: 60000,
    });

    console.log("✅ Successfully pinged your Streamlit site!");
    await browser.close();
  } catch (error) {
    console.error("❌ Ping failed:", error);
    process.exit(1);
  }
})();
