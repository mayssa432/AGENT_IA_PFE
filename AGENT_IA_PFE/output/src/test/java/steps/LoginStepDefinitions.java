package steps;

import org.junit.Assert;

import io.cucumber.java.After;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import pages.LoginPage;

public class LoginStepDefinitions {
    private final TestContext context;
    private final LoginPage loginPage;

    public LoginStepDefinitions(TestContext context) {
        this.context = context;
        this.loginPage = context.getLoginPage();
    }

    @After
    public void tearDown() {
        context.tearDown();
    }

    @Given("I am on the login page")
    public void iAmOnTheLoginPage() {
        loginPage.openLoginPage();
    }

    @When("I enter username {string}")
    public void iEnterUsername(String username) {
        loginPage.enterUsername(username);
    }

    @And("I enter password {string}")
    public void iEnterPassword(String password) {
        loginPage.enterPassword(password);
    }

    @And("I click the login button")
    public void iClickTheLoginButton() {
        loginPage.clickLoginButton();
    }

    @Then("I should be redirected to the dashboard")
    public void iShouldBeRedirectedToTheDashboard() {
        Assert.assertTrue(loginPage.isDashboardPage());
    }

    @And("I should see the welcome message {string}")
    public void iShouldSeeTheWelcomeMessage(String message) {
        Assert.assertEquals(message, loginPage.getWelcomeMessage());
    }

    @Then("I should see an error message {string}")
    public void iShouldSeeAnErrorMessage(String message) {
        Assert.assertEquals(message, loginPage.getErrorMessage());
    }

    @And("I should remain on the login page")
    public void iShouldRemainOnTheLoginPage() {
        Assert.assertTrue(loginPage.isLoginPage());
    }
}
