package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.DownloadsPage;
import com.orange.otvp.automation.pages.DownloadDetailsPage;
import com.orange.otvp.automation.pages.DownloadListPage;

public class DownloadsSteps {

    private DownloadsPage downloadsPage;
    private DownloadDetailsPage downloadDetailsPage;
    private DownloadListPage downloadListPage;

    @Given("que je suis sur la page de téléchargements")
    public void queJeSuisSurLaPageDeTéléchargements() {
        // Commentaire : Initialisation de la page de téléchargements
        // Action : Appel de la méthode pour initialiser la page
        downloadsPage = new DownloadsPage();
    }

    @Given("que j'ai des téléchargements en cours")
    public void queJaiDesTéléchargementsEnCours() {
        // Commentaire : Simulation de téléchargements en cours
        // Action : Appel de la méthode pour simuler les téléchargements
        downloadsPage.simulerTéléchargementsEnCours();
    }

    @When("la page est chargée")
    public void laPageEstChargée() {
        // Commentaire : Chargement de la page de téléchargements
        // Action : Appel de la méthode pour charger la page
        downloadsPage.chargerPage();
    }

    @Then("je vois l'icône {string}")
    public void jeVoisLIcone(String icone) {
        // Commentaire : Vérification de l'icône
        // Action : Appel de la méthode pour vérifier l'icône
        Assert.assertTrue(downloadsPage.estPrésent(icone));
    }

    @Then("je vois le texte {string}")
    public void jeVoisLeTexte(String texte) {
        // Commentaire : Vérification du texte
        // Action : Appel de la méthode pour vérifier le texte
        Assert.assertTrue(downloadsPage.estPrésent(texte));
    }

    @Then("je vois une liste de téléchargements")
    public void jeVoisUneListeDeTéléchargements() {
        // Commentaire : Vérification de la liste de téléchargements
        // Action : Appel de la méthode pour vérifier la liste
        Assert.assertTrue(downloadListPage.estPrésent());
    }

    @Then("chaque téléchargement a une image")
    public void chaqueTéléchargementAUneImage() {
        // Commentaire : Vérification de l'image pour chaque téléchargement
        // Action : Appel de la méthode pour vérifier les images
        downloadListPage.vérifierImages();
    }

    @Then("chaque téléchargement a un texte")
    public void chaqueTéléchargementAUnTexte() {
        // Commentaire : Vérification du texte pour chaque téléchargement
        // Action : Appel de la méthode pour vérifier les textes
        downloadListPage.vérifierTextes();
    }

    @Then("chaque téléchargement a un icône de lecture")
    public void chaqueTéléchargementAUnIconeDeLecture() {
        // Commentaire : Vérification de l'icône de lecture pour chaque téléchargement
        // Action : Appel de la méthode pour vérifier les icônes de lecture
        downloadListPage.vérifierIconesLecture();
    }

    @Then("chaque téléchargement a un icône de suppression")
    public void chaqueTéléchargementAUnIconeDeSuppression() {
        // Commentaire : Vérification de l'icône de suppression pour chaque téléchargement
        // Action : Appel de la méthode pour vérifier les icônes de suppression
        downloadListPage.vérifierIconesSuppression();
    }

    @Then("chaque téléchargement a un indicateur de téléchargement")
    public void chaqueTéléchargementAUnIndicateurDeTéléchargement() {
        // Commentaire : Vérification de l'indicateur de téléchargement pour chaque téléchargement
        // Action : Appel de la méthode pour vérifier les indicateurs de téléchargement
        downloadListPage.vérifierIndicateursTéléchargement();
    }

    @Then("je vois les détails du téléchargement")
    public void jeVoisLesDétailsDuTéléchargement() {
        // Commentaire : Vérification des détails du téléchargement
        // Action : Appel de la méthode pour vérifier les détails
        downloadDetailsPage.vérifierDétails();
    }

    @Then("je vois le texte du téléchargement")
    public void jeVoisLeTexteDuTéléchargement() {
        // Commentaire : Vérification du texte du téléchargement
        // Action : Appel de la méthode pour vérifier le texte
        Assert.assertTrue(downloadDetailsPage.estPrésent("texte du téléchargement"));
    }

    @Then("je vois le sous-texte du téléchargement")
    public void jeVoisLeSousTexteDuTéléchargement() {
        // Commentaire : Vérification du sous-texte du téléchargement
        // Action : Appel de la méthode pour vérifier le sous-texte
        Assert.assertTrue(downloadDetailsPage.estPrésent("sous-texte du téléchargement"));
    }

    @Then("je vois l'icône de lecture du téléchargement")
    public void jeVoisLIconeDeLectureDuTéléchargement() {
        // Commentaire : Vérification de l'icône de lecture du téléchargement
        // Action : Appel de la méthode pour vérifier l'icône de lecture
        Assert.assertTrue(downloadDetailsPage.estPrésent("icône de lecture"));
    }

    @Then("je vois l'icône de suppression du téléchargement")
    public void jeVoisLIconeDeSuppressionDuTéléchargement() {
        // Commentaire : Vérification de l'icône de suppression du téléchargement
        // Action : Appel de la méthode pour vérifier l'icône de suppression
        Assert.assertTrue(downloadDetailsPage.estPrésent("icône de suppression"));
    }

    @Then("je vois l'indicateur de téléchargement du téléchargement")
    public void jeVoisLIndicateurDeTéléchargementDuTéléchargement() {
        // Commentaire : Vérification de l'indicateur de téléchargement du téléchargement
        // Action : Appel de la méthode pour vérifier l'indicateur de téléchargement
        Assert.assertTrue(downloadDetailsPage.estPrésent("indicateur de téléchargement"));
    }

    @Then("le téléchargement est supprimé de la liste")
    public void leTéléchargementEstSuppriméDeLaListe() {
        // Commentaire : Vérification de la suppression du téléchargement
        // Action : Appel de la méthode pour vérifier la suppression
        downloadListPage.vérifierSuppression();
    }

    @Then("je vois un message de confirmation de suppression")
    public void jeVoisUnMessageDeConfirmationDeSuppression() {
        // Commentaire : Vérification du message de confirmation de suppression
        // Action : Appel de la méthode pour vérifier le message
        Assert.assertTrue(downloadDetailsPage.estPrésent("message de confirmation de suppression"));
    }

    @Then("le téléchargement est lancé en lecture")
    public void leTéléchargementEstLancéEnLecture() {
        // Commentaire : Vérification de la lecture du téléchargement
        // Action : Appel de la méthode pour vérifier la lecture
        downloadDetailsPage.vérifierLecture();
    }

    @Then("je vois le contenu du téléchargement en lecture")
    public void jeVoisLeContenuDuTéléchargementEnLecture() {
        // Commentaire : Vérification du contenu du téléchargement en lecture
        // Action : Appel de la méthode pour vérifier le contenu
        Assert.assertTrue(downloadDetailsPage.estPrésent("contenu du téléchargement"));
    }
}