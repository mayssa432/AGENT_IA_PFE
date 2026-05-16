package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.OnboardingPage;
import com.orange.otvp.automation.pages.ConnexionPage;
import com.orange.otvp.automation.pages.DécouvertePage;
import com.orange.otvp.automation.pages.TéléchargementsPage;

public class OnboardingSteps {

    private OnboardingPage onboardingPage;
    private ConnexionPage connexionPage;
    private DécouvertePage découvertePage;
    private TéléchargementsPage téléchargementsPage;

    @Given("L'utilisateur lance l'application")
    public void lUtilisateurLanceLApplication() {
        // Commentaire : Lance l'application
        // Action : Appel de la méthode pour lancer l'application
        onboardingPage = new OnboardingPage();
        onboardingPage.lancerApplication();
    }

    @When("L'utilisateur est sur l'écran d'onboarding")
    public void lUtilisateurEstSurLÉcranDOnboarding() {
        // Commentaire : Vérifie que l'utilisateur est sur l'écran d'onboarding
        // Action : Vérifie que l'utilisateur est sur l'écran d'onboarding
        Assert.assertTrue(onboardingPage.estSurLÉcranDOnboarding());
    }

    @Then("L'utilisateur voit le texte {string}")
    public void lUtilisateurVoitLeTexte(String texte) {
        // Commentaire : Vérifie que l'utilisateur voit le texte
        // Action : Vérifie que l'utilisateur voit le texte
        Assert.assertTrue(onboardingPage.voirTexte(texte));
    }

    @When("L'utilisateur clique sur le bouton {string}")
    public void lUtilisateurCliqueSurLeBouton(String bouton) {
        // Commentaire : Clique sur le bouton
        // Action : Clique sur le bouton
        onboardingPage.cliqueSurBouton(bouton);
    }

    @Then("L'utilisateur est redirigé vers l'écran de connexion")
    public void lUtilisateurEstRedirigéVersLÉcranDeConnexion() {
        // Commentaire : Vérifie que l'utilisateur est redirigé vers l'écran de connexion
        // Action : Vérifie que l'utilisateur est redirigé vers l'écran de connexion
        connexionPage = new ConnexionPage();
        Assert.assertTrue(connexionPage.estSurLÉcranDeConnexion());
    }

    @Then("L'utilisateur est redirigé vers l'écran de découverte")
    public void lUtilisateurEstRedirigéVersLÉcranDeDécouverte() {
        // Commentaire : Vérifie que l'utilisateur est redirigé vers l'écran de découverte
        // Action : Vérifie que l'utilisateur est redirigé vers l'écran de découverte
        découvertePage = new DécouvertePage();
        Assert.assertTrue(découvertePage.estSurLÉcranDeDécouverte());
    }

    @Then("L'utilisateur voit les options de découverte de télévision")
    public void lUtilisateurVoitLesOptionsDeDécouverteDeTélévision() {
        // Commentaire : Vérifie que l'utilisateur voit les options de découverte de télévision
        // Action : Vérifie que l'utilisateur voit les options de découverte de télévision
        Assert.assertTrue(découvertePage.voirOptionsDeDécouverteDeTélévision());
    }

    @Then("L'utilisateur voit le titre de l'option de télévision")
    public void lUtilisateurVoitLeTitreDeLOptionDeTélévision() {
        // Commentaire : Vérifie que l'utilisateur voit le titre de l'option de télévision
        // Action : Vérifie que l'utilisateur voit le titre de l'option de télévision
        Assert.assertTrue(découvertePage.voirTitreDeLOptionDeTélévision());
    }

    @Then("L'utilisateur voit le texte de l'option de télévision")
    public void lUtilisateurVoitLeTexteDeLOptionDeTélévision() {
        // Commentaire : Vérifie que l'utilisateur voit le texte de l'option de télévision
        // Action : Vérifie que l'utilisateur voit le texte de l'option de télévision
        Assert.assertTrue(découvertePage.voirTexteDeLOptionDeTélévision());
    }

    @Then("L'utilisateur voit le fournisseur de l'option de télévision")
    public void lUtilisateurVoitLeFournisseurDeLOptionDeTélévision() {
        // Commentaire : Vérifie que l'utilisateur voit le fournisseur de l'option de télévision
        // Action : Vérifie que l'utilisateur voit le fournisseur de l'option de télévision
        Assert.assertTrue(découvertePage.voirFournisseurDeLOptionDeTélévision());
    }

    @Then("L'utilisateur voit le bouton d'abonnement à l'option de télévision")
    public void lUtilisateurVoitLeBoutonDAbonnementÀLOptionDeTélévision() {
        // Commentaire : Vérifie que l'utilisateur voit le bouton d'abonnement à l'option de télévision
        // Action : Vérifie que l'utilisateur voit le bouton d'abonnement à l'option de télévision
        Assert.assertTrue(découvertePage.voirBoutonDAbonnementÀLOptionDeTélévision());
    }

    @Then("L'utilisateur est redirigé vers l'écran de connexion pour s'identifier")
    public void lUtilisateurEstRedirigéVersLÉcranDeConnexionPourSIdentifier() {
        // Commentaire : Vérifie que l'utilisateur est redirigé vers l'écran de connexion pour s'identifier
        // Action : Vérifie que l'utilisateur est redirigé vers l'écran de connexion pour s'identifier
        connexionPage = new ConnexionPage();
        Assert.assertTrue(connexionPage.estSurLÉcranDeConnexionPourSIdentifier());
    }

    @Then("L'utilisateur n'est plus sur l'écran d'onboarding")
    public void lUtilisateurNEstPlusSurLÉcranDOnboarding() {
        // Commentaire : Vérifie que l'utilisateur n'est plus sur l'écran d'onboarding
        // Action : Vérifie que l'utilisateur n'est plus sur l'écran d'onboarding
        Assert.assertFalse(onboardingPage.estSurLÉcranDOnboarding());
    }

    @Then("L'utilisateur est redirigé vers la page de téléchargements")
    public void lUtilisateurEstRedirigéVersLaPageDeTéléchargements() {
        // Commentaire : Vérifie que l'utilisateur est redirigé vers la page de téléchargements
        // Action : Vérifie que l'utilisateur est redirigé vers la page de téléchargements
        téléchargementsPage = new TéléchargementsPage();
        Assert.assertTrue(téléchargementsPage.estSurLaPageDeTéléchargements());
    }

    @Then("L'utilisateur est redirigé vers l'écran de connexion pour réessayer la connexion")
    public void lUtilisateurEstRedirigéVersLÉcranDeConnexionPourRéessayerLaConnexion() {
        // Commentaire : Vérifie que l'utilisateur est redirigé vers l'écran de connexion pour réessayer la connexion
        // Action : Vérifie que l'utilisateur est redirigé vers l'écran de connexion pour réessayer la connexion
        connexionPage = new ConnexionPage();
        Assert.assertTrue(connexionPage.estSurLÉcranDeConnexionPourRéessayerLaConnexion());
    }

    @Then("L'utilisateur est redirigé vers l'écran de connexion pour s'identifier")
    public void lUtilisateurEstRedirigéVersLÉcranDeConnexionPourSIdentifier() {
        // Commentaire : Vérifie que l'utilisateur est redirigé vers l'écran de connexion pour s'identifier
        // Action : Vérifie que l'utilisateur est redirigé vers l'écran de connexion pour s'identifier
        connexionPage = new ConnexionPage();
        Assert.assertTrue(connexionPage.estSurLÉcranDeConnexionPourSIdentifier());
    }

    @Then("L'utilisateur peut saisir une nouvelle adresse")
    public void lUtilisateurPeutSaisirUneNouvelleAdresse() {
        // Commentaire : Vérifie que l'utilisateur peut saisir une nouvelle adresse
        // Action : Vérifie que l'utilisateur peut saisir une nouvelle adresse
        Assert.assertTrue(onboardingPage.peutSaisirUneNouvelleAdresse());
    }
}