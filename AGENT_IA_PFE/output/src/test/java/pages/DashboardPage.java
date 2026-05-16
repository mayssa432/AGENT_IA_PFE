
package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class DashboardPage extends BasePage {

    private final By welcomeMessage = By.cssSelector(".welcome-message");
    private final By dashboardContainer = By.id("dashboard");

    public DashboardPage(WebDriver driver) {
        super(driver);
    }

    public boolean isDashboardPageDisplayed() {
        return driver.getCurrentUrl().contains("dashboard");
    }

    public String getWelcomeMessage() {
        return driver.findElement(welcomeMessage).getText();
    }
}
