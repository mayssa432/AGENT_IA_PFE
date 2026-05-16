package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.RemoteControlPage;
import com.orange.otvp.automation.pages.HomePage;

public class RemoteControlSteps {

    private RemoteControlPage remoteControlPage;
    private HomePage homePage;

    @Given("que je suis sur la page d'accueil")
    public void queJeSuisSurLaPageDAccueil() {
        // TODO : Implémenter la navigation vers la page d'accueil
        // homePage = new HomePage();
        // homePage.navigateTo();
    }

    @When("je clique sur le bouton de télécommande")
    public void jeCliqueSurLeBoutonDeTélécommande() {
        // TODO : Implémenter la sélection du bouton de télécommande
        // remoteControlPage = new RemoteControlPage();
        // remoteControlPage.clickOnRemoteControlButton();
    }

    @Then("la télécommande est affichée")
    public void laTélécommandeEstAffichée() {
        // TODO : Vérifier que la télécommande est affichée
        // Assert.assertTrue(remoteControlPage.isRemoteControlDisplayed());
    }

    @And("le bouton de retour est visible")
    public void leBoutonDeRetourEstVisible() {
        // TODO : Vérifier que le bouton de retour est visible
        // Assert.assertTrue(remoteControlPage.isReturnButtonVisible());
    }

    @And("le menu déroulant de sélection de l'appareil est visible")
    public void leMenuDéroulantDeSélectionDeLAppareilEstVisible() {
        // TODO : Vérifier que le menu déroulant de sélection de l'appareil est visible
        // Assert.assertTrue(remoteControlPage.isDeviceSelectionMenuVisible());
    }

    @And("le bouton d'alimentation est visible")
    public void leBoutonDalimentationEstVisible() {
        // TODO : Vérifier que le bouton d'alimentation est visible
        // Assert.assertTrue(remoteControlPage.isPowerButtonVisible());
    }

    @And("les boutons de navigation (haut, bas, gauche, droite) sont visibles")
    public void lesBoutonsDeNavigationHautBasGaucheDroiteSontVisibles() {
        // TODO : Vérifier que les boutons de navigation sont visibles
        // Assert.assertTrue(remoteControlPage.isNavigationButtonsVisible());
    }

    @And("le bouton OK est visible")
    public void leBoutonOKEstVisible() {
        // TODO : Vérifier que le bouton OK est visible
        // Assert.assertTrue(remoteControlPage.isOKButtonVisible());
    }

    @And("le bouton de réversion est visible")
    public void leBoutonDeRéversionEstVisible() {
        // TODO : Vérifier que le bouton de réversion est visible
        // Assert.assertTrue(remoteControlPage.isReversionButtonVisible());
    }

    @And("le bouton de menu est visible")
    public void leBoutonDeMenuEstVisible() {
        // TODO : Vérifier que le bouton de menu est visible
        // Assert.assertTrue(remoteControlPage.isMenuButtonVisible());
    }

    @Given("que je suis sur la page de télécommande")
    public void queJeSuisSurLaPageDeTélécommande() {
        // TODO : Implémenter la navigation vers la page de télécommande
        // remoteControlPage = new RemoteControlPage();
        // remoteControlPage.navigateTo();
    }

    @When("je clique sur le menu déroulant de sélection de l'appareil")
    public void jeCliqueSurLeMenuDéroulantDeSélectionDeLAppareil() {
        // TODO : Implémenter la sélection du menu déroulant de sélection de l'appareil
        // remoteControlPage.clickOnDeviceSelectionMenu();
    }

    @And("je sélectionne un appareil \"Appareil 1\"")
    public void jeSélectionneUnAppareilAppareil1() {
        // TODO : Implémenter la sélection de l'appareil
        // remoteControlPage.selectDevice("Appareil 1");
    }

    @Then("l'appareil \"Appareil 1\" est sélectionné")
    public void lAppareilAppareil1EstSélectionné() {
        // TODO : Vérifier que l'appareil est sélectionné
        // Assert.assertTrue(remoteControlPage.isDeviceSelected("Appareil 1"));
    }

    @When("je clique sur le bouton de navigation \"haut\"")
    public void jeCliqueSurLeBoutonDeNavigationHaut() {
        // TODO : Implémenter la sélection du bouton de navigation "haut"
        // remoteControlPage.clickOnNavigationButton("haut");
    }

    @Then("la page de télécommande est mise à jour")
    public void laPageDeTélécommandeEstMiseÀJour() {
        // TODO : Vérifier que la page de télécommande est mise à jour
        // Assert.assertTrue(remoteControlPage.isPageUpdated());
    }

    @When("je clique sur le bouton de navigation \"bas\"")
    public void jeCliqueSurLeBoutonDeNavigationBas() {
        // TODO : Implémenter la sélection du bouton de navigation "bas"
        // remoteControlPage.clickOnNavigationButton("bas");
    }

    @When("je clique sur le bouton de volume \"augmenter\"")
    public void jeCliqueSurLeBoutonDeVolumeAugmenter() {
        // TODO : Implémenter la sélection du bouton de volume "augmenter"
        // remoteControlPage.clickOnVolumeButton("augmenter");
    }

    @Then("le volume est augmenté")
    public void leVolumeEstAugmenté() {
        // TODO : Vérifier que le volume est augmenté
        // Assert.assertTrue(remoteControlPage.isVolumeIncreased());
    }

    @When("je clique sur le bouton de volume \"diminuer\"")
    public void jeCliqueSurLeBoutonDeVolumeDiminuer() {
        // TODO : Implémenter la sélection du bouton de volume "diminuer"
        // remoteControlPage.clickOnVolumeButton("diminuer");
    }

    @Then("le volume est diminué")
    public void leVolumeEstDiminué() {
        // TODO : Vérifier que le volume est diminué
        // Assert.assertTrue(remoteControlPage.isVolumeDecreased());
    }

    @When("je clique sur le bouton de numérotation \"0\"")
    public void jeCliqueSurLeBoutonDeNumérotation0() {
        // TODO : Implémenter la sélection du bouton de numérotation "0"
        // remoteControlPage.clickOnNumberButton("0");
    }

    @Then("le numéro \"0\" est saisi")
    public void leNuméro0EstSaisi() {
        // TODO : Vérifier que le numéro "0" est saisi
        // Assert.assertTrue(remoteControlPage.isNumberEntered("0"));
    }

    @When("je clique sur le bouton de numérotation \"1\"")
    public void jeCliqueSurLeBoutonDeNumérotation1() {
        // TODO : Implémenter la sélection du bouton de numérotation "1"
        // remoteControlPage.clickOnNumberButton("1");
    }

    @Then("le numéro \"1\" est saisi")
    public void leNuméro1EstSaisi() {
        // TODO : Vérifier que le numéro "1" est saisi
        // Assert.assertTrue(remoteControlPage.isNumberEntered("1"));
    }
}