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
public class TrustBadgePO {

    AppiumDriver driver;

    public TrustBadgePO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "otb_header_tv_appName")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.landing_controller_uilabel")
    private WebElement dataUsageAppName;

    @AndroidFindBy(id = "otb_header_tv_subtitle")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.landing_controller_uilabel_1")
    private WebElement dataUsageHeader;

    @AndroidFindBy(id = "otb_home_subtitle")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.landing_controller_uilabel")
    private WebElement dataUsageSubtitle;

    @AndroidFindBy(id = "otb_home_data_card")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_orange_trust_badge.element_menu_cell_2"),
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_uitable_view_cell_2") //Tablet
    })

    private WebElement dataUsageDataCard;

    @AndroidFindBy(id = "otb_data_usage_item_ll")
    @AndroidFindBy(className = "android.widget.LinearLayout")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.device_permissions_controller_uiview")
    private List<WebElement> dataViewItems;

    @AndroidFindBy(id = "otb_permissions_bt_parameter")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Modifier cette autorisation'")
    private WebElement dataViewBtnParameter;

    @AndroidFindBy(id = "otb_home_usage_card")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_orange_trust_badge.element_menu_cell_1"),
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_uitable_view_cell_1") //Tablet
    })
    private WebElement dataUsageUsageCard;

    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "//*[contains(@name,'orange_trust_badge.landing_controller_orange_trust_badge.element_menu_cell')]"),
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_uiview") //Tablet
    })
    private List<WebElement> dataUsageCardsIOS;

    @AndroidFindBy(id = "otb_app_data_layout")
    @AndroidFindBy(className = "android.widget.LinearLayout")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'orange_trust_badge.application_data_table_orange_trust_badge.element_cell')]")
    private List<WebElement> usageViewItems;

    @AndroidFindBy(id = "otb_data_usage_tv_goto")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Modifier cette autorisation'")
    private WebElement usageViewBtnParameter;

    @AndroidFindBy(id = "otb_data_usage_item_sc_switch")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeSwitch")
    private WebElement usageViewAudienceMeasurementSwitch;

    @AndroidFindBy(id = "otb_home_terms_card")
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_orange_trust_badge.terms_menu_cell"),
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_uitable_view_cell") //Tablet
    })
    private WebElement dataUsageTermsCard;

    @AndroidFindBy(id = "otb_data_manage_didomi_item_btn_manage")
    @iOSXCUITFindBy(accessibility = "orange_trust_badge.application_data_table_ob1.obobutton_1")
    private WebElement manageConsentButton;

    @AndroidFindBy(id = "otb_home_custom_data_card" )
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_orange_trust_badge.custom_menu_cell"),
            @iOSXCUITBy(accessibility = "orange_trust_badge.landing_controller_uitable_view_cell") //Tablet
    })

    private WebElement dataUsageDjingoCard;

    @AndroidFindBy(id = "djingo_data_protection_agreement_access_button")
    @iOSXCUITFindBy(accessibility = "djingo_trust_custom_uibutton_2")
    private WebElement djingoDataProtectionAgreementButton;

    @AndroidFindBy(id = "djingo_data_protection_agreement_confirm_checkbox")
    @iOSXCUITFindBy(accessibility = "djingo_personal_uibutton_6")
    private WebElement djingoDataProtectionAgreementCheckbox;

    @AndroidFindBy(id = "djingo_data_protection_agreement_positive_button")
    @iOSXCUITFindBy(accessibility = "djingo_personal_custom_uibutton_2")
    private WebElement djingoDataProtectionAgreementAcceptButton;

    @AndroidFindBy(id = "djingo_data_protection_agreement_negative_button_text")
    @iOSXCUITFindBy(accessibility = "djingo_personal_uibutton_3")
    private WebElement djingoDataProtectionAgreementCancelButton;

    @AndroidFindBy(id = "djingo_gdpr_agreement_item_group_switch")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeSwitch")
    private List<WebElement> djingoSwitchItems;

    @AndroidFindBy(id = "djingo_gdpr_delete_item_button")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'SUPPRIMER'")
    private List<WebElement> djingoDeleteButtons;

}
