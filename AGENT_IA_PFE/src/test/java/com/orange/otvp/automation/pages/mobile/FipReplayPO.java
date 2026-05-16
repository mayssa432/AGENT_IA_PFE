package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class FipReplayPO {

    AppiumDriver driver;

    public FipReplayPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "fip_content_top_landscape_image_view")
    @iOSXCUITFindBy(accessibility = "action_replay_season_uiview_1" )
    private WebElement replayListProgramThumbnail;

    @AndroidFindBy(id = "fip_content_top_portrait_image")
    @iOSXCUITFindBy(accessibility = "action_replay_season_uiview_2" )
    private WebElement replayListProgramChannelLogo;

    @AndroidFindBy(id = "fip_title_text")
    @iOSXCUITFindBy(accessibility = "replay_series_title")
    private WebElement replayListProgramTitle;

    @AndroidFindBy(id = "fip_content_top_group_count")
    @iOSXCUITFindBy(accessibility = "replay_series_list_title")
    private WebElement replayListGroupCount;

    @AndroidFindBy(id = "fip_episode_list_play_icon_parent")
    @iOSXCUITFindBy(accessibility = "fip_replay_episode_list_play_button")
    private List<WebElement> replayListPlayIcon;

    @AndroidFindBy(id = "fip_info_layout")
    @iOSXCUITFindBy(accessibility = "fip_replay_episode_list_info")
    private List<WebElement> replayListInfo;

    @iOSXCUITFindBy(accessibility = "replay_series_list_episode_cell")
    private List<WebElement> episodeCellIOS;

    @AndroidFindBy(id = "fip_content_top_landscape_image_view")
    @iOSXCUITFindBy(accessibility = "action_tvod_uiview_1")
    private WebElement replayUnitaryProgramThumbnail;

    @AndroidFindBy(id = "fip_title_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_title")
    private WebElement replayUnitaryProgramTitle;

    @AndroidFindBy(id = "fip_content_top_portrait_image")
    @iOSXCUITFindBy(iOSClassChain = "**/XCUIElementTypeButton[`name == 'action_tvod_custom_uibutton_2'`]")
    private WebElement replayUnitaryProgramChannelLogo;

    @AndroidFindBy(id = "information_sheet_info_module")
    @iOSXCUITFindBy(accessibility = "top_tvodserie_uiview_1")
    private WebElement replayUnitaryAvailability;

    @AndroidFindBy(id = "fip_cast_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_cast")
    private WebElement replayUnitaryCast;

    @AndroidFindBy(id = "fip_description_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_description")
    private WebElement replayUnitaryDescription;

    @AndroidFindBy(id = "long_summary_unitary")
    private WebElement replayLongUnitarySummary;

    @AndroidFindBy(id = "fip_content_list_item_secondary_text" )
    @iOSXCUITFindBy(accessibility = "info_sheet_list_uilabel_1")
    private WebElement replayProgramListTitle;

    @AndroidFindBy(id = "fip_play_button")
    @iOSXCUITFindBy(accessibility = "fip_content_top_button_play")
    private WebElement replayPlayButton;

    @AndroidFindBy(id = "fip_content_top_replay_button_subscribe")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == \"S\'ABONNER\""),
            @iOSXCUITBy(xpath = "//*[@label=\"S'ABONNER\"]")})
    private WebElement subscribeButton;

    @AndroidFindBy(id = "fip_info_layout")
    @iOSXCUITFindBy(accessibility = "fip_replay_episode_list_info")
    private List<WebElement> replayEpisodeList;

    @AndroidFindBy(id = "fip_replay_deeplink_button")
    @iOSXCUITFindBy(accessibility = "info_sheet_partner_area_custom_uibutton_3")
    private WebElement replayProgramChannelCornerButton;

    public void replayListProgramShown() {
        replayListProgramThumbnail.isDisplayed();
        replayListProgramChannelLogo.isDisplayed();
        replayListProgramTitle.isDisplayed();
        replayProgramListTitle.isDisplayed();
    }

    public void replayUnitaryProgramShown() {
        replayUnitaryProgramThumbnail.isDisplayed();
        replayUnitaryProgramChannelLogo.isDisplayed();
        replayUnitaryProgramTitle.isDisplayed();
        replayUnitaryAvailability.isDisplayed();
        replayUnitaryDescription.isDisplayed();
    }

}
