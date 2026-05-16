package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.By;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.WebElement;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.pagefactory.AndroidBy;
import io.appium.java_client.pagefactory.AndroidFindAll;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class SearchPO {

    AppiumDriver driver;

    public SearchPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    // Search view
    @AndroidFindBy(id = "header_search_text")
    @iOSXCUITFindBy(accessibility = "search_bar_icustom_search_bar")
    private WebElement searchBarTextField;

    @AndroidFindBy(id = "search_completion_list_view_one_i")
    @iOSXCUITFindBy(accessibility = "search_completion_uiview")
    private WebElement searchCompletionList;

    @AndroidFindBy(id = "header_list_item")
    private List<WebElement> searchCompletionListItems;

    @iOSXCUITFindBy(accessibility = "Search")
    private WebElement searchKeyboardButton;

    @AndroidFindBy(id = "search_results_list_layout")
    @iOSXCUITFindBy(accessibility = "polaris_search_uiview_1")
    private WebElement searchResultView;

    @iOSXCUITFindBy(iOSNsPredicate = "label == 'OK'")
    private WebElement popupOkButton;

    @AndroidFindBy(id = "content_area")
    @AndroidFindAll({
            @AndroidBy(xpath = "//*[contains(@text,'Séries')]"),
            @AndroidBy(xpath = "//*[contains(@text,'Série')]")})
    @iOSXCUITFindBy(accessibility = "uuid_60770e51_14ad_4b45_8152_5cbb443a4031")
    private WebElement seasonPanel;

    @AndroidFindBy(id = "content_area")
    @AndroidFindAll({
            @AndroidBy(xpath = "//*[contains(@text,'Films')]"),
            @AndroidBy(xpath = "//*[contains(@text,'Film')]")})
    @iOSXCUITFindBy(accessibility = "uuid_89a80de0_b412_4b77_b335_25ac7b6ef471")
    private WebElement filmsPanel;

    @AndroidFindBy(id = "content_area")
    @AndroidFindAll({
            @AndroidBy(xpath = "//*[contains(@text,'Emissions')]"),
            @AndroidBy(xpath = "//*[contains(@text,'Emission')]")})
    @iOSXCUITFindBy(accessibility = "uuid_a9c08baa_7b0d_487a_9011_4b662a7e649b")
    private WebElement emissionPanel;

    @AndroidFindBy(id = "content_area")
    @AndroidFindAll({
            @AndroidBy(xpath = "//*[contains(@text,'Episodes')]"),
            @AndroidBy(xpath = "//*[contains(@text,'Episode')]")})
    @iOSXCUITFindBy(accessibility = "uuid_e20db88a_ced8_45e9_8833_ae430743e776")
    private WebElement episodesPanel;

    @AndroidFindBy(id = "header_search_clear")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Effacer le texte'")
    private WebElement clearButton;

    @AndroidFindBy(id = "header_search_icon")
    private List<WebElement> searchIcon;

    // Search result elements
    @AndroidFindBy(id = "search_results_list_state_switcher")
    @iOSXCUITFindBy(iOSNsPredicate = "name BEGINSWITH 'search_result_search_result_object'")
    private List<WebElement> searchResultElements;

    @AndroidFindBy(xpath = "//*[@text= 'Voir en replay']")
    @iOSXCUITFindBy(accessibility = "uuid_527f6a3f_88d6_4289_bdb0_6a46e0617d0d")
    private List<WebElement> watchInReplayButtons;

    @AndroidFindAll({
            @AndroidBy(xpath = "//*[@text= 'Voir en VOD']"),
            @AndroidBy(xpath = "//*[@text= 'regarder']")})
    @iOSXCUITFindBy(accessibility = "uuid_700b1eff_d5a7_4294_bf7f_8ab01b98ed63")
    private List<WebElement> watchInVodButtons;

    @AndroidFindBy(xpath = "//*[@text= 'Voir les épisodes']")
    @iOSXCUITFindBy(accessibility = "uuid_3f2e16c3_56e5_4c35_9df0_d0aca2fa3723")
    private List<WebElement> watchEpisodesButtons;

    @iOSXCUITFindBy(xpath = "//*[contains (@name, 'search_result_search_result_object')]/child::XCUIElementTypeImage[2]")
    private List<WebElement> thumbnails;

    @AndroidFindBy(id = "searchlistitemview_subtitle")
    @iOSXCUITFindBy(xpath = "//*[contains (@label, 'résultat pour')]")
    private WebElement searchSubTitle;

    @AndroidFindBy(id = "searchlistitemview_csa_level")
    @iOSXCUITFindBy(iOSNsPredicate = "name == \"CSA-10-white\"")
    private WebElement searchCsaIconWhite;

    @AndroidFindBy(id = "searchlistitemview_csa_level")
    @iOSXCUITFindBy(iOSNsPredicate = "name == \"CSA-10-black\"")
    private WebElement searchCsaIconBlack;

    @AndroidFindBy(id = "searchlistitemview_title")
    @iOSXCUITFindBy(accessibility = "search_result_uilabel_10")
    private List<WebElement> searchItemTitle;

    @AndroidFindBy(id = "searchlistitemview_info")
    @iOSXCUITFindBy(accessibility = "search_result_uilabel_2")
    private List<WebElement> searchItemYearGenreDuration;

    @AndroidFindBy(id = "searchlistitemview_ratingtitle")
    @iOSXCUITFindBy(accessibility = "search_result_uilabel_9")
    private List<WebElement> searchAllocineSpectator;

    @iOSXCUITFindBy(accessibility = "thin_horizontal_line.png")
    private List<WebElement> searchSeparator;

    @AndroidFindBy(id = "searchlistitemview_subtitle")
    @iOSXCUITFindBy(accessibility = "search_result_uilabel_12")
    private List<WebElement> searchItemSubtitle;

    @AndroidFindBy(id = "searchlistitemview_info2")
    private List<WebElement> searchItemEpisod;

    public void setSearchTerm() {
        searchBarTextField.sendKeys("le");
    }

    public void completionListShown() {
        searchCompletionList.isDisplayed();
    }

    public void initiateSearch() {

        if (driver instanceof AndroidDriver) {
            //TODO: touch action as workaround. not working for AndroidKey.SEARCH
            searchCompletionListItems.get(3).click();
        }
        if (driver instanceof IOSDriver) {
            searchKeyboardButton.click();

            try {
                popupOkButton.click();
            }
            catch (Exception e) {
            }
        }
    }

    public void searchResultViewShown() {
        searchResultView.isDisplayed();
    }

    public void selectSearchCategory(int number) {
        if (number == 1) {
            filmsPanel.click();
        }
        else if (number == 2) {
            seasonPanel.click();
        }
        else if (number == 3) {
            emissionPanel.click();
        }
        else {
            episodesPanel.click();
        }
    }

    public void programNameTextShown(String programName) {
        if (driver instanceof AndroidDriver) {
            searchResultView.findElement(By.xpath("//*[contains(@text,'" + programName + "')]")).isDisplayed();
        }
        if (driver instanceof IOSDriver) {
            searchResultView.findElement(By.xpath("//*[contains(@label,'" + programName + "')]")).isDisplayed();
        }
    }

}
