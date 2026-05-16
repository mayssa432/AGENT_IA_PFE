package com.orange.otvp.automation.pages.mobile;

import io.appium.java_client.AppiumBy;
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
public class LivePO {

    AppiumDriver driver;

    public LivePO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "tab_one")
    @iOSXCUITFindBy(accessibility = "live_tabbar_now")
    private WebElement tvNowButton;

    @AndroidFindBy(id = "tab_two")
    @iOSXCUITFindBy(accessibility = "live_tabbar_tonight")
    private WebElement tvTonightButton;

    @AndroidFindBy(id = "tab_three")
    @iOSXCUITFindBy(accessibility = "live_tabbar_tvguide")
    private WebElement tvEpgButton;

    @AndroidFindBy(id = "primetime_first_image")
    @iOSXCUITFindBy(accessibility = "primetime_filter_1")
    private WebElement tvTonightPrimary;

    @AndroidFindBy(id = "primetime_second_image")
    @iOSXCUITFindBy(accessibility = "primetime_filter_2")
    private WebElement tvTonightSecondary;

    @iOSXCUITFindBy(accessibility = "live_uibutton_1")
    private List<WebElement> tvTonightButtons;

    @Deprecated
    @AndroidFindBy(id = "chip_show_all_options_button")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'filter_item_view_cell')]")
    private WebElement genreFilterButton;

    @Deprecated
    @AndroidFindBy(id = "chip_show_all_options_button")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'filter_item_view_cell')]")
    @iOSXCUITFindBy(className = "XCUIElementTypeStaticText")
    private WebElement genreFilterButtonText;

    //Program items
    @AndroidFindBy(id = "channel_list_container")
    @iOSXCUITFindBy(accessibility = "live_uicollection_view")
    private WebElement programList;

    @AndroidFindBy(id = "live_playback_interaction_zone")
    @iOSXCUITFindBy(accessibility = "live_channel_program_play_button")
    private WebElement livePlaybackInteractionZone;

    @AndroidFindBy(id = "live_fip_interaction_zone")
    @iOSXCUITFindBy(accessibility = "live_channel_proram_cell")
    private WebElement liveFipInteractionZone;

    @AndroidFindBy(id = "channel_list_container")
    @iOSXCUITFindBy(accessibility = "live_uicollection_view")
    @iOSXCUITFindBy(className = "XCUIElementTypeCell")
    private List<WebElement> programTV;

    @AndroidFindBy(id = "channel_list_container")
    @AndroidFindBy(id = "live_list_item_channel_id_iptv")
    @iOSXCUITFindBy(accessibility = "live_uilabel_5")
    private List<WebElement> channelNumber;

    @AndroidFindBy(id = "channel_list_container")
    @AndroidFindBy(id = "live_list_item_play_icon")
    @iOSXCUITFindBy(accessibility = "live_uicollection_view")
    @iOSXCUITFindBy(className = "XCUIElementTypeCell")
    @iOSXCUITFindBy(accessibility = "live_uibutton_8")
    private List<WebElement> programPlayButton;

    @AndroidFindBy(id = "channel_list_container")
    @AndroidFindBy(id = "live_list_item_play_icon")
    @iOSXCUITFindBy(accessibility = "live_uicollection_view")
    @iOSXCUITFindBy(className = "XCUIElementTypeCell")
    @iOSXCUITFindBy(accessibility = "play")
    private List<WebElement> programPlayIcon;

    @AndroidFindBy(id = "channel_list_container")
    @AndroidFindBy(id = "live_list_item_channel_logo")
    @iOSXCUITFindBy(accessibility = "live_list_item_channel_logo")
    private List<WebElement> channelLogo;

    @AndroidFindBy(id = "channel_list_container")
    @AndroidFindBy(id = "live_list_item_primary_text")
    @iOSXCUITFindBy(accessibility = "live_list_item_primary_text")
    private List<WebElement> programPrimaryText;

    @AndroidFindBy(id = "channel_list_container")
    @AndroidFindBy(id = "live_list_item_secondary_text")
    @iOSXCUITFindBy(accessibility = "live_list_item_secondary_text")
    private List<WebElement> programSecondaryText;

    @AndroidFindBy(id = "live_list_item_progress_bar")
    @iOSXCUITFindBy(accessibility = "live_list_item_progress_bar")
    private WebElement liveProgramItemProgressBar;

    // HeroZone Items
    @AndroidFindBy(id = "herozone")
    @iOSXCUITFindBy(accessibility = "live_recommendation_hero_zone.recommendation_hero_zone")
    private WebElement heroZoneTV;

    @AndroidFindBy(id = "herozone_item_thumbnail")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "herozone_item_thumbnail"),
            @iOSXCUITBy(accessibility = "herozone_item")})
    private List<WebElement> heroZoneItems;

    @AndroidFindBy(id = "herozone_item_center_button")
    @iOSXCUITFindBy(accessibility = "live_recommendation_hero_zone.recommendation_hero_zone]")
    @iOSXCUITFindBy(accessibility = "play")
    private List<WebElement> heroZonePlayButtons;

    public String getProgramTimeGenre(int program) {
        return programSecondaryText.get(program).getText();
    }

    public void openProgramInfoSheet(int program) {

        if (driver instanceof AndroidDriver) {
            programPrimaryText.get(program).click();
        }
        if (driver instanceof IOSDriver) {
            programTV.get(program).click();
        }
    }

    public void channelProgramShown(int program) {
        channelLogo.get(program).isDisplayed();
        programPrimaryText.get(program).isDisplayed();
        channelNumber.get(program).isDisplayed();
        programSecondaryText.get(program).isDisplayed();
    }

    @Deprecated
    public void changeGenreFilter(String genre) {
        genreFilterButton.click();
        if (driver instanceof AndroidDriver) {
            driver.findElement(AppiumBy.xpath("//*[contains(@text,'" + genre + "')]")).click();
        }
        if (driver instanceof IOSDriver) {
            driver.findElement(AppiumBy.xpath("//*[contains(@label,'" + genre + "')]")).click();
        }
    }

    //Add PO to Apple TV
    @AndroidFindBy(accessibility = "Accueil")
    @iOSXCUITFindBy(accessibility = "/accueil")
    private WebElement accueil;

    @AndroidFindBy(accessibility = "Programme TV")
    @iOSXCUITFindBy(accessibility = "/en-direct/programmes-en-cours")
    private WebElement tv;

    @AndroidFindBy(accessibility = "Espace Replay")
    private WebElement replayHome;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeScrollView[1])[2]/*/XCUIElementTypeOther")
    private WebElement thematicStrip;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'thematiques')]/XCUIElementTypeImage")
    private List<WebElement> thematicStripImageiOS;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'thematiques')]/XCUIElementTypeStaticText")
    private List<WebElement> thematicStripTextiOS;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/*/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.Button")
    private List<WebElement> thematicStripThumnailAndTextAndroid;

    @AndroidFindBy(accessibility = "En ce moment à la TV")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"En ce moment à la TV\"")
    private WebElement nowOntv;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/*/android.view.View[2]/android.view.View/android.view.View[3]")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeScrollView[2]/*/XCUIElementTypeOther")
    private WebElement nowOnTvStrip;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'focusable_En ce moment à la TV_')]/XCUIElementTypeStaticText[1]")
    private List<WebElement> nowOnTvInfoiOS;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'focusable_En ce moment à la TV_')]/XCUIElementTypeImage[1]")
    private List<WebElement> nowOnTvThumbnailiOS;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'focusable_En ce moment à la TV_')]/XCUIElementTypeImage[3]")
    private List<WebElement> nowOnTvLogoiOS;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'focusable_En ce moment à la TV_')]/XCUIElementTypeStaticText[1]")
    private List<WebElement> nowOnTvTitleiOS;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button")
    private List<WebElement> nowOnTvThumbnailAndroid;

    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "homepage_progress_bar"),
            @iOSXCUITBy(accessibility = "progress_bar"),
    })
    private List<WebElement> nowOnTvProgressBar;

    @AndroidFindBy(id = "Tout le live")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"Tout le live\" AND name == \"focusable_En ce moment à la TV_/programme-tv/maintenant\"")
    private WebElement allLiveSmartTv;

    @iOSXCUITFindBy(accessibility = "homepage_swift_ui.hosting_scroll_view_6")
    private WebElement replayStrip;

    @iOSXCUITFindBy(iOSNsPredicate = "label == \"Vous pensiez l'avoir manqué\"")
    private WebElement replay;

    @iOSXCUITFindBy(xpath = "Thumbnail : //*[contains(@name,\"focusable_Vous pensiez l'avoir manqué_\")]/XCUIElementTypeImage[1]")
    private List<WebElement> replayThumbnail;

    @iOSXCUITFindBy(xpath = " //*[contains(@name,\"focusable_Vous pensiez l'avoir manqué_\")]/XCUIElementTypeStaticText[1]")
    private List <WebElement> replayTitle;

    @iOSXCUITFindBy(xpath = " //*[contains(@name,\"focusable_Vous pensiez l'avoir manqué_\")]/XCUIElementTypeStaticText[2]")
    private List <WebElement> replaySubTitle;







    // Replay Unitary Fip



}
