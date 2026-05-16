package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.PointerInput;
import org.openqa.selenium.interactions.Sequence;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.Collections;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class ConsentPO {

    AppiumDriver driver;

    public ConsentPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(10)), this);
    }

    @AndroidFindBy(id = "otb_consent_tv_content")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.consents_ob1.uitext_view_fixed")
    private WebElement consentDescription;

    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Gérer les partenaires'")
    private WebElement consentPolicyTextLinkIOS;

    @AndroidFindBy(id = "otb_consent_tv_custom_content")
    @iOSXCUITFindBy(accessibility = "uilabel")
    private WebElement consentDescription2;


    @iOSXCUITFindBy(xpath = "//XCUIElementTypeTextView[@name=\"orange_trust_badge.consents_uitext_view\"]/XCUIElementTypeTextView")
    private List<WebElement> consentiOSDesCription;

    @AndroidFindBy(id = "otb_consent_bt_accept")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.consents_ob1.obobutton")
    private WebElement consentAcceptButton;

    @AndroidFindBy(id = "otb_consent_tv_decline")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "orange_trust_badge.consents_uibutton_1"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'Continuer sans accepter'")})
    private WebElement consentDeclineButton;

    @AndroidFindBy(xpath = "//android.widget.LinearLayout[@content-desc=\"Personnaliser vos choix\"]/android.widget.TextView")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.consents_ob1.obobutton_1")
    private WebElement consentPersonalizeButton;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'image_toggle_button')])[1]")
    @iOSXCUITFindBy(accessibility = "purposes_bulk_action_root")
    private WebElement acceptAllToggleButton;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'purpose_item_title')])[1]")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeCell[@name='purposes_table_cell_view_0']")
    private WebElement statisticsCell;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'image_toggle_button')])[2]")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'purpose_toggle_0'")
    private WebElement statisticsToggleButton;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'purpose_item_title')])[2]")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeCell[@name='purposes_table_cell_view_1']")
    private WebElement customOrangeExperienceCell;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'image_toggle_button')])[3]")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'purpose_toggle_1'")
    private WebElement customOrangeExperienceToggleButton;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'purpose_item_title')])[3]")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeCell[@name='purposes_table_cell_view_2']")
    private WebElement customAdsCell;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'image_toggle_button')])[4]")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'purpose_toggle_2'")
    private WebElement customAdsToggleButton;

    @AndroidFindBy(xpath = "(//*[contains(@resource-id,'image_toggle_button')])[3]")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"Expérience enrichie par le partage avec des filiales & partenaires\" AND name == \"purpose_toggle_1\"")
    private WebElement orangePartnersExperienceToggleButton;

    @AndroidFindBy(id = "button_purpose_save")
    @iOSXCUITFindBy(accessibility = "didomi_toolbar_save_category_button")
    private WebElement saveCategoryButton;

    @AndroidFindBy(id = "button_purpose_save")
    @iOSXCUITFindBy(accessibility = "didomi_toolbar_save_button")
    private WebElement saveButton;

    public void gdprConsentScreenShown() {

        consentDescription.isDisplayed();
        if (driver instanceof IOSDriver) {
            consentPolicyTextLinkIOS.isDisplayed();
        }
        consentDescription2.isDisplayed();
        consentAcceptButton.isDisplayed();
        consentDeclineButton.isDisplayed();
        consentPersonalizeButton.isDisplayed();
    }

    public void clickConsentLinkAndroid() {
        // Top left corner of the element where the link usually is. HaX after the link was moved as part of the text
        int x = consentDescription.getLocation().x + 10;
        int y = consentDescription.getLocation().y + 80;
        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger");
        Sequence tap = new Sequence(finger, 1);
        tap.addAction(finger.createPointerMove(Duration.ofMillis(0), PointerInput.Origin.viewport(),x, y));
        tap.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        tap.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));
        driver.perform(Collections.singletonList(tap));

    }

    public void clickAcceptButtonIOS() {
        // iOS bottom buttons are invisible for framework
        int x = 188;
        int y = 550;

        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger");
        Sequence tap = new Sequence(finger, 1);
        tap.addAction(finger.createPointerMove(Duration.ofMillis(0), PointerInput.Origin.viewport(),x, y));
        tap.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        tap.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));
        driver.perform(Collections.singletonList(tap));
    }

    public void clickPersonalizeButtonIOS() {
        // iOS bottom buttons are invisible for framework
        int x = 188;
        int y = 613;

        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger");
        Sequence tap = new Sequence(finger, 1);
        tap.addAction(finger.createPointerMove(Duration.ofMillis(0), PointerInput.Origin.viewport(),x, y));
        tap.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        tap.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));
        driver.perform(Collections.singletonList(tap));
    }

}
