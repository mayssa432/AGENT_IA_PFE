package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.MessagingPage;
import com.orange.otvp.automation.pages.FeedbackPage;

public class MessagingSteps {

    private MessagingPage messagingPage;
    private FeedbackPage feedbackPage;

    @Given("que je suis sur la page de messagerie")
    public void queJeSuisSurLaPageDeMessagerie() {
        // Commentaire : Vérifier que la page de messagerie est affichée
        // Action : Appeler la méthode pour ouvrir la page de messagerie
        messagingPage = new MessagingPage();
        messagingPage.open();
    }

    @Then("je vois le titre de la barre d'outils \"lpui_toolbar_title\"")
    public void jeVoisLeTitreDeLaBarreDOutils(String lpui_toolbar_title) {
        // Commentaire : Vérifier que le titre de la barre d'outils est affiché
        // Action : Appeler la méthode pour vérifier le titre de la barre d'outils
        Assert.assertTrue(messagingPage.isTitleToolbarVisible(lpui_toolbar_title));
    }

    @And("je vois l'avatar de l'agent \"lpui_toolbar_agent_avatar\"")
    public void jeVoisLAvatarDeLAgent(String lpui_toolbar_agent_avatar) {
        // Commentaire : Vérifier que l'avatar de l'agent est affiché
        // Action : Appeler la méthode pour vérifier l'avatar de l'agent
        Assert.assertTrue(messagingPage.isAgentAvatarVisible(lpui_toolbar_agent_avatar));
    }

    @And("je vois le bouton de navigation \"Revenir en haut de la page\"")
    public void jeVoisLeBoutonDeNavigation(String revenirEnHautDeLaPage) {
        // Commentaire : Vérifier que le bouton de navigation est affiché
        // Action : Appeler la méthode pour vérifier le bouton de navigation
        Assert.assertTrue(messagingPage.isNavigationButtonVisible(revenirEnHautDeLaPage));
    }

    @And("je vois le bouton de menu \"Plus d'options\"")
    public void jeVoisLeBoutonDeMenu(String plusDOptions) {
        // Commentaire : Vérifier que le bouton de menu est affiché
        // Action : Appeler la méthode pour vérifier le bouton de menu
        Assert.assertTrue(messagingPage.isMenuButtonVisible(plusDOptions));
    }

    @And("je vois la liste des éléments d'options \"content\"")
    public void jeVoisLaListeDesElementsDOptions(String content) {
        // Commentaire : Vérifier que la liste des éléments d'options est affichée
        // Action : Appeler la méthode pour vérifier la liste des éléments d'options
        Assert.assertTrue(messagingPage.isOptionsListVisible(content));
    }

    @When("je tape un message dans le champ de texte \"lpui_enter_message_text\"")
    public void jeTapeUnMessageDansLeChampDeTexte(String lpui_enter_message_text) {
        // Commentaire : Tapez un message dans le champ de texte
        // Action : Appeler la méthode pour taper un message dans le champ de texte
        messagingPage.typeMessage(lpui_enter_message_text);
    }

    @And("je clique sur le bouton d'envoi \"lpui_enter_message_send\"")
    public void jeCliqueSurLeBoutonDEnvoi(String lpui_enter_message_send) {
        // Commentaire : Cliquez sur le bouton d'envoi
        // Action : Appeler la méthode pour cliquer sur le bouton d'envoi
        messagingPage.clickSendMessageButton(lpui_enter_message_send);
    }

    @Then("je vois le message envoyé dans la liste des messages \"lpui_message_text\"")
    public void jeVoisLeMessageEnvoyéDansLaListeDesMessages(String lpui_message_text) {
        // Commentaire : Vérifier que le message envoyé est affiché dans la liste des messages
        // Action : Appeler la méthode pour vérifier le message envoyé
        Assert.assertTrue(messagingPage.isSendMessageVisible(lpui_message_text));
    }

    @And("je vois un message avec un bouton de réponse rapide \"QuickReplyTableViewCellQuickReplyContainerView0\"")
    public void jeVoisUnMessageAvecUnBoutonDeRéponseRapide(String quickReplyTableViewCellQuickReplyContainerView0) {
        // Commentaire : Vérifier que le message avec un bouton de réponse rapide est affiché
        // Action : Appeler la méthode pour vérifier le message avec un bouton de réponse rapide
        Assert.assertTrue(messagingPage.isQuickReplyMessageVisible(quickReplyTableViewCellQuickReplyContainerView0));
    }

    @When("je clique sur le bouton de réponse rapide")
    public void jeCliqueSurLeBoutonDeRéponseRapide() {
        // Commentaire : Cliquez sur le bouton de réponse rapide
        // Action : Appeler la méthode pour cliquer sur le bouton de réponse rapide
        messagingPage.clickQuickReplyButton();
    }

    @And("je sélectionne l'option \"Feedback\"")
    public void jeSélectionneLOptionFeedback() {
        // Commentaire : Sélectionnez l'option "Feedback"
        // Action : Appeler la méthode pour sélectionner l'option "Feedback"
        feedbackPage = new FeedbackPage();
        feedbackPage.selectFeedbackOption();
    }

    @Then("je vois le bouton de skip de feedback \"CustomerSatisfactionSkipButton\"")
    public void jeVoisLeBoutonDeSkipDeFeedback(String customerSatisfactionSkipButton) {
        // Commentaire : Vérifier que le bouton de skip de feedback est affiché
        // Action : Appeler la méthode pour vérifier le bouton de skip de feedback
        Assert.assertTrue(feedbackPage.isSkipButtonVisible(customerSatisfactionSkipButton));
    }

    @And("je vois l'avatar de feedback \"CustomerSatisfactionAgentAvatarImageView\"")
    public void jeVoisLAvatarDeFeedback(String customerSatisfactionAgentAvatarImageView) {
        // Commentaire : Vérifier que l'avatar de feedback est affiché
        // Action : Appeler la méthode pour vérifier l'avatar de feedback
        Assert.assertTrue(feedbackPage.isFeedbackAvatarVisible(customerSatisfactionAgentAvatarImageView));
    }

    @And("je vois le bouton de soumission de feedback \"CustomerSatisfactionSubmitButton\"")
    public void jeVoisLeBoutonDeSoumissionDeFeedback(String customerSatisfactionSubmitButton) {
        // Commentaire : Vérifier que le bouton de soumission de feedback est affiché
        // Action : Appeler la méthode pour vérifier le bouton de soumission de feedback
        Assert.assertTrue(feedbackPage.isSubmitButtonVisible(customerSatisfactionSubmitButton));
    }

    @When("je clique sur le bouton de navigation \"Revenir en haut de la page\"")
    public void jeCliqueSurLeBoutonDeNavigation(String revenirEnHautDeLaPage) {
        // Commentaire : Cliquez sur le bouton de navigation
        // Action : Appeler la méthode pour cliquer sur le bouton de navigation
        messagingPage.clickNavigationButton(revenirEnHautDeLaPage);
    }

    @Then("je ne vois plus la page de messagerie")
    public void jeNeVoisPlusLaPageDeMessagerie() {
        // Commentaire : Vérifier que la page de messagerie n'est plus visible
        // Action : Appeler la méthode pour vérifier que la page de messagerie n'est plus visible
        Assert.assertFalse(messagingPage.isPageVisible());
    }
}