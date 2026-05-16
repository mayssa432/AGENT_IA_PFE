package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.FipReplayPage;
import com.orange.otvp.automation.pages.ProgrammeReplayPage;
import com.orange.otvp.automation.pages.EpisodeReplayPage;

public class FipReplaySteps {

    private FipReplayPage fipReplayPage;
    private ProgrammeReplayPage programmeReplayPage;
    private EpisodeReplayPage episodeReplayPage;

    @Given("que l'utilisateur est sur la page d'accueil de FipReplay")
    public void queLUtilisateurEstSurLaPageDAccueilDeFipReplay() {
        // Commentaire : Récupération de la page d'accueil de FipReplay
        // Action : Récupération de la page d'accueil de FipReplay
        fipReplayPage = new FipReplayPage();
    }

    @When("l'utilisateur clique sur l'onglet \"Réplay\"")
    public void lUtilisateurCliqueSurLOngletRéplay() {
        // Commentaire : Clique sur l'onglet "Réplay"
        // Action : Clique sur l'onglet "Réplay"
        fipReplayPage.cliqueSurOngletReplay();
    }

    @Then("la liste des programmes de réplay est affichée")
    public void laListeDesProgrammesDeRéplayEstAffichée() {
        // Commentaire : Vérification de la liste des programmes de réplay
        // Action : Vérification de la liste des programmes de réplay
        Assert.assertTrue(fipReplayPage.estLaListeDesProgrammesDeReplayAffichee());
    }

    @And("le titre du programme est affiché")
    public void leTitreDuProgrammeEstAffiche() {
        // Commentaire : Vérification du titre du programme
        // Action : Vérification du titre du programme
        Assert.assertTrue(fipReplayPage.estLeTitreDuProgrammeAffiche());
    }

    @And("la miniature du programme est affichée")
    public void laMiniatureDuProgrammeEstAffichee() {
        // Commentaire : Vérification de la miniature du programme
        // Action : Vérification de la miniature du programme
        Assert.assertTrue(fipReplayPage.estLaMiniatureDuProgrammeAffichee());
    }

    @And("le logo de la chaîne est affiché")
    public void leLogoDeLaChaineEstAffiche() {
        // Commentaire : Vérification du logo de la chaîne
        // Action : Vérification du logo de la chaîne
        Assert.assertTrue(fipReplayPage.estLeLogoDeLaChaineAffiche());
    }

    @And("le nombre d'épisodes est affiché")
    public void leNombreDEpisodesEstAffiche() {
        // Commentaire : Vérification du nombre d'épisodes
        // Action : Vérification du nombre d'épisodes
        Assert.assertTrue(fipReplayPage.estLeNombreDEpisodesAffiche());
    }

    @When("l'utilisateur clique sur un programme de réplay")
    public void lUtilisateurCliqueSurUnProgrammeDeReplay() {
        // Commentaire : Clique sur un programme de réplay
        // Action : Clique sur un programme de réplay
        programmeReplayPage = new ProgrammeReplayPage();
    }

    @Then("les détails du programme sont affichés")
    public void lesDetailsDuProgrammeSontAffiches() {
        // Commentaire : Vérification des détails du programme
        // Action : Vérification des détails du programme
        Assert.assertTrue(programmeReplayPage.estLesDetailsDuProgrammeAffiches());
    }

    @And("la miniature du programme est affichée")
    public void laMiniatureDuProgrammeEstAffichee1() {
        // Commentaire : Vérification de la miniature du programme
        // Action : Vérification de la miniature du programme
        Assert.assertTrue(programmeReplayPage.estLaMiniatureDuProgrammeAffichee());
    }

    @And("le logo de la chaîne est affiché")
    public void leLogoDeLaChaineEstAffiche1() {
        // Commentaire : Vérification du logo de la chaîne
        // Action : Vérification du logo de la chaîne
        Assert.assertTrue(programmeReplayPage.estLeLogoDeLaChaineAffiche());
    }

    @And("la disponibilité du programme est affichée")
    public void laDisponibiliteDuProgrammeEstAffichee() {
        // Commentaire : Vérification de la disponibilité du programme
        // Action : Vérification de la disponibilité du programme
        Assert.assertTrue(programmeReplayPage.estLaDisponibiliteDuProgrammeAffichee());
    }

    @And("la description du programme est affichée")
    public void laDescriptionDuProgrammeEstAffichee() {
        // Commentaire : Vérification de la description du programme
        // Action : Vérification de la description du programme
        Assert.assertTrue(programmeReplayPage.estLaDescriptionDuProgrammeAffichee());
    }

    @And("le bouton de lecture est affiché")
    public void leBoutonDeLectureEstAffiche() {
        // Commentaire : Vérification du bouton de lecture
        // Action : Vérification du bouton de lecture
        Assert.assertTrue(programmeReplayPage.estLeBoutonDeLectureAffiche());
    }

    @When("l'utilisateur clique sur un épisode de réplay")
    public void lUtilisateurCliqueSurUnEpisodeDeReplay() {
        // Commentaire : Clique sur un épisode de réplay
        // Action : Clique sur un épisode de réplay
        episodeReplayPage = new EpisodeReplayPage();
    }

    @Then("la lecture de l'épisode est lancée")
    public void laLectureDelEpisodeEstLancee() {
        // Commentaire : Vérification de la lecture de l'épisode
        // Action : Vérification de la lecture de l'épisode
        Assert.assertTrue(episodeReplayPage.estLaLectureDelEpisodeLancee());
    }

    @And("le bouton de pause est affiché")
    public void leBoutonDePauseEstAffiche() {
        // Commentaire : Vérification du bouton de pause
        // Action : Vérification du bouton de pause
        Assert.assertTrue(episodeReplayPage.estLeBoutonDePauseAffiche());
    }

    @And("le temps de lecture est affiché")
    public void leTempsDeLectureEstAffiche() {
        // Commentaire : Vérification du temps de lecture
        // Action : Vérification du temps de lecture
        Assert.assertTrue(episodeReplayPage.estLeTempsDeLectureAffiche());
    }

    @When("l'utilisateur clique sur le bouton \"S'abonner\"")
    public void lUtilisateurCliqueSurLeBoutonSAbonner() {
        // Commentaire : Clique sur le bouton "S'abonner"
        // Action : Clique sur le bouton "S'abonner"
        programmeReplayPage.cliqueSurBoutonSAbonner();
    }

    @Then("la page d'abonnement est affichée")
    public void laPageDAbonnementEstAffichee() {
        // Commentaire : Vérification de la page d'abonnement
        // Action : Vérification de la page d'abonnement
        Assert.assertTrue(programmeReplayPage.estLaPageDAbonnementAffichee());
    }

    @And("les informations d'abonnement sont affichées")
    public void lesInformationsDAbonnementSontAffichees() {
        // Commentaire : Vérification des informations d'abonnement
        // Action : Vérification des informations d'abonnement
        Assert.assertTrue(programmeReplayPage.estLesInformationsDAbonnementAffichees());
    }

    @And("le bouton de validation est affiché")
    public void leBoutonDeValidationEstAffiche() {
        // Commentaire : Vérification du bouton de validation
        // Action : Vérification du bouton de validation
        Assert.assertTrue(programmeReplayPage.estLeBoutonDeValidationAffiche());
    }

    @When("l'utilisateur clique sur un épisode de réplay")
    public void lUtilisateurCliqueSurUnEpisodeDeReplay1() {
        // Commentaire : Clique sur un épisode de réplay
        // Action : Clique sur un épisode de réplay
        episodeReplayPage = new EpisodeReplayPage();
    }

    @Then("les informations de l'épisode sont affichées")
    public void lesInformationsDelEpisodeSontAffichees() {
        // Commentaire : Vérification des informations de l'épisode
        // Action : Vérification des informations de l'épisode
        Assert.assertTrue(episodeReplayPage.estLesInformationsDelEpisodeAffichees());
    }

    @And("le titre de l'épisode est affiché")
    public void leTitreDelEpisodeEstAffiche() {
        // Commentaire : Vérification du titre de l'épisode
        // Action : Vérification du titre de l'épisode
        Assert.assertTrue(episodeReplayPage.estLeTitreDelEpisodeAffiche());
    }
}
