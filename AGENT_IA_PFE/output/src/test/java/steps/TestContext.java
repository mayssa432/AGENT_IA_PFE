package steps;

import java.time.Duration;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import pages.LoginPage;

public class TestContext {
    private WebDriver driver;
    private LoginPage loginPage;

    public TestContext() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");
        this.driver = new ChromeDriver(options);
        this.driver.manage().timeouts()
            .implicitlyWait(Duration.ofSeconds(10));
        this.loginPage = new LoginPage(driver);
    }

    public WebDriver getDriver() {
        return driver;
    }

    public LoginPage getLoginPage() {
        return loginPage;
    }

    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
