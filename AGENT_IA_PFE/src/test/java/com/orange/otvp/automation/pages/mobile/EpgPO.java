package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class EpgPO {

    AppiumDriver driver;

    public EpgPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    private WebElement channelList = null;
    private WebElement channelProgram = null;

    @AndroidFindBy(id = "live_list_channel_epg_program_list")
    @iOSXCUITFindBy(iOSNsPredicate = "name CONTAINS 'live_live.epgchannel_cell'")
    private List<WebElement> channelLists;

    @AndroidFindBy(id = "live_list_channel_epg_program_list")
    @AndroidFindBy(className = "android.widget.LinearLayout")
    @iOSXCUITFindBy(iOSNsPredicate = "name CONTAINS 'live_live.epgchannel_cell'")
    @iOSXCUITFindBy(iOSNsPredicate = "name CONTAINS 'live_live.epgprogram_cell'")
    private List<WebElement> channelPrograms;

    @AndroidFindBy(id = "herozone_item_details")
    @iOSXCUITFindBy(accessibility = "live_recommendation_hero_zone.recommendation_hero_zone")
    private WebElement heroZoneEPG;

    @AndroidFindBy(id = "tab_layout")
    @iOSXCUITFindBy(accessibility = "live_live.live_tab_bar_4")
    private WebElement tabBar;

    @AndroidFindBy(id = "live_list_item_channel_logo")
    @iOSXCUITFindBy(accessibility = "live_channel_logo")
    private WebElement channelLogo;

    @AndroidFindBy(id = "live_list_item_channel_id_iptv")
    @iOSXCUITFindBy(accessibility = "live_uilabel_2")
    private WebElement channelNumber;

    @AndroidFindBy(id = "header_title_text")
    @iOSXCUITFindBy(accessibility = "live_genre_picker_uilabel_2")
    private WebElement genreTitle;

    @AndroidFindBy(id = "epg_program_live_play_icon")
    @iOSXCUITFindBy(accessibility = "live_uibutton_8")
    private WebElement programPlayButton;

    @AndroidFindBy(id = "epg_program_playback_interaction_zone")
    private WebElement programThumbnail;

    @AndroidFindBy(id = "epg_program_live_progress_bar")
    private WebElement programProgressBar;

    @AndroidFindBy(id = "epg_program_start_time_text")
    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE '*live.epgprogram_cell*'")
    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE '*uilabel'")
    private WebElement channelProgramTime;

    @AndroidFindBy(id = "epg_program_title_text")
    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE '*live.epgprogram_cell*'")
    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE '*uilabel_1'")
    private WebElement channelProgramTitle;

    @AndroidFindBy(id = "epg_program_genre_text")
    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE '*live.epgprogram_cell*'")
    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE '*uilabel_2'")
    private WebElement channelProgramGenre;

    @iOSXCUITFindBy(accessibility = "live_custom_uibutton_9")
    private WebElement programTextFieldLiveIOS;

    @iOSXCUITFindBy(accessibility = "live_custom_uibutton_4")
    private WebElement programTextFieldIOS;

    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE 'live_live.epgprogram_cell*'")
    @iOSXCUITFindBy(accessibility = "live_uilabel_1")
    private WebElement channelProgramTimeLiveIOS;

    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE 'live_live.epgprogram_cell*'")
    @iOSXCUITFindBy(accessibility = "live_uilabel_2")
    private WebElement channelProgramTitleLiveIOS;

    @iOSXCUITFindBy(iOSNsPredicate = "name LIKE 'live_live.epgprogram_cell*'")
    @iOSXCUITFindBy(accessibility = "live_uilabel_3")
    private WebElement channelProgramGenreLiveIOS;

    public WebElement getChannelProgram(int channel, int program) {

        channelList = channelLists.get(channel);

        if (driver instanceof AndroidDriver) {
            channelPrograms = channelList.findElements(AppiumBy.className("android.widget.LinearLayout"));
            channelProgram = channelPrograms.get(program);
        }
        if (driver instanceof IOSDriver) {
            channelPrograms = channelList.findElements(AppiumBy.xpath("//*[contains(@name,'live_live.epgprogram_cell')]"));
            channelProgram = channelPrograms.get(program);
        }
        return channelProgram;
    }

    public WebElement getProgramImage(int channel, int program) {

        channelProgram = getChannelProgram(channel, program);
        WebElement channelImage;
        if (driver instanceof AndroidDriver) {

            channelImage = channelProgram.findElement(AppiumBy.id(programThumbnail.getAttribute("resource-id")));
        }
        else {
            channelImage = channelProgram.findElement(AppiumBy.id(programPlayButton.getAttribute("name")));
        }
        return channelImage;
    }

    public void nowPlayingIsFirst() {

        channelProgram = getChannelProgram(0, 0);

        if (driver instanceof AndroidDriver) {
            channelProgram.findElement(AppiumBy.id(programPlayButton.getAttribute("resource-id"))).isDisplayed();
            channelProgram.findElement(AppiumBy.id(programThumbnail.getAttribute("resource-id"))).isDisplayed();
            channelProgram.findElement(AppiumBy.id(programProgressBar.getAttribute("resource-id"))).isDisplayed();
        }
        if (driver instanceof IOSDriver) {
            channelProgram.findElement(AppiumBy.accessibilityId(programPlayButton.getAttribute("name"))).isDisplayed();
        }
    }

    public void accessProgramInfosheet(int channel, int program, boolean live) {
        channelProgram = getChannelProgram(channel, program);

        if (driver instanceof AndroidDriver) {
            channelProgram.click();
        }
        if (driver instanceof IOSDriver) {

            if (live) {
                channelProgram.findElement(AppiumBy.accessibilityId(programTextFieldLiveIOS.getAttribute("name"))).click();
            }
            else {
                channelProgram.findElement(AppiumBy.accessibilityId(programTextFieldIOS.getAttribute("name"))).click();
            }
        }
    }

    public String getProgramTime(int channel, int program, boolean live) {

        String time = null;
        channelProgram = getChannelProgram(channel, program);

        if (driver instanceof AndroidDriver) {
            time = channelProgram.findElement(AppiumBy.id(channelProgramTime.getAttribute("resource-id"))).getText();
        }
        if (driver instanceof IOSDriver) {
            time = channelProgram.findElement(AppiumBy.iOSNsPredicateString("name LIKE '*uilabel'")).getText();
        }
        return time;
    }

    public String getProgramTitle(int channel, int program, boolean live) {
        String title = null;
        channelProgram = getChannelProgram(channel, program);

        if (driver instanceof AndroidDriver) {
            title = channelProgram.findElement(AppiumBy.id(channelProgramTitle.getAttribute("resource-id"))).getText();
        }
        if (driver instanceof IOSDriver) {
            title = channelProgram.findElement(AppiumBy.iOSNsPredicateString("name LIKE '*uilabel_1'")).getText();
        }
        return title;
    }

    public WebElement getProgramTitleElement(int channel, int program, boolean live) {
        WebElement title = null;
        channelProgram = getChannelProgram(channel, program);

        if (driver instanceof AndroidDriver) {
            title = channelProgram.findElement(AppiumBy.id(channelProgramTitle.getAttribute("resource-id")));
        }
        if (driver instanceof IOSDriver) {
            title = channelProgram.findElement(AppiumBy.iOSNsPredicateString("name LIKE '*uilabel_1'"));
        }
        return title;
    }

    public String getChannelProgramGenre(int channel, int program, boolean live) {
        String programGenre = null;
        channelProgram = getChannelProgram(channel, program);

        if (driver instanceof AndroidDriver) {
            programGenre = channelProgram.findElement(AppiumBy.id(channelProgramGenre.getAttribute("resource-id"))).getText();
        }
        if (driver instanceof IOSDriver) {
            if (live) {
                programGenre = channelProgram.findElement(AppiumBy.iOSNsPredicateString("name LIKE '*uilabel_3'")).getText();
            }
            else {
                programGenre = channelProgram.findElement(AppiumBy.iOSNsPredicateString("name LIKE '*uilabel_2'")).getText();
            }
        }
        return programGenre;
    }

}
