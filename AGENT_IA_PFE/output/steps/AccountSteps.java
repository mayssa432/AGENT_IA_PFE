package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.AccountPage;
import com.orange.otvp.automation.pages.LoginPage;

public class AccountSteps {

    private AccountPage accountPage;
    private LoginPage loginPage;

    @Given("que l'utilisateur est sur la page de connexion")
    public void queLUtilisateurEstSurLaPageDeConnexion() {
        // Commentaire : Implémentation de la connexion à la page de connexion
        // Action : Appel de la méthode pour se connecter à la page de connexion
        loginPage = new LoginPage();
        loginPage.connectToLoginPage();
    }

    @When("l'utilisateur clique sur le bouton \"Identify\"")
    public void lUtilisateurCliqueSurLeBoutonIdentify() {
        // Commentaire : Implémentation du clic sur le bouton "Identify"
        // Action : Appel de la méthode pour cliquer sur le bouton "Identify"
        accountPage = new AccountPage();
        accountPage.clickOnIdentifyButton();
    }

    @Then("le système affiche les détails du compte")
    public void leSystemeAfficheLesDetailsDuCompte() {
        // Commentaire : Implémentation de la vérification des détails du compte
        // Action : Appel de la méthode pour vérifier les détails du compte
        Assert.assertTrue(accountPage.isAccountDetailsDisplayed());
    }

    @Given("que l'utilisateur est connecté à son compte")
    public void queLUtilisateurEstConnecteA SonCompte() {
        // Commentaire : Implémentation de la connexion à son compte
        // Action : Appel de la méthode pour se connecter à son compte
        accountPage = new AccountPage();
        accountPage.connectToAccountPage();
    }

    @When("l'utilisateur clique sur le bouton \"Déconnexion\"")
    public void lUtilisateurCliqueSurLeBoutonDeconnexion() {
        // Commentaire : Implémentation du clic sur le bouton "Déconnexion"
        // Action : Appel de la méthode pour cliquer sur le bouton "Déconnexion"
        accountPage.clickOnLogoutButton();
    }

    @Then("le système déconnecte l'utilisateur et affiche la page de connexion")
    public void leSystemeDeconnecteLUtilisateurEtAfficheLaPageDeConnexion() {
        // Commentaire : Implémentation de la déconnexion et de la vérification de la page de connexion
        // Action : Appel de la méthode pour vérifier que l'utilisateur est déconnecté et sur la page de connexion
        Assert.assertTrue(loginPage.isLoginPageDisplayed());
    }

    @When("l'utilisateur clique sur le bouton \"Détails du compte\"")
    public void lUtilisateurCliqueSurLeBoutonDetailsDuCompte() {
        // Commentaire : Implémentation du clic sur le bouton "Détails du compte"
        // Action : Appel de la méthode pour cliquer sur le bouton "Détails du compte"
        accountPage.clickOnAccountDetailsButton();
    }

    @Then("le système affiche les détails du compte, y compris les informations de service et les offres")
    public void leSystemeAfficheLesDetailsDuCompteYComprisLesInformationsDeServiceEtLesOffres() {
        // Commentaire : Implémentation de la vérification des détails du compte
        // Action : Appel de la méthode pour vérifier les détails du compte
        Assert.assertTrue(accountPage.isAccountDetailsDisplayed());
    }

    @When("l'utilisateur clique sur le bouton \"Gérer mes abonnements TV\"")
    public void lUtilisateurCliqueSurLeBoutonGererMesAbonnementsTV() {
        // Commentaire : Implémentation du clic sur le bouton "Gérer mes abonnements TV"
        // Action : Appel de la méthode pour cliquer sur le bouton "Gérer mes abonnements TV"
        accountPage.clickOnManageTVSubscriptionsButton();
    }

    @Then("le système affiche la page de gestion des abonnements TV")
    public void leSystemeAfficheLaPageDeGestionDesAbonnementsTV() {
        // Commentaire : Implémentation de la vérification de la page de gestion des abonnements TV
        // Action : Appel de la méthode pour vérifier que la page de gestion des abonnements TV est affichée
        Assert.assertTrue(accountPage.isTVSubscriptionsPageDisplayed());
    }

    @When("l'utilisateur vérifie les informations d'identification")
    public void lUtilisateurVérifieLesInformationsDIdentification() {
        // Commentaire : Implémentation de la vérification des informations d'identification
        // Action : Appel de la méthode pour vérifier les informations d'identification
        accountPage.verifyIdentificationInformation();
    }

    @Then("le système affiche les informations d'identification correctes")
    public void leSystemeAfficheLesInformationsDIdentificationCorrectes() {
        // Commentaire : Implémentation de la vérification des informations d'identification
        // Action : Appel de la méthode pour vérifier les informations d'identification
        Assert.assertTrue(accountPage.isIdentificationInformationCorrect());
    }

    @When("l'utilisateur entre des informations de connexion incorrectes")
    public void lUtilisateurEntreDesInformationsDeConnexionIncorrectes() {
        // Commentaire : Implémentation de la saisie de mauvaises informations de connexion
        // Action : Appel de la méthode pour saisir des informations de connexion incorrectes
        loginPage.enterIncorrectLoginCredentials();
    }

    @Then("le système affiche un message d'erreur de connexion")
    public void leSystemeAfficheUnMessageDErreurDeConnexion() {
        // Commentaire : Implémentation de la vérification du message d'erreur de connexion
        // Action : Appel de la méthode pour vérifier que le message d'erreur de connexion est affiché
        Assert.assertTrue(loginPage.isLoginErrorDisplayed());
    }

    @When("l'utilisateur vérifie les détails de l'offre")
    public void lUtilisateurVérifieLesDétailsDeLOffre() {
        // Commentaire : Implémentation de la vérification des détails de l'offre
        // Action : Appel de la méthode pour vérifier les détails de l'offre
        accountPage.verifyOfferDetails();
    }

    @Then("le système affiche les détails de l'offre, y compris les informations de service et les offres")
    public void leSystemeAfficheLesDétailsDeLOffreYComprisLesInformationsDeServiceEtLesOffres() {
        // Commentaire : Implémentation de la vérification des détails de l'offre
        // Action : Appel de la méthode pour vérifier les détails de l'offre
        Assert.assertTrue(accountPage.isOfferDetailsDisplayed());
    }

    @When("l'utilisateur vérifie les détails de la souscription")
    public void lUtilisateurVérifieLesDétailsDeLaSouscription() {
        // Commentaire : Implémentation de la vérification des détails de la souscription
        // Action : Appel de la méthode pour vérifier les détails de la souscription
        accountPage.verifySubscriptionDetails();
    }

    @Then("le système affiche les détails de la souscription, y compris les informations de service et les offres")
    public void leSystemeAfficheLesDétailsDeLaSouscriptionYComprisLesInformationsDeServiceEtLesOffres() {
        // Commentaire : Implémentation de la vérification des détails de la souscription
        // Action : Appel de la méthode pour vérifier les détails de la souscription
        Assert.assertTrue(accountPage.isSubscriptionDetailsDisplayed());
    }

    @When("l'utilisateur vérifie les détails de l'inclusion")
    public void lUtilisateurVérifieLesDétailsDeLInclusion() {
        // Commentaire : Implémentation de la vérification des détails de l'inclusion
        // Action : Appel de la méthode pour vérifier les détails de l'inclusion
        accountPage.verifyInclusionDetails();
    }

    @Then("le système affiche les détails de l'inclusion, y compris les informations de service et les offres")
    public void leSystemeAfficheLesDétailsDeLInclusionYComprisLesInformationsDeServiceEtLesOffres() {
        // Commentaire : Implémentation de la vérification des détails de l'inclusion
        // Action : Appel de la méthode pour vérifier les détails de l'inclusion
        Assert.assertTrue(accountPage.isInclusionDetailsDisplayed());
    }

    @When("l'utilisateur vérifie les détails des offres")
    public void lUtilisateurVérifieLesDétailsDesOffres() {
        // Commentaire : Implémentation de la vérification des détails des offres
        // Action : Appel de la méthode pour vérifier les détails des offres
        accountPage.verifyOffersDetails();
    }

    @Then("le système affiche les détails des offres, y compris les informations de service et les offres")
    public void leSystemeAfficheLesDétailsDesOffresYComprisLesInformationsDeServiceEtLes