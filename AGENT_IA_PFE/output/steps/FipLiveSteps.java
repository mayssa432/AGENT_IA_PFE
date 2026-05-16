package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.FipLivePage;
import com.orange.otvp.automation.pages.ProgrammePage;
import com.orange.otvp.automation.pages.EnregistrementPage;
import com.orange.otvp.automation.pages.ModificationEnregistrementPage;

public class FipLiveSteps {

    private FipLivePage fipLivePage;
    private ProgrammePage programmePage;
    private EnregistrementPage enregistrementPage;
    private ModificationEnregistrementPage modificationEnregistrementPage;

    @Given("que l'utilisateur est sur la page FipLive")
    public void queLUtilisateurEstSurLaPageFipLive() {
        // Commentaire : Initialiser la page FipLive
        // Action : Récupérer l'instance de la page FipLive
        fipLivePage = new FipLivePage();
    }

    @When("l'utilisateur affiche la page")
    public void lUtilisateurAfficheLaPage() {
        // Commentaire : Afficher la page FipLive
        // Action : Appeler la méthode pour afficher la page FipLive
        fipLivePage.afficherPage();
    }

    @Then("les éléments suivants sont présents :")
    public void lesElementsSuivantsSontPresentes() {
        // Commentaire : Vérifier la présence des éléments sur la page FipLive
        // Action : Appeler les méthodes pour vérifier la présence des éléments
        Assert.assertTrue(fipLivePage.estLeTitreDeLaPageFipLiveAffiche());
        Assert.assertTrue(fipLivePage.estLeBoutonDeLectureAffiche());
        Assert.assertTrue(fipLivePage.estLeBoutonDeRedemarrageAffiche());
        Assert.assertTrue(fipLivePage.estLeBoutonDeRappelAffiche());
        Assert.assertTrue(fipLivePage.estLeBoutonDenregistrementAffiche());
        Assert.assertTrue(fipLivePage.estLaListeDesActeursAffichee());
        Assert.assertTrue(fipLivePage.estLaDescriptionDuProgrammeAffichee());
        Assert.assertTrue(fipLivePage.estLaBarreDeProgressionAffichee());
    }

    @Then("le titre de la page FipLive est affiché")
    public void leTitreDeLaPageFipLiveEstAffiche() {
        // Commentaire : Vérifier que le titre de la page FipLive est affiché
        // Action : Appeler la méthode pour vérifier la présence du titre
        Assert.assertTrue(fipLivePage.estLeTitreDeLaPageFipLiveAffiche());
    }

    @Then("le bouton de lecture est affiché")
    public void leBoutonDeLectureEstAffiche() {
        // Commentaire : Vérifier que le bouton de lecture est affiché
        // Action : Appeler la méthode pour vérifier la présence du bouton
        Assert.assertTrue(fipLivePage.estLeBoutonDeLectureAffiche());
    }

    @Then("le bouton de redémarrage est affiché")
    public void leBoutonDeRedemarrageEstAffiche() {
        // Commentaire : Vérifier que le bouton de redémarrage est affiché
        // Action : Appeler la méthode pour vérifier la présence du bouton
        Assert.assertTrue(fipLivePage.estLeBoutonDeRedemarrageAffiche());
    }

    @Then("le bouton de rappel est affiché")
    public void leBoutonDeRappelEstAffiche() {
        // Commentaire : Vérifier que le bouton de rappel est affiché
        // Action : Appeler la méthode pour vérifier la présence du bouton
        Assert.assertTrue(fipLivePage.estLeBoutonDeRappelAffiche());
    }

    @Then("le bouton d'enregistrement est affiché")
    public void leBoutonDenregistrementEstAffiche() {
        // Commentaire : Vérifier que le bouton d'enregistrement est affiché
        // Action : Appeler la méthode pour vérifier la présence du bouton
        Assert.assertTrue(fipLivePage.estLeBoutonDenregistrementAffiche());
    }

    @Then("la liste des acteurs est affichée")
    public void laListeDesActeursEstAffichee() {
        // Commentaire : Vérifier que la liste des acteurs est affichée
        // Action : Appeler la méthode pour vérifier la présence de la liste
        Assert.assertTrue(fipLivePage.estLaListeDesActeursAffichee());
    }

    @Then("la description du programme est affichée")
    public void laDescriptionDuProgrammeEstAffichee() {
        // Commentaire : Vérifier que la description du programme est affichée
        // Action : Appeler la méthode pour vérifier la présence de la description
        Assert.assertTrue(fipLivePage.estLaDescriptionDuProgrammeAffichee());
    }

    @Then("la barre de progression est affichée")
    public void laBarreDeProgressionEstAffichee() {
        // Commentaire : Vérifier que la barre de progression est affichée
        // Action : Appeler la méthode pour vérifier la présence de la barre
        Assert.assertTrue(fipLivePage.estLaBarreDeProgressionAffichee());
    }

    @When("l'utilisateur clique sur le bouton de lecture")
    public void lUtilisateurCliqueSurLeBoutonDeLecture() {
        // Commentaire : Clique sur le bouton de lecture
        // Action : Appeler la méthode pour cliquer sur le bouton
        programmePage = fipLivePage.cliqueSurLeBoutonDeLecture();
    }

    @Then("le programme commence à être lu")
    public void leProgrammeCommenceATreLu() {
        // Commentaire : Vérifier que le programme commence à être lu
        // Action : Appeler la méthode pour vérifier la lecture du programme
        Assert.assertTrue(programmePage.estLeProgrammeCommenceATreLu());
    }

    @Then("la barre de progression commence à avancer")
    public void laBarreDeProgressionCommenceAAvancer() {
        // Commentaire : Vérifier que la barre de progression commence à avancer
        // Action : Appeler la méthode pour vérifier l'avancement de la barre
        Assert.assertTrue(programmePage.estLaBarreDeProgressionCommenceAAvancer());
    }

    @Then("le bouton de lecture est remplacé par le bouton de pause")
    public void leBoutonDeLectureEstRemplaceParLeBoutonDePause() {
        // Commentaire : Vérifier que le bouton de lecture est remplacé par le bouton de pause
        // Action : Appeler la méthode pour vérifier la remplacement du bouton
        Assert.assertTrue(programmePage.estLeBoutonDeLectureEstRemplaceParLeBoutonDePause());
    }

    @When("l'utilisateur clique sur le bouton d'enregistrement")
    public void lUtilisateurCliqueSurLeBoutonDenregistrement() {
        // Commentaire : Clique sur le bouton d'enregistrement
        // Action : Appeler la méthode pour cliquer sur le bouton
        enregistrementPage = fipLivePage.cliqueSurLeBoutonDenregistrement();
    }

    @Then("le programme est enregistré")
    public void leProgrammeEstEnregistre() {
        // Commentaire : Vérifier que le programme est enregistré
        // Action : Appeler la méthode pour vérifier l'enregistrement du programme
        Assert.assertTrue(enregistrementPage.estLeProgrammeEstEnregistre());
    }

    @Then("un message de confirmation d'enregistrement est affiché")
    public void unMessageDeConfirmationDenregistrementEstAffiche() {
        // Commentaire : Vérifier que le message de confirmation d'enregistrement est affiché
        // Action : Appeler la méthode pour vérifier l'affichage du message
        Assert.assertTrue(enregistrementPage.estUnMessageDeConfirmationDenregistrementEstAffiche());
    }

    @Then("le bouton d'enregistrement est remplacé par le bouton de modification de l'enregistrement")
    public void leBoutonDenregistrementEstRemplaceParLeBoutonDeModificationDeLenregistrement() {
        // Commentaire : Vérifier que le bouton d'enregistrement est remplacé par le bouton de modification de l'enregistrement
        // Action : Appeler la méthode pour vérifier la remplacement du bouton
        Assert.assertTrue(enregistrementPage.estLeBoutonDenregistrementEstRemplaceParLeBoutonDeModificationDeLenregistrement());
    }

    @When("l'utilisateur clique sur le bouton de suppression de l'enregistrement")
    public void lUtilisateurCliqueSurLeBoutonDeSuppressionDeLenregistrement() {
        // Commentaire : Clique sur le bouton de suppression de l'enregistrement
        // Action : Appeler la méthode pour cliquer sur le bouton
        enregistrementPage = fipLivePage.cliqueSurLeBoutonDeSuppressionDeLenregistrement();