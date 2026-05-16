package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.time.temporal.ChronoUnit;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.pagefactory.AndroidBy;
import io.appium.java_client.pagefactory.AndroidFindAll;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.WithTimeout;
import io.appium.java_client.pagefactory.iOSXCUITBy;
import io.appium.java_client.pagefactory.iOSXCUITFindAll;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class FipVodPO {

    AppiumDriver driver;

    public FipVodPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "fip_content_top_landscape_image")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "action_vodmovie_uiview_1"),
            @iOSXCUITBy(accessibility = "action_vodseason_uiview"),
            @iOSXCUITBy(xpath = "//*[contains (@name,'action_vodseason_uiview')]")})
    private WebElement bigThumbnail;

    @AndroidFindBy(id = "fip_content_top_bookmark_icon")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "top_vodmovie_custom_uibutton_5"), //Ipad
            @iOSXCUITBy(accessibility = "top_vodmovie_custom_uibutton")})
    private WebElement bookmarkButton;

    @WithTimeout(time = 2, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindBy(id = "fip_title_text")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "action_vodmovie_uilabel_3"),
            @iOSXCUITBy(accessibility = "action_vodmovie_uilabel_5"),
            @iOSXCUITBy(accessibility = "action_vodseason_uilabel_4")})
    private WebElement programTitle;

    @AndroidFindBy(id = "fip_play_button")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'REGARDER'")
    private WebElement playButton;

    @AndroidFindBy(id = "fip_pack_list_item_play_icon")
    @iOSXCUITFindBy(accessibility = "fip_replay_episode_list_play_button")
    private WebElement playIconOnPackThumbnail;

    @AndroidFindBy(id = "fip_download_button")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == 'TÉLÉCHARGER'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'ANNULER LE TÉLÉCHARGEMENT'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'SUPPRIMER LE TÉLÉCHARGEMENT'")})
    private WebElement downloadButton;

    @AndroidFindBy(xpath = "//*[contains(@text,\"Supprimer l'alerte\")]")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"SUPPRIMER L'ALERTE\"")
    private WebElement setDeleteAlertButton;

    @AndroidFindBy(xpath = "//*[contains(@text,\"M'alerter de la disponibilité\")]")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"M'ALERTER DE LA DISPONIBILITÉ\"")
    private WebElement setCreateAlertButton;

    @AndroidFindBy(id = "fip_content_top_remove_wishlist")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"RETIRER DE MA LISTE D'ALERTES\"")
    private WebElement deleteAlertButton;

    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Comment acheter ou louer cette vidéo'")
    private WebElement howToBuyHelpIOS;

    @iOSXCUITFindBy(accessibility = "vod_how_to_buy_uiview_1")
    private WebElement howToBuyHelpUiViewIOS;

    @iOSXCUITFindBy(accessibility = "vod_how_to_buy_custom_uibutton_2")
    private WebElement howToBuyHelpUiViewButtonIOS;

    @iOSXCUITFindBy(accessibility = "action_vodmovie_uibutton_2")
    private WebElement howToBuyHelpButtonIOS;

    @WithTimeout(time = 2, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindBy(id = "fip_content_top_availability_row_parent")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "top_vodmovie_uiview"),
            @iOSXCUITBy(accessibility = "top_vodseason_uiview"),
            @iOSXCUITBy(xpath = "//*[contains (@name,'top_vodseason_uiview')]")})
    private WebElement supportedDevices;

    @WithTimeout(time = 2, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindBy(id = "fip_content_top_genre_date_country")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "top_vodseason_custom_uilabel"),
            @iOSXCUITBy(accessibility = "top_vodmovie_custom_uilabel"),
            @iOSXCUITBy(accessibility = "top_vodmovie_uilabel"),
            @iOSXCUITBy(accessibility = "action_vodseason_uilabel_4"),
            @iOSXCUITBy(accessibility = "top_vodseason_custom_uilabel")})
    private WebElement programGenreYear;

    @WithTimeout(time = 2, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindBy(id = "fip_content_top_pictograms")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "top_vodmovie_info_sheet_restriction_icons"),
            @iOSXCUITBy(accessibility = "top_vodmovie_info_sheet_restriction_icons_3"),
            @iOSXCUITBy(accessibility = "top_vodmovie_info_sheet_restriction_icons_4"),
            @iOSXCUITBy(accessibility = "top_vodseason_info_sheet_restriction_icons_3")})
    private WebElement programLanguages;

    @AndroidFindBy(id = "fip_cast_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_cast")
    private WebElement programActors;

    @AndroidFindBy(id = "fip_description_text")
    @iOSXCUITFindBy(accessibility = "fip_content_top_description")
    private WebElement programDescription;

    @AndroidFindBy(id = "collapsible_text_view")
    @iOSXCUITFindBy(accessibility = "fip_content_top_description")
    private WebElement groupProgramDescription;

    @AndroidFindBy(xpath = "//*[contains (@resource-id, 'fip_content_top_details_top')]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView")
    @iOSXCUITFindBy(accessibility = "allocin")
    private WebElement ratingIcon;

    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "top_vodmovie_allocine_ratings.allocine_ratings_2"),
            @iOSXCUITBy(accessibility = "top_vodmovie_allocine_ratings.allocine_ratings_3"),
            @iOSXCUITBy(accessibility = "top_vodseason_allocine_ratings.allocine_ratings_2")})
    private WebElement ratingElementIOS;

    @iOSXCUITFindBy(accessibility = "top_vodmovie_uilabel")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "top_vodmovie_uilabel"),
            @iOSXCUITBy(accessibility = "top_vodseason_uilabel")})
    private List<WebElement> ratingTextsIOS;

    @iOSXCUITFindBy(accessibility = "top_vodmovie_rating_control.rating_control_1")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "top_vodmovie_rating_control.rating_control_1"),
            @iOSXCUITBy(accessibility = "top_vodseason_rating_control.rating_control_1")})
    private List<WebElement> ratingStarsIOS;

    @AndroidFindBy(id = "ratings_spectators_group")
    private WebElement ratingSpectatorsGroupAndroid;

    @AndroidFindBy(id = "ratings_press_group")
    private WebElement ratingPressGroupAndroid;

    @AndroidFindBy(id = "fip_content_top_button_sd")
    private WebElement qualitySDButtonAndroid;

    @AndroidFindBy(id = "fip_content_top_button_hd")
    private WebElement qualityHDButtonAndroid;

    @AndroidFindBy(id = "fip_rent_button")
    private WebElement rentButtonAndroid;

    @AndroidFindBy(id = "fip_buy_button")
    private WebElement buyButtonAndroid;

    @AndroidFindBy(id = "expand_button_container")
    @iOSXCUITFindBy(accessibility = "info_sheet_description_uibutton_4")
    private WebElement showMoreButton;

    @AndroidFindBy(id = "fip_content_top_group_count")
    @iOSXCUITFindBy(accessibility = "replay_series_list_title")
    private WebElement episodeListTitle;

    @AndroidFindBy(id = "fip_info_layout")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'info_sheet_list_info_sheet_list_table_view_cell')]")
    private List<WebElement> seasonEpisodes;

    @AndroidFindBy(xpath = "//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'info_sheet_list_vodpack_info_sheet_list_table_view_cell')]")
    private List<WebElement> packMovies;

    @AndroidFindBy(id = "fip_content_bottom_promo")
    private WebElement promoAndroidBanner;

    @AndroidFindBy(id = "fip_content_top_download_indicator")
    @iOSXCUITFindBy(accessibility = "action_vodmovie_download_status_indicator")
    private WebElement downloadIndicator;

    public void checkHowToBoyHelp() {
        howToBuyHelpIOS.isDisplayed();
        howToBuyHelpButtonIOS.click();
        howToBuyHelpUiViewIOS.isDisplayed();
        howToBuyHelpUiViewButtonIOS.click();
    }

}
