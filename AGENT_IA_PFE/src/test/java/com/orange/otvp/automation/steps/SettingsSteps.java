package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.HomePage;
import com.orange.otvp.automation.pages.SettingsPage;

public class SettingsSteps {

    private HomePage homePage;
    private SettingsPage settingsPage;

    @Given("que je suis sur la page d'accueil de l'application")
    public void queJeSuisSurLaPageDAccueilDeLApplication() {
        // Commentaire : Initialisation de la page d'accueil
        // Action : Appel de la méthode pour accéder à la page d'accueil
        homePage = new HomePage();
        homePage.accederAPage();
    }

    @When("je clique sur le bouton de paramètres")
    public void jeCliqueSurLeBoutonDeParametres() {
        // Commentaire : Clique sur le bouton de paramètres
        // Action : Appel de la méthode pour cliquer sur le bouton de paramètres
        settingsPage = homePage.cliqueSurBoutonParametres();
    }

    @Then("je vois la page des paramètres")
    public void jeVoisLaPageDesParametres() {
        // Commentaire : Vérification de la page des paramètres
        // Action : Appel de la méthode pour vérifier la page des paramètres
        Assert.assertTrue(settingsPage.estSurPageDesParametres());
    }

    @Given("que je suis sur la page des paramètres")
    public void queJeSuisSurLaPageDesParametres() {
        // Commentaire : Initialisation de la page des paramètres
        // Action : Appel de la méthode pour accéder à la page des paramètres
        settingsPage = new SettingsPage();
        settingsPage.accederAPage();
    }

    @When("je clique sur le bouton de rappel")
    public void jeCliqueSurLeBoutonDeRappel() {
        // Commentaire : Clique sur le bouton de rappel
        // Action : Appel de la méthode pour cliquer sur le bouton de rappel
        settingsPage.cliqueSurBoutonRappel();
    }

    @And("je sélectionne une option de rappel")
    public void jeSlectionneUneOptionDeRappel() {
        // Commentaire : Sélection d'une option de rappel
        // Action : Appel de la méthode pour sélectionner une option de rappel
        settingsPage.sélectionnerOptionRappel();
    }

    @Then("je vois le texte de rappel mis à jour")
    public void jeVoisLeTexteDeRappelMisÀJour() {
        // Commentaire : Vérification du texte de rappel mis à jour
        // Action : Appel de la méthode pour vérifier le texte de rappel mis à jour
        Assert.assertTrue(settingsPage.estLeTexteDeRappelMisAJour());
    }

    @When("je clique sur le bouton de qualité de streaming")
    public void jeCliqueSurLeBoutonDeQualiteDeStreaming() {
        // Commentaire : Clique sur le bouton de qualité de streaming
        // Action : Appel de la méthode pour cliquer sur le bouton de qualité de streaming
        settingsPage.cliqueSurBoutonQualiteDeStreaming();
    }

    @And("je sélectionne une option de qualité de streaming")
    public void jeSlectionneUneOptionDeQualiteDeStreaming() {
        // Commentaire : Sélection d'une option de qualité de streaming
        // Action : Appel de la méthode pour sélectionner une option de qualité de streaming
        settingsPage.sélectionnerOptionQualiteDeStreaming();
    }

    @Then("je vois le texte de qualité de streaming mis à jour")
    public void jeVoisLeTexteDeQualiteDeStreamingMisÀJour() {
        // Commentaire : Vérification du texte de qualité de streaming mis à jour
        // Action : Appel de la méthode pour vérifier le texte de qualité de streaming mis à jour
        Assert.assertTrue(settingsPage.estLeTexteDeQualiteDeStreamingMisAJour());
    }

    @When("je clique sur le bouton de téléchargement en réseau mobile")
    public void jeCliqueSurLeBoutonDeTelechargementEnReseauMobile() {
        // Commentaire : Clique sur le bouton de téléchargement en réseau mobile
        // Action : Appel de la méthode pour cliquer sur le bouton de téléchargement en réseau mobile
        settingsPage.cliqueSurBoutonTelechargementEnReseauMobile();
    }

    @And("je sélectionne une option de téléchargement en réseau mobile")
    public void jeSlectionneUneOptionDeTelechargementEnReseauMobile() {
        // Commentaire : Sélection d'une option de téléchargement en réseau mobile
        // Action : Appel de la méthode pour sélectionner une option de téléchargement en réseau mobile
        settingsPage.sélectionnerOptionTelechargementEnReseauMobile();
    }

    @Then("je vois le texte de téléchargement en réseau mobile mis à jour")
    public void jeVoisLeTexteDeTelechargementEnReseauMobileMisÀJour() {
        // Commentaire : Vérification du texte de téléchargement en réseau mobile mis à jour
        // Action : Appel de la méthode pour vérifier le texte de téléchargement en réseau mobile mis à jour
        Assert.assertTrue(settingsPage.estLeTexteDeTelechargementEnReseauMobileMisAJour());
    }

    @When("je clique sur le bouton de lecture vidéo")
    public void jeCliqueSurLeBoutonDeLectureVideo() {
        // Commentaire : Clique sur le bouton de lecture vidéo
        // Action : Appel de la méthode pour cliquer sur le bouton de lecture vidéo
        settingsPage.cliqueSurBoutonLectureVideo();
    }

    @And("je sélectionne une option de lecture vidéo")
    public void jeSlectionneUneOptionDeLectureVideo() {
        // Commentaire : Sélection d'une option de lecture vidéo
        // Action : Appel de la méthode pour sélectionner une option de lecture vidéo
        settingsPage.sélectionnerOptionLectureVideo();
    }

    @Then("je vois le texte de lecture vidéo mis à jour")
    public void jeVoisLeTexteDeLectureVideoMisÀJour() {
        // Commentaire : Vérification du texte de lecture vidéo mis à jour
        // Action : Appel de la méthode pour vérifier le texte de lecture vidéo mis à jour
        Assert.assertTrue(settingsPage.estLeTexteDeLectureVideoMisAJour());
    }

    @When("je clique sur le bouton de qualité de streaming")
    public void jeCliqueSurLeBoutonDeQualiteDeStreaming2() {
        // Commentaire : Clique sur le bouton de qualité de streaming
        // Action : Appel de la méthode pour cliquer sur le bouton de qualité de streaming
        settingsPage.cliqueSurBoutonQualiteDeStreaming();
    }

    @And("je sélectionne une option de qualité de streaming")
    public void jeSlectionneUneOptionDeQualiteDeStreaming2() {
        // Commentaire : Sélection d'une option de qualité de streaming
        // Action : Appel de la méthode pour sélectionner une option de qualité de streaming
        settingsPage.sélectionnerOptionQualiteDeStreaming();
    }

    @Then("je vois le texte d'impact carbone de la qualité de streaming mis à jour")
    public void jeVoisLeTexteDImpactCarboneDeLaQualiteDeStreamingMisÀJour() {
        // Commentaire : Vérification du texte d'impact carbone de la qualité de streaming mis à jour
        // Action : Appel de la méthode pour vérifier le texte d'impact carbone de la qualité de streaming mis à jour
        Assert.assertTrue(settingsPage.estLeTexteDImpactCarboneDeLaQualiteDeStreamingMisAJour());
    }

    @When("je clique sur le bouton de stockage de téléchargement")
    public void jeCliqueSurLeBoutonDeStockageDeTelechargement() {
        // Commentaire : Clique sur le bouton de stockage de téléchargement
        // Action : Appel de la méthode pour cliquer sur le bouton de stockage de téléchargement
        settingsPage.cliqueSurBoutonStockageDeTelechargement();
    }

    @And("je sélectionne une option de stockage de téléchargement")
    public void jeSlectionneUneOptionDeStockageDeTelechargement() {
        // Commentaire : Sélection d'une option de stockage de téléchargement
        // Action : Appel de la méthode pour sélectionner une option de stockage de téléchargement
        settingsPage.sélectionnerOptionStockageDeTelechargement();
    }

    @Then("je vois le texte de stockage de téléchargement mis à jour")
    public void jeVoisLeTexteDeStockageDeTelechargementMisÀJour() {
        // Commentaire : Vérification du texte de stockage de téléchargement mis à jour
        // Action : Appel de la méthode pour vérifier le texte de stockage de téléchargement mis à jour
        Assert.assertTrue(settingsPage.estLeTexteDeStockageDeTelechargementMisAJour());
    }

    @When("je clique sur le bouton de sauvegarde des paramètres")
    public void jeCliqueSurLeBoutonDeSauvegardeDesParametres() {
        // Commentaire : Clique sur le bouton de sauvegarde des paramètres
        // Action : Appel de la méthode pour cliquer sur le bouton de sauvegarde des paramètres
        settingsPage.cliqueSurLeBoutonDeSauvegardeDesParametres();
    }

    @Then("je vois le message de sauvegarde des paramètres")
    public void jeVoisLeMessageDeSauvegardeDesParametres() {
        // Commentaire : Vérification du message de sauvegarde des paramètres
        // Action : Appel de la méthode pour vérifier le message de sauvegarde des paramètres
        Assert.assertTrue(settingsPage.estLeMessageDeSauvegardeDesParametresAffiche());
    }
}
