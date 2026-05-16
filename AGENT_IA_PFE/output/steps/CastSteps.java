package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.CastPage;
import com.orange.otvp.automation.pages.ConnectionPage;
import com.orange.otvp.automation.pages.MediaControlPage;

public class CastSteps {

    private CastPage castPage;
    private ConnectionPage connectionPage;
    private MediaControlPage mediaControlPage;

    @Given("que l'utilisateur est sur la page Cast")
    public void queLUtilisateurEstSurLaPageCast() {
        // Commentaire : Initialisation de la page Cast
        // Action : Appel de la méthode pour initialiser la page Cast
        castPage = new CastPage();
        castPage.navigateToCastPage();
    }

    @When("l'utilisateur affiche la liste des appareils")
    public void lUtilisateurAfficheLaListeDesAppareils() {
        // Commentaire : Affichage de la liste des appareils
        // Action : Appel de la méthode pour afficher la liste des appareils
        castPage.displayDeviceList();
    }

    @Then("la liste des appareils est affichée")
    public void laListeDesAppareilsEstAffichée() {
        // Commentaire : Vérification de la présence de la liste des appareils
        // Action : Appel de la méthode pour vérifier la présence de la liste des appareils
        Assert.assertTrue(castPage.isDeviceListDisplayed());
    }

    @And("le bouton de déconnexion du ChromeCast est affiché")
    public void leBoutonDeDéconnexionDuChromeCastEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de déconnexion du ChromeCast
        // Action : Appel de la méthode pour vérifier la présence du bouton de déconnexion du ChromeCast
        Assert.assertTrue(castPage.isChromeCastDisconnectButtonDisplayed());
    }

    @And("le bouton de déconnexion de la STB est affiché")
    public void leBoutonDeDéconnexionDeLaSTBEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de déconnexion de la STB
        // Action : Appel de la méthode pour vérifier la présence du bouton de déconnexion de la STB
        Assert.assertTrue(castPage.isSTBDisconnectButtonDisplayed());
    }

    @And("le titre de la média est affiché")
    public void leTitreDeLaMédiaEstAffiché() {
        // Commentaire : Vérification de la présence du titre de la média
        // Action : Appel de la méthode pour vérifier la présence du titre de la média
        Assert.assertTrue(castPage.isMediaTitleDisplayed());
    }

    @And("le bouton de réduction est affiché")
    public void leBoutonDeRéductionEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de réduction
        // Action : Appel de la méthode pour vérifier la présence du bouton de réduction
        Assert.assertTrue(castPage.isReduceButtonDisplayed());
    }

    @And("le bouton d'expansion est affiché")
    public void leBoutonDExpansionEstAffiché() {
        // Commentaire : Vérification de la présence du bouton d'expansion
        // Action : Appel de la méthode pour vérifier la présence du bouton d'expansion
        Assert.assertTrue(castPage.isExpandButtonDisplayed());
    }

    @And("le titre de l'appareil est affiché")
    public void leTitreDeLAppareilEstAffiché() {
        // Commentaire : Vérification de la présence du titre de l'appareil
        // Action : Appel de la méthode pour vérifier la présence du titre de l'appareil
        Assert.assertTrue(castPage.isDeviceTitleDisplayed());
    }

    @And("la couverture de la média est affichée")
    public void laCouvertureDeLaMédiaEstAffichée() {
        // Commentaire : Vérification de la présence de la couverture de la média
        // Action : Appel de la méthode pour vérifier la présence de la couverture de la média
        Assert.assertTrue(castPage.isMediaCoverDisplayed());
    }

    @And("le logo de la chaîne est affiché")
    public void leLogoDeLaChaîneEstAffiché() {
        // Commentaire : Vérification de la présence du logo de la chaîne
        // Action : Appel de la méthode pour vérifier la présence du logo de la chaîne
        Assert.assertTrue(castPage.isChannelLogoDisplayed());
    }

    @And("l'heure de début est affichée")
    public void lHeureDeDébutEstAffichée() {
        // Commentaire : Vérification de la présence de l'heure de début
        // Action : Appel de la méthode pour vérifier la présence de l'heure de début
        Assert.assertTrue(castPage.isStartTimeDisplayed());
    }

    @And("l'heure de fin est affichée")
    public void lHeureDeFinEstAffichée() {
        // Commentaire : Vérification de la présence de l'heure de fin
        // Action : Appel de la méthode pour vérifier la présence de l'heure de fin
        Assert.assertTrue(castPage.isEndTimeDisplayed());
    }

    @And("la barre de progression est affichée")
    public void laBarreDeProgressionEstAffichée() {
        // Commentaire : Vérification de la présence de la barre de progression
        // Action : Appel de la méthode pour vérifier la présence de la barre de progression
        Assert.assertTrue(castPage.isProgressBarDisplayed());
    }

    @And("le bouton de lecture/pause est affiché")
    public void leBoutonDeLecturePauseEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de lecture/pause
        // Action : Appel de la méthode pour vérifier la présence du bouton de lecture/pause
        Assert.assertTrue(castPage.isPlayPauseButtonDisplayed());
    }

    @And("le bouton d'information est affiché")
    public void leBoutonDInformationEstAffiché() {
        // Commentaire : Vérification de la présence du bouton d'information
        // Action : Appel de la méthode pour vérifier la présence du bouton d'information
        Assert.assertTrue(castPage.isInfoButtonDisplayed());
    }

    @And("le bouton d'enregistrement est affiché")
    public void leBoutonDEnregistrementEstAffiché() {
        // Commentaire : Vérification de la présence du bouton d'enregistrement
        // Action : Appel de la méthode pour vérifier la présence du bouton d'enregistrement
        Assert.assertTrue(castPage.isRecordButtonDisplayed());
    }

    @And("le bouton de langues et sous-titres est affiché")
    public void leBoutonDeLanguesEtSousTitresEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de langues et sous-titres
        // Action : Appel de la méthode pour vérifier la présence du bouton de langues et sous-titres
        Assert.assertTrue(castPage.isLanguageSubtitleButtonDisplayed());
    }

    @And("le bouton de volume est affiché")
    public void leBoutonDeVolumeEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de volume
        // Action : Appel de la méthode pour vérifier la présence du bouton de volume
        Assert.assertTrue(castPage.isVolumeButtonDisplayed());
    }

    @When("l'utilisateur sélectionne un appareil dans la liste")
    public void lUtilisateurSélectionneUnAppareilDansLaListe() {
        // Commentaire : Sélection d'un appareil dans la liste
        // Action : Appel de la méthode pour sélectionner un appareil dans la liste
        castPage.selectDeviceFromList();
    }

    @And("l'utilisateur affiche les éléments de contrôle")
    public void lUtilisateurAfficheLesÉlémentsDeContrôle() {
        // Commentaire : Affichage des éléments de contrôle
        // Action : Appel de la méthode pour afficher les éléments de contrôle
        mediaControlPage = new MediaControlPage();
        mediaControlPage.displayMediaControlElements();
    }

    @Then("le bouton de lecture/pause est affiché")
    public void leBoutonDeLecturePauseEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de lecture/pause
        // Action : Appel de la méthode pour vérifier la présence du bouton de lecture/pause
        Assert.assertTrue(mediaControlPage.isPlayPauseButtonDisplayed());
    }

    @And("le bouton de réduction est affiché")
    public void leBoutonDeRéductionEstAffiché() {
        // Commentaire : Vérification de la présence du bouton de réduction
        // Action : Appel