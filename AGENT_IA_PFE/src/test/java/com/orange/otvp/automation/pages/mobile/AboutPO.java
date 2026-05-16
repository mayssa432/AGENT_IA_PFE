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
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class AboutPO {

    AppiumDriver driver;

    public AboutPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(className = "android.view.ViewGroup")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'about_uiview')]")
    private List<WebElement> aboutListElements;

    @AndroidFindBy(className = "android.widget.ImageView")
    @iOSXCUITFindBy(accessibility = "common_orange_logo.png")
    private WebElement orangeLogo;

    @AndroidFindBy(xpath = "//*[@text='Orange TV']")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "help_and_contact_about_uilabel_2"),
            @iOSXCUITBy(accessibility = "help_and_contact_about_uilabel")}) //Ipad
    private WebElement appName;



    @AndroidFindBy(id = "about_legal_mentions_informations_version")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "help_and_contact_about_uilabel_3"),
            @iOSXCUITBy(accessibility = "help_and_contact_about_uilabel_1")}) //Ipad
    private WebElement versionNumber;

    @AndroidFindBy(id = "about_legal_mentions_message")
    @iOSXCUITFindBy(accessibility = "help_and_contact_about_uiview")
    private WebElement aboutText;

    //add PO for accessibility declaration
    @AndroidFindBy(id = "header_title_text")
    @iOSXCUITFindBy(accessibility = "header_title")
    private WebElement headerAccessibility;

    @AndroidFindBy(id = "title")
    private WebElement accessibilityTitle;

    @AndroidFindBy(id = "resultProgressBar" )
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_declaration_accessibility.circular_progress_bar_1")
    private WebElement accessibilityProgressBar;

    @AndroidFindBy(id = "resultDetailTextView")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeStaticText[@name='declaration_accessibility.declaration_uilabel_3'])[1]")
    private WebElement accessibilityResultDetail;

    @AndroidFindBy(id = "dateTitle")
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uilabel_1")
    private WebElement accessibilityDate;

    @AndroidFindBy(id = "dateTextView")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeStaticText[@name='declaration_accessibility.declaration_uilabel_2'])[2]")
    private WebElement accessibilityDateText;

    @AndroidFindBy(id = "declarantTile")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeStaticText[@name='declaration_accessibility.declaration_uilabel_3'])[2]")
    private WebElement accessibilityDeclarant;

    @AndroidFindBy(id = "declarantTextView")
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uilabel_4")
    private WebElement accessibilityDeclarantText;

    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uilabel_5")
    private WebElement accessibilityDeclarantText1;

    @AndroidFindBy(id = "referentialTitle")
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uilabel_6")
    private WebElement accessibilityReferential;

    @AndroidFindBy(id = "referentialTextView")
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uilabel_7")
    private WebElement accessibilityReferentialText;

    @AndroidFindBy(id = "technologieTitle")
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uilabel_8")
    private WebElement accessibilityTechnologie;

    @AndroidFindBy(id = "technologieTextView")
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uilabel_9")
    private WebElement accessibilityTechnologieText;

    @AndroidFindBy(id = "buttonSeeMore")
    @iOSXCUITFindBy(accessibility = "declaration_accessibility.declaration_uibutton_label")
    private WebElement accessibilitySeeMore;

    public void accessAboutElement(int number) {

        int i = 0;
        do {
            i++;
        }
        while (aboutListElements.size() < 4 && i < 2);

        switch (number) {
            case 1:
                if (driver instanceof AndroidDriver) {
                    aboutListElements.get(0).click();
                }
                if (driver instanceof IOSDriver) {
                    aboutListElements.get(1).click();
                }
                break;
            case 2:
                if (driver instanceof AndroidDriver) {
                    aboutListElements.get(1).click();
                }
                if (driver instanceof IOSDriver) {
                    aboutListElements.get(2).click();
                }
                break;
            case 3:
                if (driver instanceof AndroidDriver) {
                    aboutListElements.get(2).click();
                }
                if (driver instanceof IOSDriver) {
                    aboutListElements.get(3).click();
                }
                break;
            default:
        }
    }

    public void legalMentionsShown() {
        orangeLogo.isDisplayed();
        appName.isDisplayed();
        versionNumber.isDisplayed();
        aboutText.isDisplayed();
    }

}
