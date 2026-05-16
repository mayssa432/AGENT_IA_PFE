package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.WebElement;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class AccountPO {

    AppiumDriver driver;

    public AccountPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "identity_login_button")
    @iOSXCUITFindBy(accessibility = "myaccount_view_custom_uibutton")
    private WebElement identifyButton;

    @AndroidFindBy(id = "settings_reset_application_button")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'SE DÉCONNECTER'")
    private WebElement disconnectAccountButton;

    @AndroidFindBy(id = "details_secondary_layout")
    @iOSXCUITFindBy(accessibility = "myaccount_view_uiview_3")
    private WebElement serviceDetailsElement;

    @AndroidFindBy(id = "identity_title_text")
    private WebElement identityTitleTextAndroid;

    @AndroidFindBy(id = "identity_login_text")
    private WebElement identityLoginTextAndroid;

    @AndroidFindBy(id = "details_title_text")
    @iOSXCUITFindBy(accessibility = "myaccount_view_uilabel")
    private WebElement offerTitleText;

    @AndroidFindBy(id = "details_error_text")
    private WebElement offerErrorTextAndroid;

    @AndroidFindBy(id = "details_title_text")
    private WebElement detailsTitleTextAndroid;

    @AndroidFindBy(id = "details_primary_text")
    private WebElement detailsPrimaryText;

    @AndroidFindBy(id = "details_secondary_text")
    private WebElement detailsSecondaryText;

    @AndroidFindBy(id = "details_includes_text")
    private WebElement detailsIncludesText;

    @AndroidFindBy(id = "details_offers_text")
    private WebElement detailsOffersText;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'myaccount_view_uilabel')]")
    private List<WebElement> myAccountUiLabelIOS;

    @AndroidFindBy(id = "details_subscription_text")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Gérer mes abonnements TV'")
    private WebElement myAccountSubsButton;

    public String getIdentificationText() {
        String text = null;

        if (driver instanceof AndroidDriver) {
            text = identityLoginTextAndroid.getText();
        }
        if (driver instanceof IOSDriver) {
            text = myAccountUiLabelIOS.get(1).getText();
        }
        return text;
    }

}
