package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.pagefactory.AndroidBy;
import io.appium.java_client.pagefactory.AndroidFindAll;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class ReplayPO {

    AppiumDriver driver;

    public ReplayPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "replay_channel_grid")
    @iOSXCUITFindBy(accessibility = "replay_channel_grid")
    private WebElement replayChannelGrid;

    @AndroidFindBy(id = "channel_logo")
    @iOSXCUITFindBy(accessibility = "replay_channel_logo")
    private List<WebElement> replayChannels;

    @AndroidFindBy(id = "replay_home_channel_item")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//*[contains(@name,'focusable_/replay/')]"),
            @iOSXCUITBy(xpath = "//*[contains(@name,'focusable_/partner/replay/')]")})
    private List<WebElement> replayHomeChannelItem;

    @AndroidFindAll({
            @AndroidBy(xpath = "//android.widget.Button[@text=\"regarder\"]"),
            @AndroidBy(id = "fip_episode_list_play_icon_parent")
    })
    @iOSXCUITFindBy(accessibility = "fip_replay_episode_list_play_button")
    private List<WebElement> groupInfoSheetPlayButtons;

    @AndroidFindBy(id = "tvod_channel_banner")
    @iOSXCUITFindBy(accessibility = "replay_channel_mosaic_uiview")
    private WebElement replayChannelCornerLogo;

    @AndroidFindBy(id = "tab_navigation_container")
    @iOSXCUITFindBy(accessibility = "replay_channel_mosaic_uiview_2")
    private WebElement replayChannelCornerButtons;

    @AndroidFindBy(id = "universe_scroll_pane_item_layout")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'replay_channel_mosaic_tvodprogram_cell')]")
    private List<WebElement> replayChannelCornerPrograms;

    @AndroidFindBy(id = "herozone")
    @iOSXCUITFindBy(accessibility = "replay_recommendation_hero_zone.recommendation_hero_zone")
    private WebElement heroZoneBlock;

    @AndroidFindBy(id = "herozone_item")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "herozone_item_thumbnail"),
            @iOSXCUITBy(accessibility = "herozone_item")})
    private List<WebElement> heroZoneReplay;

    @AndroidFindBy(id = "tab_navigation_item_title")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'replay_channel_mosaic_tvod_channel_segmented_control_button')]")
    private List<WebElement> replayTabNavigation;

    @AndroidFindBy(id = "header_title_text")
    @iOSXCUITFindBy(accessibility = "header_title")
    private WebElement replayHeaderTitle;

    @AndroidFindBy(id = "replay_shop_basket")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == 'abonnement'"),
            @iOSXCUITBy(accessibility = "abonnement")}) //Ipad
    private WebElement subscriptionIcon;

    @AndroidFindBy(id = "item_title")
    @iOSXCUITFindBy(accessibility = "header_title")
    private List<WebElement> replayChannelTitles;

    @AndroidFindBy(id = "row_heading_text")
    @iOSXCUITFindBy(accessibility = "category_stripe_title_label")
    private List<WebElement> replayCategoryTitle;

    @AndroidFindBy(id = "row_heading_text" )
    @iOSXCUITFindBy(accessibility = "unitary_grid_title_label" )
    private WebElement replayGrid;



    @AndroidFindBy(id = "see_more_button")
    @iOSXCUITFindBy(accessibility = "category_stripe_view_all_button")
    private List<WebElement> replaySeeMoreButton;

    @AndroidFindBy(id = "stripe_item")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "replay_channel_row_item"),
            @iOSXCUITBy(accessibility = "article_title_label-article_genre_label")}) //Ipad
    private List<WebElement> replayChannelRowItem;

    @AndroidFindBy(id = "item_image")
    private List<WebElement> replayItemImage;

    @AndroidFindBy(id = "item_primary_text")
    @iOSXCUITFindBy(xpath = "//*[@name='replay_channel_row_item']/*/XCUIElementTypeStaticText[1]")
    private List<WebElement> replayItemPrimaryText;

    @AndroidFindBy(id = "item_secondary_text")
    @iOSXCUITFindBy(xpath = "//*[@name='replay_channel_row_item']/*/XCUIElementTypeStaticText[2]")
    private List<WebElement> replayItemSecondaryText;

    @AndroidFindBy(id = "item_channel_small_logo")
    private List<WebElement> replayItemChannelSmallLogo;

    @AndroidFindBy(id = "replay_row_recycler")
    private List<WebElement> replayHighlightRow;

    @AndroidFindBy(id = "item_csa_icon")
    private List<WebElement> replayCsaIcon;

    @AndroidFindBy(id = "strip_sort_dropdown")
    @iOSXCUITFindBy(accessibility = "drop_down_list_button")
    private List<WebElement> replaySortDropdown;

    @AndroidFindBy(id = "spinner_view_collapsed")
    private List<WebElement> replaySortCollapsed;

    @AndroidFindBy(id = "replay_grid_sorting_filtering_options")
    private List<WebElement> replaySortAndFilteringOptions;

    @AndroidFindBy(id = "spinner_dropdown_item_text")
    private List<WebElement> replaySortItems;

    public List<WebElement> getReplayChannels() {
        int i = 0;
        do {
            i++;
        }
        while (replayChannels.size() < 4 && i < 5);
        return replayChannels;
    }
//add PO to replay apple TV
@AndroidFindBy(id = "header_title")
@iOSXCUITFindBy(accessibility = "header_title")//to be verified
private WebElement searchBarTextField;

    @AndroidFindBy(accessibility = "Replay")
    @iOSXCUITFindBy(accessibility = "/replay")
    private WebElement Replay;

    @AndroidFindBy(id = "logo")
    @iOSXCUITFindBy(accessibility = "common_orange_logo")
    private WebElement orangeLogo;

    @AndroidFindBy(id = "Toutes les chaînes")
    @iOSXCUITFindBy(accessibility = "Toutes les chaînes")
    private WebElement allChannel;

    @AndroidFindBy(id = "focusable_button")
    @iOSXCUITFindBy(accessibility = "focusable_button")
    private WebElement continuerButton;

    @AndroidFindBy(id = "universe_scroll_pane_item_layout")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'focusable_/replay/catchuptv_')]")
    private List<WebElement> replayChannelTV;

}
