package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.HelpPage;
import com.orange.otvp.automation.pages.ChatPage;
import com.orange.otvp.automation.pages.FaqPage;

public class HelpSteps {

    private HelpPage helpPage;
    private ChatPage chatPage;
    private FaqPage faqPage;

    @Given("que je suis sur la page d'aide")
    public void queJeSuisSurLaPageDAide() {
        // Commentaire : Récupérer l'instance de la page d'aide
        // Action : Récupérer l'instance de la page d'aide
        helpPage = new HelpPage();
    }

    @When("je regarde le titre de la page")
    public void jeRegardeLeTitreDeLaPage() {
        // Commentaire : Récupérer le titre de la page
        // Action : Récupérer le titre de la page
        String titre = helpPage.getTitre();
        Assert.assertEquals("Orange TV", titre);
    }

    @Then("je vois le titre {string}")
    public void jeVoisLeTitre(String titre) {
        // Commentaire : Vérifier que le titre est bien celui attendu
        // Action : Vérifier que le titre est bien celui attendu
        Assert.assertEquals(titre, helpPage.getTitre());
    }

    @When("je regarde la liste d'aide")
    public void jeRegardeLaListeDAide() {
        // Commentaire : Récupérer la liste d'aide
        // Action : Récupérer la liste d'aide
        helpPage.getLaListeDAide();
    }

    @Then("je vois les éléments suivants {string}")
    public void jeVoisLesElementsSuivants(String table) {
        // Commentaire : Vérifier que les éléments de la liste sont bien ceux attendus
        // Action : Vérifier que les éléments de la liste sont bien ceux attendus
        String[][] elements = HelpPage.getLesElementsDeLaListe(table);
        Assert.assertArrayEquals(elements, helpPage.getLesElementsDeLaListe());
    }

    @When("je clique sur le bouton de chat")
    public void jeCliqueSurLeBoutonDeChat() {
        // Commentaire : Clique sur le bouton de chat
        // Action : Clique sur le bouton de chat
        chatPage = helpPage.cliqueSurLeBoutonDeChat();
    }

    @Then("je suis redirigé vers la page de chat")
    public void jeSuisRedirigeVersLaPageDeChat() {
        // Commentaire : Vérifier que l'utilisateur est bien redirigé vers la page de chat
        // Action : Vérifier que l'utilisateur est bien redirigé vers la page de chat
        Assert.assertNotNull(chatPage);
    }

    @When("je regarde les titres des FAQs")
    public void jeRegardeLesTitresDesFaqs() {
        // Commentaire : Récupérer les titres des FAQs
        // Action : Récupérer les titres des FAQs
        faqPage = helpPage.getLesTitresDesFaqs();
    }

    @Then("je vois les titres suivants {string}")
    public void jeVoisLesTitresSuivants(String table) {
        // Commentaire : Vérifier que les titres des FAQs sont bien ceux attendus
        // Action : Vérifier que les titres des FAQs sont bien ceux attendus
        String[][] titres = HelpPage.getLesTitresDesFaqs(table);
        Assert.assertArrayEquals(titres, faqPage.getLesTitresDesFaqs());
    }

    @When("je clique sur l'élément 1 de la liste d'aide")
    public void jeCliqueSurLElément1DeLaListeDAide() {
        // Commentaire : Clique sur l'élément 1 de la liste d'aide
        // Action : Clique sur l'élément 1 de la liste d'aide
        helpPage.cliqueSurLElément1DeLaListeDAide();
    }

    @Then("je vois le contenu de l'élément 1")
    public void jeVoisLeContenuDELElément1() {
        // Commentaire : Vérifier que le contenu de l'élément 1 est bien celui attendu
        // Action : Vérifier que le contenu de l'élément 1 est bien celui attendu
        Assert.assertEquals("Chatter avec un conseiller Orange", helpPage.getLeContenuDELElément1());
    }

    @When("je clique sur le bouton de chatter")
    public void jeCliqueSurLeBoutonDeChatter() {
        // Commentaire : Clique sur le bouton de chatter
        // Action : Clique sur le bouton de chatter
        chatPage = helpPage.cliqueSurLeBoutonDeChatter();
    }

    @Then("je suis redirigé vers la page de chatter")
    public void jeSuisRedirigeVersLaPageDeChatter() {
        // Commentaire : Vérifier que l'utilisateur est bien redirigé vers la page de chatter
        // Action : Vérifier que l'utilisateur est bien redirigé vers la page de chatter
        Assert.assertNotNull(chatPage);
    }

    @When("je regarde les questions des FAQs")
    public void jeRegardeLesQuestionsDesFaqs() {
        // Commentaire : Récupérer les questions des FAQs
        // Action : Récupérer les questions des FAQs
        faqPage = helpPage.getLesQuestionsDesFaqs();
    }

    @Then("je vois les questions suivantes {string}")
    public void jeVoisLesQuestionsSuivantes(String table) {
        // Commentaire : Vérifier que les questions des FAQs sont bien celles attendues
        // Action : Vérifier que les questions des FAQs sont bien celles attendues
        String[][] questions = HelpPage.getLesQuestionsDesFaqs(table);
        Assert.assertArrayEquals(questions, faqPage.getLesQuestionsDesFaqs());
    }
}