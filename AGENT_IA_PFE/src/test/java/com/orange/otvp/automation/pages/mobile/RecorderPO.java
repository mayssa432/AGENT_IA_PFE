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
public class RecorderPO {

    AppiumDriver driver;

    public RecorderPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "header_title_text")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "pvr_uilabel_2"),
            @iOSXCUITBy(iOSNsPredicate = "label == 'Retour'")})
    private WebElement headerTitle;
    /**
     * Set & modify recording
     */
    // EPG based
    @AndroidFindBy(id = "recording_title")
    @iOSXCUITFindBy(accessibility = "pvrtime_picker.pvrtime_picker_view_uilabel_1")
    private WebElement recordingTitle;

    @AndroidFindBy(id = "recording_time")
    @iOSXCUITFindBy(accessibility = "pvrend_time_picker.pvrend_time_picker_view_uilabel_2")
    private WebElement recordingTime;

    @AndroidFindBy(id = "recording_description")
    @iOSXCUITFindBy(accessibility = "pvrtime_picker.pvrtime_picker_view_uilabel_1")
    private WebElement recordingDescription;

    @AndroidFindBy(xpath = "//*[@text=\"Heure de fin\"]")
    @iOSXCUITFindBy(accessibility = "pvrend_time_picker.pvrend_time_picker_view_uilabel_4")
    private WebElement endTimeTitleText;

    @AndroidFindBy(id = "spinner_view_collapsed")
    @iOSXCUITFindBy(accessibility = "pvrend_time_picker.pvrend_time_picker_view_uilabel_4")
    private WebElement endTimeText;

    @AndroidFindBy(id = "recording_end_dropdown")
    private WebElement endTimeButtonAndroid;

    @iOSXCUITFindBy(accessibility = "pvrend_time_picker.pvrend_time_picker_view_uidate_picker_8")
    private WebElement endTimePickerIOS;

    @AndroidFindBy(className = "android.widget.ListView")
    @AndroidFindBy(id = "spinner_dropdown_item")
    private List<WebElement> endTimeListElementsAndroid;

    @AndroidFindBy(id = "recording_button_1")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"Programmer l'enregistrement\"")
    private WebElement recordButton;

    @AndroidFindBy(id = "recording_button_1")
    @iOSXCUITFindAll({
            @iOSXCUITBy(iOSNsPredicate = "label == \"MODIFIER L'ENREGISTREMENT\""),
            @iOSXCUITBy(iOSNsPredicate = "label == \"MODIFIER LA PROGRAMMATION\"")})
    private WebElement modifyRecordButton;

    @AndroidFindBy(id = "recording_button_2")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"ANNULER\"")
    private WebElement cancelButton;

    // Time based
    @AndroidFindBy(id = "recording_start_time_text")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'HORAIRE DE DÉBUT'")
    private WebElement recordingStartTime;

    @AndroidFindAll({
            @AndroidBy(id = "recording_end_time_text"),
            @AndroidBy(id = "update_recording_end_time_text")})
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'HORAIRE DE FIN'")
    private WebElement recordingEndTime;

    @AndroidFindBy(id = "hourWheel")
    private WebElement recordHourWheel;

    @AndroidFindBy(id = "minuteWheel")
    private WebElement recordMinuteWheel;

    @AndroidFindBy(id = "custom_dialog_title_block")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "recording_picker_uilabel"),
            @iOSXCUITBy(accessibility = "pvrend_time_picker.pvrend_time_picker_view_uilabel")})
    private WebElement dialogTimeBasedTitle;

    @AndroidFindBy(id = "custom_dialog_content")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "recording_picker_uiview_1"),
            @iOSXCUITBy(accessibility = "pvrend_time_picker.pvrend_time_picker_view_uidate_picker_1")})
    private WebElement dialogTimeBasedText;

    // Confirmation view
    @AndroidFindBy(id = "recording_title")
    @iOSXCUITFindBy(accessibility = "pvrtime_picker.pvrtime_picker_view_uilabel")
    private WebElement confirmationTitle;

    @AndroidFindBy(id = "recording_description")
    @iOSXCUITFindBy(accessibility = "pvrtime_picker.pvrtime_picker_view_uilabel_1")
    private WebElement confirmationText;

    @AndroidFindBy(id = "recording_button_1")
    @iOSXCUITFindBy(accessibility = "pvrtime_picker.pvrtime_picker_view_custom_uibutton_2")
    private WebElement confirmationButton;

    //Confirmation snack bar. For snack bar checks use only fast element locators
    @AndroidFindBy(id = "snackbar_text")
    private WebElement snackBartTextAndroid;
    @iOSXCUITFindBy(accessibility = "snack_bar_success")
    private WebElement snackBarSuccessIconIOS;

    /**
     * Recordings view
     */

    @AndroidFindBy(id = "my_recordings_storage")
    @iOSXCUITFindBy(accessibility = "npvr_capacity_info")
    private WebElement storageElement;

    @AndroidFindBy(id = "my_recordings_storage_used_and_remaining_text")
    @iOSXCUITFindBy(accessibility = "npvr_capacity_info")
    private WebElement storageRemainingText;

    @AndroidFindBy(id = "my_recordings_storage_used_and_remaining_progress_bar")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "pvr_uiview_2"),
            @iOSXCUITBy(accessibility = "uiview_2")})
    private WebElement storageRemainingBar;

    @AndroidFindBy(id = "tab_one")
    @iOSXCUITFindBy(accessibility = "npvr_available_tab")
    private WebElement recordedBarButton;

    @AndroidFindBy(id = "tab_two")
    @iOSXCUITFindBy(accessibility = "npvr_scheduled_tab")
    private WebElement programmedBarButton;

    @AndroidFindBy(id = "my_recordings_fip_interaction_zone")
    @iOSXCUITFindBy(accessibility = "npvr_list_info")
    private List<WebElement> recordedProgramInfoList;

    @AndroidFindBy(id = "my_recordings_fip_interaction_zone")
    @AndroidFindBy(id = "my_recordings_list_item_channel_logo")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "pvr_channel_logo_6"),
            @iOSXCUITBy(accessibility = "pvr_channel_logo_8")})
    private List<WebElement> recordingProgramChannelLogo;

    @AndroidFindBy(id = "my_recordings_fip_interaction_zone")
    @AndroidFindBy(id = "my_recordings_list_item_primary_text")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "pvr_uilabel_7"),
            @iOSXCUITBy(accessibility = "pvr_uilabel_9"),
            @iOSXCUITBy(accessibility = "pvr_uilabel_6")})
    private List<WebElement> recordingProgramPrimaryText;

    @iOSXCUITFindBy(accessibility = "pvr_uilabel_6")
    private List<WebElement> recordingProgramPrimaryTextForIpad;

    @AndroidFindBy(id = "my_recordings_fip_interaction_zone")
    @AndroidFindBy(id = "my_recordings_list_item_secondary_text")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "pvr_uilabel_8"),
            @iOSXCUITBy(accessibility = "pvr_uilabel_10"),
            @iOSXCUITBy(accessibility = "pvr_uilabel_7")})
    private List<WebElement> recordingProgramSecondaryText;

    @AndroidFindBy(id = "recording_list_item_progress_bar")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "pvr_progress_bar_4"),
            @iOSXCUITBy(accessibility = "pvr_progress_bar_9")})
    private List<WebElement> recordingProgramProgressBar;

    @AndroidFindBy(id = "my_recordings_error_text")
    @iOSXCUITFindBy(xpath = "//*[contains(@label,\"Vous n'avez aucun programme enregistré.\")]")
    private WebElement emptySceduledRecords;

    @AndroidFindBy(id = "my_recordings_list_item_ic_recording_ongoing")
    @iOSXCUITFindBy(accessibility = "syncing")
    private WebElement recordingOnGoingIcon;

    @AndroidFindBy(id = "my_recordings_list_item_play_icon")
    @iOSXCUITFindBy(accessibility = "play")
    private List<WebElement> buttonPlayRecord;

    @AndroidFindBy(id = "my_recordings_list_empty_content")
    @iOSXCUITFindBy(accessibility = "npvr_list_empty_content")
    private WebElement myRecordingsListEmptyContent;
    
    @AndroidFindBy(id = "create_time_recording_fab")
    @iOSXCUITFindBy(accessibility = "create_time_recording_button")
    private WebElement createTimeRecordingButton;

    /**
     * Create time recording view
     */
    @AndroidFindBy(id = "recording_title")
    @iOSXCUITFindBy(accessibility = "recording_title")
    private WebElement recordingTitleTimeBased;

    @AndroidFindBy(id = "recording_description")
    @iOSXCUITFindBy(accessibility = "recording_description")
    private WebElement recordingDescriptionTimeBased;

    @AndroidFindBy(id = "recording_channel_dropdown_parent")
    @iOSXCUITFindBy(accessibility = "recording_channel_title")
    private WebElement recordingChannelSelection;

    @iOSXCUITFindBy(
            className = "XCUIElementTypePickerWheel")
    private WebElement recordingChannelPickerIOS;

    @AndroidFindBy(id = "recording_date_dropdown_parent")
    @iOSXCUITFindBy(accessibility = "recording_date_title")
    private WebElement recordingDateSelection;

    @iOSXCUITFindBy(accessibility = "recording_date_picker")
    private WebElement recordingDatePickerIOS;

    @AndroidFindBy(id = "recording_start_dropdown_parent")
    @iOSXCUITFindBy(accessibility = "recording_start_title")
    private WebElement recordingStartSelection;

    @iOSXCUITFindBy(accessibility = "recording_start_picker")
    private WebElement recordingStartPickerIOS;

    @AndroidFindBy(id = "recording_end_dropdown_parent")
    @iOSXCUITFindBy(accessibility = "recording_end_title")
    private WebElement recordingEndSelection;

    @iOSXCUITFindBy(accessibility = "recording_end_picker")
    private WebElement recordingEndPickerIOS;

    @AndroidFindBy(id = "spinner_dropdown_item")
    private List<WebElement> spinnerDropdownItemAndroid;

    @iOSXCUITFindBy(className = "XCUIElementTypePickerWheel")
    private WebElement recordingPickerIOS;

    @AndroidFindBy(id = "recording_button_1")
    @iOSXCUITFindBy(accessibility = "recording_button_1")
    private WebElement recordingConfirmButton;

    @AndroidFindBy(id = "recording_button_2")
    @iOSXCUITFindBy(accessibility = "recording_button_2")
    private WebElement recordingCancelButton;

    //Time recording confirmation view
    @AndroidFindBy(id = "recording_title")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Programmation prise en compte'")
    private WebElement timeConfirmationTitle;

    @AndroidFindBy(id = "recording_description")
    @iOSXCUITFindBy(iOSNsPredicate = "label CONTAINS 'Retrouvez-la dans quelques minutes dans'")
    private WebElement timeConfirmationText;

    @AndroidFindBy(id = "recording_button_1")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'OK'")
    private WebElement timeConfirmationButton;
    
    /**
     * Delete query view
     */
    @AndroidFindBy(id = "custom_dialog_title")
    @iOSXCUITFindBy(accessibility = "dialog_screen_uilabel")
    private WebElement deleteViewTitle;

    @AndroidFindBy(id = "dialog_message_text")
    @iOSXCUITFindBy(accessibility = "dialog_screen_uilabel_1")
    private WebElement deleteViewText;

    @AndroidFindBy(id = "custom_dialog_button_primary_positive")
    @iOSXCUITFindBy(accessibility = "idialog_manager_alert_controller_custom_uibutton_3")
    private WebElement deleteViewButtonPositive;

    @AndroidFindBy(id = "custom_dialog_button_secondary_negative")
    @iOSXCUITFindBy(accessibility = "idialog_manager_alert_controller_custom_uibutton_4")
    private WebElement deleteViewButtonNegative;

    /**
     * Add new PO for the multiples records
     */

    @AndroidFindBy(id = "episode_recording_series_name")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'pvrtime_picker.pvrtime_picker_view_pvrtime_picker.pvrcreate_serie_title_cell')]")
    private WebElement episodeRecordingSeriesName;

    @AndroidFindBy(id = "episode_recording_episode_info")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'pvrtime_picker.pvrtime_picker_view_pvrtime_picker.pvrmulti_create_cell')]/XCUIElementTypeStaticText[@name=\"pvrtime_picker.pvrtime_picker_view_uilabel\"]")
    private List<WebElement> episodeRecordingEpisodeInfo;

    @AndroidFindBy(id = "episode_recording_check_box")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'pvrtime_picker.pvrtime_picker_view_pvrtime_picker.pvrmulti_create_cell')]/XCUIElementTypeImage")
    private List<WebElement> episodeRecordingCheckBox;

    @AndroidFindBy(id = "episode_recording_episode_start_end_time")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'pvrtime_picker.pvrtime_picker_view_pvrtime_picker.pvrmulti_create_cell')]/XCUIElementTypeStaticText[@name=\"pvrtime_picker.pvrtime_picker_view_uilabel_1\"]")
    private WebElement episodeRecordingEpisodeStartEndTime;

    @AndroidFindBy(id = "recording_selection")
    @iOSXCUITFindBy(iOSNsPredicate = "label == \"PROGRAMMER\"")
    private WebElement recordSelectedRecordsButton;

    @AndroidFindBy(id = "recording_all")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'PROGRAMMER TOUS LES ÉPISODES'")
    private WebElement recordAllRecordsButton;

    public void recordingsViewElementsShown() {
        storageRemainingText.isDisplayed();
        storageRemainingBar.isDisplayed();
        recordedBarButton.isDisplayed();
        programmedBarButton.isDisplayed();
    }

    public void programItemShown(int itemNumber) {
        recordingProgramChannelLogo.get(itemNumber).isDisplayed();
        recordingProgramPrimaryText.get(itemNumber).isDisplayed();
        recordingProgramSecondaryText.get(itemNumber).isDisplayed();
    }

}
