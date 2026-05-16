package com.orange.otvp.automation.steps;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.FilterPage;
import com.orange.otvp.automation.pages.HomePage;

public class FilterSteps {

    private FilterPage filterPage;
    private HomePage homePage;

    @Given("que je suis sur la page de filtre")
    public void queJeSuisSurLaPageDeFiltre() {
        // Commentaire : Aller sur la page de filtre
        // Action : Aller sur la page de filtre
        homePage = new HomePage();
        homePage.navigateToFilterPage();
        filterPage = new FilterPage();
    }

    @When("je clique sur le bouton de filtre par genre")
    public void jeCliqueSurLeBoutonDeFiltreParGenre() {
        // Commentaire : Clique sur le bouton de filtre par genre
        // Action : Clique sur le bouton de filtre par genre
        filterPage.clickFilterByGenreButton();
    }

    @And("je sélectionne le genre {string}")
    public void jeSelectionneLeGenre(String genre) {
        // Commentaire : Sélectionner le genre
        // Action : Sélectionner le genre
        filterPage.selectGenre(genre);
    }

    @Then("je vois uniquement les contenus de genre {string}")
    public void jeVoisUniquementLesContenusDeGenre(String genre) {
        // Commentaire : Vérifier que les contenus de genre sont affichés
        // Action : Vérifier que les contenus de genre sont affichés
        Assert.assertTrue(filterPage.isGenreFilterApplied(genre));
    }

    @When("je clique sur le bouton de filtre par jour")
    public void jeCliqueSurLeBoutonDeFiltreParJour() {
        // Commentaire : Clique sur le bouton de filtre par jour
        // Action : Clique sur le bouton de filtre par jour
        filterPage.clickFilterByDayButton();
    }

    @And("je sélectionne le jour {string}")
    public void jeSelectionneLeJour(String jour) {
        // Commentaire : Sélectionner le jour
        // Action : Sélectionner le jour
        filterPage.selectDay(jour);
    }

    @Then("je vois uniquement les contenus diffusés aujourd'hui")
    public void jeVoisUniquementLesContenusDiffusesAujourdHui() {
        // Commentaire : Vérifier que les contenus diffusés aujourd'hui sont affichés
        // Action : Vérifier que les contenus diffusés aujourd'hui sont affichés
        Assert.assertTrue(filterPage.isDayFilterApplied("Aujourd'hui"));
    }

    @When("je clique sur le bouton de filtre par heure")
    public void jeCliqueSurLeBoutonDeFiltreParHeure() {
        // Commentaire : Clique sur le bouton de filtre par heure
        // Action : Clique sur le bouton de filtre par heure
        filterPage.clickFilterByHourButton();
    }

    @And("je sélectionne l'heure {string}")
    public void jeSelectionneLHeure(String heure) {
        // Commentaire : Sélectionner l'heure
        // Action : Sélectionner l'heure
        filterPage.selectHour(heure);
    }

    @Then("je vois uniquement les contenus diffusés entre {string} et {string}")
    public void jeVoisUniquementLesContenusDiffusesEntreEt(String heureDebut, String heureFin) {
        // Commentaire : Vérifier que les contenus diffusés entre les heures sont affichés
        // Action : Vérifier que les contenus diffusés entre les heures sont affichés
        Assert.assertTrue(filterPage.isHourFilterApplied(heureDebut, heureFin));
    }

    @When("je clique sur le bouton de filtre par catégorie VOD")
    public void jeCliqueSurLeBoutonDeFiltreParCatégorieVod() {
        // Commentaire : Clique sur le bouton de filtre par catégorie VOD
        // Action : Clique sur le bouton de filtre par catégorie VOD
        filterPage.clickFilterByVodCategoryButton();
    }

    @And("je sélectionne la catégorie {string}")
    public void jeSelectionneLaCatégorie(String categorie) {
        // Commentaire : Sélectionner la catégorie
        // Action : Sélectionner la catégorie
        filterPage.selectVodCategory(categorie);
    }

    @Then("je vois uniquement les contenus VOD de catégorie {string}")
    public void jeVoisUniquementLesContenusVodDeCatégorie(String categorie) {
        // Commentaire : Vérifier que les contenus VOD de catégorie sont affichés
        // Action : Vérifier que les contenus VOD de catégorie sont affichés
        Assert.assertTrue(filterPage.isVodCategoryFilterApplied(categorie));
    }

    @When("je clique sur le bouton de réinitialisation des filtres")
    public void jeCliqueSurLeBoutonDeRéinitialisationDesFiltres() {
        // Commentaire : Clique sur le bouton de réinitialisation des filtres
        // Action : Clique sur le bouton de réinitialisation des filtres
        filterPage.clickResetFiltersButton();
    }

    @Then("tous les filtres sont réinitialisés et je vois tous les contenus")
    public void tousLesFiltresSontRéinitialisésEtJeVoisTousLesContenus() {
        // Commentaire : Vérifier que tous les filtres sont réinitialisés et que tous les contenus sont affichés
        // Action : Vérifier que tous les filtres sont réinitialisés et que tous les contenus sont affichés
        Assert.assertTrue(filterPage.areAllFiltersReset());
    }

    @When("je clique sur le bouton d'application des filtres")
    public void jeCliqueSurLeBoutonDAppliquerLesFiltres() {
        // Commentaire : Clique sur le bouton d'application des filtres
        // Action : Clique sur le bouton d'application des filtres
        filterPage.clickApplyFiltersButton();
    }

    @Then("les contenus sont affichés en fonction des filtres sélectionnés")
    public void lesContenusSontAffichésEnFonctionDesFiltresSélectionnés() {
        // Commentaire : Vérifier que les contenus sont affichés en fonction des filtres sélectionnés
        // Action : Vérifier que les contenus sont affichés en fonction des filtres sélectionnés
        Assert.assertTrue(filterPage.areContentsDisplayedAccordingToFilters());
    }

    @When("je clique sur le bouton de filtre par genre")
    public void jeCliqueSurLeBoutonDeFiltreParGenre2() {
        // Commentaire : Clique sur le bouton de filtre par genre
        // Action : Clique sur le bouton de filtre par genre
        filterPage.clickFilterByGenreButton();
    }

    @And("je sélectionne le genre {string}")
    public void jeSelectionneLeGenre2(String genre) {
        // Commentaire : Sélectionner le genre
        // Action : Sélectionner le genre
        filterPage.selectGenre(genre);
    }

    @When("je clique sur le bouton de filtre par jour")
    public void jeCliqueSurLeBoutonDeFiltreParJour2() {
        // Commentaire : Clique sur le bouton de filtre par jour
        // Action : Clique sur le bouton de filtre par jour
        filterPage.clickFilterByDayButton();
    }

    @And("je sélectionne le jour {string}")
    public void jeSelectionneLeJour2(String jour) {
        // Commentaire : Sélectionner le jour
        // Action : Sélectionner le jour
        filterPage.selectDay(jour);
    }

    @Then("je vois uniquement les contenus de genre {string} diffusés aujourd'hui")
    public void jeVoisUniquementLesContenusDeGenreDiffusesAujourdHui(String genre) {
        // Commentaire : Vérifier que les contenus de genre diffusés aujourd'hui sont affichés
        // Action : Vérifier que les contenus de genre diffusés aujourd'hui sont affichés
        Assert.assertTrue(filterPage.isGenreAndDayFilterApplied(genre, "Aujourd'hui"));
    }
}