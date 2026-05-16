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
public class NavigationPO {

    AppiumDriver driver;

    public NavigationPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "header_title_text")
    @iOSXCUITFindBy(accessibility = "header_title")
    private WebElement headerTitle;

    @AndroidFindBy(id = "footer")
    @iOSXCUITFindBy(accessibility = "tab_bar_uistack_view_1")
    private WebElement tabbar;

    @AndroidFindBy(accessibility = "Accueil")
    @iOSXCUITFindBy(accessibility = "/accueil/accueil-de-la-tv-d-orange")
    private WebElement homePage;

    @AndroidFindBy(id = "Espace Replay")
    @iOSXCUITFindBy(accessibility = "/replay")
    private WebElement espacereplay;


    @AndroidFindBy(id = "bottom_navigation_one")
    @iOSXCUITFindBy(accessibility = "/programme-tv")
    private WebElement tvChannels;

    @AndroidFindBy(id = "bottom_navigation_two")
    @iOSXCUITFindBy(accessibility = "/replay")
    private WebElement replay;

    @AndroidFindBy(id = "bottom_navigation_three")
    @iOSXCUITFindBy(accessibility = "/vod")
    private WebElement vod;

    @AndroidFindBy(id = "bottom_navigation_four")
    @iOSXCUITFindBy(accessibility = "/boutiquetv")
    private WebElement shop;

    @AndroidFindBy(id = "header_search_icon")
    @iOSXCUITFindBy(accessibility = "header_search_button")
    private WebElement search;

    @AndroidFindBy(id = "bottom_navigation_five")
    @iOSXCUITFindBy(accessibility = "/more")
    private WebElement plus;

    @AndroidFindBy(xpath = "//*[@text='Mon compte']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Mon compte'")
    private WebElement myAccount;

    @AndroidFindBy(xpath = "//*[@text=\"Partage de ma TV d'Orange\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"Partage de ma TV d'Orange\"")
    private WebElement shareAccount;

    @AndroidFindBy(xpath = "//*[@text='Mes réglages']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Mes réglages'")
    private WebElement mySettings;

    @AndroidFindBy(id = "details_subscription_text")
    @iOSXCUITFindBy(accessibility = "myaccount_view_uibutton")
    private WebElement myPurchases;

    @AndroidFindBy(xpath = "//*[@text='Pass vidéo']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Pass vidéo'")
    private WebElement passVideo;

    @AndroidFindBy(xpath = "//*[@text='Mes enregistrements']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Mes enregistrements'")
    private WebElement recorder;

    @AndroidFindBy(xpath = "//*[@text=\"Noter l'application\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"Noter l'application\"")
    private WebElement rating;

    @AndroidFindBy(id = "tab_two")
    @iOSXCUITFindBy(accessibility = "npvr_scheduled_tab")
    private WebElement programmed;

    @AndroidFindBy(xpath = "//*[@text='Badge de confiance']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Badge de confiance'")
    private WebElement dataUsage;

    @AndroidFindBy(xpath = "//*[@text='A propos']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'A propos'")
    private WebElement about;

    @AndroidFindBy(xpath = "//*[@text=\"Découverte de l'app\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "value == \"Découverte de l'app\"")
    private WebElement discovery;

    @AndroidFindBy(xpath = "//*[@text='Aide & contact']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Aide & contact'")
    private WebElement help;

    @Deprecated
    @AndroidFindBy(xpath = "//*[@text='Identifiants']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Identifiants'")
    private WebElement myAccountTitle;

    @AndroidFindBy(id = "header_remote_icon")
    @iOSXCUITFindBy(accessibility = "header_remote_button")
    private WebElement remoteButton;

    @AndroidFindBy(id = "header_cast")
    @iOSXCUITFindBy(accessibility = "header_playto_button")
    private WebElement playToButton;

    @AndroidFindAll({
            @AndroidBy(id = "header_back"),
            @AndroidBy(accessibility = "Retour"),
            @AndroidBy(accessibility = "Remonter"),
            @AndroidBy(accessibility = "Revenir en haut de la page")
    })
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "Précédent"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'RETOUR'"),
            @iOSXCUITBy(accessibility = "header_back"),
            @iOSXCUITBy(accessibility = "button_close_manage"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'fermer'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'Fermer'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'Réglages'")
    })
    private WebElement headerBack;

    @iOSXCUITFindBy(accessibility = "Annuler")
    private WebElement ratingStoreAnnuler;

    @iOSXCUITFindBy(accessibility = "Envoyer")
    private WebElement ratingStoreEnvoyer;

    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Rédiger un avis'")
    private WebElement ratingStoreTitle;

    @AndroidFindBy(xpath = "//androidx.compose.ui.platform.ComposeView/*/*/android.widget.TextView")
    private List<WebElement> androidStoreInformations;

    @AndroidFindBy(accessibility = "Désinstaller")
    private WebElement androidStoreUninstallButton;

    @AndroidFindBy(accessibility = "Ouvrir")
    private WebElement androidStoreOpenButton;

    @iOSXCUITFindBy(iOSNsPredicate = "label == 'DEBUG'")
    private WebElement debugMenuIos;

    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Player Overlay Idle Time'")
    private WebElement debugOptionOverlayIdleTimeIos;

    @iOSXCUITFindBy(accessibility = "uialert_controller_uiview_4")
    private WebElement debugOptionOverlayIdleTimeTextFiled;

    @iOSXCUITFindBy(accessibility = "uialert_controller_uiinterface_action_custom_view_representation_view")
    private WebElement debugOptionOverlayIdleTimeTextFiledOkButton;



}
