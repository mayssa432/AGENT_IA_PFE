package com.orange.otvp.automation.pages.mobile;


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
public class ShopPO {

    AppiumDriver driver;

    public ShopPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "shop_home_herozone_item_thumbnail")
    @iOSXCUITFindBy(accessibility = "shop_hero_zone_offer_shop_hero_zone_table_view_cell")
    private WebElement offersHeroZone;

    @AndroidFindBy(id = "thumbnail_image")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//*[contains(@name,'shop_carrousel_zone_offer_shop_carrousel_zone_table_view_cell')]"),
            @iOSXCUITBy(xpath = "//*[contains(@name,'shop_subscribe_offer_uiview')]/XCUIElementTypeImage[2]"),
            @iOSXCUITBy(xpath = "//*[contains(@name,'shop_offer_info_price_uiview')]/XCUIElementTypeImage[1]")})
    private List<WebElement> shopOffersThumbnails;

    @AndroidFindBy(id = "horizontal_banner_title")
    @iOSXCUITFindBy(accessibility = "shop_carrousel_zone_offer_uilabel_2")
    private List<WebElement> shopOffersCategories;

    @AndroidFindBy(id = "offer_list_container")
    @iOSXCUITFindBy(accessibility = "mypurchases_page_uiscroll_view_3")
    private WebElement myPurchasesContainer;

    @AndroidFindBy(id = "subscription_offer_name")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "shop_offer_info_price_uilabel"),
            @iOSXCUITBy(accessibility = "shop_subscribe_offer_uilabel_2")})
    private WebElement subscriptionOfferName;

    @AndroidFindBy(id = "subscription_offer_price")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "shop_offer_info_price_uilabel_1"),
            @iOSXCUITBy(accessibility = "shop_subscribe_offer_uilabel_3")})
    private WebElement subscriptionOfferPrice;

    @AndroidFindBy(id = "subscription_offer_price_details")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "shop_offer_info_price_uilabel_2"),
            @iOSXCUITBy(accessibility = "shop_subscribe_offer_uilabel_4")})
    private WebElement subscriptionOfferPriceDetail;

    @AndroidFindBy(id = "offers_for_channel_header_text")
    @iOSXCUITFindBy(accessibility = "shop_subscribe_label_uiview_1")
    private WebElement subscriptionOfferHeader;

    @AndroidFindBy(xpath = "//android.widget.ListView/*/android.widget.ImageView")
    @iOSXCUITFindBy(accessibility = "shop_subscribe_offer_uibutton_6")
    private WebElement subscriptionOfferArrow;

    @AndroidFindBy(id = "shop_home_error")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "shop_page_uilabel_1"),
            @iOSXCUITBy(accessibility = "mypurchases_page_uilabel_1")})
    private WebElement shopErrorMessage;

    @AndroidFindBy(id = "subscription_button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == \"S\'ABONNER\""),
            @iOSXCUITBy(xpath = "//*[@label=\"S'ABONNER\"]")})
    private WebElement subscriptionButton;

    @AndroidFindBy(id = "subscription_live_channels_list_view_all_link")
    @iOSXCUITFindBy(accessibility = "shop_offer_info_channel_logos_uilabel_13")
    private WebElement channelsListViewAll;

    @AndroidFindBy(id = "subscription_live_channel_list")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeOther[contains (@name, 'shop_offer_info_channel_logos_uiview')]")
    private WebElement subscriptionLiveChannelList;


    @AndroidFindBy(id = "available_for_text")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'shop_offer_info_availability_uiview')]")
    private WebElement availableForText;

    @AndroidFindBy(id = "collapsed_text_view")
    @iOSXCUITFindBy(accessibility = "info_sheet_description_uilabel_1")
    private WebElement availableChannel;

 
}
