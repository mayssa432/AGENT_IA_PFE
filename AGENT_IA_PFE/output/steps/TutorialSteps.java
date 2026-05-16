package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.TutorialPage;
import com.orange.otvp.automation.pages.TutorialViewPage;

public class TutorialSteps {

    private TutorialPage tutorialPage;
    private TutorialViewPage tutorialViewPage;

    @Given("que je suis sur la page de tutoriel")
    public void queJeSuisSurLaPageDeTutoriel() {
        // Commentaire : Initialiser la page de tutoriel
        // Action : Appeler la méthode pour naviguer vers la page de tutoriel
        tutorialPage = new TutorialPage();
        tutorialPage.navigateToTutorialPage();
    }

    @When("je regarde la page")
    public void jeRegardeLaPage() {
        // Commentaire : Récupérer les éléments de la page de tutoriel
        // Action : Appeler la méthode pour récupérer les éléments de la page de tutoriel
        tutorialPage.getTutorialElements();
    }

    @Then("je vois le header de la liste de découverte")
    public void jeVoisLeHeaderDeLaListeDeDécouverte() {
        // Commentaire : Vérifier la présence du header de la liste de découverte
        // Action : Appeler la méthode pour vérifier la présence du header de la liste de découverte
        Assert.assertTrue(tutorialPage.isDiscoveryHeaderVisible());
    }

    @Then("je vois la liste des éléments de découverte")
    public void jeVoisLaListeDesElementsDeDécouverte() {
        // Commentaire : Vérifier la présence de la liste des éléments de découverte
        // Action : Appeler la méthode pour vérifier la présence de la liste des éléments de découverte
        Assert.assertTrue(tutorialPage.isDiscoveryListVisible());
    }

    @Then("je vois le header du tutoriel")
    public void jeVoisLeHeaderDuTutoriel() {
        // Commentaire : Vérifier la présence du header du tutoriel
        // Action : Appeler la méthode pour vérifier la présence du header du tutoriel
        Assert.assertTrue(tutorialPage.isTutorialHeaderVisible());
    }

    @Then("je vois le corps du tutoriel")
    public void jeVoisLeCorpsDuTutoriel() {
        // Commentaire : Vérifier la présence du corps du tutoriel
        // Action : Appeler la méthode pour vérifier la présence du corps du tutoriel
        Assert.assertTrue(tutorialPage.isTutorialBodyVisible());
    }

    @Then("je vois le pied de page du tutoriel")
    public void jeVoisLePiedDePageDuTutoriel() {
        // Commentaire : Vérifier la présence du pied de page du tutoriel
        // Action : Appeler la méthode pour vérifier la présence du pied de page du tutoriel
        Assert.assertTrue(tutorialPage.isTutorialFooterVisible());
    }

    @Then("je vois le bouton \"Partager ma TV d'Orange\"")
    public void jeVoisLeBoutonPartagerMaTVdOrange() {
        // Commentaire : Vérifier la présence du bouton "Partager ma TV d'Orange"
        // Action : Appeler la méthode pour vérifier la présence du bouton "Partager ma TV d'Orange"
        Assert.assertTrue(tutorialPage.isShareButtonVisible());
    }

    @Then("je vois le bouton \"Enregistrer un contenu\"")
    public void jeVoisLeBoutonEnregistrerUnContenu() {
        // Commentaire : Vérifier la présence du bouton "Enregistrer un contenu"
        // Action : Appeler la méthode pour vérifier la présence du bouton "Enregistrer un contenu"
        Assert.assertTrue(tutorialPage.isSaveButtonVisible());
    }

    @Then("je vois le bouton \"Caster un contenu\"")
    public void jeVoisLeBoutonCasterUnContenu() {
        // Commentaire : Vérifier la présence du bouton "Caster un contenu"
        // Action : Appeler la méthode pour vérifier la présence du bouton "Caster un contenu"
        Assert.assertTrue(tutorialPage.isCastButtonVisible());
    }

    @Then("je vois le bouton \"Utiliser la télécommande\"")
    public void jeVoisLeBoutonUtiliserLaTélécommande() {
        // Commentaire : Vérifier la présence du bouton "Utiliser la télécommande"
        // Action : Appeler la méthode pour vérifier la présence du bouton "Utiliser la télécommande"
        Assert.assertTrue(tutorialPage.isRemoteButtonVisible());
    }

    @Then("je vois le bouton \"Reprendre du début\"")
    public void jeVoisLeBoutonReprendreDuDébut() {
        // Commentaire : Vérifier la présence du bouton "Reprendre du début"
        // Action : Appeler la méthode pour vérifier la présence du bouton "Reprendre du début"
        Assert.assertTrue(tutorialPage.isRestartButtonVisible());
    }

    @When("je clique sur le bouton \"Reprendre du début\"")
    public void jeCliqueSurLeBoutonReprendreDuDébut() {
        // Commentaire : Clique sur le bouton "Reprendre du début"
        // Action : Appeler la méthode pour cliquer sur le bouton "Reprendre du début"
        tutorialPage.clickRestartButton();
    }

    @Then("je suis redirigé vers le début du tutoriel")
    public void jeSuisRedirigéVersLeDébutDuTutoriel() {
        // Commentaire : Vérifier que l'utilisateur est redirigé vers le début du tutoriel
        // Action : Appeler la méthode pour vérifier que l'utilisateur est redirigé vers le début du tutoriel
        Assert.assertTrue(tutorialPage.isTutorialStarted());
    }

    @When("je clique sur le bouton \"Partager ma TV d'Orange\"")
    public void jeCliqueSurLeBoutonPartagerMaTVdOrange() {
        // Commentaire : Clique sur le bouton "Partager ma TV d'Orange"
        // Action : Appeler la méthode pour cliquer sur le bouton "Partager ma TV d'Orange"
        tutorialPage.clickShareButton();
    }

    @Then("je suis redirigé vers la page de partage de ma TV d'Orange")
    public void jeSuisRedirigéVersLaPageDePartageDeMaTVdOrange() {
        // Commentaire : Vérifier que l'utilisateur est redirigé vers la page de partage de ma TV d'Orange
        // Action : Appeler la méthode pour vérifier que l'utilisateur est redirigé vers la page de partage de ma TV d'Orange
        Assert.assertTrue(tutorialPage.isSharePageVisible());
    }

    @When("je clique sur le bouton \"Jouer au tutoriel\"")
    public void jeCliqueSurLeBoutonJouerAuTutoriel() {
        // Commentaire : Clique sur le bouton "Jouer au tutoriel"
        // Action : Appeler la méthode pour cliquer sur le bouton "Jouer au tutoriel"
        tutorialPage.clickPlayButton();
    }

    @Then("je suis redirigé vers le tutoriel")
    public void jeSuisRedirigéVersLeTutoriel() {
        // Commentaire : Vérifier que l'utilisateur est redirigé vers le tutoriel
        // Action : Appeler la méthode pour vérifier que l'utilisateur est redirigé vers le tutoriel
        Assert.assertTrue(tutorialPage.isTutorialVisible());
    }

    @When("je clique sur le bouton de fermeture de la vue de tutoriel")
    public void jeCliqueSurLeBoutonDeFermetureDeLaVueDeTutoriel() {
        // Commentaire : Clique sur le bouton de fermeture de la vue de tutoriel
        // Action : Appeler la méthode pour cliquer sur le bouton de fermeture de la vue de tutoriel
        tutorialViewPage.clickCloseButton();
    }

    @Then("la vue de tutoriel est fermée")
    public void laVueDeTutorielEstFermée() {
        // Commentaire : Vérifier que la vue de tutoriel est fermée
        // Action : Appeler la méthode pour vérifier que la vue de tutoriel est fermée
        Assert.assertFalse(tutorialViewPage.isTutorialVisible());
    }
}