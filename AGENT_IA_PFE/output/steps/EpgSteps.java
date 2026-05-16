package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.EpgPage;
import com.orange.otvp.automation.pages.HomePage;
import com.orange.otvp.automation.utils.AppiumDriverFactory;
import com.orange.otvp.automation.utils.DeviceType;

public class EpgSteps {

    private EpgPage epgPage;
    private HomePage homePage;
    private AppiumDriverFactory appiumDriverFactory;

    @Given("que l'utilisateur est sur la page EPG")
    public void queLUtilisateurEstSurLaPageEpg() {
        // Commentaire : Récupération de la page EPG
        // Action : Appel de la méthode pour ouvrir la page EPG
        homePage = new HomePage();
        homePage.openEpgPage();
        epgPage = new EpgPage();
    }

    @When("l'utilisateur consulte la liste des chaînes")
    public void lUtilisateurConsulteLaListeDesChaines() {
        // Commentaire : Consultation de la liste des chaînes
        // Action : Appel de la méthode pour consulter la liste des chaînes
        epgPage.consultChannelList();
    }

    @Then("les éléments suivants sont affichés :")
    public void lesElementsSuivantsSontAffiches(io.cucumber.datatable.DataTable dataTable) {
        // Commentaire : Vérification de la présence des éléments
        // Action : Appel de la méthode pour vérifier la présence des éléments
        epgPage.verifyElements(dataTable);
    }

    @When("l'utilisateur sélectionne un programme en direct")
    public void lUtilisateurSelectionneUnProgrammeEnDirect() {
        // Commentaire : Sélection d'un programme en direct
        // Action : Appel de la méthode pour sélectionner un programme en direct
        epgPage.selectDirectProgram();
    }

    @And("l'utilisateur clique sur le bouton de lecture")
    public void lUtilisateurCliqueSurLeBoutonDeLecture() {
        // Commentaire : Lecture du programme
        // Action : Appel de la méthode pour lancer la lecture du programme
        epgPage.playDirectProgram();
    }

    @Then("le programme est lancé en lecture")
    public void leProgrammeEstLanceEnLecture() {
        // Commentaire : Vérification de la lecture du programme
        // Action : Appel de la méthode pour vérifier la lecture du programme
        Assert.assertTrue(epgPage.isProgramPlaying());
    }

    @When("l'utilisateur sélectionne un programme")
    public void lUtilisateurSelectionneUnProgramme() {
        // Commentaire : Sélection d'un programme
        // Action : Appel de la méthode pour sélectionner un programme
        epgPage.selectProgram();
    }

    @And("l'utilisateur clique sur le bouton d'informations")
    public void lUtilisateurCliqueSurLeBoutonDInformations() {
        // Commentaire : Affichage des informations du programme
        // Action : Appel de la méthode pour afficher les informations du programme
        epgPage.showProgramInfo();
    }

    @Then("les informations suivantes sont affichées :")
    public void lesInformationsSuivantesSontAffiches(io.cucumber.datatable.DataTable dataTable) {
        // Commentaire : Vérification des informations du programme
        // Action : Appel de la méthode pour vérifier les informations du programme
        epgPage.verifyProgramInfo(dataTable);
    }

    @When("l'utilisateur navigue entre les chaînes")
    public void lUtilisateurNavigueEntreLesChaines() {
        // Commentaire : Navigation entre les chaînes
        // Action : Appel de la méthode pour naviguer entre les chaînes
        epgPage.navigateBetweenChannels();
    }

    @And("l'utilisateur sélectionne un programme")
    public void lUtilisateurSlectionneUnProgramme() {
        // Commentaire : Sélection d'un programme
        // Action : Appel de la méthode pour sélectionner un programme
        epgPage.selectProgram();
    }

    @Then("les informations du programme sont affichées")
    public void lesInformationsDuProgrammeSontAffiches() {
        // Commentaire : Vérification des informations du programme
        // Action : Appel de la méthode pour vérifier les informations du programme
        Assert.assertTrue(epgPage.isProgramInfoDisplayed());
    }

    @When("l'utilisateur recherche un programme")
    public void lUtilisateurRechercheUnProgramme() {
        // Commentaire : Recherche d'un programme
        // Action : Appel de la méthode pour rechercher un programme
        epgPage.searchProgram();
    }

    @And("l'utilisateur sélectionne le programme recherché")
    public void lUtilisateurSlectionneLeProgrammeRecherche() {
        // Commentaire : Sélection du programme recherché
        // Action : Appel de la méthode pour sélectionner le programme recherché
        epgPage.selectSearchedProgram();
    }

    @Then("les informations du programme sont affichées")
    public void lesInformationsDuProgrammeSontAffiches2() {
        // Commentaire : Vérification des informations du programme
        // Action : Appel de la méthode pour vérifier les informations du programme
        Assert.assertTrue(epgPage.isProgramInfoDisplayed());
    }

    @Given("que l'utilisateur est sur la page EPG sur un appareil {string}")
    public void queLUtilisateurEstSurLaPageEpgSurUnAppareil(String deviceType) {
        // Commentaire : Récupération de la page EPG sur un appareil spécifique
        // Action : Appel de la méthode pour ouvrir la page EPG sur un appareil spécifique
        appiumDriverFactory = new AppiumDriverFactory();
        appiumDriverFactory.setDeviceType(DeviceType.valueOf(deviceType));
        homePage = new HomePage();
        homePage.openEpgPage();
        epgPage = new EpgPage();
    }

    @When("l'utilisateur consulte la liste des chaînes")
    public void lUtilisateurConsulteLaListeDesChaines2() {
        // Commentaire : Consultation de la liste des chaînes
        // Action : Appel de la méthode pour consulter la liste des chaînes
        epgPage.consultChannelList();
    }

    @Then("les éléments suivants sont affichés :")
    public void lesElementsSuivantsSontAffiches2(io.cucumber.datatable.DataTable dataTable) {
        // Commentaire : Vérification de la présence des éléments
        // Action : Appel de la méthode pour vérifier la présence des éléments
        epgPage.verifyElements(dataTable);
    }
}


Notez que les méthodes des page objects (EpgPage et HomePage) sont supposées être déjà implémentées et ne sont pas incluses dans ce code.