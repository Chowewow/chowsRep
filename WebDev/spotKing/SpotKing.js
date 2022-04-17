
//country.setAttribute("Australia",true);

const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    await page.goto('https://www.kingupgrader.cc/renew.html');

    document.getElementById("renewKey").value = "78de7b2b-d478-4a85-aa52-7b32cbca9c32"; 
    document.getElementById("password").value = "K47jv4tZSKFxa4"; 
    await browser.waitForTarget(() => false);
    await browser.close();
});