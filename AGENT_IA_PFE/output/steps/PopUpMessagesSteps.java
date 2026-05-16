package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.PopUpMessagesPage;
import com.orange.otvp.automation.pages.HomePage;

public class PopUpMessagesSteps {

    private PopUpMessagesPage popUpMessagesPage;
    private HomePage homePage;

    @Given("que l'application est ouverte")
    public void queLApplicationEstOuverte() {
        // Commentaire : Ouvrir l'application
        // Action : Ouvrir l'application en utilisant la méthode open() de la classe HomePage
        homePage = new HomePage();
        homePage.open();
    }

    @Given("que l'application est ouverte pour la première fois")
    public void queLApplicationEstOuvertePourLaPremiereFois() {
        // Commentaire : Ouvrir l'application pour la première fois
        // Action : Ouvrir l'application en utilisant la méthode openFirstTime() de la classe HomePage
        homePage = new HomePage();
        homePage.openFirstTime();
    }

    @Given("que le pop-up message personnalisé est affiché")
    public void queLePopUpMessagePersonnaliseEstAffiche() {
        // Commentaire : Afficher le pop-up message personnalisé
        // Action : Appeler la méthode showCustomPopUpMessage() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.showCustomPopUpMessage();
    }

    @When("je clique sur un élément qui déclenche un pop-up message personnalisé")
    public void jeCliqueSurUnElementQuiDeclencheUnPopUpMessagePersonnalise() {
        // Commentaire : Clique sur un élément qui déclenche un pop-up message personnalisé
        // Action : Appeler la méthode clickOnElementToShowCustomPopUpMessage() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.clickOnElementToShowCustomPopUpMessage();
    }

    @When("je clique sur le bouton positif du pop-up message personnalisé")
    public void jeCliqueSurLeBoutonPositifDuPopUpMessagePersonnalise() {
        // Commentaire : Clique sur le bouton positif du pop-up message personnalisé
        // Action : Appeler la méthode clickOnPositiveButton() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.clickOnPositiveButton();
    }

    @When("je clique sur le bouton négatif du pop-up message personnalisé")
    public void jeCliqueSurLeBoutonNegatifDuPopUpMessagePersonnalise() {
        // Commentaire : Clique sur le bouton négatif du pop-up message personnalisé
        // Action : Appeler la méthode clickOnNegativeButton() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.clickOnNegativeButton();
    }

    @When("je clique sur le bouton de démarrage")
    public void jeCliqueSurLeBoutonDeDémarrage() {
        // Commentaire : Clique sur le bouton de démarrage
        // Action : Appeler la méthode clickOnStartButton() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.clickOnStartButton();
    }

    @When("je reçois un rappel")
    public void jeReçoisUnRappel() {
        // Commentaire : Recevoir un rappel
        // Action : Appeler la méthode receiveReminder() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.receiveReminder();
    }

    @When("je reçois une notification")
    public void jeReçoisUneNotification() {
        // Commentaire : Recevoir une notification
        // Action : Appeler la méthode receiveNotification() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.receiveNotification();
    }

    @When("je clique sur le bouton de changement de compte")
    public void jeCliqueSurLeBoutonDeChangementDeCompte() {
        // Commentaire : Clique sur le bouton de changement de compte
        // Action : Appeler la méthode clickOnChangeAccountButton() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.clickOnChangeAccountButton();
    }

    @When("je clique sur le bouton de déconnexion")
    public void jeCliqueSurLeBoutonDeDéconnexion() {
        // Commentaire : Clique sur le bouton de déconnexion
        // Action : Appeler la méthode clickOnDisconnectButton() de la classe PopUpMessagesPage
        popUpMessagesPage = new PopUpMessagesPage();
        popUpMessagesPage.clickOnDisconnectButton();
    }

    @Then("le pop-up message personnalisé est affiché")
    public void lePopUpMessagePersonnaliseEstAffiche() {
        // Commentaire : Vérifier que le pop-up message personnalisé est affiché
        // Action : Vérifier que le titre du pop-up message personnalisé est "Titre du pop-up" en utilisant la méthode getTitle() de la classe PopUpMessagesPage
        Assert.assertTrue(popUpMessagesPage.getTitle().equals("Titre du pop-up"));
    }

    @Then("le titre du pop-up message personnalisé est {string}")
    public void leTitreDuPopUpMessagePersonnaliseEst(String titre) {
        // Commentaire : Vérifier que le titre du pop-up message personnalisé est {string}
        // Action : Vérifier que le titre du pop-up message personnalisé est {string} en utilisant la méthode getTitle() de la classe PopUpMessagesPage
        Assert.assertTrue(popUpMessagesPage.getTitle().equals(titre));
    }

    @Then("le texte du pop-up message personnalisé est {string}")
    public void leTexteDuPopUpMessagePersonnaliseEst(String texte) {
        // Commentaire : Vérifier que le texte du pop-up message personnalisé est {string}
        // Action : Vérifier que le texte du pop-up message personnalisé est {string} en utilisant la méthode getText() de la classe PopUpMessagesPage
        Assert.assertTrue(popUpMessagesPage.getText().equals(texte));
    }

    @Then("le pop-up message personnalisé disparaît")
    public void lePopUpMessagePersonnaliseDisparait() {
        // Commentaire : Vérifier que le pop-up message personnalisé disparaît
        // Action : Vérifier que le pop-up message personnalisé est invisible en utilisant la méthode isCustomPopUpMessageVisible() de la classe PopUpMessagesPage
        Assert.assertFalse(popUpMessagesPage.isCustomPopUpMessageVisible());
    }

    @Then("les pop-up messages de démarrage sont affichés")
    public void lesPopUpMessagesDeDémarrageSontAffiches() {
        // Commentaire : Vérifier que les pop-up messages de démarrage sont affichés
        // Action : Vérifier que les pop-up messages de démarrage sont affichés en utilisant la méthode areStartUpPopUpMessagesShown() de la classe PopUpMessagesPage
        Assert.assertTrue(popUpMessagesPage.areStartUpPopUpMessagesShown());
    }

    @Then("je peux cliquer sur le bouton positif pour les fermer")
    public void jePeuxCliqueSurLeBoutonPositifPourLesFermer() {
        // Commentaire : Vérifier que je peux cliquer sur le bouton positif pour fermer les pop-up messages de démarrage
        // Action : Vérifier que le bouton positif est visible en utilisant la méthode isPositiveButtonVisible() de la classe PopUpMessagesPage
        Assert.assertTrue(popUpMessagesPage.isPositiveButtonVisible());
    }

    @Then("le pop-up message de rappel est affiché")
    public void lePopUpMessageDeRappelEstAffiche() {
        // Commentaire : Vérifier que le pop-up message de rappel est affiché
        // Action : Vérifier que le titre du pop-up message de rappel est "Rappel" en utilisant la méthode getTitle() de la classe PopUpMessagesPage
        Assert.assertTrue(popUpMessagesPage.getTitle().equals("Rappel"));
    }

    @Then("le pop-up message de notification est affiché")
    public void lePopUpMessageDeNotificationEstAffiche() {
        // Commentaire : Vérifier que le pop-up message de notification est affiché
        // Action : Vérifier que le titre du pop-up message de notification est "Notification" en utilisant la méthode getTitle() de la classe PopUpMessagesPage
        Assert.assertTrue(popUpMessagesPage.getTitle().equals("Notification"));
    }

    @Then("le pop-up message de changement de compte est affiché")
    public void lePopUpMessageDeChangementDeCompteEstAffiche() {
        // Commentaire : Vérifier que le pop-up message de changement de compte est affiché
        // Action : Vérifier que le titre du pop-up message de changement de compte est "Changement de