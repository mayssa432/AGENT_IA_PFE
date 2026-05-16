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
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class FilterPO {

    AppiumDriver driver;

    public FilterPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    /**
     * Filter components
     */
    @AndroidFindBy(id = "chip_show_all_options_button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "name == 'filter_show_all_cell'"),
            @iOSXCUITBy(iOSNsPredicate = "name == 'filter_expand_cell'")})
    private WebElement filterButton;

    @AndroidFindBy(id = "chip_item_button")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'filter_option_cell'")
    private List<WebElement> filterItems;

    @AndroidFindBy(id = "chips_show_all_tablet_button")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'filter_expand_cell'")
    private WebElement moreCriteriaButtonTablet;

    @AndroidFindBy(className = "androidx.recyclerview.widget.RecyclerView")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'live_genre_picker_uicollection_view'")
    private WebElement genreFilterList;

    // VOD Multi filtering items
    @AndroidFindBy(xpath = "//*[@resource-id='multi_filter_back']")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'vod_category_filter_back_button'")
    private WebElement vodCategoryFilterBackButton;

    @AndroidFindBy(xpath = "//*[@resource-id='multi_filter_close']")
    private WebElement vodCategoryFilterCloseTabletAndroid;

    @AndroidFindBy(xpath = "//*[@resource-id='multi_filter_group_title']")
    private List<WebElement> vodCategoryFilterTitlesAndroid;

    @iOSXCUITFindBy(accessibility = "vod_category_filter_title")
    private WebElement vodCategoryFilterTitleIOS;

    @iOSXCUITFindBy(accessibility = "vod_category_filter_genre_title")
    private WebElement vodCategoryFilterGenreTitleIOS;

    @iOSXCUITFindBy(accessibility = "tick")
    private WebElement vodCategoryFilterButtonTickIOS;

    @AndroidFindBy(xpath = "//*[@resource-id='multi_filter_group_item']")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'vod_category_filter_option_cell'")
    private List<WebElement> vodFilterOption;

    @AndroidFindBy(xpath = "//*[@resource-id='multi_filter_clear']")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'vod_category_filter_reset_button'")
    private WebElement vodFilterResetButton;

    @AndroidFindBy(xpath = "//*[@resource-id='multi_filter_show_results']")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'vod_category_filter_apply_button'")
    private WebElement vodFilterApplyButton;

    /**
     * Sorting components
     * Including date sorting
     */

    // date & time selector is same id on ios
    @iOSXCUITFindBy(accessibility = "drop_down_list_button")
    private List<WebElement> sortButtonsIOS;

    @AndroidFindBy(id = "vod_grid_filter_dropdown")
    private WebElement vodSortButtonAndroid;

    @AndroidFindBy(id = "strip_sort_dropdown")
    private WebElement replaySortButtonAndroid;

    @AndroidFindBy(id = "recordings_sorter_dropdown")
    private WebElement npvrSortButtonAndroid;

    @AndroidFindBy(id = "live_epg_date_selection_dropdown")
    private WebElement daySortingButtonAndroid;

    @AndroidFindBy(id = "spinner_dropdown_item")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'drop_down_list_option_cell'")
    private List<WebElement> sortItems;

    @AndroidFindBy(id = "live_epg_date_selection_dropdown")
    @iOSXCUITFindBy(xpath = "//*[@name=\"main_screen_container_2\"]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]") // Todo
    private WebElement dayFilterButton;

    /**
     * Time selector components
     */

    @AndroidFindBy(id = "live_epg_time_selection_dropdown")
    private WebElement timeSelectionButtonAndroid;

    @AndroidFindBy(className = "android.widget.ListView")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'live_uitable_view'")
    private WebElement timeFilterList;

    @AndroidFindBy(id = "spinner_dropdown_item_text")
    @iOSXCUITFindBy(xpath = "(//XCUIElementTypeButton[@name='live_uibutton_3'])[2]")
    private WebElement timeFilterText;

    public void changeTimeFilter(String time) {

        if (driver instanceof AndroidDriver) {
            timeSelectionButtonAndroid.click();
            timeFilterList.findElement(AppiumBy.xpath("//*[contains(@text,'" + time + "')]")).click();
        }
        if (driver instanceof IOSDriver) {
            sortButtonsIOS.get(1).click();
            timeFilterList.findElement(AppiumBy.xpath("//*[contains(@label,'" + time + "')]")).click();
        }
    }

    public void changeDayFilter(int index) throws InterruptedException {

        if (driver instanceof AndroidDriver) {
            daySortingButtonAndroid.click();
            Thread.sleep(500);
        }
        if (driver instanceof IOSDriver) {
            sortButtonsIOS.get(0).click();
        }
        sortItems.get(index).click();
    }

    public void changeGenreFilter(String genre) {

        filterButton.click();
        if (driver instanceof AndroidDriver) {
            driver.findElement(AppiumBy.xpath("//*[contains(@text,'" + genre + "')]")).click();
        }
        if (driver instanceof IOSDriver) {
            driver.findElement(AppiumBy.xpath("//*[contains(@label,'" + genre + "')]")).click();
        }
    }

}
