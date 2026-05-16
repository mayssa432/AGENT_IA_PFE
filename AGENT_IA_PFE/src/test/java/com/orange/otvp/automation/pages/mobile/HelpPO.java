package com.orange.otvp.automation.pages.mobile;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.util.List;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import lombok.Getter;

@Getter
public class HelpPO {

    AppiumDriver driver;

    public HelpPO(AppiumDriver driver) {
        this.driver = driver;
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(5)), this);
    }

    @AndroidFindBy(id = "one_i_list_item_section_text")
    @iOSXCUITFindBy(accessibility = "help_and_contact_main_uitable_view_label")
    private WebElement mainText;

    @AndroidFindBy(accessibility = "one_i_list_item_primary_text")
    @iOSXCUITFindBy(accessibility = "help_and_contact_main_uitable_view_label")
    private List<WebElement> elementTexts;

    @AndroidFindBy(className = "android.view.ViewGroup")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'help_and_contact_main_uitable_view_cell')]")
    private List<WebElement> helpListElements;

    @AndroidFindBy(id = "faq_chapter_title")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'help_and_contact_faq_uitable_view_cell')]")
    private List<WebElement> faqTitles;

    @AndroidFindBy(id = "faq_list_question")
    @iOSXCUITFindBy(xpath = "//*[contains(@name,'help_and_contact_faq_uitable_view_cell')]")
    private List<WebElement> faqQuestionTopics;

    @AndroidFindBy(id = "header_title_text")
    @iOSXCUITFindBy(accessibility = "Contacter un conseiller")
    private WebElement helpHeader;

    @AndroidFindBy(xpath = "//*[@text='Orange TV']")
    @iOSXCUITFindBy( xpath = "//*[@label='Orange TV']")
    private WebElement helpTittle;

    @AndroidFindBy(xpath = "//*[@text='Chatter avec un conseiller Orange']")
    @iOSXCUITFindBy(accessibility = "Chatter avec un conseiller Orange")
    private WebElement helpText1;

    @AndroidFindBy(xpath = "//*[@text='Du']")
    @iOSXCUITFindBy(accessibility = "Du")
    private WebElement helpText2;

    @AndroidFindBy(xpath = "//*[@text='lundi au samedi de 8h à 22h']")
    @iOSXCUITFindBy(accessibility = "lundi au samedi de 8h à 22h")
    private WebElement helpText3;

    @AndroidFindBy(xpath = "//*[@text='Posez directement votre question à un conseiller.']")
    @iOSXCUITFindBy(accessibility = "Posez directement votre question à un conseiller.")
    private WebElement helpText4;

    @AndroidFindBy(xpath = "//*[@text='Chatter']")
    @iOSXCUITFindBy(accessibility = "Chatter")
    private WebElement helpChattButton;

    @AndroidFindBy(xpath = "//*[@text='icone chat']")
    @iOSXCUITFindBy(accessibility = "icone chat")
    private WebElement iconeChat;


    private void accessHelpElementByOs(int numberForAndroid, int numberForIos) {
        if (driver instanceof AndroidDriver) {
            helpListElements.get(numberForAndroid).click();
        }
        if (driver instanceof IOSDriver) {
            helpListElements.get(numberForIos).click();
        }
    }

    /**
     * For the difference between platforms, method to translate correct index number
     *
     * @param number element to be selected from the list 1-4
     */
    public void accessHelpElement(int number) {
        switch (number) {
            case 1:
                accessHelpElementByOs(0, 1);
                break;
            case 2:
                accessHelpElementByOs(1, 2);
                break;
            case 3:
                accessHelpElementByOs(2, 3);
                break;
            case 4:
                accessHelpElementByOs(3, 4);
                break;
            default:
        }
    }

}
