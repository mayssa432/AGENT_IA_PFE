package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.AuthenticationPage;
import com.orange.otvp.automation.pages.ForgotPasswordPage;
import com.orange.otvp.automation.pages.OthersAccountPage;
import com.orange.otvp.automation.pages.TVRightsManagementPage;

public class AuthenticationSteps {

    private AuthenticationPage authenticationPage;
    private ForgotPasswordPage forgotPasswordPage;
    private OthersAccountPage othersAccountPage;
    private TVRightsManagementPage tvRightsManagementPage;

    @Given("que je suis sur la page d'authentification")
    public void queJeSuisSurLaPageDAuthentification() {
        // Commentaire : Initialisation de la page d'authentification
        // Action : Récupération de l'instance de la page d'authentification
        authenticationPage = new AuthenticationPage();
    }

    @When("je saisis un nom d'utilisateur valide")
    public void jeSaisisUnNomDUtilisateurValide() {
        // Commentaire : Saisie d'un nom d'utilisateur valide
        // Action : Entrée du nom d'utilisateur valide dans le champ de saisie
        authenticationPage.enterValidUsername();
    }

    @When("je saisis un nom d'utilisateur invalide")
    public void jeSaisisUnNomDUtilisateurInvalide() {
        // Commentaire : Saisie d'un nom d'utilisateur invalide
        // Action : Entrée du nom d'utilisateur invalide dans le champ de saisie
        authenticationPage.enterInvalidUsername();
    }

    @When("je saisis un mot de passe valide")
    public void jeSaisisUnMotDePasseValide() {
        // Commentaire : Saisie d'un mot de passe valide
        // Action : Entrée du mot de passe valide dans le champ de saisie
        authenticationPage.enterValidPassword();
    }

    @When("je saisis un mot de passe invalide")
    public void jeSaisisUnMotDePasseInvalide() {
        // Commentaire : Saisie d'un mot de passe invalide
        // Action : Entrée du mot de passe invalide dans le champ de saisie
        authenticationPage.enterInvalidPassword();
    }

    @When("je clique sur le bouton \"Se connecter\"")
    public void jeCliqueSurLeBoutonSeConnecter() {
        // Commentaire : Clique sur le bouton "Se connecter"
        // Action : Clique sur le bouton "Se connecter"
        authenticationPage.clickOnLoginButton();
    }

    @Then("je devrais être connecté avec succès")
    public void jeDevraisEtreConnecteAvecSucces() {
        // Commentaire : Vérification de la connexion réussie
        // Action : Vérification de la connexion réussie
        Assert.assertTrue(authenticationPage.isConnected());
    }

    @Then("je devrais voir un message d'erreur \"Nom d'utilisateur invalide\"")
    public void jeDevraisVoirUnMessageDErreurNomDUtilisateurInvalide() {
        // Commentaire : Vérification du message d'erreur "Nom d'utilisateur invalide"
        // Action : Vérification du message d'erreur "Nom d'utilisateur invalide"
        Assert.assertTrue(authenticationPage.isInvalidUsernameErrorDisplayed());
    }

    @Then("je devrais voir un message d'erreur \"Mot de passe invalide\"")
    public void jeDevraisVoirUnMessageDErreurMotDePasseInvalide() {
        // Commentaire : Vérification du message d'erreur "Mot de passe invalide"
        // Action : Vérification du message d'erreur "Mot de passe invalide"
        Assert.assertTrue(authenticationPage.isInvalidPasswordErrorDisplayed());
    }

    @When("je clique sur le bouton \"Mot de passe oublié\"")
    public void jeCliqueSurLeBoutonMotDePasseOublie() {
        // Commentaire : Clique sur le bouton "Mot de passe oublié"
        // Action : Clique sur le bouton "Mot de passe oublié"
        forgotPasswordPage = new ForgotPasswordPage();
        forgotPasswordPage.clickOnForgotPasswordButton();
    }

    @When("je saisis mon adresse e-mail")
    public void jeSaisisMonAdresseEmail() {
        // Commentaire : Saisie de l'adresse e-mail
        // Action : Entrée de l'adresse e-mail dans le champ de saisie
        forgotPasswordPage.enterEmail();
    }

    @When("je clique sur le bouton \"Réinitialiser le mot de passe\"")
    public void jeCliqueSurLeBoutonReinitialiserLeMotDePasse() {
        // Commentaire : Clique sur le bouton "Réinitialiser le mot de passe"
        // Action : Clique sur le bouton "Réinitialiser le mot de passe"
        forgotPasswordPage.clickOnResetPasswordButton();
    }

    @Then("je devrais recevoir un e-mail de réinitialisation de mot de passe")
    public void jeDevraisRecevoirUnEmailDeReinitialisationDeMotDePasse() {
        // Commentaire : Vérification de l'e-mail de réinitialisation de mot de passe
        // Action : Vérification de l'e-mail de réinitialisation de mot de passe
        Assert.assertTrue(forgotPasswordPage.isResetPasswordEmailSent());
    }

    @When("je clique sur le bouton \"Compte autre\"")
    public void jeCliqueSurLeBoutonCompteAutre() {
        // Commentaire : Clique sur le bouton "Compte autre"
        // Action : Clique sur le bouton "Compte autre"
        othersAccountPage = new OthersAccountPage();
        othersAccountPage.clickOnOthersAccountButton();
    }

    @When("je saisis mon nom d'utilisateur et mon mot de passe")
    public void jeSaisisMonNomDUtilisateurEtMonMotDePasse() {
        // Commentaire : Saisie du nom d'utilisateur et du mot de passe
        // Action : Entrée du nom d'utilisateur et du mot de passe dans les champs de saisie
        othersAccountPage.enterUsernameAndPassword();
    }

    @Then("je devrais être connecté avec succès")
    public void jeDevraisEtreConnecteAvecSucces2() {
        // Commentaire : Vérification de la connexion réussie
        // Action : Vérification de la connexion réussie
        Assert.assertTrue(othersAccountPage.isConnected());
    }

    @When("je clique sur le bouton \"Gérer les droits TV\"")
    public void jeCliqueSurLeBoutonGererLesDroitsTV() {
        // Commentaire : Clique sur le bouton "Gérer les droits TV"
        // Action : Clique sur le bouton "Gérer les droits TV"
        tvRightsManagementPage = new TVRightsManagementPage();
        tvRightsManagementPage.clickOnTVRightsManagementButton();
    }

    @When("je sélectionne mon fournisseur de services TV")
    public void jeSlectionneMonFournisseurDeServicesTV() {
        // Commentaire : Sélection du fournisseur de services TV
        // Action : Sélection du fournisseur de services TV
        tvRightsManagementPage.selectTVServiceProvider();
    }

    @Then("je devrais être en mesure de gérer mes droits TV")
    public void jeDevraisEtreEnMesureDeGérerMesDroitsTV() {
        // Commentaire : Vérification de la gestion des droits TV
        // Action : Vérification de la gestion des droits TV
        Assert.assertTrue(tvRightsManagementPage.isTVRightsManagementEnabled());
    }

    @When("je sélectionne un fournisseur de services TV non autorisé")
    public void jeSlectionneUnFournisseurDeServicesTVNonAutorise() {
        // Commentaire : Sélection d'un fournisseur de services TV non autorisé
        // Action : Sélection d'un fournisseur de services TV non autorisé
        tvRightsManagementPage.selectUnauthorizedTVServiceProvider();
    }

    @Then("je devrais voir un message d'erreur \"Droits TV non autorisés\"")
    public void jeDevraisVoirUnMessageDErreurDroitsTVNonAutorises() {
        // Commentaire : Vérification du message d'erreur "Droits TV non autorisés"
        // Action : Vérification du message d'erreur "Droits TV non autorisés"
        Assert.assertTrue(tvRightsManagementPage.isUnauthorizedTVErrorDisplayed());
    }
}