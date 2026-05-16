package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.RecorderPage;

public class RecorderSteps {

    private RecorderPage recorderPage;

    @Given("que l'utilisateur est sur la page d'accueil")
    public void queLUtilisateurEstSurLaPageDAccueil() {
        // Commentaire : Initialisation de la page RecorderPage
        // Action : Appel de la méthode navigateToHomePage de la page RecorderPage
        recorderPage = new RecorderPage();
        recorderPage.navigateToHomePage();
    }

    @When("l'utilisateur clique sur le bouton \"Enregistrements\"")
    public void lUtilisateurCliqueSurLeBoutonEnregistrements() {
        // Commentaire : Clique sur le bouton "Enregistrements"
        // Action : Appel de la méthode clickOnEnregistrementsButton de la page RecorderPage
        recorderPage.clickOnEnregistrementsButton();
    }

    @Then("la liste des enregistrements est affichée")
    public void laListeDesEnregistrementsEstAffichée() {
        // Commentaire : Vérification de la liste des enregistrements
        // Action : Appel de la méthode isEnregistrementsListDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isEnregistrementsListDisplayed());
    }

    @And("le bouton \"Enregistrer\" est visible")
    public void leBoutonEnregistrerEstVisible() {
        // Commentaire : Vérification du bouton "Enregistrer"
        // Action : Appel de la méthode isEnregistrerButtonDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isEnregistrerButtonDisplayed());
    }

    @And("le bouton \"Programmer\" est visible")
    public void leBoutonProgrammerEstVisible() {
        // Commentaire : Vérification du bouton "Programmer"
        // Action : Appel de la méthode isProgrammerButtonDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isProgrammerButtonDisplayed());
    }

    @Given("que l'utilisateur est sur la page d'enregistrement")
    public void queLUtilisateurEstSurLaPageDenregistrement() {
        // Commentaire : Initialisation de la page RecorderPage
        // Action : Appel de la méthode navigateToEnregistrementPage de la page RecorderPage
        recorderPage.navigateToEnregistrementPage();
    }

    @When("l'utilisateur sélectionne un programme à enregistrer")
    public void lUtilisateurSelectionneUnProgrammeAEnregistrer() {
        // Commentaire : Sélection d'un programme à enregistrer
        // Action : Appel de la méthode selectProgrammeToEnregistrer de la page RecorderPage
        recorderPage.selectProgrammeToEnregistrer();
    }

    @And("l'utilisateur clique sur le bouton \"Enregistrer\"")
    public void lUtilisateurCliqueSurLeBoutonEnregistrer() {
        // Commentaire : Clique sur le bouton "Enregistrer"
        // Action : Appel de la méthode clickOnEnregistrerButton de la page RecorderPage
        recorderPage.clickOnEnregistrerButton();
    }

    @Then("le programme est enregistré avec succès")
    public void leProgrammeEstEnregistreAvecSucces() {
        // Commentaire : Vérification de la réussite de l'enregistrement
        // Action : Appel de la méthode isEnregistrementSuccessful de la page RecorderPage
        Assert.assertTrue(recorderPage.isEnregistrementSuccessful());
    }

    @And("un message de confirmation est affiché")
    public void unMessageDeConfirmationEstAffiche() {
        // Commentaire : Vérification du message de confirmation
        // Action : Appel de la méthode isConfirmationMessageDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isConfirmationMessageDisplayed());
    }

    @Given("que l'utilisateur est sur la page de programmation")
    public void queLUtilisateurEstSurLaPageDeProgrammation() {
        // Commentaire : Initialisation de la page RecorderPage
        // Action : Appel de la méthode navigateToProgrammationPage de la page RecorderPage
        recorderPage.navigateToProgrammationPage();
    }

    @When("l'utilisateur sélectionne un programme à programmer")
    public void lUtilisateurSelectionneUnProgrammeAProgrammer() {
        // Commentaire : Sélection d'un programme à programmer
        // Action : Appel de la méthode selectProgrammeToProgrammer de la page RecorderPage
        recorderPage.selectProgrammeToProgrammer();
    }

    @And("l'utilisateur clique sur le bouton \"Programmer\"")
    public void lUtilisateurCliqueSurLeBoutonProgrammer() {
        // Commentaire : Clique sur le bouton "Programmer"
        // Action : Appel de la méthode clickOnProgrammerButton de la page RecorderPage
        recorderPage.clickOnProgrammerButton();
    }

    @Then("le programme est programmé avec succès")
    public void leProgrammeEstProgrammeAvecSucces() {
        // Commentaire : Vérification de la réussite de la programmation
        // Action : Appel de la méthode isProgrammationSuccessful de la page RecorderPage
        Assert.assertTrue(recorderPage.isProgrammationSuccessful());
    }

    @And("un message de confirmation est affiché")
    public void unMessageDeConfirmationEstAffiche1() {
        // Commentaire : Vérification du message de confirmation
        // Action : Appel de la méthode isConfirmationMessageDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isConfirmationMessageDisplayed());
    }

    @Given("que l'utilisateur est sur la page d'enregistrements")
    public void queLUtilisateurEstSurLaPageDenregistrements() {
        // Commentaire : Initialisation de la page RecorderPage
        // Action : Appel de la méthode navigateToEnregistrementsPage de la page RecorderPage
        recorderPage.navigateToEnregistrementsPage();
    }

    @When("l'utilisateur sélectionne un enregistrement à supprimer")
    public void lUtilisateurSelectionneUnEnregistrementASupprimer() {
        // Commentaire : Sélection d'un enregistrement à supprimer
        // Action : Appel de la méthode selectEnregistrementToDelete de la page RecorderPage
        recorderPage.selectEnregistrementToDelete();
    }

    @And("l'utilisateur clique sur le bouton \"Supprimer\"")
    public void lUtilisateurCliqueSurLeBoutonSupprimer() {
        // Commentaire : Clique sur le bouton "Supprimer"
        // Action : Appel de la méthode clickOnSupprimerButton de la page RecorderPage
        recorderPage.clickOnSupprimerButton();
    }

    @Then("l'enregistrement est supprimé avec succès")
    public void lEnregistrementEstSupprimeAvecSucces() {
        // Commentaire : Vérification de la réussite de la suppression
        // Action : Appel de la méthode isEnregistrementDeleted de la page RecorderPage
        Assert.assertTrue(recorderPage.isEnregistrementDeleted());
    }

    @And("un message de confirmation est affiché")
    public void unMessageDeConfirmationEstAffiche2() {
        // Commentaire : Vérification du message de confirmation
        // Action : Appel de la méthode isConfirmationMessageDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isConfirmationMessageDisplayed());
    }

    @Given("que l'utilisateur est sur la page d'enregistrements")
    public void queLUtilisateurEstSurLaPageDenregistrements1() {
        // Commentaire : Initialisation de la page RecorderPage
        // Action : Appel de la méthode navigateToEnregistrementsPage de la page RecorderPage
        recorderPage.navigateToEnregistrementsPage();
    }

    @When("l'utilisateur clique sur un enregistrement")
    public void lUtilisateurCliqueSurUnEnregistrement() {
        // Commentaire : Clique sur un enregistrement
        // Action : Appel de la méthode clickOnEnregistrement de la page RecorderPage
        recorderPage.clickOnEnregistrement();
    }

    @Then("les détails de l'enregistrement sont affichés")
    public void lesDetailsDeLEnregistrementSontAffiches() {
        // Commentaire : Vérification des détails de l'enregistrement
        // Action : Appel de la méthode isEnregistrementDetailsDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isEnregistrementDetailsDisplayed());
    }

    @And("le titre de l'enregistrement est visible")
    public void leTitreDeLEnregistrementEstVisible() {
        // Commentaire : Vérification du titre de l'enregistrement
        // Action : Appel de la méthode isEnregistrementTitleDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isEnregistrementTitleDisplayed());
    }

    @And("la description de l'enregistrement est visible")
    public void laDescriptionDeLEnregistrementEstVisible() {
        // Commentaire : Vérification de la description de l'enregistrement
        // Action : Appel de la méthode isEnregistrementDescriptionDisplayed de la page RecorderPage
        Assert.assertTrue(recorderPage.isEnregistrementDescriptionDisplayed());
    }
}