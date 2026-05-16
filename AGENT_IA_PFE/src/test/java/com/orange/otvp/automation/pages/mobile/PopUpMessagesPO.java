package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.StaleElementReferenceException;
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
public class PopUpMessagesPO {

    AppiumDriver driver;

    public PopUpMessagesPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "custom_dialog")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "idialog_manager_alert_controller_uialert_controller_view_3"),
            @iOSXCUITBy(accessibility = "idialog_manager_alert_controller_uiview_1"),
            @iOSXCUITBy(accessibility = "list_of_stbs_pop_up_uiview_2")})
    private WebElement customDialog;

    @AndroidFindBy(id = "custom_dialog_title_block")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "idialog_manager_alert_controller_uilabel_1"),
            @iOSXCUITBy(accessibility = "custom_uialert_controller_uilabel_1")})
    private WebElement customDialogTitle;

    @AndroidFindBy(id = "custom_dialog_content")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "idialog_manager_alert_controller_uilabel_2"),
            @iOSXCUITBy(accessibility = "custom_uialert_controller_uilabel_2")})
    private WebElement customDialogText;

    @AndroidFindAll({
            @AndroidBy(id = "dialog_message_text"),
            @AndroidBy(id = "subscription_offers_for_channel_loading_error")})
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "custom_uialert_controller_uilabel_1"),
            @iOSXCUITBy(accessibility = "idialog_manager_alert_controller_uilabel_2")})
    private WebElement customDialogMessageText;

    @WithTimeout(time = 2, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindAll({
            @AndroidBy(id = "custom_dialog_button_primary_positive"),
            @AndroidBy(xpath = "//*[@text='OK']")})
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == 'Allow'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'VALIDER'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'OK'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'oui'"),
            @iOSXCUITBy(accessibility = "pvrend_time_picker.pvrend_time_picker_view_uiview_1"),
            @iOSXCUITBy(accessibility = "Allow")})
    private WebElement customDialogButtonPositive;

    @AndroidFindBy(id = "custom_dialog_button_primary_positive")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'plus tard'")
    private WebElement startupDialogButtonPositive;

    @iOSXCUITFindBy(id = "Plus tard")
    private WebElement ratingPopUpShowMeLater;

    @AndroidFindBy(id = "custom_dialog_button_secondary_negative")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'recuperer mon mot de passe'")
    private WebElement startupDialogButtonRetrievePassword;

    @AndroidFindBy(id = "custom_dialog_button_primary_positive")
    @iOSXCUITFindBy(accessibility = "bandwidth_usage_dialog_custom_uibutton_1")
    private WebElement bandwithDialogButtonPositive;

    @WithTimeout(time = 2, chronoUnit = ChronoUnit.SECONDS)
    @AndroidFindBy(id = "custom_dialog_button_secondary_negative")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == 'Annuler'"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'ANNULER'")})
    private WebElement customDialogButtonNeg;

    @AndroidFindBy(id = "custom_dialog_button_primary_positive")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Changer de compte'")
    private WebElement changeAccountButton;

    @AndroidFindBy(id = "reminder_selection_list_text")
    private List<WebElement> customDialogAlertTime;

    @AndroidFindAll({
            @AndroidBy(xpath = "//*[@text='DISCONNECT']"),
            @AndroidBy(xpath = "//*[@text='OK']"),
            @AndroidBy(xpath = "//*[@text='DÉCONNECTER']")})
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Déconnecter'")
    private WebElement disconnectAccountButton;

    //Reminder Pop up App Opened
    @AndroidFindBy(id = "custom_dialog_button_primary_positive")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'voir'")
    private WebElement watchRemindedProgram;

    //Reminder Notification
    @iOSXCUITFindBy(id = "NotificationCell")
    private WebElement notificationAppClosediOS;

    //Reminder Notification
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Ouvrir'")
    private WebElement openNotificationiOS;

    //Reminder Pop up App Opened
    @AndroidFindAll({
            @AndroidBy(id = "android:id/title"),
            @AndroidBy(id = "android:id/big_text")})
    @iOSXCUITFindBy(id = "NotificationCell")
    private List<WebElement> notificationTitleAppClosed;

    @AndroidFindBy(id = "custom_dialog_button_primary_positive")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Installer'")
    private WebElement buttonInstallOcs;

    public void clearStartupMessage() {
        try {
            startupDialogButtonPositive.click();
        }
        catch (NoSuchElementException e) {
        }
    }

    public void customDialogShow() {
        int attempts = 0;
        while (attempts < 2) {
            try {
                customDialog.isDisplayed();
                break;
            }
            catch (StaleElementReferenceException e) {
            }
            attempts++;
        }
    }

    public void clearStartupPopUpIOS() {
        for (int i = 0; i != 2; i++) {
            try {
                Thread.sleep(500);
                customDialogButtonPositive.click();
            }
            catch (NoSuchElementException | InterruptedException e) {
            }
        }
    }

}
