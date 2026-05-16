package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.time.temporal.ChronoUnit;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.WebElement;
import io.appium.java_client.pagefactory.AndroidBy;
import io.appium.java_client.pagefactory.AndroidFindAll;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.WithTimeout;
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class OnboardingPO {

    AppiumDriver driver;

    public OnboardingPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(10)), this);
    }

    @WithTimeout(time = 15, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindBy(xpath = "//*[contains(@text,'Et profitez')]")
    @iOSXCUITFindBy(xpath = "//*[contains(@label,'Et profitez')]")
    private WebElement onBoardingScreenText;

    @WithTimeout(time = 15, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindBy(xpath = "//*[contains(@text,'Hors connexion')]")
    @iOSXCUITFindBy(xpath = "//*[contains(@label,'Hors connexion')]")
    private WebElement onBoardingOfflineScreenText;

    @AndroidFindBy(id = "onboarding_button_1")
    @iOSXCUITFindBy(accessibility = "M'identifier")
    private WebElement buttonLogin;

    @AndroidFindBy(id = "onboarding_button_1")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'RÉESSAYER'")
    private WebElement buttonRetry;

    @AndroidFindBy(id = "onboarding_button_2")
    @iOSXCUITFindBy(accessibility = "DÉCOUVRIR  ")
    private WebElement buttonVisitor;

    @AndroidFindBy(xpath = "//*[contains(@text,'Mes téléchargements')]")
    @iOSXCUITFindBy(xpath = "//*[contains(@label,'Mes vidéos')]")
    private WebElement buttonMyDownloads;

    @AndroidFindBy(id = "onboarding_share_close_image")
    @iOSXCUITFindBy(accessibility = "onboarding_sharing_message_uibutton_1")
    private WebElement buttonstopSharing;


    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/*/android.view.View[1]/android.widget.TextView[1]")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeStaticText)[5]")
    private WebElement discoveryTvOptionTitle;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/*/android.view.View[1]/android.widget.TextView[2]")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeStaticText)[6]")
    private WebElement discoveryTvOptionText;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/*/android.view.View[1]/android.widget.TextView[3]")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeStaticText)[7]")
    private WebElement discoveryTvOptionVendor;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.TextView")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeStaticText)[8]")
    private WebElement discoveryTvOptionSubscribe;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/*/android.view.View[4]/android.widget.Button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "label == \"S'IDENTIFIER\""),
            @iOSXCUITBy(accessibility = "focusable_button"),
            @iOSXCUITBy(accessibility = "ui_uibutton_8")})
    private WebElement buttonIdentify;



    @iOSXCUITFindBy(accessibility = "//uirecents_input_uirecent_input_table_cell")
    private WebElement newAdresse;



}
