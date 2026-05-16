package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class RemoteControlPO {

    AppiumDriver driver;

    public RemoteControlPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "header_remote_icon")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'TÉLÉCOMMANDE'")
    private WebElement remoteButton;

    @AndroidFindBy(id = "remote_back_button")
    @iOSXCUITFindBy(accessibility = "remote_back_button")
    private WebElement backButton;

    @AndroidFindBy(id = "remote_device_dropdown")
    @iOSXCUITFindBy(accessibility = "drop_down_list_button")
    private WebElement selectSTBdropdown;

    @AndroidFindBy(id = "remote_power_button")
    @iOSXCUITFindBy(accessibility = "remote_power_button")
    private WebElement powerButton;

    @AndroidFindBy(id = "remote_up_button")
    @iOSXCUITFindBy(accessibility = "remote_up_button")
    private WebElement upButton;

    @AndroidFindBy(id = "remote_down_button")
    @iOSXCUITFindBy(accessibility = "remote_down_button")
    private WebElement downButton;

    @AndroidFindBy(id = "remote_left_button")
    @iOSXCUITFindBy(accessibility = "remote_left_button")
    private WebElement leftButton;

    @AndroidFindBy(id = "remote_right_button")
    @iOSXCUITFindBy(accessibility = "remote_right_button")
    private WebElement rightButton;

    @AndroidFindBy(id = "remote_ok_button")
    @iOSXCUITFindBy(accessibility = "remote_ok_button")
    private WebElement okButton;

    @AndroidFindBy(id = "remote_undo_button")
    @iOSXCUITFindBy(accessibility = "remote_undo_button")
    private WebElement revertButton;

    @AndroidFindBy(id = "remote_menu_button")
    @iOSXCUITFindBy(accessibility = "remote_menu_button")
    private WebElement menuButton;

    @AndroidFindBy(className = "android.widget.ListView")
    @iOSXCUITFindBy(accessibility = "remote_control_page_uitable_view")
    private WebElement drobdownSTBlist;

    @AndroidFindBy(id = "remote_djingo_button")
    @iOSXCUITFindBy(accessibility = "remote_djingo_button")
    private WebElement djingoButton;

    @AndroidFindBy(id = "remote_stop_button")
    @iOSXCUITFindBy(accessibility = "remote_stop_button")
    private WebElement stopButton;

    @AndroidFindBy(id = "remote_rec_button")
    @iOSXCUITFindBy(accessibility = "remote_rec_button")
    private WebElement recButton;

    @AndroidFindBy(id = "remote_rewind_button")
    @iOSXCUITFindBy(accessibility = "remote_rewind_button")
    private WebElement rewindButton;

    @AndroidFindBy(id = "remote_play_pause_button")
    @iOSXCUITFindBy(accessibility = "remote_play_pause_button")
    private WebElement playPauseButton;

    @AndroidFindBy(id = "remote_forward_button")
    @iOSXCUITFindBy(accessibility = "remote_forward_button")
    private WebElement forwardButton;

    @AndroidFindBy(id = "remote_channel_up_button")
    @iOSXCUITFindBy(accessibility = "remote_channel_up_button")
    private WebElement channelUpButton;

    @AndroidFindBy(id = "remote_channel_down_button")
    @iOSXCUITFindBy(accessibility = "remote_channel_down_button")
    private WebElement channelDownButton;

    @AndroidFindBy(id = "remote_vol_up_button")
    @iOSXCUITFindBy(accessibility = "remote_vol_up_button")
    private WebElement volumeUpButton;

    @AndroidFindBy(id = "remote_vol_down_button")
    @iOSXCUITFindBy(accessibility = "remote_vol_down_button")
    private WebElement volumeDownButton;

    @AndroidFindBy(id = "remote_mute_button")
    @iOSXCUITFindBy(accessibility = "remote_mute_button")
    private WebElement muteButton;

    @AndroidFindBy(id = "remote_number_0_button")
    @iOSXCUITFindBy(accessibility = "remote_number_0_button")
    private WebElement zeroButton;

    @AndroidFindBy(id = "remote_number_1_button")
    @iOSXCUITFindBy(accessibility = "remote_number_1_button")
    private WebElement oneButton;

    @AndroidFindBy(id = "remote_number_2_button")
    @iOSXCUITFindBy(accessibility = "remote_number_2_button")
    private WebElement twoButton;

    @AndroidFindBy(id = "remote_number_3_button")
    @iOSXCUITFindBy(accessibility = "remote_number_3_button")
    private WebElement threeButton;

    @AndroidFindBy(id = "remote_number_4_button")
    @iOSXCUITFindBy(accessibility = "remote_number_4_button")
    private WebElement fourButton;

    @AndroidFindBy(id = "remote_number_5_button")
    @iOSXCUITFindBy(accessibility = "remote_number_5_button")
    private WebElement fiveButton;

    @AndroidFindBy(id = "remote_number_6_button")
    @iOSXCUITFindBy(accessibility = "remote_number_6_button")
    private WebElement sixButton;

    @AndroidFindBy(id = "remote_number_7_button")
    @iOSXCUITFindBy(accessibility = "remote_number_7_button")
    private WebElement sevenButton;

    @AndroidFindBy(id = "remote_number_8_button")
    @iOSXCUITFindBy(accessibility = "remote_number_8_button")
    private WebElement eightButton;

    @AndroidFindBy(id = "remote_number_9_button")
    @iOSXCUITFindBy(accessibility = "remote_number_9_button")
    private WebElement nineButton;

    public void remoteShown() {
        backButton.isDisplayed();
        selectSTBdropdown.isDisplayed();
        powerButton.isDisplayed();
        upButton.isDisplayed();
        downButton.isDisplayed();
        leftButton.isDisplayed();
        rightButton.isDisplayed();
        okButton.isDisplayed();
        revertButton.isDisplayed();
        menuButton.isDisplayed();
    }

    public Boolean stbDetected(String stbName) {
        Boolean isFound = null;

        if (driver instanceof AndroidDriver) {
            isFound = drobdownSTBlist.findElement(AppiumBy.xpath("//*[@text='" + stbName + "']")).isDisplayed();
        }
        if (driver instanceof IOSDriver) {
            isFound = drobdownSTBlist.findElement(AppiumBy.xpath("//*[@label='" + stbName + "']")).isDisplayed();
        }
        return isFound;
    }

}
