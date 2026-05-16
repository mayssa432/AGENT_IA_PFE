package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class SettingsPO {

    AppiumDriver driver;

    public SettingsPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "settings_spinner")
    private List<WebElement> buttonsElementsAndroid;

    @AndroidFindBy(id = "spinner_dropdown_item")
    private List<WebElement> dropDownItemsAndroid;

    @iOSXCUITFindBy(className = "XCUIElementTypePickerWheel")
    private WebElement pickerWheelElement;

    @iOSXCUITFindBy(iOSNsPredicate = "label == 'VALIDER'")
    private WebElement validateButtonIOS;

    @AndroidFindBy(id = "settings_vod_download_in_mobile_network_switch")
    @iOSXCUITFindBy(accessibility = "mysettings_view_acuiswitch_2")
    private WebElement mobilePermissionSwitch;

    // the text of mobile permission and video playback
    @AndroidFindBy(xpath = "//android.widget.LinearLayout/android.widget.TextView[2]")
    private List<WebElement> mySettingsSubTextAnd;

    @iOSXCUITFindBy(accessibility = "mysettings_view_uibutton_4")
    private WebElement mySettingsButtonsIOS;

    @iOSXCUITFindBy(accessibility = "mysettings_view_uibutton_6")
    private WebElement mySettingsStreamingQualityIOS;

    @AndroidFindBy(id = "spinner_view_collapsed")
    @iOSXCUITFindBy(accessibility = "mysettings_view_uilabel_2")
    private List<WebElement> mySettingsSubTexts;

    @iOSXCUITFindBy(accessibility = "mysettings_view_uilabel_1")
    private List<WebElement> mySettingSubTextiOS;

    @AndroidFindBy(id = "settings_item_description_text")
    private WebElement mySettingCarbonImpactSubTestsAnd;

    @AndroidFindBy(id = "settings_force_widevine_level_switch")
    private WebElement videoPlaybackSwitch;

    public WebElement getReminderSettingButton() {
        WebElement element = null;
        if (driver instanceof AndroidDriver) {
            element = buttonsElementsAndroid.get(0);
        }
        if (driver instanceof IOSDriver) {
            element = mySettingsButtonsIOS;
        }
        return element;
    }

    public String getReminderSubText() {
        WebElement element = null;
        if (driver instanceof AndroidDriver) {
            element = mySettingsSubTexts.get(0);
        }
        if (driver instanceof IOSDriver) {
            element = mySettingSubTextiOS.get(0);
        }
        return element.getText();
    }

    public WebElement getStreamQualitySettingButton() {
        WebElement element = null;
        if (driver instanceof AndroidDriver) {
            element = buttonsElementsAndroid.get(1);
        }
        if (driver instanceof IOSDriver) {
            element = mySettingsStreamingQualityIOS;
        }
        return element;
    }

    public String getStreamQualitySubText() {
        String element = null;
        if (driver instanceof AndroidDriver) {
            element = mySettingsSubTexts.get(1).getText();
        }
        if (driver instanceof IOSDriver) {
            element = mySettingsSubTexts.get(0).getText();
        }
        return element;

    }

    public String getStreamQualityCarbonImpactSubText() {
        String element = null;
        if (driver instanceof AndroidDriver) {
            element = mySettingCarbonImpactSubTestsAnd.getText();
        }
        if (driver instanceof IOSDriver) {
            element = mySettingSubTextiOS.get(3).getText();
        }
        return element;

    }

    public boolean checkMobilePermissionSwitch() {
        boolean checked = false;
        if (driver instanceof AndroidDriver) {
            checked = mobilePermissionSwitch.getAttribute("checked").equalsIgnoreCase("true");
        }
        if (driver instanceof IOSDriver) {
            // element boolean value is returned as 0,1
            checked = mobilePermissionSwitch.getAttribute("value").equalsIgnoreCase("1");
        }
        return checked;
    }

    public String getMobilePermissionSubText() {
        String element = null;
        if (driver instanceof AndroidDriver) {
            element = mySettingsSubTextAnd.get(0).getText();
        }
        if (driver instanceof IOSDriver) {
            element = mySettingSubTextiOS.get(2).getText();
        }
        return element;

    }

    public WebElement getDownloadStorage() {
        WebElement element = null;
        //toAdd SD
        if (driver instanceof AndroidDriver) {
            element = buttonsElementsAndroid.get(2);
        }
        return element;
    }

    public String getDownloadStorageSubText() {
        String element = null;
        if (driver instanceof AndroidDriver) {
            element = mySettingsSubTexts.get(2).getText();
        }
        return element;

    }

    //check the toggle "video playback" on android
    public boolean checkVideoPlaybackSwitch() {
        boolean checked = false;
        if (driver instanceof AndroidDriver) {
            checked = videoPlaybackSwitch.getAttribute("checked").equalsIgnoreCase("true");
        }
        return checked;
    }



}
