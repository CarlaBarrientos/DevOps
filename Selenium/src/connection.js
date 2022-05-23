const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

(async function openChromeTest() {
    try {
        let options = new chrome.Options();
        let driver = await new Builder()
            .setChromeOptions(options)
            .forBrowser('chrome')
            .build();//start session
        await driver.get('https://www.google.com');//navigating to a web page

        driver.manage().setTimeouts({ implicit: 1000 })

        let searchBox = await driver.findElement(By.name('q'));
        let searchButton = await driver.findElement(By.name('btnK'));

        await searchBox.sendKeys('Selenium');
        await searchButton.click();

        driver.manage().setTimeouts({ implicit: 5000 })

        await driver.quit();
    } catch (error) {
        console.log(error)
    }
})();
