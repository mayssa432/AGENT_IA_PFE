package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.PlayerOverlayPage;
import com.orange.otvp.automation.pages.VideoPage;

public class PlayerOverlaySteps {

    private PlayerOverlayPage playerOverlayPage;
    private VideoPage videoPage;

    @Given("que je suis sur la page de lecture de vidéo")
    public void queJeSuisSurLaPageDeLectureDeVideo() {
        // Commentaire : Initialiser la page de lecture de vidéo
        // Action : Appeler la méthode pour initialiser la page de lecture de vidéo
        videoPage = new VideoPage();
        videoPage.initialiserPage();
    }

    @When("je clique sur le bouton \"Info\" dans le player overlay")
    public void jeCliqueSurLeBoutonInfoDansLePlayerOverlay() {
        // Commentaire : Clique sur le bouton "Info" dans le player overlay
        // Action : Appeler la méthode pour cliquer sur le bouton "Info" dans le player overlay
        playerOverlayPage = new PlayerOverlayPage();
        playerOverlayPage.cliqueSurBoutonInfo();
    }

    @Then("je vois les informations de la vidéo, notamment le titre, le genre et la description")
    public void jeVoisLesInformationsDeLaVideoNotammentLeTitreLeGenreEtLaDescription() {
        // Commentaire : Vérifier que les informations de la vidéo sont affichées
        // Action : Appeler la méthode pour vérifier que les informations de la vidéo sont affichées
        Assert.assertTrue(playerOverlayPage.afficherInformationsVideo());
    }

    @When("je clique sur le bouton \"Qualité\" dans le player overlay")
    public void jeCliqueSurLeBoutonQualiteDansLePlayerOverlay() {
        // Commentaire : Clique sur le bouton "Qualité" dans le player overlay
        // Action : Appeler la méthode pour cliquer sur le bouton "Qualité" dans le player overlay
        playerOverlayPage.cliqueSurBoutonQualite();
    }

    @And("je sélectionne une qualité de vidéo différente")
    public void jeSelectionneUneQualiteDeVideoDifferent() {
        // Commentaire : Sélectionner une qualité de vidéo différente
        // Action : Appeler la méthode pour sélectionner une qualité de vidéo différente
        playerOverlayPage.selectionnerQualiteVideo();
    }

    @Then("la qualité de la vidéo est mise à jour")
    public void laQualiteDeLaVideoEstMiseAjour() {
        // Commentaire : Vérifier que la qualité de la vidéo est mise à jour
        // Action : Appeler la méthode pour vérifier que la qualité de la vidéo est mise à jour
        Assert.assertTrue(playerOverlayPage.afficherQualiteVideoMiseAjour());
    }

    @When("je clique sur le bouton \"Langues\" dans le player overlay")
    public void jeCliqueSurLeBoutonLanguesDansLePlayerOverlay() {
        // Commentaire : Clique sur le bouton "Langues" dans le player overlay
        // Action : Appeler la méthode pour cliquer sur le bouton "Langues" dans le player overlay
        playerOverlayPage.cliqueSurBoutonLangues();
    }

    @And("je sélectionne une langue audio différente")
    public void jeSelectionneUneLangueAudioDifferent() {
        // Commentaire : Sélectionner une langue audio différente
        // Action : Appeler la méthode pour sélectionner une langue audio différente
        playerOverlayPage.selectionnerLangueAudio();
    }

    @And("je sélectionne un sous-titre différent")
    public void jeSelectionneUnSousTitreDifferent() {
        // Commentaire : Sélectionner un sous-titre différent
        // Action : Appeler la méthode pour sélectionner un sous-titre différent
        playerOverlayPage.selectionnerSousTitre();
    }

    @Then("la langue audio et le sous-titre sont mis à jour")
    public void laLangueAudioEtLeSousTitreSontMisesAjour() {
        // Commentaire : Vérifier que la langue audio et le sous-titre sont mis à jour
        // Action : Appeler la méthode pour vérifier que la langue audio et le sous-titre sont mis à jour
        Assert.assertTrue(playerOverlayPage.afficherLangueAudioEtSousTitreMisesAjour());
    }

    @When("je clique sur le bouton \"Lecture/Pause\" dans le player overlay")
    public void jeCliqueSurLeBoutonLecturePauseDansLePlayerOverlay() {
        // Commentaire : Clique sur le bouton "Lecture/Pause" dans le player overlay
        // Action : Appeler la méthode pour cliquer sur le bouton "Lecture/Pause" dans le player overlay
        playerOverlayPage.cliqueSurBoutonLecturePause();
    }

    @Then("la lecture de la vidéo est mise en pause ou reprise")
    public void laLectureDeLaVideoEstMiseEnPauseOuReprise() {
        // Commentaire : Vérifier que la lecture de la vidéo est mise en pause ou reprise
        // Action : Appeler la méthode pour vérifier que la lecture de la vidéo est mise en pause ou reprise
        Assert.assertTrue(playerOverlayPage.afficherLectureVideoMiseEnPauseOuReprise());
    }

    @When("une erreur de lecture se produit")
    public void uneErreurDeLectureSeProduit() {
        // Commentaire : Simuler une erreur de lecture
        // Action : Appeler la méthode pour simuler une erreur de lecture
        playerOverlayPage.simulerErreurLecture();
    }

    @Then("je vois un message d'erreur avec un bouton \"Réessayer\"")
    public void jeVoisUnMessageDErreurAvecUnBoutonReessayer() {
        // Commentaire : Vérifier que le message d'erreur est affiché avec un bouton "Réessayer"
        // Action : Appeler la méthode pour vérifier que le message d'erreur est affiché avec un bouton "Réessayer"
        Assert.assertTrue(playerOverlayPage.afficherMessageErreurAvecBoutonReessayer());
    }

    @When("je clique sur le bouton \"Réessayer\"")
    public void jeCliqueSurLeBoutonReessayer() {
        // Commentaire : Clique sur le bouton "Réessayer"
        // Action : Appeler la méthode pour cliquer sur le bouton "Réessayer"
        playerOverlayPage.cliqueSurBoutonReessayer();
    }

    @Then("la lecture de la vidéo est reprise")
    public void laLectureDeLaVideoEstReprise() {
        // Commentaire : Vérifier que la lecture de la vidéo est reprise
        // Action : Appeler la méthode pour vérifier que la lecture de la vidéo est reprise
        Assert.assertTrue(playerOverlayPage.afficherLectureVideoReprise());
    }

    @When("je clique sur le bouton \"Carrousel\" dans le player overlay")
    public void jeCliqueSurLeBoutonCarrouselDansLePlayerOverlay() {
        // Commentaire : Clique sur le bouton "Carrousel" dans le player overlay
        // Action : Appeler la méthode pour cliquer sur le bouton "Carrousel" dans le player overlay
        playerOverlayPage.cliqueSurBoutonCarrousel();
    }

    @Then("je vois le carrousel de vidéos")
    public void jeVoisLeCarrouselDeVideos() {
        // Commentaire : Vérifier que le carrousel de vidéos est affiché
        // Action : Appeler la méthode pour vérifier que le carrousel de vidéos est affiché
        Assert.assertTrue(playerOverlayPage.afficherCarrouselVideos());
    }

    @When("je clique sur le bouton \"Plein écran\" dans le player overlay")
    public void jeCliqueSurLeBoutonPleinEcranDansLePlayerOverlay() {
        // Commentaire : Clique sur le bouton "Plein écran" dans le player overlay
        // Action : Appeler la méthode pour cliquer sur le bouton "Plein écran" dans le player overlay
        playerOverlayPage.cliqueSurBoutonPleinEcran();
    }

    @Then("la vidéo est affichée en plein écran")
    public void laVideoEstAfficheeEnPleinEcran() {
        // Commentaire : Vérifier que la vidéo est affichée en plein écran
        // Action : Appeler la méthode pour vérifier que la vidéo est affichée en plein écran
        Assert.assertTrue(playerOverlayPage.afficherVideoEnPleinEcran());
    }

    @When("je clique sur le bouton \"Carrousel\" dans le player overlay")
    public void jeCliqueSurLeBoutonCarrouselDansLePlayerOverlay2() {
        // Commentaire : Clique sur le bouton "Carrousel" dans le player overlay
        // Action : Appeler la méthode pour cliquer sur le bouton "Carrousel" dans le player overlay
        playerOverlayPage.cliqueSurBoutonCarrousel();
    }

    @And("je navigue dans le carrousel de vidéos")
    public void jeNavigueDansLeCarrouselDeVideos() {
        // Commentaire : Navigation dans le carrousel de vidéos
        // Action : Appeler la méthode pour naviguer dans le carrousel
        playerOverlayPage.naviguerDansLeCarrouselDeVideos();
    }
}