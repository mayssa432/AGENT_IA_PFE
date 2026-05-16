package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.WebElement;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class DownloadsPO {

    static AppiumDriver driver;

    public DownloadsPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "downloads_heading_text")
    @iOSXCUITFindBy(accessibility = "offline_myvideos_uitable_view_label")
    private WebElement headerText;

    @AndroidFindBy(id = "downloads_item_image")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeOther[@name=\"offline_myvideos_any_view\"])/*/XCUIElementTypeImage[1]")
    private List<WebElement> itemImageList;

    @AndroidFindBy(id = "downloads_item_text")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeOther[@name=\"offline_myvideos_any_view\"])/*/XCUIElementTypeStaticText[1]")
    private List<WebElement> itemTextList;

    @AndroidFindBy(id = "downloads_item_play_icon")
    @iOSXCUITFindBy(accessibility = "play")
    private List<WebElement> itemPlayIconList;

    @AndroidFindBy(id = "downloads_item_text2")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeOther[@name=\"offline_myvideos_any_view\"])/*/XCUIElementTypeStaticText[2]")
    private List<WebElement> itemSubTextList;

    @AndroidFindBy(id = "downloads_item_delete_image")
    @iOSXCUITFindBy(accessibility = "Supprimer de l'appareil")
    private List<WebElement> itemDeleteIconList;

    @AndroidFindBy(id = "downloads_item_indicator")
    @iOSXCUITFindBy(accessibility = "offline_myvideos_download_status_indicator")
    private List<WebElement> itemIndicatorList;

    @AndroidFindBy(id = "downloads_item_text3")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeOther[@name=\"offline_myvideos_any_view\"])/*/XCUIElementTypeStaticText[3]")
    private List<WebElement> itemDownloadTextList;

    @AndroidFindBy(id = "downloads_empty_image")
    @iOSXCUITFindBy(accessibility = "noDownload")
    private WebElement NoDownloadIcon;

    @AndroidFindBy(id = "downloads_empty_text")
    @iOSXCUITFindBy(accessibility = "offline_myvideos_uitable_view_label")
    private WebElement NoDownloadText;
}
