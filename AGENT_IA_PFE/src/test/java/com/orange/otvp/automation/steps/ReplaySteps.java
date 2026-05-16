package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import com.orange.otvp.automation.pages.HomePage;
import com.orange.otvp.automation.pages.ReplayPage;
import com.orange.otvp.automation.pages.SearchPage;

public class ReplaySteps {

    private WebDriver driver;
    private HomePage homePage;
    private ReplayPage replayPage;
    private SearchPage searchPage;

    @Given("que je suis sur la page d'accueil")
    public void queJeSuisSurLaPageDAccueil() {
        // Commentaire : Récupérer l'instance de la page d'accueil
        // Action : Récupérer l'instance de la page d'accueil
        homePage = new HomePage(driver);
        homePage.navigateTo();
    }

    @When("je clique sur le bouton \"Replay\"")
    public void jeCliqueSurLeBoutonReplay() {
        // Commentaire : Clique sur le bouton "Replay"
        // Action : Clique sur le bouton "Replay"
        homePage.clickReplayButton();
    }

    @Then("je devrais voir la page Replay avec le titre \"Replay\"")
    public void jeDevraisVoirLaPageReplayAvecLeTitreReplay() {
        // Commentaire : Vérifier que la page Replay est affichée avec le titre "Replay"
        // Action : Vérifier que la page Replay est affichée avec le titre "Replay"
        replayPage = new ReplayPage(driver);
        Assert.assertTrue(replayPage.isReplayPageDisplayed());
        Assert.assertTrue(replayPage.getReplayTitle().contains("Replay"));
    }

    @Given("que je suis sur la page Replay")
    public void queJeSuisSurLaPageReplay() {
        // Commentaire : Récupérer l'instance de la page Replay
        // Action : Récupérer l'instance de la page Replay
        replayPage = new ReplayPage(driver);
        replayPage.navigateTo();
    }

    @When("je clique sur le bouton \"Toutes les chaînes\"")
    public void jeCliqueSurLeBoutonToutesLesChaines() {
        // Commentaire : Clique sur le bouton "Toutes les chaînes"
        // Action : Clique sur le bouton "Toutes les chaînes"
        replayPage.clickAllChannelsButton();
    }

    @Then("je devrais voir la liste des chaînes de replay")
    public void jeDevraisVoirLaListeDesChainesDeReplay() {
        // Commentaire : Vérifier que la liste des chaînes de replay est affichée
        // Action : Vérifier que la liste des chaînes de replay est affichée
        Assert.assertTrue(replayPage.isChannelsListDisplayed());
    }

    @And("je devrais voir les logos des chaînes de replay")
    public void jeDevraisVoirLesLogosDesChainesDeReplay() {
        // Commentaire : Vérifier que les logos des chaînes de replay sont affichés
        // Action : Vérifier que les logos des chaînes de replay sont affichés
        Assert.assertTrue(replayPage.areChannelLogosDisplayed());
    }

    @When("je clique sur une chaîne de replay")
    public void jeCliqueSurUneChaineDeReplay() {
        // Commentaire : Clique sur une chaîne de replay
        // Action : Clique sur une chaîne de replay
        replayPage.clickChannel();
    }

    @Then("je devrais voir les détails de la chaîne de replay sélectionnée")
    public void jeDevraisVoirLesDetailsDeLaChaineDeReplaySelectionnee() {
        // Commentaire : Vérifier que les détails de la chaîne de replay sélectionnée sont affichés
        // Action : Vérifier que les détails de la chaîne de replay sélectionnée sont affichés
        Assert.assertTrue(replayPage.isChannelDetailsDisplayed());
    }

    @And("je devrais voir les épisodes disponibles pour la chaîne de replay sélectionnée")
    public void jeDevraisVoirLesEpisodesDisponiblesPourLaChaineDeReplaySelectionnee() {
        // Commentaire : Vérifier que les épisodes disponibles pour la chaîne de replay sélectionnée sont affichés
        // Action : Vérifier que les épisodes disponibles pour la chaîne de replay sélectionnée sont affichés
        Assert.assertTrue(replayPage.areEpisodesDisplayed());
    }

    @When("je clique sur le menu de tri et de filtrage")
    public void jeCliqueSurLeMenuDeTriEtDeFiltrage() {
        // Commentaire : Clique sur le menu de tri et de filtrage
        // Action : Clique sur le menu de tri et de filtrage
        replayPage.clickFilterMenu();
    }

    @Then("je devrais voir les options de tri et de filtrage")
    public void jeDevraisVoirLesOptionsDeTriEtDeFiltrage() {
        // Commentaire : Vérifier que les options de tri et de filtrage sont affichées
        // Action : Vérifier que les options de tri et de filtrage sont affichées
        Assert.assertTrue(replayPage.isFilterOptionsDisplayed());
    }

    @And("je devrais pouvoir sélectionner une option de tri ou de filtrage")
    public void jeDevraisPouvoirSelectionnerUneOptionDeTriOuDeFiltrage() {
        // Commentaire : Vérifier que les options de tri et de filtrage peuvent être sélectionnées
        // Action : Vérifier que les options de tri et de filtrage peuvent être sélectionnées
        Assert.assertTrue(replayPage.canSelectFilterOption());
    }

    @When("je saisie un mot-clé dans le champ de recherche")
    public void jeSaisieUnMotCleDansLeChampDeRecherche() {
        // Commentaire : Saisir un mot-clé dans le champ de recherche
        // Action : Saisir un mot-clé dans le champ de recherche
        searchPage = new SearchPage(driver);
        searchPage.navigateTo();
        searchPage.sendKeysToSearchField("mot-clé");
    }

    @Then("je devrais voir les résultats de la recherche pour le mot-clé saisi")
    public void jeDevraisVoirLesResultatsDeLaRecherchePourLeMotCleSaisi() {
        // Commentaire : Vérifier que les résultats de la recherche sont affichés
        // Action : Vérifier que les résultats de la recherche sont affichés
        Assert.assertTrue(searchPage.isSearchResultsDisplayed());
    }

    @When("je clique sur un épisode de replay")
    public void jeCliqueSurUnEpisodeDeReplay() {
        // Commentaire : Clique sur un épisode de replay
        // Action : Clique sur un épisode de replay
        replayPage.clickEpisode();
    }

    @Then("je devrais voir les informations détaillées de l'épisode de replay sélectionné")
    public void jeDevraisVoirLesInformationsDetaillesDeLEpisodeDeReplaySelectionne() {
        // Commentaire : Vérifier que les informations détaillées de l'épisode de replay sélectionné sont affichées
        // Action : Vérifier que les informations détaillées de l'épisode de replay sélectionné sont affichées
        Assert.assertTrue(replayPage.isEpisodeDetailsDisplayed());
    }

    @And("je devrais voir les options pour regarder ou télécharger l'épisode de replay sélectionné")
    public void jeDevraisVoirLesOptionsPourRegarderOuTéléchargerLEpisodeDeReplaySelectionné() {
        // Commentaire : Vérifier que les options pour regarder ou télécharger l'épisode de replay sélectionné sont affichées
        // Action : Vérifier que les options pour regarder ou télécharger l'épisode de replay sélectionné sont affichées
        Assert.assertTrue(replayPage.areEpisodeOptionsDisplayed());
    }

    @Then("je devrais voir le logo Orange en haut de la page")
    public void jeDevraisVoirLeLogoOrangeEnHautDeLaPage() {
        // Commentaire : Vérifier que le logo Orange est affiché en haut de la page
        // Action : Vérifier que le logo Orange est affiché en haut de la page
        Assert.assertTrue(replayPage.isOrangeLogoDisplayed());
    }

    @Then("je devrais voir le bouton \"Continuer\" en bas de la page")
    public void jeDevraisVoirLeBoutonContinuerEnBasDeLaPage() {
        // Commentaire : Vérifier que le bouton "Continuer" est affiché en bas de la page
        // Action : Vérifier que le bouton "Continuer" est affiché en bas de la page
        Assert.assertTrue(replayPage.isContinueButtonDisplayed());
    }

    @Then("je devrais voir la barre de recherche en haut de la page")
    public void jeDevraisVoirLaBarreDeRechercheEnHautDeLaPage() {
        // Commentaire : Vérifier que la barre de recherche est affichée en haut de la page
        // Action : Vérifier que la barre de recherche est affichée en haut de la page
        Assert.assertTrue(replayPage.isSearchBarDisplayed());
    }
}