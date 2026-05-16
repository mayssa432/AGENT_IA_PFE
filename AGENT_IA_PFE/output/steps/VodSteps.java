package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.VodPage;
import com.orange.otvp.automation.pages.VodCatalogPage;
import com.orange.otvp.automation.pages.VideoDetailsPage;
import com.orange.otvp.automation.pages.VideoAlertsPage;

public class VodSteps {

    private VodPage vodPage;
    private VodCatalogPage vodCatalogPage;
    private VideoDetailsPage videoDetailsPage;
    private VideoAlertsPage videoAlertsPage;

    @Given("que je suis connecté à l'application")
    public void queJeSuisConnecteA LalApplication() {
        // Commentaire : Implémentation de la connexion à l'application
        // Action : Appeler la méthode de connexion de la page VodPage
        vodPage = new VodPage();
        vodPage.connectToApplication();
    }

    @When("je clique sur l'onglet \"VOD\"")
    public void jeCliqueSurLOngletVod() {
        // Commentaire : Implémentation du clic sur l'onglet VOD
        // Action : Appeler la méthode de clic sur l'onglet VOD de la page VodPage
        vodPage.clickOnVodTab();
    }

    @Then("je devrais voir la page VOD avec les éléments suivants :")
    public void jeDevraisVoirLaPageVodAvecLesElementsSuivants() {
        // Commentaire : Implémentation de la vérification de la page VOD
        // Action : Appeler la méthode de vérification de la page VOD de la page VodPage
        vodPage.verifyVodPage();
    }

    @Given("que je suis sur la page VOD")
    public void queJeSuisSurLaPageVod() {
        // Commentaire : Implémentation de la navigation vers la page VOD
        // Action : Appeler la méthode de navigation vers la page VOD de la page VodPage
        vodPage.navigateToVodPage();
    }

    @When("je clique sur l'onglet \"Catalogue\"")
    public void jeCliqueSurLOngletCatalogue() {
        // Commentaire : Implémentation du clic sur l'onglet Catalogue
        // Action : Appeler la méthode de clic sur l'onglet Catalogue de la page VodCatalogPage
        vodCatalogPage = new VodCatalogPage();
        vodCatalogPage.clickOnCatalogTab();
    }

    @And("je recherche un contenu vidéo spécifique")
    public void jeRechercheUnContenuVideoSpecifique() {
        // Commentaire : Implémentation de la recherche d'un contenu vidéo
        // Action : Appeler la méthode de recherche de contenu vidéo de la page VodCatalogPage
        vodCatalogPage.searchForVideo();
    }

    @Then("je devrais voir les résultats de recherche avec les éléments suivants :")
    public void jeDevraisVoirLesResultatsDeRechercheAvecLesElementsSuivants() {
        // Commentaire : Implémentation de la vérification des résultats de recherche
        // Action : Appeler la méthode de vérification des résultats de recherche de la page VodCatalogPage
        vodCatalogPage.verifySearchResults();
    }

    @When("je clique sur un contenu vidéo")
    public void jeCliqueSurUnContenuVideo() {
        // Commentaire : Implémentation du clic sur un contenu vidéo
        // Action : Appeler la méthode de clic sur un contenu vidéo de la page VideoDetailsPage
        videoDetailsPage = new VideoDetailsPage();
        videoDetailsPage.clickOnVideo();
    }

    @Then("je devrais voir les détails du contenu vidéo avec les éléments suivants :")
    public void jeDevraisVoirLesDetailsDuContenuVideoAvecLesElementsSuivants() {
        // Commentaire : Implémentation de la vérification des détails du contenu vidéo
        // Action : Appeler la méthode de vérification des détails du contenu vidéo de la page VideoDetailsPage
        videoDetailsPage.verifyVideoDetails();
    }

    @When("je clique sur le bouton \"Créer une alerte\"")
    public void jeCliqueSurLeBoutonCreerUneAlerte() {
        // Commentaire : Implémentation du clic sur le bouton Créer une alerte
        // Action : Appeler la méthode de clic sur le bouton Créer une alerte de la page VideoAlertsPage
        videoAlertsPage = new VideoAlertsPage();
        videoAlertsPage.clickOnCreateAlertButton();
    }

    @Then("je devrais voir les options d'alerte avec les éléments suivants :")
    public void jeDevraisVoirLesOptionsDAlerteAvecLesElementsSuivants() {
        // Commentaire : Implémentation de la vérification des options d'alerte
        // Action : Appeler la méthode de vérification des options d'alerte de la page VideoAlertsPage
        videoAlertsPage.verifyAlertOptions();
    }

    @When("je sélectionne un contenu vidéo")
    public void jeSlectionneUnContenuVideo() {
        // Commentaire : Implémentation de la sélection d'un contenu vidéo
        // Action : Appeler la méthode de sélection d'un contenu vidéo de la page VodCatalogPage
        vodCatalogPage.selectVideo();
    }

    @And("je clique sur le bouton \"Ajouter à ma liste\"")
    public void jeCliqueSurLeBoutonAjouterAMaListe() {
        // Commentaire : Implémentation du clic sur le bouton Ajouter à ma liste
        // Action : Appeler la méthode de clic sur le bouton Ajouter à ma liste de la page VodCatalogPage
        vodCatalogPage.clickOnAddToListButton();
    }

    @Then("je devrais voir le contenu vidéo ajouté à ma liste avec les éléments suivants :")
    public void jeDevraisVoirLeContenuVideoAjouteAAMaListeAvecLesElementsSuivants() {
        // Commentaire : Implémentation de la vérification du contenu vidéo ajouté à ma liste
        // Action : Appeler la méthode de vérification du contenu vidéo ajouté à ma liste de la page VodCatalogPage
        vodCatalogPage.verifyVideoAddedToList();
    }

    @Then("je devrais voir une confirmation d'ajout avec les éléments suivants :")
    public void jeDevraisVoirUneConfirmationDAjoutAvecLesElementsSuivants() {
        // Commentaire : Implémentation de la vérification de la confirmation d'ajout
        // Action : Appeler la méthode de vérification de la confirmation d'ajout de la page VodCatalogPage
        vodCatalogPage.verifyAddToListConfirmation();
    }
}