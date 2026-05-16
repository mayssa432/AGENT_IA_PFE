package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.HomePage;
import com.orange.otvp.automation.pages.LivePage;
import com.orange.otvp.automation.pages.ProgrammeTVPage;
import com.orange.otvp.automation.pages.EnCeMomentATVPage;
import com.orange.otvp.automation.pages.ProgramsPage;
import com.orange.otvp.automation.pages.ToutLeLivePage;
import com.orange.otvp.automation.pages.ProgramsATvenirPage;
import com.orange.otvp.automation.pages.FiltrePage;
import com.orange.otvp.automation.pages.RecommandationsPage;

public class LiveSteps {

    private HomePage homePage;
    private LivePage livePage;
    private ProgrammeTVPage programmeTVPage;
    private EnCeMomentATVPage enCeMomentATVPage;
    private ProgramsPage programsPage;
    private ToutLeLivePage toutLeLivePage;
    private ProgramsATvenirPage programsATvenirPage;
    private FiltrePage filtrePage;
    private RecommandationsPage recommandationsPage;

    @Given("que je suis sur la page d'accueil")
    public void queJeSuisSurLaPageDAccueil() {
        // Commentaire : Initialisation de la page d'accueil
        // Action : Récupération de l'instance de la page d'accueil
        homePage = new HomePage();
        // Action : Navigation vers la page d'accueil
        homePage.navigateTo();
    }

    @When("je clique sur le bouton \"Programme TV\"")
    public void jeCliqueSurLeBoutonProgrammeTV() {
        // Commentaire : Clique sur le bouton "Programme TV"
        // Action : Récupération de l'instance de la page "Programme TV"
        programmeTVPage = homePage.clickOnProgrammeTVButton();
    }

    @Then("je suis redirigé vers la page Live")
    public void jeSuisRedirigeVersLaPageLive() {
        // Commentaire : Vérification de la redirection vers la page Live
        // Action : Récupération de l'instance de la page Live
        livePage = programmeTVPage.clickOnLiveButton();
        // Action : Vérification de la page Live
        Assert.assertTrue(livePage.isLivePage());
    }

    @Given("que je suis sur la page Live")
    public void queJeSuisSurLaPageLive() {
        // Commentaire : Initialisation de la page Live
        // Action : Récupération de l'instance de la page Live
        livePage = new LivePage();
        // Action : Navigation vers la page Live
        livePage.navigateTo();
    }

    @When("je clique sur le bouton \"En ce moment à la TV\"")
    public void jeCliqueSurLeBoutonEnCeMomentATV() {
        // Commentaire : Clique sur le bouton "En ce moment à la TV"
        // Action : Récupération de l'instance de la page "En ce moment à la TV"
        enCeMomentATVPage = livePage.clickOnEnCeMomentATVButton();
    }

    @Then("je vois la liste des programmes en direct")
    public void jeVoisLaListeDesProgrammesEnDirect() {
        // Commentaire : Vérification de la liste des programmes en direct
        // Action : Vérification de la liste des programmes en direct
        Assert.assertTrue(enCeMomentATVPage.isProgrammesEnDirectListVisible());
    }

    @And("je vois les informations de chaque programme, notamment le titre, la chaîne et l'heure de diffusion")
    public void jeVoisLesInformationsDeChaqueProgrammeNotammentLeTitreLaChaîneEtLHeureDeDiffusion() {
        // Commentaire : Vérification des informations de chaque programme
        // Action : Vérification des informations de chaque programme
        Assert.assertTrue(enCeMomentATVPage.isProgrammeInfoVisible());
    }

    @When("je clique sur un programme en direct")
    public void jeCliqueSurUnProgrammeEnDirect() {
        // Commentaire : Clique sur un programme en direct
        // Action : Récupération de l'instance de la page du programme en direct
        programsPage = enCeMomentATVPage.clickOnProgrammeEnDirect();
    }

    @Then("le programme démarre et je peux le visionner")
    public void leProgrammeDémarreraJePeuxLeVisionner() {
        // Commentaire : Vérification du démarrage du programme
        // Action : Vérification du démarrage du programme
        Assert.assertTrue(programsPage.isProgrammeStarted());
    }

    @And("je vois les contrôles de lecture, notamment les boutons de pause et de stop")
    public void jeVoisLesContrôlesDeLectureNotammentLesBoutonsDePauseEtDeStop() {
        // Commentaire : Vérification des contrôles de lecture
        // Action : Vérification des contrôles de lecture
        Assert.assertTrue(programsPage.isControlsVisible());
    }

    @When("je clique sur le bouton \"Tout le live\"")
    public void jeCliqueSurLeBoutonToutLeLive() {
        // Commentaire : Clique sur le bouton "Tout le live"
        // Action : Récupération de l'instance de la page "Tout le live"
        toutLeLivePage = livePage.clickOnToutLeLiveButton();
    }

    @Then("je vois la liste de toutes les chaînes disponibles")
    public void jeVoisLaListeDeToutesLesChaînesDisponibles() {
        // Commentaire : Vérification de la liste de toutes les chaînes disponibles
        // Action : Vérification de la liste de toutes les chaînes disponibles
        Assert.assertTrue(toutLeLivePage.isChaînesListVisible());
    }

    @And("je peux sélectionner une chaîne pour la visionner")
    public void jePeuxSélectionnerUneChaînePourLaVisionner() {
        // Commentaire : Vérification de la sélection d'une chaîne
        // Action : Vérification de la sélection d'une chaîne
        Assert.assertTrue(toutLeLivePage.isChaîneSelected());
    }

    @When("je clique sur le bouton \"Programmes à venir\"")
    public void jeCliqueSurLeBoutonProgrammesÀVenir() {
        // Commentaire : Clique sur le bouton "Programmes à venir"
        // Action : Récupération de l'instance de la page "Programmes à venir"
        programsATvenirPage = livePage.clickOnProgrammesATvenirButton();
    }

    @Then("je vois la liste des programmes qui seront diffusés plus tard")
    public void jeVoisLaListeDesProgrammesQuiSerontDiffusésPlusTard() {
        // Commentaire : Vérification de la liste des programmes à venir
        // Action : Vérification de la liste des programmes à venir
        Assert.assertTrue(programsATvenirPage.isProgrammesATvenirListVisible());
    }

    @And("je peux voir les informations de chaque programme, notamment le titre, la chaîne et l'heure de diffusion")
    public void jePeuxVoirLesInformationsDeChaqueProgrammeNotammentLeTitreLaChaîneEtLHeureDeDiffusion() {
        // Commentaire : Vérification des informations de chaque programme
        // Action : Vérification des informations de chaque programme
        Assert.assertTrue(programsATvenirPage.isProgrammeInfoVisible());
    }

    @When("je clique sur le bouton de filtre")
    public void jeCliqueSurLeBoutonDeFiltre() {
        // Commentaire : Clique sur le bouton de filtre
        // Action : Récupération de l'instance de la page de filtre
        filtrePage = livePage.clickOnFiltreButton();
    }

    @Then("je peux sélectionner des critères de recherche, notamment la chaîne ou le genre de programme")
    public void jePeuxSélectionnerDesCritèresDeRechercheNotammentLaChaîneOuLeGenreDeProgramme() {
        // Commentaire : Vérification de la sélection des critères de recherche
        // Action : Vérification de la sélection des critères de recherche
        Assert.assertTrue(filtrePage.isCritèresDeRechercheSelected());
    }

    @And("je vois les résultats de la recherche, notamment la liste des programmes qui correspondent aux critères sélectionnés")
    public void jeVoisLesRésultatsDeLaRechercheNotammentLaListeDesProgrammesQuiCorrespondentAuxCritèresSélectionnés() {
        // Commentaire : Vérification des résultats de la recherche
        // Action : Vérification des résultats de la recherche
        Assert.assertTrue(filtrePage.isRésultatsDeLaRechercheVisible());
    }

    @When("je clique sur le bouton \"Recommandations\"")
    public void jeCliqueSurLeBoutonRecommandations() {
        // Commentaire : Clique sur le bouton "Recommandations"
        // Action : Récupération de l'instance de la page "Recommandations"
        recommandationsPage = livePage.clickOnRecommandationsButton();
    }
}