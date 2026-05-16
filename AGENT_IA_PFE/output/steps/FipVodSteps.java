package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.FipVodPage;
import com.orange.otvp.automation.pages.ProgramPage;

public class FipVodSteps {

    private FipVodPage fipVodPage;
    private ProgramPage programPage;

    @Given("que je suis sur la page FipVod")
    public void queJeSuisSurLaPageFipVod() {
        // Commentaire : Initialisation de la page FipVod
        // Action : Ouvrir la page FipVod
        fipVodPage = new FipVodPage();
        fipVodPage.open();
    }

    @When("je vérifie la présence des éléments de la page")
    public void jeVérifieLaPrésenceDesÉlémentsDeLaPage() {
        // Commentaire : Vérifier la présence des éléments de la page FipVod
        // Action : Vérifier la présence des éléments de la page
        fipVodPage.verifyElementsPresence();
    }

    @Then("je vois l'image de la vidéo {string}")
    public void jeVoisLImageDeLaVidéo(String imageVideo) {
        // Commentaire : Vérifier la présence de l'image de la vidéo
        // Action : Vérifier la présence de l'image de la vidéo
        fipVodPage.verifyVideoImage(imageVideo);
    }

    @Then("je vois le bouton de marque-page {string}")
    public void jeVoisLeBoutonDeMarquePage(String boutonMarquePage) {
        // Commentaire : Vérifier la présence du bouton de marque-page
        // Action : Vérifier la présence du bouton de marque-page
        fipVodPage.verifyBookmarkButton(boutonMarquePage);
    }

    @Then("je vois le titre du programme {string}")
    public void jeVoisLeTitreDuProgramme(String titreProgramme) {
        // Commentaire : Vérifier la présence du titre du programme
        // Action : Vérifier la présence du titre du programme
        fipVodPage.verifyProgramTitle(titreProgramme);
    }

    @Then("je vois le bouton de lecture {string}")
    public void jeVoisLeBoutonDeLecture(String boutonLecture) {
        // Commentaire : Vérifier la présence du bouton de lecture
        // Action : Vérifier la présence du bouton de lecture
        fipVodPage.verifyPlayButton(boutonLecture);
    }

    @Then("je vois le bouton de téléchargement {string}")
    public void jeVoisLeBoutonDeTéléchargement(String boutonTéléchargement) {
        // Commentaire : Vérifier la présence du bouton de téléchargement
        // Action : Vérifier la présence du bouton de téléchargement
        fipVodPage.verifyDownloadButton(boutonTéléchargement);
    }

    @When("je clique sur le bouton de lecture {string}")
    public void jeCliqueSurLeBoutonDeLecture(String boutonLecture) {
        // Commentaire : Clique sur le bouton de lecture
        // Action : Clique sur le bouton de lecture
        fipVodPage.clickPlayButton(boutonLecture);
    }

    @Then("je vois la vidéo en cours de lecture")
    public void jeVoisLaVidéoEnCoursDeLecture() {
        // Commentaire : Vérifier que la vidéo est en cours de lecture
        // Action : Vérifier que la vidéo est en cours de lecture
        Assert.assertTrue(fipVodPage.isVideoPlaying());
    }

    @When("je clique sur le bouton de téléchargement {string}")
    public void jeCliqueSurLeBoutonDeTéléchargement(String boutonTéléchargement) {
        // Commentaire : Clique sur le bouton de téléchargement
        // Action : Clique sur le bouton de téléchargement
        fipVodPage.clickDownloadButton(boutonTéléchargement);
    }

    @Then("je vois l'indicateur de téléchargement {string}")
    public void jeVoisLIndicateurDeTéléchargement(String indicateurTéléchargement) {
        // Commentaire : Vérifier la présence de l'indicateur de téléchargement
        // Action : Vérifier la présence de l'indicateur de téléchargement
        fipVodPage.verifyDownloadIndicator(indicateurTéléchargement);
    }

    @Then("je vois le bouton de suppression du téléchargement {string}")
    public void jeVoisLeBoutonDeSuppressionDuTéléchargement(String boutonSuppressionTéléchargement) {
        // Commentaire : Vérifier la présence du bouton de suppression du téléchargement
        // Action : Vérifier la présence du bouton de suppression du téléchargement
        fipVodPage.verifyDeleteDownloadButton(boutonSuppressionTéléchargement);
    }

    @When("je clique sur le bouton de création d'alerte {string}")
    public void jeCliqueSurLeBoutonDeCréationDAlerte(String boutonCréationAlerte) {
        // Commentaire : Clique sur le bouton de création d'alerte
        // Action : Clique sur le bouton de création d'alerte
        fipVodPage.clickCreateAlertButton(boutonCréationAlerte);
    }

    @Then("je vois le bouton de suppression d'alerte {string}")
    public void jeVoisLeBoutonDeSuppressionDAlerte(String boutonSuppressionAlerte) {
        // Commentaire : Vérifier la présence du bouton de suppression d'alerte
        // Action : Vérifier la présence du bouton de suppression d'alerte
        fipVodPage.verifyDeleteAlertButton(boutonSuppressionAlerte);
    }

    @When("je clique sur le bouton d'affichage des détails {string}")
    public void jeCliqueSurLeBoutonDAffichageDesDétails(String boutonAffichageDétails) {
        // Commentaire : Clique sur le bouton d'affichage des détails
        // Action : Clique sur le bouton d'affichage des détails
        fipVodPage.clickShowMoreButton(boutonAffichageDétails);
    }

    @Then("je vois les détails du programme {string}, {string}, {string}, {string}")
    public void jeVoisLesDétailsDuProgramme(String détail1, String détail2, String détail3, String détail4) {
        // Commentaire : Vérifier la présence des détails du programme
        // Action : Vérifier la présence des détails du programme
        programPage = new ProgramPage();
        programPage.verifyProgramDetails(détail1, détail2, détail3, détail4);
    }

    @When("je clique sur le bouton de notation {string}")
    public void jeCliqueSurLeBoutonDeNotation(String boutonNotation) {
        // Commentaire : Clique sur le bouton de notation
        // Action : Clique sur le bouton de notation
        fipVodPage.clickRatingIcon(boutonNotation);
    }

    @Then("je vois les notes et les commentaires {string}, {string}")
    public void jeVoisLesNotesEtLesCommentaires(String notesCommentaires1, String notesCommentaires2) {
        // Commentaire : Vérifier la présence des notes et des commentaires
        // Action : Vérifier la présence des notes et des commentaires
        fipVodPage.verifyRatingTexts(notesCommentaires1, notesCommentaires2);
    }

    @When("je clique sur le bouton de qualité SD {string}")
    public void jeCliqueSurLeBoutonDeQualitéSD(String boutonQualitéSD) {
        // Commentaire : Clique sur le bouton de qualité SD
        // Action : Clique sur le bouton de qualité SD
        fipVodPage.clickQualitySDButton(boutonQualitéSD);
    }

    @Then("je vois la vidéo en qualité SD")
    public void jeVoisLaVidéoEnQualitéSD() {
        // Commentaire : Vérifier que la vidéo est en qualité SD
        // Action : Vérifier que la vidéo est en qualité SD
        Assert.assertTrue(fipVodPage.isVideoInSDQuality());
    }

    @When("je clique sur le bouton de qualité HD {string}")
    public void jeCliqueSurLeBoutonDeQualitéHD(String boutonQualitéHD) {
        // Commentaire : Clique sur le bouton de qualité HD
        // Action : Clique sur le bouton de qualité HD
        fipVodPage.clickQualityHDButton(boutonQualitéHD);
    }

    @Then("je vois la vidéo en qualité HD")
    public void jeVoisLaVidéoEnQualitéHD() {
        // Commentaire : Vérifier que la vidéo est en qualité HD