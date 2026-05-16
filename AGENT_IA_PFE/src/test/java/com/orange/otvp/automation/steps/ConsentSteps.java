package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.ConsentPage;
import com.orange.otvp.automation.pages.PersonnalisationPage;
import com.orange.otvp.automation.pages.PolitiqueConsentementPage;

public class ConsentSteps {

    private ConsentPage consentPage;
    private PersonnalisationPage personnalisationPage;
    private PolitiqueConsentementPage politiqueConsentementPage;

    @Given("L'utilisateur est sur la page de consentement")
    public void lUtilisateurEstSurLaPageDeConsentement() {
        // Commentaire : L'utilisateur est redirigé vers la page de consentement
        // Action : Appel de la méthode pour accéder à la page de consentement
        consentPage = new ConsentPage();
        consentPage.accederALaPageDeConsentement();
    }

    @When("La page de consentement est affichée")
    public void laPageDeConsentementEstAffichée() {
        // Commentaire : La page de consentement est affichée
        // Action : Vérification de l'affichage de la page de consentement
        Assert.assertTrue(consentPage.estLaPageDeConsentementAffichée());
    }

    @Then("Le texte de description du consentement est affiché")
    public void leTexteDeDescriptionDuConsentementEstAffiche() {
        // Commentaire : Le texte de description du consentement est affiché
        // Action : Vérification de l'affichage du texte de description du consentement
        Assert.assertTrue(consentPage.estLeTexteDeDescriptionDuConsentementAffiche());
    }

    @And("Le lien de politique de consentement est affiché")
    public void leLienDePolitiqueDeConsentementEstAffiche() {
        // Commentaire : Le lien de politique de consentement est affiché
        // Action : Vérification de l'affichage du lien de politique de consentement
        Assert.assertTrue(consentPage.estLeLienDePolitiqueDeConsentementAffiche());
    }

    @And("Le bouton d'acceptation est affiché")
    public void leBoutonDAcceptationEstAffiche() {
        // Commentaire : Le bouton d'acceptation est affiché
        // Action : Vérification de l'affichage du bouton d'acceptation
        Assert.assertTrue(consentPage.estLeBoutonDAcceptationAffiche());
    }

    @And("Le bouton de refus est affiché")
    public void leBoutonDeRefusEstAffiche() {
        // Commentaire : Le bouton de refus est affiché
        // Action : Vérification de l'affichage du bouton de refus
        Assert.assertTrue(consentPage.estLeBoutonDeRefusAffiche());
    }

    @And("Le bouton de personnalisation est affiché")
    public void leBoutonDePersonnalisationEstAffiche() {
        // Commentaire : Le bouton de personnalisation est affiché
        // Action : Vérification de l'affichage du bouton de personnalisation
        Assert.assertTrue(consentPage.estLeBoutonDePersonnalisationAffiche());
    }

    @When("L'utilisateur clique sur le bouton d'acceptation")
    public void lUtilisateurCliqueSurLeBoutonDAcceptation() {
        // Commentaire : L'utilisateur clique sur le bouton d'acceptation
        // Action : Appel de la méthode pour cliquer sur le bouton d'acceptation
        consentPage.cliquerSurLeBoutonDAcceptation();
    }

    @Then("La page de consentement est fermée")
    public void laPageDeConsentementEstFermee() {
        // Commentaire : La page de consentement est fermée
        // Action : Vérification de la fermeture de la page de consentement
        Assert.assertTrue(consentPage.estLaPageDeConsentementFermee());
    }

    @And("L'utilisateur est redirigé vers la page suivante")
    public void lUtilisateurEstRedirigeVersLaPageSuivante() {
        // Commentaire : L'utilisateur est redirigé vers la page suivante
        // Action : Vérification de la redirection vers la page suivante
        Assert.assertTrue(consentPage.estLUtilisateurRedirigeVersLaPageSuivante());
    }

    @When("L'utilisateur clique sur le bouton de personnalisation")
    public void lUtilisateurCliqueSurLeBoutonDePersonnalisation() {
        // Commentaire : L'utilisateur clique sur le bouton de personnalisation
        // Action : Appel de la méthode pour cliquer sur le bouton de personnalisation
        personnalisationPage = new PersonnalisationPage();
        personnalisationPage.accederALaPageDePersonnalisation();
    }

    @Then("La page de personnalisation des consentements est affichée")
    public void laPageDePersonnalisationDesConsentementsEstAffiche() {
        // Commentaire : La page de personnalisation des consentements est affichée
        // Action : Vérification de l'affichage de la page de personnalisation des consentements
        Assert.assertTrue(personnalisationPage.estLaPageDePersonnalisationDesConsentementsAffiche());
    }

    @And("Les options de personnalisation sont affichées")
    public void lesOptionsDePersonnalisationSontAffichees() {
        // Commentaire : Les options de personnalisation sont affichées
        // Action : Vérification de l'affichage des options de personnalisation
        Assert.assertTrue(personnalisationPage.estLesOptionsDePersonnalisationAffichees());
    }

    @And("L'utilisateur peut sélectionner les options de personnalisation")
    public void lUtilisateurPeutSélectionnerLesOptionsDePersonnalisation() {
        // Commentaire : L'utilisateur peut sélectionner les options de personnalisation
        // Action : Vérification de la possibilité de sélectionner les options de personnalisation
        Assert.assertTrue(personnalisationPage.estLUtilisateurPeutSélectionnerLesOptionsDePersonnalisation());
    }

    @When("L'utilisateur clique sur le lien de politique de consentement")
    public void lUtilisateurCliqueSurLeLienDePolitiqueDeConsentement() {
        // Commentaire : L'utilisateur clique sur le lien de politique de consentement
        // Action : Appel de la méthode pour cliquer sur le lien de politique de consentement
        politiqueConsentementPage = new PolitiqueConsentementPage();
        politiqueConsentementPage.accederALaPageDePolitiqueDeConsentement();
    }

    @Then("La page de politique de consentement est affichée")
    public void laPageDePolitiqueDeConsentementEstAffiche() {
        // Commentaire : La page de politique de consentement est affichée
        // Action : Vérification de l'affichage de la page de politique de consentement
        Assert.assertTrue(politiqueConsentementPage.estLaPageDePolitiqueDeConsentementAffiche());
    }

    @And("Les informations de politique de consentement sont affichées")
    public void lesInformationsDePolitiqueDeConsentementSontAffichees() {
        // Commentaire : Les informations de politique de consentement sont affichées
        // Action : Vérification de l'affichage des informations de politique de consentement
        Assert.assertTrue(politiqueConsentementPage.estLesInformationsDePolitiqueDeConsentementAffichees());
    }

    @Given("L'utilisateur est sur la page de personnalisation des consentements")
    public void lUtilisateurEstSurLaPageDePersonnalisationDesConsentements() {
        // Commentaire : L'utilisateur est sur la page de personnalisation des consentements
        // Action : Appel de la méthode pour accéder à la page de personnalisation des consentements
        personnalisationPage = new PersonnalisationPage();
        personnalisationPage.accederALaPageDePersonnalisation();
    }

    @When("L'utilisateur sélectionne les options de personnalisation")
    public void lUtilisateurSélectionneLesOptionsDePersonnalisation() {
        // Commentaire : L'utilisateur sélectionne les options de personnalisation
        // Action : Appel de la méthode pour sélectionner les options de personnalisation
        personnalisationPage.sélectionnerLesOptionsDePersonnalisation();
    }

    @And("L'utilisateur clique sur le bouton de sauvegarde")
    public void lUtilisateurCliqueSurLeBoutonDeSauvegarde() {
        // Commentaire : L'utilisateur clique sur le bouton de sauvegarde
        // Action : Appel de la méthode pour cliquer sur le bouton de sauvegarde
        personnalisationPage.cliquerSurLeBoutonDeSauvegarde();
    }

    @Then("Les options de personnalisation sont enregistrées")
    public void lesOptionsDePersonnalisationSontEnregistrees() {
        // Commentaire : Les options de personnalisation sont enregistrées
        // Action : Vérification de l'enregistrement des options de personnalisation
        Assert.assertTrue(personnalisationPage.estLesOptionsDePersonnalisationEnregistrees());
    }
}
