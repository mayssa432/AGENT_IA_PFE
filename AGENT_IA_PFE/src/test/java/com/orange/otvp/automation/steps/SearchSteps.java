package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.SearchPage;
import com.orange.otvp.automation.pages.SearchResultPage;

public class SearchSteps {

    private SearchPage searchPage;
    private SearchResultPage searchResultPage;

    @Given("L'utilisateur est sur la page d'accueil de l'application")
    public void lUtilisateurEstSurLaPageDAccueilDeLApplication() {
        // Commentaire : Initialiser la page de recherche
        // Action : Appeler la méthode pour initialiser la page de recherche
        searchPage = new SearchPage();
        searchPage.initialiserPage();
    }

    @When("L'utilisateur saisit le terme de recherche {string} dans la barre de recherche")
    public void lUtilisateurSaisitLeTermeDeRechercheDansLaBarreDeRecherche(String termeDeRecherche) {
        // Commentaire : Saisir le terme de recherche dans la barre de recherche
        // Action : Appeler la méthode pour saisir le terme de recherche
        searchPage.saisirTermeDeRecherche(termeDeRecherche);
    }

    @When("L'utilisateur clique sur le bouton de recherche")
    public void lUtilisateurCliqueSurLeBoutonDeRecherche() {
        // Commentaire : Clique sur le bouton de recherche
        // Action : Appeler la méthode pour cliquer sur le bouton de recherche
        searchPage.cliqueSurBoutonDeRecherche();
    }

    @Then("La liste des résultats de recherche est affichée")
    public void laListeDesRésultatsDeRechercheEstAffichée() {
        // Commentaire : Vérifier que la liste des résultats de recherche est affichée
        // Action : Appeler la méthode pour vérifier que la liste des résultats de recherche est affichée
        Assert.assertTrue(searchResultPage.estLaListeDesRésultatsDeRechercheAffichée());
    }

    @Then("La vue des résultats de recherche contient des éléments de recherche")
    public void laVueDesRésultatsDeRechercheContientDesÉlémentsDeRecherche() {
        // Commentaire : Vérifier que la vue des résultats de recherche contient des éléments de recherche
        // Action : Appeler la méthode pour vérifier que la vue des résultats de recherche contient des éléments de recherche
        Assert.assertTrue(searchResultPage.estLaVueDesRésultatsDeRechercheContientDesÉlémentsDeRecherche());
    }

    @When("L'utilisateur clique sur le bouton {string}")
    public void lUtilisateurCliqueSurLeBouton(String bouton) {
        // Commentaire : Clique sur le bouton
        // Action : Appeler la méthode pour cliquer sur le bouton
        searchPage.cliqueSurBouton(bouton);
    }

    @Then("Un message d'erreur est affiché pour indiquer que le terme de recherche est vide")
    public void unMessageDErreurEstAffichéPourIndiquerQueLeTermeDeRechercheEstVide() {
        // Commentaire : Vérifier que le message d'erreur est affiché
        // Action : Appeler la méthode pour vérifier que le message d'erreur est affiché
        Assert.assertTrue(searchResultPage.estUnMessageDErreurAffichéPourIndiquerQueLeTermeDeRechercheEstVide());
    }

    @When("L'utilisateur sélectionne la catégorie {string}")
    public void lUtilisateurSélectionneLaCatégorie(String catégorie) {
        // Commentaire : Sélectionner la catégorie
        // Action : Appeler la méthode pour sélectionner la catégorie
        searchPage.sélectionnerCatégorie(catégory);
    }

    @Then("La liste des résultats de recherche affiche uniquement des {string}")
    public void laListeDesRésultatsDeRechercheAfficheUniquementDes(String catégorie) {
        // Commentaire : Vérifier que la liste des résultats de recherche affiche uniquement des programmes de la catégorie sélectionnée
        // Action : Appeler la méthode pour vérifier que la liste des résultats de recherche affiche uniquement des programmes de la catégorie sélectionnée
        Assert.assertTrue(searchResultPage.estLaListeDesRésultatsDeRechercheAfficheUniquementDes(catégory));
    }

    @When("L'utilisateur sélectionne un programme dans la liste des résultats de recherche")
    public void lUtilisateurSélectionneUnProgrammeDansLaListeDesRésultatsDeRecherche() {
        // Commentaire : Sélectionner un programme dans la liste des résultats de recherche
        // Action : Appeler la méthode pour sélectionner un programme dans la liste des résultats de recherche
        searchPage.sélectionnerProgrammeDansLaListeDesRésultatsDeRecherche();
    }

    @Then("Les détails du programme sont affichés, notamment le titre, la durée et la note")
    public void lesDétailsDuProgrammeSontAffichésNotammentLeTitreLaDuréeEtLaNote() {
        // Commentaire : Vérifier que les détails du programme sont affichés
        // Action : Appeler la méthode pour vérifier que les détails du programme sont affichés
        Assert.assertTrue(searchResultPage.estLesDétailsDuProgrammeAffichésNotammentLeTitreLaDuréeEtLaNote());
    }

    @Then("Un message est affiché pour indiquer que aucun résultat n'a été trouvé")
    public void unMessageEstAffichéPourIndiquerQueAucunRésultatNAuEtéTrouvé() {
        // Commentaire : Vérifier que le message est affiché
        // Action : Appeler la méthode pour vérifier que le message est affiché
        Assert.assertTrue(searchResultPage.estUnMessageAffichéPourIndiquerQueAucunRésultatNAuEtéTrouvé());
    }

    @When("L'utilisateur clique sur le bouton {string} pour vider la barre de recherche")
    public void lUtilisateurCliqueSurLeBoutonPourViderLaBarreDeRecherche(String bouton) {
        // Commentaire : Clique sur le bouton pour vider la barre de recherche
        // Action : Appeler la méthode pour cliquer sur le bouton pour vider la barre de recherche
        searchPage.cliqueSurBoutonPourViderLaBarreDeRecherche(bouton);
    }

    @Then("La barre de recherche est vidée")
    public void laBarreDeRechercheEstVidée() {
        // Commentaire : Vérifier que la barre de recherche est vidée
        // Action : Appeler la méthode pour vérifier que la barre de recherche est vidée
        Assert.assertTrue(searchPage.estLaBarreDeRechercheVidée());
    }

    @When("L'utilisateur clique sur le bouton {string} pour accéder à un programme en replay")
    public void lUtilisateurCliqueSurLeBoutonPourAccéderÀUnProgrammeEnReplay(String bouton) {
        // Commentaire : Clique sur le bouton pour accéder à un programme en replay
        // Action : Appeler la méthode pour cliquer sur le bouton pour accéder à un programme en replay
        searchPage.cliqueSurBoutonPourAccéderÀUnProgrammeEnReplay(bouton);
    }

    @Then("Le programme est lancé en replay")
    public void leProgrammeEstLancéEnReplay() {
        // Commentaire : Vérifier que le programme est lancé en replay
        // Action : Appeler la méthode pour vérifier que le programme est lancé en replay
        Assert.assertTrue(searchResultPage.estLeProgrammeLancéEnReplay());
    }

    @When("L'utilisateur clique sur le bouton {string} pour accéder à un programme en VOD")
    public void lUtilisateurCliqueSurLeBoutonPourAccéderÀUnProgrammeEnVOD(String bouton) {
        // Commentaire : Clique sur le bouton pour accéder à un programme en VOD
        // Action : Appeler la méthode pour cliquer sur le bouton pour accéder à un programme en VOD
        searchPage.cliqueSurBoutonPourAccéderÀUnProgrammeEnVOD(bouton);
    }

    @Then("Le programme est lancé en VOD")
    public void leProgrammeEstLancéEnVOD() {
        // Commentaire : Vérifier que le programme est lancé en VOD
        // Action : Appeler la méthode pour vérifier que le programme est lancé en VOD
        Assert.assertTrue(searchResultPage.estLeProgrammeLancéEnVOD());
    }

    @When("L'utilisateur clique sur le bouton {string} pour accéder à la liste des épisodes d'un programme")
    public void lUtilisateurCliqueSurLeBoutonPourAccéderÀLaListeDesÉpisodesDUnProgramme(String bouton) {
        // Commentaire : Clique sur le bouton pour accéder à la liste des épisodes d'un programme
        // Action : Appeler la méthode pour cliquer sur le bouton
        searchPage.clickOnButtonToAccessEpisodesList(bouton);
    }
}