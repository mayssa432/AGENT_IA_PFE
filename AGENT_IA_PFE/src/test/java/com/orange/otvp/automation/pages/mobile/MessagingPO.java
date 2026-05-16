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
public class MessagingPO {

    AppiumDriver driver;

    public MessagingPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "lpui_toolbar_title")
    private WebElement toolbarTitle;

    @AndroidFindBy(id = "lpui_toolbar_agent_avatar")
    private WebElement toolbarAgentAvatar;

    @AndroidFindBy(xpath = "//android.widget.ImageButton[@content-desc='Revenir en haut de la page']")
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Fermer'")
    private WebElement navigationUp;

    @AndroidFindAll({
            @AndroidBy(xpath = "//android.widget.ImageView[@content-desc=\"Plus d'options\"]"),
            @AndroidBy(xpath = "//android.widget.ImageView[@content-desc='Options supplémentaires']")
    })
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'Menu'")
    private WebElement menuButton;

    @AndroidFindBy(id = "content")
    @iOSXCUITFindBy(accessibility = "lpmessaging_sdk.action_menu_controller_uialert_controller_action_view")

    private List<WebElement> optionItems;

    @AndroidFindAll({
            @AndroidBy(xpath = "//*[contains(@text,'TERMINER')]"),
            @AndroidBy(xpath = "//*[contains(@text,'EFFACER')]"),
            @AndroidBy(id = "button1"),
    })
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "(//XCUIElementTypeStaticText[@name='uialert_controller_uilabel'])[1]"),
            @iOSXCUITBy(xpath = "(//XCUIElementTypeButton[@name='uialert_controller_uialert_controller_action_view'])[1]")
    })
    private WebElement buttonValid;

    @AndroidFindBy(id = "button2")
    @iOSXCUITFindAll({
            @iOSXCUITBy(xpath = "(//XCUIElementTypeStaticText[@name='uialert_controller_uilabel'])[2]"),
            @iOSXCUITBy(xpath = "(//XCUIElementTypeButton[@name='uialert_controller_uialert_controller_action_view'])[2]")})
    private WebElement buttonCancel;


    @AndroidFindBy(id = "lpui_toolbar_feedback_action")
    @iOSXCUITFindBy(accessibility = "CustomerSatisfactionSkipButton")
    private WebElement feedbackSkipButton;

    @AndroidFindBy(id = "lpui_feedback_avatar_view_details")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'CustomerSatisfactionAgentAvatarImageView'")
    private WebElement feedbackAvatar;

    @AndroidFindBy(id = "lpui_feedback_submit_button")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'CustomerSatisfactionSubmitButton'")
    private WebElement feedbackSubmitButton;

    @AndroidFindBy(xpath = "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[contains(@resource-id,'lpui_message_text')]")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeCell[@name='ConversationViewControllerUserMessageTableViewCell-userMsg-nil']//*[contains (@name,'lpmessaging_sdk.conversation_lptttattributed_label')]")
    private List<WebElement> userMessages;

    @AndroidFindBy(id = "lpui_message_text" )
    @iOSXCUITFindBy(accessibility = "lpmessaging_sdk.conversation_lptttattributed_label")
    private List<WebElement> remoteMessages;

    @AndroidFindBy(id = "button_element")
    @iOSXCUITFindBy(xpath = "//*[contains (@name,'QuickReplyTableViewCellQuickReplyContainerView0')]")
    private List<WebElement> buttonElements;

    @AndroidFindBy(id = "lpui_enter_message_text")
    @iOSXCUITFindBy(accessibility = "InputTextView")
    private WebElement messageText;

    @AndroidFindBy(id = "lpui_enter_message_send")
    @iOSXCUITFindBy(iOSNsPredicate = "name == 'InputTextViewSendButton'")
    private WebElement sendMessageButton;
}
