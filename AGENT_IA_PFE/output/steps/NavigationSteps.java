package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.NavigationPage;
import com.orange.otvp.automation.pages.ReplayPage;
import com.orange.otvp.automation.pages.TVEnDirectPage;
import com.orange.otvp.automation.pages.VODPage;
import com.orange.otvp.automation.pages.BoutiqueTVPage;
import com.orange.otvp.automation.pages.RecherchePage;
import com.orange.otvp.automation.pages.MonComptePage;
import com.orange.otvp.automation.pages.PartageDeMaTVPage;
import com.orange.otvp.automation.pages.MesReglagesPage;
import com.orange.otvp.automation.pages.MesAchatsPage;
import com.orange.otvp.automation.pages.PassVideoPage;
import com.orange.otvp.automation.pages.MesEnregistrementsPage;
import com.orange.otvp.automation.pages.NotationDeLApplicationPage;
import com.orange.otvp.automation.pages.ProgrammationPage;
import com.orange.otvp.automation.pages.BadgeDeConfiancePage;
import com.orange.otvp.automation.pages.AideEtContactPage;
import com.orange.otvp.automation.pages.AProposPage;
import com.orange.otvp.automation.pages.DecouverteDeLApplicationPage;

public class NavigationSteps {

    private NavigationPage navigationPage;

    @Given("que je suis sur la page de navigation")
    public void queJeSuisSurLaPageDeNavigation() {
        navigationPage = new NavigationPage();
        navigationPage.navigateToNavigationPage();
    }

    @When("je clique sur le bouton \"Accueil\"")
    public void jeCliqueSurLeBoutonAccueil() {
        navigationPage.clickOnAccueilButton();
    }

    @Then("je devrais être redirigé vers la page d'accueil")
    public void jeDevraisEtreRedirigeVersLaPageDAccueil() {
        Assert.assertTrue(navigationPage.isAccueilPage());
    }

    @When("je clique sur le bouton \"Espace Replay\"")
    public void jeCliqueSurLeBoutonEspaceReplay() {
        navigationPage.clickOnEspaceReplayButton();
    }

    @Then("je devrais être redirigé vers la page de replay")
    public void jeDevraisEtreRedirigeVersLaPageDeReplay() {
        Assert.assertTrue(navigationPage.isReplayPage());
    }

    @When("je clique sur le bouton \"TV en direct\"")
    public void jeCliqueSurLeBoutonTVEnDirect() {
        navigationPage.clickOnTVEnDirectButton();
    }

    @Then("je devrais être redirigé vers la page de TV en direct")
    public void jeDevraisEtreRedirigeVersLaPageDeTVEnDirect() {
        Assert.assertTrue(navigationPage.isTVEnDirectPage());
    }

    @When("je clique sur le bouton \"VOD\"")
    public void jeCliqueSurLeBoutonVOD() {
        navigationPage.clickOnVODButton();
    }

    @Then("je devrais être redirigé vers la page de VOD")
    public void jeDevraisEtreRedirigeVersLaPageDeVOD() {
        Assert.assertTrue(navigationPage.isVODPage());
    }

    @When("je clique sur le bouton \"Boutique TV\"")
    public void jeCliqueSurLeBoutonBoutiqueTV() {
        navigationPage.clickOnBoutiqueTVButton();
    }

    @Then("je devrais être redirigé vers la page de boutique TV")
    public void jeDevraisEtreRedirigeVersLaPageDeBoutiqueTV() {
        Assert.assertTrue(navigationPage.isBoutiqueTVPage());
    }

    @When("je clique sur le bouton de recherche")
    public void jeCliqueSurLeBoutonDeRecherche() {
        navigationPage.clickOnRechercheButton();
    }

    @Then("je devrais être redirigé vers la page de recherche")
    public void jeDevraisEtreRedirigeVersLaPageDeRecherche() {
        Assert.assertTrue(navigationPage.isRecherchePage());
    }

    @When("je clique sur le bouton \"Mon compte\"")
    public void jeCliqueSurLeBoutonMonCompte() {
        navigationPage.clickOnMonCompteButton();
    }

    @Then("je devrais être redirigé vers la page de mon compte")
    public void jeDevraisEtreRedirigeVersLaPageDeMonCompte() {
        Assert.assertTrue(navigationPage.isMonComptePage());
    }

    @When("je clique sur le bouton \"Partage de ma TV d'Orange\"")
    public void jeCliqueSurLeBoutonPartageDeMaTV() {
        navigationPage.clickOnPartageDeMaTVButton();
    }

    @Then("je devrais être redirigé vers la page de partage de ma TV d'Orange")
    public void jeDevraisEtreRedirigeVersLaPageDePartageDeMaTV() {
        Assert.assertTrue(navigationPage.isPartageDeMaTVPage());
    }

    @When("je clique sur le bouton \"Mes réglages\"")
    public void jeCliqueSurLeBoutonMesReglages() {
        navigationPage.clickOnMesReglagesButton();
    }

    @Then("je devrais être redirigé vers la page de mes réglages")
    public void jeDevraisEtreRedirigeVersLaPageDeMesReglages() {
        Assert.assertTrue(navigationPage.isMesReglagesPage());
    }

    @When("je clique sur le bouton \"Mes achats\"")
    public void jeCliqueSurLeBoutonMesAchats() {
        navigationPage.clickOnMesAchatsButton();
    }

    @Then("je devrais être redirigé vers la page de mes achats")
    public void jeDevraisEtreRedirigeVersLaPageDeMesAchats() {
        Assert.assertTrue(navigationPage.isMesAchatsPage());
    }

    @When("je clique sur le bouton \"Pass vidéo\"")
    public void jeCliqueSurLeBoutonPassVideo() {
        navigationPage.clickOnPassVideoButton();
    }

    @Then("je devrais être redirigé vers la page de pass vidéo")
    public void jeDevraisEtreRedirigeVersLaPageDePassVideo() {
        Assert.assertTrue(navigationPage.isPassVideoPage());
    }

    @When("je clique sur le bouton \"Mes enregistrements\"")
    public void jeCliqueSurLeBoutonMesEnregistrements() {
        navigationPage.clickOnMesEnregistrementsButton();
    }

    @Then("je devrais être redirigé vers la page de mes enregistrements")
    public void jeDevraisEtreRedirigeVersLaPageDeMesEnregistrements() {
        Assert.assertTrue(navigationPage.isMesEnregistrementsPage());
    }

    @When("je clique sur le bouton \"Noter l'application\"")
    public void jeCliqueSurLeBoutonNoterLApplication() {
        navigationPage.clickOnNoterLApplicationButton();
    }

    @Then("je devrais être redirigé vers la page de notation de l'application")
    public void jeDevraisEtreRedirigeVersLaPageDeNotationDeLApplication() {
        Assert.assertTrue(navigationPage.isNotationDeLApplicationPage());
    }

    @When("je clique sur le bouton \"Programmation\"")
    public void jeCliqueSurLeBoutonProgrammation() {
        navigationPage.clickOnProgrammationButton();
    }

    @Then("je devrais être redirigé vers la page de programmation")
    public void jeDevraisEtreRedirigeVersLaPageDeProgrammation() {
        Assert.assertTrue(navigationPage.isProgrammationPage());
    }

    @When("je clique sur le bouton \"Badge de confiance\"")
    public void jeCliqueSurLeBoutonBadgeDeConfiance() {
        navigationPage.clickOnBadgeDeConfianceButton();
    }

    @Then("je devrais être redirigé vers la page de badge de confiance")
    public void jeDevraisEtreRedirigeVersLaPageDeBadgeDeConfiance() {
        Assert.assertTrue(navigationPage.isBadgeDeConfiancePage());
    }

    @When("je clique sur le bouton \"Aide & contact\"")
    public void jeCliqueSurLeBoutonAideEtContact() {
        navigationPage.clickOnAideEtContactButton();
    }

    @Then("je devrais être redirigé vers la page d'aide et de contact")
    public void jeDevraisEtreRedirigeVersLaPageDAideEtContact() {
        Assert.assertTrue(navigationPage.isAideEtContactPage());
    }

    @When("je clique sur le bouton \"A propos\"")
    public void jeCliqueSurLeBoutonAPropos() {
        navigationPage.clickOnAProposButton();
    }

    @Then("je devrais être redirigé vers la page d'a propos")
    public void jeDevraisEtreRedirigeVersLaPageDAPropos() {
        Assert.assertTrue(navigationPage.isAProposPage());
    }

    @When("je clique sur le bouton \"Découverte de l'application\"")