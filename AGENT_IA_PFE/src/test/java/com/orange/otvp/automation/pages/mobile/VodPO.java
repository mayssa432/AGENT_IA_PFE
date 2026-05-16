package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.WebElement;
import io.appium.java_client.pagefactory.AndroidBy;
import io.appium.java_client.pagefactory.AndroidFindAll;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class VodPO {

    AppiumDriver driver;

    public VodPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    /**
     * Shared elements
     */
    @AndroidFindBy(id = "herozone_item")
    @iOSXCUITFindBy(accessibility = "herozone_item")
    private List<WebElement> heroZoneItem;

    @AndroidFindBy(id = "herozone_item_big_title")
    @iOSXCUITFindBy(accessibility = "herozone_item_big_title")
    private List<WebElement> heroZoneBigTitle;

    @AndroidFindBy(id = "herozone_item_title")
    @iOSXCUITFindBy(accessibility = "herozone_item_title")
    private List<WebElement> heroZoneItemTitle;

    @AndroidFindBy(id = "thumbnail_image")
    @iOSXCUITFindBy(accessibility = "thumbnail_image")
    private List<WebElement> heroZoneImage;

    @AndroidFindBy(id = "tab_one")
    @iOSXCUITFindBy(accessibility = "vod_tabbar_catalog")
    private WebElement catalog;

    @AndroidFindBy(id = "tab_two")
    @iOSXCUITFindBy(accessibility = "vod_tabbar_myvideos")
    private WebElement myVideos;

    @AndroidFindBy(id = "tab_three")
    @iOSXCUITFindBy(accessibility = "vod_tabbar_myfavorites")
    private WebElement myList;

    @AndroidFindBy(id = "row_heading_text")
    @iOSXCUITFindBy(accessibility = "row_heading_text")
    private List<WebElement> categoryTitle;

    @AndroidFindBy(id = "vod_row_recycler")
    @iOSXCUITFindBy(accessibility = "vod_strip")
    private List<WebElement> categoryStrip;

    @AndroidFindBy(id = "item_image")
    @iOSXCUITFindBy(accessibility = "item_image")
    private List<WebElement> itemImage;

    @AndroidFindBy(id = "item_download_indicator")
    @iOSXCUITFindBy(accessibility = "item_download_indicator")
    private List<WebElement> itemDownloadIndicator;

    @AndroidFindBy(id = "item_primary_text")
    @iOSXCUITFindBy(accessibility = "item_primary_text")
    private List<WebElement> itemPrimaryText;

    @AndroidFindBy(id = "item_secondary_text")
    @iOSXCUITFindBy(accessibility = "item_secondary_text")
    private List<WebElement> itemSecondaryText;

    @AndroidFindBy(id = "item_pastil_text")
    @iOSXCUITFindBy(accessibility = "item_pastil_text")
    private List<WebElement> itemPastilText;

    @AndroidFindBy(id = "see_more_button")
    @iOSXCUITFindBy(accessibility = "see_more_button")
    private List<WebElement> seeMoreButton;



    /**
     * Catalog
     */

    /**
     * My videos
     */

    /**
     * My list
     */

    @AndroidFindBy(id = "row_heading_text")
    @iOSXCUITFindBy(accessibility = "category_stripe_title_label")
    private List<WebElement> myListCategoryTitle;

    @AndroidFindBy(id = "vod_row_recycler")
    @AndroidFindBy(className = "android.view.ViewGroup")
    @iOSXCUITFindBy(accessibility = "bookmarks_wishlist_6s")
    @iOSXCUITFindBy(className = "XCUIElementTypeButton")
    private List<WebElement> myListElements;

    @AndroidFindBy(id = "see_more_button")
    @iOSXCUITFindBy(accessibility = "category_stripe_view_all_button")
    private List<WebElement> myListseeMoreButton;

    // todo: old, remove after is replaced with new one
    @AndroidFindBy(id = "row_heading_text")
    @iOSXCUITFindBy(accessibility = "catalog_page_uilabel")
    private List<WebElement> catalogCategoryTitles;

    @AndroidFindBy(id = "vod_row_recycler")
    @iOSXCUITFindBy(accessibility = "vod_strip")
    private List<WebElement> programSliderBanners;

    @AndroidFindBy(id = "item_primary_text")
    @iOSXCUITFindBy(accessibility = "item_primary_text")
    private List<WebElement> elementTitles;

    @iOSXCUITFindBy(xpath = "//*[contains(@name,'catalog_page_vodthumbnail_cell')]")
    private List<WebElement> vodCatalogElementsIOS;

    @iOSXCUITFindBy(accessibility = "catalog_category_terminal_uilabel_3")
    private List<WebElement> vodCategoryElementsTextIOS;

    @AndroidFindBy(id = "vod_row_recycler")
    @AndroidFindBy(className = "android.view.ViewGroup")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'myvideos_page_my_video_item_view')]")
    private List<WebElement> vodMyVideosElements;

    @AndroidFindAll({
            @AndroidBy(id = "thumbnail_title"),
            @AndroidBy(id = "item_primary_text")
    })
    @iOSXCUITFindBy(accessibility = "item_primary_text")
    private List<WebElement> vodMyVideosTitles;

    @AndroidFindBy(id = "vod_row_recycler")
    @AndroidFindBy(className = "android.view.ViewGroup")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//*[contains(@name,'bookmarks_wishlist_swift_ui.hosting_scroll_view')]/*/XCUIElementTypeButton"),
            @iOSXCUITBy(xpath = "//*[contains(@name,'mybookmarks_page_vodbookmark_cell')]")}) //Ipad
    private List<WebElement> vodMyBookmarksElements;


    @AndroidFindBy(id = "bookmarks_content")
    @AndroidFindBy(xpath = "//android.widget.LinearLayout[2]/*/*/*/android.widget.TextView")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//XCUIElementTypeScrollView[@name='bookmarks_wishlist_swift_ui.hosting_scroll_view_1']/*/*/XCUIElementTypeStaticText"),
            @iOSXCUITBy(xpath = "(//XCUIElementTypeScrollView[@name=\"swift_ui.hosting_scroll_view\"])[3]/*/*/XCUIElementTypeStaticText")
    })
    private List<WebElement> vodMyBookmarksTitles;

    @AndroidFindBy(xpath = "//androidx.recyclerview.widget.RecyclerView/(*/androidx.recyclerview.widget.RecyclerView)[2]")
    @AndroidFindBy(id = "android.view.ViewGroup")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//*[contains(@name,'bookmarks_wishlist_swift_ui.hosting_scroll_view_3')]/*/XCUIElementTypeButton"),
            @iOSXCUITBy(xpath = "//*[contains(@name,'bookmarks_wishlist_swift_ui.hosting_scroll_view_5')]/*/XCUIElementTypeButton"),
            @iOSXCUITBy(xpath = "//*[contains(@name,'mybookmarks_page_vodbookmark_cell')]")}) //Ipad
    private List<WebElement> vodMyAlertsElements;


    @AndroidFindBy(xpath = "//androidx.recyclerview.widget.RecyclerView/(*/androidx.recyclerview.widget.RecyclerView)[2]")
    @AndroidFindBy(id = "item_primary_text")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//XCUIElementTypeScrollView[@name='bookmarks_wishlist_swift_ui.hosting_scroll_view_5']/*/*/XCUIElementTypeStaticText"),
            @iOSXCUITBy(xpath = "(//XCUIElementTypeScrollView[@name='swift_ui.hosting_scroll_view'])[4]/*/*/XCUIElementTypeStaticText")
    })
    private List<WebElement> vodMyAlertsTitles;

    @AndroidFindBy(id = "horizontal_banner_open_all")
    @iOSXCUITFindBy(accessibility = "catalog_page_uibutton_2")
    private WebElement openAllCategoryButton;

    @AndroidFindBy(id = "herozone")
    @iOSXCUITFindBy(accessibility = "catalog_page_recommendation_hero_zone.recommendation_hero_zone")
    private WebElement heroZoneBlock;

    @AndroidFindBy(id = "herozone_item")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'catalog_page_recommendation_hero_zone.recommendation_hero_zone')]")
    private List<WebElement> heroZoneVOD;

    @iOSXCUITFindBy(accessibility = "catalog_page_vodtab_view_4")
    @iOSXCUITFindBy(accessibility = "catalog_page_uiview_3")
    private WebElement tabNavigationIOS;

    @Deprecated
    @AndroidFindAll({
            @AndroidBy(id = "category_sorter_spinner_container"),
            @AndroidBy(id = "vod_grid_sort_dropdown_parent")})
    @iOSXCUITFindBy(accessibility = "catalog_category_terminal_uibutton_3")
    private WebElement categoryArrangeButton;

    @Deprecated
    @AndroidFindBy(id = "spinner_dropdown_item")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'catalog_category_terminal_uitable_view_cell')]")
    private List<WebElement> categoryArrangeItems;

    @Deprecated
    @AndroidFindBy(id = "chip_show_all_options_button")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'catalog_category_terminal_filter_bar.filter_item_view_cell')]")
    private WebElement categoryFilterButton;

    @Deprecated
    @AndroidFindBy(id = "chip_item_button")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'vod_category_filter_picker_filter_bar.filter_item_view_cell')]")
    private List<WebElement> categoryFilterItems;

    @AndroidFindBy(id = "vod_category_content_highlights_recycler")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'catalog_category_terminal_vod.vodcategory_highlights_cell')]")
    private WebElement categoryTerminalHighlights;

    @AndroidFindBy(id = "vod_category_content_recycler")
    @AndroidFindBy(className = "android.view.ViewGroup")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'catalog_category_terminal_vodthumbnail_collection_view_cell')]")
    private List<WebElement> categoryTerminalElements;


    @AndroidFindBy(id = "vod_row_recycler")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'myvideos_page_vodtable_view_cell')]")
    private List<WebElement> myVideosSliderBanners;

    @AndroidFindBy(id = "see_more_button")
    @iOSXCUITFindBy(xpath = "myvideos_page_uibutton_2")
    private List<WebElement> myVideosShowMoreButton;

    @AndroidFindBy(xpath = "//android.widget.HorizontalScrollView//android.widget.TextView")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeOther[@name='tabbed_series_uiview']/XCUIElementTypeStaticText")
    private List<WebElement> seasonTabs;

    @AndroidFindBy(xpath = "//android.widget.HorizontalScrollView//android.widget.TextView[@selected=\"true\"]")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeOther[@name='tabbed_series_uiview']/XCUIElementTypeOther[@name='tabbed_series_uiview']/../XCUIElementTypeStaticText")
    private WebElement activeSeasonTab;

    //Alerting
    @iOSXCUITFindBy(accessibility = "mylist_vod_alert_dot")
    private WebElement myListVodAlertDot;

    @iOSXCUITFindBy(accessibility = "tabbar_vod_alert_dot")
    private WebElement tabbarVodAlertDot;

    @AndroidFindBy(xpath = "//*[contains(@content-desc,'maintenant disponible')]")
    @iOSXCUITFindBy(accessibility = "article_vod_alert_dot")
    private List<WebElement> articleVodAlertDot;

    @AndroidFindBy(id = "row_title_text")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'Créez des alertes')]")
    private WebElement createAlertText;

    @AndroidFindBy(id = "tab_three")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Ma Liste, Nouveaux films disponibles'")
    private WebElement myListWithAlert;

    @AndroidFindAll({
            @AndroidBy(xpath = "//*[contains(@content-desc,'maintenant disponible')]"),
            @AndroidBy(xpath = "//*[contains(@content-desc,'Disponible')]")})
    @iOSXCUITFindBy(accessibility = "Disponible")
    private List<WebElement> itemAvailable;

    //Confirmation snack bar. For snack bar checks use only fast element locators
    @AndroidFindBy(id = "snackbar_text")
    @iOSXCUITFindBy(accessibility = "main_uilabel_1")
    private WebElement snackBartText;

    @iOSXCUITFindBy(accessibility = "snack_bar_success")
    private WebElement snackBarSuccessIconIOS;

    @AndroidFindBy(id = "item_image")
    @iOSXCUITFindBy(accessibility = "main_uilabel_1")
    private WebElement unitaryFilm;

    @AndroidFindBy(id = "vod_row_recycler")
    @iOSXCUITFindBy(accessibility = "main_uilabel_1")
    private WebElement severalFilm;


}
