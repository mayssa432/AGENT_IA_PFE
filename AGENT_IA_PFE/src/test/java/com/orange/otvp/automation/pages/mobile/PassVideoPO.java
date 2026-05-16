package com.orange.otvp.automation.pages.mobile;


import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.WebElement;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class PassVideoPO {

    AppiumDriver driver;
    @AndroidFindBy(id = "svod_info_subscription")
    @iOSXCUITFindBy(accessibility = "pass_video_page_custom_uilabel")
    private WebElement svodInfoSubscription;
    @AndroidFindBy(id = "svod_logo")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'partner_application_uiview')]/XCUIElementTypeImage[1]")
    private List<WebElement> svodLogo;
    @AndroidFindBy(id = "svod_partner_title")
    @iOSXCUITFindBy(accessibility = "partner_application_custom_uilabel_2")
    private List<WebElement> svodPartnerTitle;
    @iOSXCUITFindBy(accessibility = "partner_application_custom_uilabel_1")
    private List<WebElement> svodPartnerTitleIpad;
    @AndroidFindBy(id = "expandable_text_view")
    @iOSXCUITFindBy(accessibility = "partner_application_custom_uilabel_1")
    private List<WebElement> svodPartnerSubTitle;
    @iOSXCUITFindBy(accessibility = "partner_application_custom_uilabel")
    private List<WebElement> svodPartnerSubTitleIpad;

    @AndroidFindBy(id = "svod_partner_discover_button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "partner_application_custom_uibutton_4"),
            @iOSXCUITBy(accessibility = "partner_application_custom_uibutton_2") //Tablet
    })
    private List<WebElement> svodPartnerDiscoverButton;
    @AndroidFindBy(id = "svod_partner_offer_button")
    private List<WebElement> svodPartnerOfferButton;

    public PassVideoPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(10)), this);
    }


}
