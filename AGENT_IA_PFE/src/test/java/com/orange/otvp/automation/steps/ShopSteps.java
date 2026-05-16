package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.ShopPage;
import com.orange.otvp.automation.pages.OffrePage;
import com.orange.otvp.automation.pages.ErrorPage;

public class ShopSteps {

    private ShopPage shopPage;
    private OffrePage offrePage;
    private ErrorPage errorPage;

    @Given("que l'utilisateur est sur la page Shop")
    public void queLUtilisateurEstSurLaPageShop() {
        // Commentaire : Initialisation de la page Shop
        // Action : Appel de la méthode pour initialiser la page Shop
        shopPage = new ShopPage();
        shopPage.initialiserPage();
    }

    @When("l'utilisateur parcourt les offres disponibles")
    public void lUtilisateurParcourtLesOffresDisponibles() {
        // Commentaire : Parcours des offres disponibles
        // Action : Appel de la méthode pour parcourir les offres disponibles
        shopPage.parcourirOffres();
    }

    @Then("les offres sont affichées avec leurs images et leurs catégories")
    public void lesOffresSontAfficheesAvecLeursImagesEtLeursCategories() {
        // Commentaire : Vérification des offres affichées
        // Action : Appel de la méthode pour vérifier les offres affichées
        Assert.assertTrue(shopPage.vérifierOffresAffichées());
    }

    @And("les offres sont classées par catégorie")
    public void lesOffresSontClasséesParCatégorie() {
        // Commentaire : Vérification des offres classées par catégorie
        // Action : Appel de la méthode pour vérifier les offres classées par catégorie
        Assert.assertTrue(shopPage.vérifierOffresClasséesParCatégorie());
    }

    @When("l'utilisateur sélectionne une offre et clique sur le bouton \"S'ABONNER\"")
    public void lUtilisateurSélectionneUneOffreEtCliqueSurLeBoutonSAbonner() {
        // Commentaire : Sélection d'une offre et clic sur le bouton "S'ABONNER"
        // Action : Appel de la méthode pour sélectionner une offre et clic sur le bouton "S'ABONNER"
        offrePage = shopPage.sélectionnerOffreEtCliqueSurBoutonSAbonner();
    }

    @Then("l'utilisateur est redirigé vers la page de détails de l'offre")
    public void lUtilisateurEstRedirigéVersLaPageDeDétailsDeLOffre() {
        // Commentaire : Vérification de la redirection vers la page de détails de l'offre
        // Action : Appel de la méthode pour vérifier la redirection vers la page de détails de l'offre
        Assert.assertTrue(offrePage.vérifierRedirectionVersPageDeDétails());
    }

    @And("les détails de l'offre sont affichés, y compris le nom, le prix et les canaux disponibles")
    public void lesDétailsDeLOffreSontAffichésYComprisLeNomLePrixEtLesCanauxDisponibles() {
        // Commentaire : Vérification des détails de l'offre affichés
        // Action : Appel de la méthode pour vérifier les détails de l'offre affichés
        Assert.assertTrue(offrePage.vérifierDétailsDeLOffreAffichés());
    }

    @And("le bouton \"S'ABONNER\" est présent et fonctionnel")
    public void leBoutonSAbonnerEstPrésentEtFonctionnel() {
        // Commentaire : Vérification du bouton "S'ABONNER" présent et fonctionnel
        // Action : Appel de la méthode pour vérifier le bouton "S'ABONNER" présent et fonctionnel
        Assert.assertTrue(offrePage.vérifierBoutonSAbonnerPrésentEtFonctionnel());
    }

    @When("une erreur se produit lors du chargement des offres")
    public void uneErreurSeProduitLorsDuChargementDesOffres() {
        // Commentaire : Simulation d'une erreur lors du chargement des offres
        // Action : Appel de la méthode pour simuler une erreur lors du chargement des offres
        errorPage = shopPage.simulerErreurLorsDuChargementDesOffres();
    }

    @Then("un message d'erreur est affiché à l'utilisateur")
    public void unMessageDErreurEstAffichéÀLUtilisateur() {
        // Commentaire : Vérification du message d'erreur affiché
        // Action : Appel de la méthode pour vérifier le message d'erreur affiché
        Assert.assertTrue(errorPage.vérifierMessageDErreurAffiché());
    }

    @And("le message d'erreur est clair et concis")
    public void leMessageDErreurEstClairEtConcis() {
        // Commentaire : Vérification du message d'erreur clair et concis
        // Action : Appel de la méthode pour vérifier le message d'erreur clair et concis
        Assert.assertTrue(errorPage.vérifierMessageDErreurClairEtConcis());
    }

    @And("l'utilisateur peut réessayer de charger les offres")
    public void lUtilisateurPeutRéessayerDeChargerLesOffres() {
        // Commentaire : Vérification de la possibilité de réessayer de charger les offres
        // Action : Appel de la méthode pour vérifier la possibilité de réessayer de charger les offres
        Assert.assertTrue(errorPage.vérifierPossibilitéDeRéessayerDeChargerLesOffres());
    }

    @When("l'utilisateur sélectionne une offre et clique sur le lien \"Voir tous les canaux\"")
    public void lUtilisateurSélectionneUneOffreEtCliqueSurLeLienVoirTousLesCanaux() {
        // Commentaire : Sélection d'une offre et clic sur le lien "Voir tous les canaux"
        // Action : Appel de la méthode pour sélectionner une offre et clic sur le lien "Voir tous les canaux"
        offrePage = shopPage.sélectionnerOffreEtCliqueSurLienVoirTousLesCanaux();
    }

    @Then("la liste des canaux disponibles pour l'offre est affichée")
    public void laListeDesCanauxDisponiblesPourLOffreEstAffichée() {
        // Commentaire : Vérification de la liste des canaux disponibles pour l'offre affichée
        // Action : Appel de la méthode pour vérifier la liste des canaux disponibles pour l'offre affichée
        Assert.assertTrue(offrePage.vérifierListeDesCanauxDisponiblesPourLOffreAffichée());
    }

    @And("les canaux sont classés par ordre alphabétique")
    public void lesCanauxSontClassésParOrdreAlphabétique() {
        // Commentaire : Vérification des canaux classés par ordre alphabétique
        // Action : Appel de la méthode pour vérifier les canaux classés par ordre alphabétique
        Assert.assertTrue(offrePage.vérifierCanauxClassésParOrdreAlphabétique());
    }

    @And("l'utilisateur peut revenir à la page précédente")
    public void lUtilisateurPeutRévenirÀLaPagePrécédente() {
        // Commentaire : Vérification de la possibilité de revenir à la page précédente
        // Action : Appel de la méthode pour vérifier la possibilité de revenir à la page précédente
        Assert.assertTrue(offrePage.vérifierPossibilitéDeRévenirÀLaPagePrécédente());
    }

    @When("l'utilisateur sélectionne une offre et clique sur le bouton \"Détails\"")
    public void lUtilisateurSélectionneUneOffreEtCliqueSurLeBoutonDétails() {
        // Commentaire : Sélection d'une offre et clic sur le bouton "Détails"
        // Action : Appel de la méthode pour sélectionner une offre et clic sur le bouton "Détails"
        offrePage = shopPage.sélectionnerOffreEtCliqueSurBoutonDétails();
    }

    @Then("les détails de l'offre sont affichés, y compris le nom, le prix et les canaux disponibles")
    public void lesDétailsDeLOffreSontAffichésYComprisLeNomLePrixEtLesCanauxDisponibles() {
        // Commentaire : Vérification des détails de l'offre affichés
        // Action : Appel de la méthode pour vérifier les détails de l'offre affichés
        Assert.assertTrue(offrePage.vérifierDétailsDeLOffreAffichés());
    }

    @And("les détails de l'offre sont clairs et concis")
    public void lesDétailsDeLOffreSontClairsEtConcis() {
        // Commentaire : Vérification que les détails de l'offre sont clairs et concis
        // Action : Appel de la méthode pour vérifier les détails de l'offre
        Assert.assertTrue(shopPage.areOfferDetailsClearAndConcise());
    }
}