package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.NoSuchElementException;
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
public class TutorialPO {

    AppiumDriver driver;

    public TutorialPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(xpath = "//*[@resource-id='tutorial_list_header']")
    @iOSXCUITFindBy(accessibility = "tutorial_list_header")
    private WebElement discoveryListHeader;

    @AndroidFindBy(xpath = "//*[@resource-id='onei_list_item']")
    @iOSXCUITFindBy(accessibility = "onei_list_item")
    private List<WebElement> discoveryListItem;

    @AndroidFindBy(xpath = "//*[@resource-id='tutorial_header']")
    @iOSXCUITFindBy(accessibility = "tutorial_header")
    private WebElement tutorialBack;

    @AndroidFindBy(xpath = "//*[@resource-id='tutorial_body']")
    @iOSXCUITFindBy(accessibility = "tutorial_body")
    private WebElement tutorialBody;

    @AndroidFindBy(xpath = "//*[@resource-id='tutorial_button']")
    @iOSXCUITFindBy(accessibility = "tutorial_footer")
    private WebElement tutorialFooter;

    @AndroidFindBy(xpath = "//*[@text=\"Partager ma TV d'Orange\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "value == \"Partager ma TV d'Orange\"")
    private WebElement shareTutorial;

    @AndroidFindBy(xpath = "//*[@text=\"Enregistrer un contenu\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "value == \"Enregistrer un contenu\"")
    private WebElement recordingTutorial;

    @AndroidFindBy(xpath = "//*[@text=\"Caster un contenu\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "value == \"Caster un contenu\"")
    private WebElement castTutorial;

    @AndroidFindBy(xpath = "//*[@text=\"Utiliser la télécommande\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "value == \"Utiliser la télécommande\"")
    private WebElement remoteTutorial;

    @AndroidFindBy(xpath = "//*[@text=\"Reprendre du début\"]")
    @iOSXCUITFindBy(iOSNsPredicate = "value == \"Reprendre du début\"")
    private WebElement startOverTutorial;

    // Old tutorial view at start up
    @AndroidFindAll({
            @AndroidBy(id = "onboarding_share_close"),
            @AndroidBy(id = "cast_tutorial_accept_button")
    })
    @iOSXCUITFindAll({
            @iOSXCUITBy(accessibility = "onboarding_message_custom_uibutton_1"),
            @iOSXCUITBy(accessibility = "play_to_tutorial_uibutton_1")})
    private WebElement playToTutorialButton;

    public void clearTutorialView() {
        try {
            playToTutorialButton.click();
        }
        catch (NoSuchElementException e) {
        }
    }

}
