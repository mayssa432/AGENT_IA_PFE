package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
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
public class FipLivePO {

    AppiumDriver driver;

    public FipLivePO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "fip_title_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_title")
    private WebElement fipTitle;

    @AndroidFindBy(id = "fip_play_button")
    @iOSXCUITFindBy(accessibility = "fip_content_top_button_play")
    private WebElement fipProgramPlayButton;

    @AndroidFindBy(id = "fip_startover_button")
    @iOSXCUITFindBy(id = "fip_content_top_button_start_over")
    private WebElement fipStartOverButton;

    @AndroidFindBy(id = "fip_remind_button")
    @iOSXCUITFindBy(accessibility = "fip_content_top_button_reminder")
    private WebElement fipButtonReminder;

    @AndroidFindBy(id = "fip_record_button")
    @iOSXCUITFindBy(accessibility = "fip_content_top_button_record")
    private WebElement fipButtonRecord;

    @AndroidFindBy(id = "fip_cast_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_cast")
    private WebElement fipActors;

    @AndroidFindBy(id = "fip_description_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_description")
    private WebElement fipDescription;

    @AndroidFindBy(id = "fip_content_top_progress_bar")
    @iOSXCUITFindBy(accessibility = "action_live_progress_bar_4")
    private WebElement fipProgressBar;

    @AndroidFindBy(id = "fip_play_button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "fip_content_top_button_play"),
            @iOSXCUITBy(accessibility = "fip_content_top_button_resume")
    })
    private WebElement fipRecordPlayButton;



    //old IDs
    @AndroidFindBy(id = "fip_content_top_landscape_image")
    @iOSXCUITFindBy(accessibility = "action_live_uiview")
    private WebElement fipProgramBigImage;

    @AndroidFindBy(id = "fip_content_top_portrait_image")
    @iOSXCUITFindBy(accessibility = "action_live_channel_logo")
    private WebElement fipChannelLogo;

    @AndroidFindBy(id = "fip_live_start_end_time")
    @iOSXCUITFindBy(accessibility = "action_live_uilabel_2")
    private WebElement fipStartEndTime;

    @iOSXCUITFindBy(accessibility = "action_live_uilabel_5")
    private WebElement fipGenreDurationIOS;

    @AndroidFindBy(id = "fip_content_top_genre_date_countries_duration")
    private WebElement fipGenreCountriesDateAndroid;

    @AndroidFindBy(xpath= "//*[contains(@resource-id,'fip_content_top_pictogram')]")
    private List<WebElement> fipPictogramAndroid;

    @AndroidFindBy(id = "fip_subscribe_button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == \"S'ABONNER\""),
            @iOSXCUITBy(xpath = "//*[@label=\"S'ABONNER\"]")})
    private WebElement fipButtonSubscribe;

    @AndroidFindBy(id = "fip_modify_button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == \"MODIFIER L'HEURE DE FIN\""),
            @iOSXCUITBy(iOSNsPredicate = "label == \"MODIFIER L'ENREGISTREMENT\"")})
    private WebElement fipButtonRecordModify;

    @AndroidFindBy(id = "fip_delete_button")
    @iOSXCUITFindBy(accessibility = "fip_content_top_button_delete")
    private WebElement fipButtonRecordDelete;

}
