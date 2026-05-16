package com.orange.otvp.automation.pages.mobile;

import io.appium.java_client.pagefactory.*;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import lombok.Getter;

@Getter
public class PlayerOverlayPO {

    AppiumDriver driver;

    public PlayerOverlayPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    /**
     * Android Ok button
     * In some Android versions hint overlay is shown at the first start up of the player
     */
    @AndroidFindBy(id = "android:id/ok")
    private WebElement fullScreenHintAndroid;

    /**
     * Main overlay common components
     */
    @AndroidFindBy(xpath =  "//*[@resource-id='PlayOverlayHeader.Back']")
    @iOSXCUITFindBy(accessibility = "header_back")
    private WebElement overlayPlayBackButton;


    @iOSXCUITFindBy(accessibility = "player_overlay_header_pip")
    private WebElement overlayPlayPIPIcon;

    @AndroidFindBy(xpath = "//*[@resource-id='PlayOverlayHeader.Cast']")
    @iOSXCUITFindBy(accessibility = "header_cast")
    private WebElement overlayHeaderCast;

    @AndroidFindBy(xpath = "//*[@resource-id='InfoButton']")
    @iOSXCUITFindBy(accessibility = "player_overlay_info")
    private WebElement overlayHeaderInfo;

    @AndroidFindBy(id = "uic_video_overlay_control_stream_quality_button")
    @iOSXCUITFindBy(accessibility = "player_overlay_quality")
    private WebElement overlayHeaderQuality;

    @AndroidFindBy(xpath = "//*[@resource-id='TracksButton']")

    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//XCUIElementTypeButton[@name=\"player_overlay_languages\"]"),
            @iOSXCUITBy(accessibility = "player_overlay_languages")
    })
    //@iOSXCUITFindBy(accessibility = "player_overlay_languages")
    private WebElement overlayHeaderLang;

    @AndroidFindBy(id = "player_overlay_header_hide")
    @iOSXCUITFindBy(accessibility = "player_overlay_header_hide")
    private WebElement overlayHeaderHide;

    @AndroidFindBy(xpath = "//*[@resource-id='PlayPauseButton']")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "player_overlay_play_pause"),
            @iOSXCUITBy(iOSNsPredicate ="name == \"player_overlay_play_pause\"")
    })
    private WebElement overlayPlayPause;

    @AndroidFindBy(xpath = "//*[@resource-id='PlayMetadataCommon.Title']")
    @iOSXCUITFindBy(accessibility = "player_overlay_info_group")
    private WebElement overlayInfoGroup;

    @AndroidFindBy(id = "player_overlay_zoom")
    @iOSXCUITFindBy(accessibility = "player_overlay_zoom")
    private WebElement overlayFullScreen;

    @AndroidFindBy(xpath = "//*[@resource-id='SliderLabelLeft']")
    @iOSXCUITFindBy(accessibility = "player_overlay_time_1")
    private WebElement overlayTimeElapsed;

    @AndroidFindBy(xpath = "//*[@resource-id='SliderInteractive']")
    @iOSXCUITFindBy(accessibility = "player_overlay_seekbar")
    private List<WebElement>  overlaySeekbar;

    @AndroidFindBy(xpath = "//*[@resource-id='SliderLabelRight']")
    @iOSXCUITFindBy(accessibility = "player_overlay_time_2")
    private WebElement overlayTimeRemained;

	@AndroidFindBy(xpath = "//*[@resource-id='ChannelControlAll']")
    @iOSXCUITFindBy(accessibility = "player_overlay_open_carousel")
    private WebElement overlayCarousel;

    @AndroidFindBy(id = "video_container")
    @iOSXCUITFindBy(accessibility = "player_background")
    private WebElement overlayPlaybackBackground;
    /**
     * Live overlay
     */
    @AndroidFindBy(xpath = "//*[@resource-id='RecordButton']")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "player_overlay_header_record"),
            @iOSXCUITBy(accessibility = "player_overlay_record")
    })
    private WebElement overlayHeaderRecordButton;

    @AndroidFindBy(id = "channel_previous_button")
    @iOSXCUITFindBy(accessibility = "player_overlay_backward")
    private WebElement channel_previous;

    @AndroidFindBy(id = "channel_next_button")
    @iOSXCUITFindBy(accessibility = "player_overlay_forward")
    private WebElement channel_next;

    @AndroidFindBy(xpath= "//*[@resource-id='ChannelControlPlus']")
    @iOSXCUITFindBy(accessibility = "player_overlay_next_channel")
    private WebElement playerOverlayNextChannel;

    @AndroidFindBy(xpath= "//*[@resource-id='ChannelControlMinus']")
    @iOSXCUITFindBy(accessibility = "player_overlay_previous_channel")
    private WebElement playerOverlayPreviousChannel;

    @AndroidFindBy(xpath= "//*[@resource-id='SeekToStartButton']")
    @iOSXCUITFindBy(accessibility = "player_overlay_start_over")
    private WebElement playerOverlayStartOver;

    @AndroidFindBy(id = "player_overlay_backward")
    @iOSXCUITFindBy(accessibility = "player_overlay_backward")
    private WebElement playerOverlayBackward;

    @AndroidFindBy(id = "player_overlay_forward")
    @iOSXCUITFindBy(accessibility = "player_overlay_forward")
    private WebElement playerOverlayForward;

    @AndroidFindBy(xpath= "//*[@resource-id='SeekToEndButton']")
    @iOSXCUITFindBy(accessibility = "player_overlay_back_to_live")
    private WebElement playerOverlayBackToLive;

    /**
     * Carousel overlay
     */

    @iOSXCUITFindBy(accessibility = "player_overlay_open_carousel")
    private WebElement playerOverlayOpenCarousel;

    @AndroidFindBy(id = "player_overlay_carousel_header_hide")
    @iOSXCUITFindBy(accessibility = "player_overlay_backward")
    private WebElement playerOverlayCarouselHeaderHide;

    @AndroidFindBy(id = "carousel_slide_down_area")
    @iOSXCUITFindBy(accessibility = "carousel_slide_down_area")
    private WebElement carouselSlideDownArea;

    @AndroidFindBy(id = "player_overlay_carousel_item")
    @iOSXCUITFindBy(accessibility = "player_overlay_carousel_item")
    private List<WebElement> playerOverlayCarouselItem;

    @AndroidFindBy(id = "player_carousel_item_channel_number")
    private List<WebElement> playerOverlayCarouselItemChannelNumber;

    /**
     * On Demande
     */
    @AndroidFindBy(id = "player_overlay_backward")
    @iOSXCUITFindBy(accessibility = "player_overlay_start_over")
    private WebElement overlayRewind;

    @AndroidFindBy(id = "player_overlay_forward")
    @iOSXCUITFindBy(accessibility = "player_overlay_forward")
    private WebElement overlayForward;

    /**
     * Info overlay
     */
    @AndroidFindBy(xpath = "//*[@resource-id='PlayOverlayHeader.Close']")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "name == 'header_back' "),
            @iOSXCUITBy(iOSNsPredicate = "name == 'Fermer' "),
            @iOSXCUITBy(accessibility = "player_info_title_group")
    })

    private WebElement overlayInfoClose;

    @AndroidFindBy(id = "player_info_title_group")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//XCUIElementTypeOther[contains(@name,\"platform_group_container\")]/XCUIElementTypeOther[2]"),
            @iOSXCUITBy(xpath = "//XCUIElementTypeOther[contains(@name,\"platform_group_container\")]/XCUIElementTypeStaticText[1]"),
            @iOSXCUITBy(accessibility = "player_info_title_group")
    })

    private WebElement overlayInfoTitle;

    @AndroidFindBy(id = "player_info_secondary")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//XCUIElementTypeOther[contains(@name,\"platform_group_container\")]/XCUIElementTypeOther[3]"),
            @iOSXCUITBy(xpath = "//XCUIElementTypeOther[contains(@name,\"platform_group_container\")]/XCUIElementTypeStaticText[3]"),
            @iOSXCUITBy(accessibility = "player_info_secondary")
    })
    private WebElement overlayInfoGenre;

    @AndroidFindBy(id = "player_info_cast_and_crew")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//XCUIElementTypeOther[contains(@name,\"platform_group_container\")]/XCUIElementTypeStaticText[1]"),
            @iOSXCUITBy(accessibility = "player_info_cast_and_crew")
    })
    private WebElement overlayInfoCasting;

    @AndroidFindBy(id = "player_info_description")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//XCUIElementTypeOther[contains(@name,\"platform_group_container\")]/XCUIElementTypeStaticText[4]"),
            @iOSXCUITBy(accessibility = "player_info_description")
    })
    private WebElement overlayInfoDescription;

    /**
     * Languages overlay
     */
    @AndroidFindBy(id = "languages_audio_heading")
    @iOSXCUITFindBy(accessibility = "languages_audio_heading")
    private WebElement overlayLangAudioTitle;

    @AndroidFindBy(id = "languages_audio_items")
    @AndroidFindBy(className = "android.widget.RadioButton")
    @iOSXCUITFindBy(accessibility = "languages_audio_items")
    @iOSXCUITFindBy(className = "XCUIElementTypeButton")
    private List<WebElement> overlayLanguageAudioItems;

    @AndroidFindBy(id = "languages_subtitle_heading")
    @iOSXCUITFindBy(accessibility = "languages_subtitle_heading")
    private WebElement overlayLangSubtitleTitle;

    @AndroidFindBy(id = "languages_subtitles_items")
    @AndroidFindBy(className = "android.widget.RadioButton")
    @iOSXCUITFindBy(accessibility = "languages_subtitle_items")
    @iOSXCUITFindBy(className = "XCUIElementTypeButton")
    private List<WebElement> overlayLangSubtitleItems;

    @AndroidFindBy(id = "languages_subtitle_options")
    @iOSXCUITFindBy(accessibility = "languages_subtitle_options")
    private WebElement overlayLangOptions;

    /**
     * Quality overlay
     */
    @AndroidFindBy(id = "player_stream_quality_title_group")
    @iOSXCUITFindBy(accessibility = "stream_quality_title")
    private WebElement streamQualityTitle;

    @AndroidFindBy(id = "player_stream_quality_title")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'La qualité peut varier selon le débit de votre connexion et votre équipement.'")
    private WebElement streamQualitySubTitle;

    @AndroidFindBy(id = "video_stream_item_layout")
    private List<WebElement> streamQualityItemAndroid;

    @AndroidFindBy(id = "hd_logo_image")
    private WebElement hdLogoImageAndroid;

    @AndroidFindBy(id = "radio_button_item")
    private List<WebElement> streamQualityButtonAndroid;

    @AndroidFindBy(id = "video_stream_title")
    private List<WebElement> streamQualityTitleAndroid;

    @AndroidFindBy(id = "video_stream_subtitle")
    private List<WebElement> streamQualitySubTitleAndroid;

    @iOSXCUITFindBy(accessibility = "stream_quality_option_hq")
    private WebElement streamQualityOptionHqIOS;

    @iOSXCUITFindBy(accessibility = "stream_quality_option_mq")
    private WebElement streamQualityOptionMqIOS;

    @iOSXCUITFindBy(accessibility = "stream_quality_option_lq")
    private WebElement streamQualityOptionLqIOS;

    @AndroidFindBy(id = "player_stream_quality_note_group")
    @iOSXCUITFindBy(accessibility = "stream_quality_info")
    private WebElement streamQualityInfo;

    /**
     * Ads overlay
     */
    @AndroidFindBy(id = "player_overlay_ads_duration")
    @iOSXCUITFindBy(accessibility = "player_overlay_ads_duration")
    private WebElement playerOverlayAdsDuration;

    @AndroidFindBy(id = "player_overlay_ads_link")
    @iOSXCUITFindBy(accessibility = "player_overlay_ads_link")
    private WebElement playerOverlayAdsLink;

    /**
     * Treminal Error
     */
    @AndroidFindBy(id = "player_overlay_error_text")
    @iOSXCUITFindBy(accessibility = "play_view_error_message2_uilabel")
    private WebElement playerOverlayTerminalError;

    /**
     * Retry button
     */
    @AndroidFindBy(id = "player_overlay_error_retry_button")
    @iOSXCUITFindBy(accessibility = "play_view_error_message2_custom_uibutton_1")
    private WebElement playerOverlayRetry;

    public void clearFullScreenHintAndroid() {
        try {
            fullScreenHintAndroid.click();
        }
        catch (Exception e) {
        }
    }

}
