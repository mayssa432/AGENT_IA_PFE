package com.orange.otvp.automation.runners;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
    features = "src/test/resources/features/RemoteControl.feature",
    glue = "com.orange.otvp.automation.steps",
    plugin = {
        "pretty",
        "html:target/cucumber-reports/RemoteControl-report.html",
        "json:target/cucumber-reports/RemoteControl-report.json"
    },
    monochrome = true
)
public class RemoteControlRunner {
}
