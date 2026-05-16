package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.AboutPage;
import com.orange.otvp.automation.pages.AccessibilitePage;
import com.orange.otvp.automation.pages.MentionsLegalesPage;

public class AboutSteps {

    private AboutPage aboutPage;
    private AccessibilitePage accessibilitePage;
    private MentionsLegalesPage mentionsLegalesPage;

    @Given("L'utilisateur est sur la page About")
    public void lUtilisateurEstSurLaPageAbout() {
        // Commentaire : Initialisation de la page About
        // Action : Appel de la méthode pour accéder à la page About
        aboutPage = new AboutPage();
        aboutPage.navigateTo();
    }

    @When("L'utilisateur affiche les informations de base")
    public void lUtilisateurAfficheLesInformationsDeBase() {
        // Commentaire : Affichage des informations de base
        // Action : Appel de la méthode pour afficher les informations de base
        aboutPage.displayBasicInfo();
    }

    @Then("Les éléments suivants sont affichés :")
    public void lesElementsSuivantsSontAffiches() {
        // Commentaire : Vérification de la présence des éléments affichés
        // Action : Appel de la méthode pour vérifier la présence des éléments
        Assert.assertTrue(aboutPage.isLogoOrangeVisible());
        Assert.assertTrue(aboutPage.isNomApplicationVisible("Orange TV"));
        Assert.assertTrue(aboutPage.isNumeroVersionVisible());
        Assert.assertTrue(aboutPage.isTexteAboutVisible());
    }

    @When("L'utilisateur clique sur l'élément \"Déclarations d'accessibilité\"")
    public void lUtilisateurCliqueSurLElémentDéclarationsDAccèsibilité() {
        // Commentaire : Clique sur l'élément "Déclarations d'accessibilité"
        // Action : Appel de la méthode pour accéder à la page d'accessibilité
        accessibilitePage = new AccessibilitePage();
        accessibilitePage.navigateTo();
    }

    @Then("Les éléments suivants sont affichés :")
    public void lesElementsSuivantsSontAffiches1() {
        // Commentaire : Vérification de la présence des éléments affichés
        // Action : Appel de la méthode pour vérifier la présence des éléments
        Assert.assertTrue(accessibilitePage.isTitreAccessibiliteVisible());
        Assert.assertTrue(accessibilitePage.isBarreDeProgressionVisible());
        Assert.assertTrue(accessibilitePage.isDetailDuRésultatVisible());
        Assert.assertTrue(accessibilitePage.isDateVisible());
        Assert.assertTrue(accessibilitePage.isDeclarantVisible());
        Assert.assertTrue(accessibilitePage.isReferentielVisible());
        Assert.assertTrue(accessibilitePage.isTechnologieVisible());
        Assert.assertTrue(accessibilitePage.isBoutonVoirPlusVisible());
    }

    @When("L'utilisateur clique sur l'élément \"Mentions légales\"")
    public void lUtilisateurCliqueSurLElémentMentionsLégales() {
        // Commentaire : Clique sur l'élément "Mentions légales"
        // Action : Appel de la méthode pour accéder à la page de mentions légales
        mentionsLegalesPage = new MentionsLegalesPage();
        mentionsLegalesPage.navigateTo();
    }

    @Then("Les éléments suivants sont affichés :")
    public void lesElementsSuivantsSontAffiches2() {
        // Commentaire : Vérification de la présence des éléments affichés
        // Action : Appel de la méthode pour vérifier la présence des éléments
        Assert.assertTrue(mentionsLegalesPage.isLogoOrangeVisible());
        Assert.assertTrue(mentionsLegalesPage.isNomApplicationVisible("Orange TV"));
        Assert.assertTrue(mentionsLegalesPage.isNumeroVersionVisible());
        Assert.assertTrue(mentionsLegalesPage.isTexteAboutVisible());
    }

    @When("L'utilisateur affiche les éléments de la page")
    public void lUtilisateurAfficheLesElementsDeLaPage() {
        // Commentaire : Affichage des éléments de la page
        // Action : Appel de la méthode pour afficher les éléments de la page
        aboutPage.displayPageElements();
    }

    @Then("Les éléments suivants sont présents :")
    public void lesElementsSuivantsSontPrésents() {
        // Commentaire : Vérification de la présence des éléments
        // Action : Appel de la méthode pour vérifier la présence des éléments
        Assert.assertTrue(aboutPage.isLogoOrangePresent());
        Assert.assertTrue(aboutPage.isNomApplicationPresent("Orange TV"));
        Assert.assertTrue(aboutPage.isNumeroVersionPresent());
        Assert.assertTrue(aboutPage.isTexteAboutPresent());
    }

    @Then("La liste des éléments est non vide")
    public void laListeDesElementsEstNonVide() {
        // Commentaire : Vérification de la présence de la liste des éléments
        // Action : Appel de la méthode pour vérifier la présence de la liste des éléments
        Assert.assertTrue(aboutPage.isListeElementsNotEmpty());
    }

    @When("L'utilisateur clique sur l'élément \"1\"")
    public void lUtilisateurCliqueSurLElément1() {
        // Commentaire : Clique sur l'élément "1"
        // Action : Appel de la méthode pour cliquer sur l'élément "1"
        aboutPage.clickElement("1");
    }

    @Then("L'élément \"1\" est sélectionné")
    public void lElement1EstSélectionné() {
        // Commentaire : Vérification de la sélection de l'élément "1"
        // Action : Appel de la méthode pour vérifier la sélection de l'élément "1"
        Assert.assertTrue(aboutPage.isElementSelected("1"));
    }

    @When("L'utilisateur clique sur l'élément \"2\"")
    public void lUtilisateurCliqueSurLElément2() {
        // Commentaire : Clique sur l'élément "2"
        // Action : Appel de la méthode pour cliquer sur l'élément "2"
        aboutPage.clickElement("2");
    }

    @Then("L'élément \"2\" est sélectionné")
    public void lElement2EstSélectionné() {
        // Commentaire : Vérification de la sélection de l'élément "2"
        // Action : Appel de la méthode pour vérifier la sélection de l'élément "2"
        Assert.assertTrue(aboutPage.isElementSelected("2"));
    }

    @When("L'utilisateur clique sur l'élément \"3\"")
    public void lUtilisateurCliqueSurLElément3() {
        // Commentaire : Clique sur l'élément "3"
        // Action : Appel de la méthode pour cliquer sur l'élément "3"
        aboutPage.clickElement("3");
    }

    @Then("L'élément \"3\" est sélectionné")
    public void lElement3EstSélectionné() {
        // Commentaire : Vérification de la sélection de l'élément "3"
        // Action : Appel de la méthode pour vérifier la sélection de l'élément "3"
        Assert.assertTrue(aboutPage.isElementSelected("3"));
    }
}