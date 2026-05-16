import org.junit.runner.RunWith;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;

@RunWith(Cucumber.class)
@CucumberOptions(
    plugin = {
        "pretty",
        "json:target/cucumber-reports/cucumber.json",
        "html:target/cucumber-reports/report.html"
    },
    features = "src/test/resources/features/LoginFunctionality.feature",
    glue = "steps"
)
public class LoginTestRunner {
   // Runner propre - WebDriver gere dans TestContext

}
