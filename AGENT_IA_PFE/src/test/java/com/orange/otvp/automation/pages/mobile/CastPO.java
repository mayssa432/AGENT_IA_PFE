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
public class CastPO {

    AppiumDriver driver;

    public CastPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(10)), this);
    }

    @AndroidFindBy(id = "device_item_name")
    @iOSXCUITFindBy(accessibility = "list_of_stbs_pop_up_uitable_view_label")
    private List<WebElement> devicesList;

    @AndroidFindBy(id = "mr_chooser_route_name")
    private WebElement chromeCastAndroid;

    @AndroidFindBy(id = "android:id/button1")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == 'Se déconnecter'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'SE DÉCONNECTER'")})
    private WebElement disconnectChromeCastButton;

    @AndroidFindBy(id = "custom_dialog_button_secondary_negative")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == 'Se déconnecter'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'SE DÉCONNECTER'")})
    private WebElement disconnectSTBButton;

    @AndroidFindBy(id = "cast_control_primaryTitle")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "controller_uilabel_5"),
            @iOSXCUITBy(accessibility = "controller_uilabel")})
    private WebElement mediaTitle;

    @AndroidFindBy(id = "cast_control_collapse_expand")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Réduire'")
    private WebElement collapseButton;

    @AndroidFindBy(id = "cast_control_collapse_expand")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Agrandir'")
    private WebElement expandButton;

    @AndroidFindBy(id = "cast_control_device_title")
    @iOSXCUITFindBy(accessibility = "controller_uilabel")
    private WebElement deviceTitle;

    @AndroidFindBy(id = "cast_control_media_cover")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeOther[@name='controller_uiview_4']/XCUIElementTypeImage")
    private WebElement mediaCover;

    @AndroidFindBy(id = "cast_control_channel_logo")
    @iOSXCUITFindBy(accessibility = "controller_channel_logo_4")
    private WebElement channelLogo;

    @AndroidFindBy(id = "cast_control_time_1")
    @iOSXCUITFindBy(accessibility = "controller_uilabel_8")
    private WebElement startTime;

    @AndroidFindBy(id = "cast_control_time_1")
    @iOSXCUITFindBy(accessibility = "controller_uilabel_9")
    private WebElement endTime;

    @AndroidFindBy(id = "cast_control_seekbar")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "controller_progress_bar_10"),
            @iOSXCUITBy(accessibility = "controller_progress_bar_1")})
    private WebElement seekBar;

    @AndroidFindBy(id = "cast_control_full_play_pause_stop")
    private WebElement fullPlayPauseButton;

    @AndroidFindBy(id = "cast_mini_control_pause_play_stop")
    @iOSXCUITFindBy(accessibility = "controller_uibutton_2")
    private WebElement miniPlayPauseButton;

    @AndroidFindBy(id = "cast_control_info")
    private WebElement infoButtonAndroid;

    @iOSXCUITFindBy(accessibility = "controller_uibutton_1")
    private List<WebElement> pauseInfoButtoniOS;

    @AndroidFindBy(id = "cast_control_record")
    @iOSXCUITFindBy(accessibility = "controller_uibutton")
    private WebElement recordButton;

    @AndroidFindBy(id = "cast_control_audio_and_subtitles")
    @iOSXCUITFindBy(accessibility = "controller_uibutton_3")
    private WebElement language;

    @AndroidFindBy(id = "cast_control_volume_icon")
    @iOSXCUITFindBy(accessibility = "controller_uibutton_4")
    private WebElement volumeIcon;

    @AndroidFindBy(id = "cast_control_back_10")
    private WebElement backButtonAndroid;

    @AndroidFindBy(id = "cast_control_forward_10")
    private WebElement forwardButtonAndroid;

    @iOSXCUITFindBy(accessibility = "controller_uibutton")
    private List<WebElement> backforwardButtonIOS;

    @AndroidFindBy(id = "header_back")
    @iOSXCUITFindBy(accessibility = "header_back")
    private WebElement headerBack;

    @AndroidFindBy(id = "languages_audio_heading")
    @iOSXCUITFindBy(accessibility = "languages_audio_heading")
    private WebElement languagesAudioHeading;

    @AndroidFindBy(id = "languages_audio_items")
    @iOSXCUITFindBy(accessibility = "languages_audio_items")
    private List<WebElement> languagesAudioItems;

    @AndroidFindBy(id = "languages_subtitle_heading")
    @iOSXCUITFindBy(accessibility = "languages_subtitle_heading")
    private WebElement languagesSubtitleHeading;

    @AndroidFindBy(id = "languages_subtitles_items")
    @iOSXCUITFindBy(accessibility = "languages_subtitle_items")
    private List<WebElement> languageSubtitleItems;

    @AndroidFindBy(id = "cast_control_volume_seekbar")
    private WebElement volumeSeekBar;

    @iOSXCUITFindBy(accessibility = "iPhone")
    private WebElement iPhone;

    @iOSXCUITFindBy(accessibility = "iPad")
    private WebElement iPad;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,', Apple TV')]/XCUIElementTypeStaticText")
    private List<WebElement> appleTVs;

    @iOSXCUITFindBy(iOSNsPredicate = "type == \"XCUIElementTypePopover\"")
    private WebElement airPlaySelector;

}
