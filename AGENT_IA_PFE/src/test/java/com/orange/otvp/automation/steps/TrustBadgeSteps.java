package com.orange.otvp.automation.steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import com.orange.otvp.automation.pages.TrustBadgePage;
import com.orange.otvp.automation.pages.ConsentManagementPage;
import com.orange.otvp.automation.pages.DjingoDataProtectionAgreementPage;

public class TrustBadgeSteps {

    private TrustBadgePage trustBadgePage;
    private ConsentManagementPage consentManagementPage;
    private DjingoDataProtectionAgreementPage djingoDataProtectionAgreementPage;

    @Given("que je suis sur la page TrustBadge")
    public void queJeSuisSurLaPageTrustBadge() {
        // Commentaire : Récupération de la page TrustBadge
        // Action : Récupération de la page TrustBadge
        trustBadgePage = new TrustBadgePage();
        trustBadgePage.navigateTo();
    }

    @When("je vérifie la présence des éléments de la page")
    public void jeVérifieLaPrésenceDesÉlémentsDeLaPage() {
        // Commentaire : Vérification de la présence des éléments de la page
        // Action : Vérification de la présence des éléments de la page
        trustBadgePage.verifyElementsPresence();
    }

    @Then("je vois le nom de l'application {string}")
    public void jeVoisLeNomDeLApplication(String dataUsageAppName) {
        // Commentaire : Vérification du nom de l'application
        // Action : Vérification du nom de l'application
        Assert.assertTrue(trustBadgePage.isApplicationNameDisplayed(dataUsageAppName));
    }

    @Then("je vois le sous-titre de la page {string}")
    public void jeVoisLeSousTitreDeLaPage(String dataUsageHeader) {
        // Commentaire : Vérification du sous-titre de la page
        // Action : Vérification du sous-titre de la page
        Assert.assertTrue(trustBadgePage.isPageSubtitleDisplayed(dataUsageHeader));
    }

    @Then("je vois le sous-titre de la page {string}")
    public void jeVoisLeSousTitreDeLaPage2(String dataUsageSubtitle) {
        // Commentaire : Vérification du sous-titre de la page
        // Action : Vérification du sous-titre de la page
        Assert.assertTrue(trustBadgePage.isPageSubtitleDisplayed(dataUsageSubtitle));
    }

    @Then("je vois la carte de données {string}")
    public void jeVoisLaCarteDeDonnées(String dataUsageDataCard) {
        // Commentaire : Vérification de la carte de données
        // Action : Vérification de la carte de données
        Assert.assertTrue(trustBadgePage.isDataCardDisplayed(dataUsageDataCard));
    }

    @Then("je vois la carte d'utilisation {string}")
    public void jeVoisLaCarteDUtilisation(String dataUsageUsageCard) {
        // Commentaire : Vérification de la carte d'utilisation
        // Action : Vérification de la carte d'utilisation
        Assert.assertTrue(trustBadgePage.isUsageCardDisplayed(dataUsageUsageCard));
    }

    @Then("je vois la carte de conditions {string}")
    public void jeVoisLaCarteDeConditions(String dataUsageTermsCard) {
        // Commentaire : Vérification de la carte de conditions
        // Action : Vérification de la carte de conditions
        Assert.assertTrue(trustBadgePage.isTermsCardDisplayed(dataUsageTermsCard));
    }

    @Then("je vois la carte de données personnalisées {string}")
    public void jeVoisLaCarteDeDonnéesPersonnalisées(String dataUsageDjingoCard) {
        // Commentaire : Vérification de la carte de données personnalisées
        // Action : Vérification de la carte de données personnalisées
        Assert.assertTrue(trustBadgePage.isDjingoCardDisplayed(dataUsageDjingoCard));
    }

    @When("je clique sur le bouton {string}")
    public void jeCliqueSurLeBouton(String manageConsentButton) {
        // Commentaire : Clique sur le bouton de gestion des consentements
        // Action : Clique sur le bouton de gestion des consentements
        trustBadgePage.clickManageConsentButton();
        consentManagementPage = new ConsentManagementPage();
        consentManagementPage.navigateTo();
    }

    @Then("je suis redirigé vers la page de gestion des consentements")
    public void jeSuisRedirigéVersLaPageDeGestionDesConsentements() {
        // Commentaire : Vérification de la redirection vers la page de gestion des consentements
        // Action : Vérification de la redirection vers la page de gestion des consentements
        Assert.assertTrue(consentManagementPage.isPageDisplayed());
    }

    @When("je clique sur la carte de données personnalisées {string}")
    public void jeCliqueSurLaCarteDeDonnéesPersonnalisées(String dataUsageDjingoCard) {
        // Commentaire : Clique sur la carte de données personnalisées
        // Action : Clique sur la carte de données personnalisées
        trustBadgePage.clickDjingoCard();
        djingoDataProtectionAgreementPage = new DjingoDataProtectionAgreementPage();
        djingoDataProtectionAgreementPage.navigateTo();
    }

    @And("je clique sur le bouton {string}")
    public void jeCliqueSurLeBouton2(String djingoDataProtectionAgreementButton) {
        // Commentaire : Clique sur le bouton d'accord de protection des données Djingo
        // Action : Clique sur le bouton d'accord de protection des données Djingo
        djingoDataProtectionAgreementPage.clickDjingoDataProtectionAgreementButton();
    }

    @And("je coche la case {string}")
    public void jeCochLaCase(String djingoDataProtectionAgreementCheckbox) {
        // Commentaire : Coche la case d'acceptation de l'accord de protection des données Djingo
        // Action : Coche la case d'acceptation de l'accord de protection des données Djingo
        djingoDataProtectionAgreementPage.checkDjingoDataProtectionAgreementCheckbox();
    }

    @And("je clique sur le bouton {string}")
    public void jeCliqueSurLeBouton3(String djingoDataProtectionAgreementAcceptButton) {
        // Commentaire : Clique sur le bouton d'acceptation de l'accord de protection des données Djingo
        // Action : Clique sur le bouton d'acceptation de l'accord de protection des données Djingo
        djingoDataProtectionAgreementPage.clickDjingoDataProtectionAgreementAcceptButton();
    }

    @Then("je vois un message de confirmation d'acceptation de l'accord de protection des données Djingo")
    public void jeVoisUnMessageDeConfirmationDAcceptationDeLAccordDeProtectionDesDonneesDjingo() {
        // Commentaire : Vérification du message de confirmation d'acceptation de l'accord de protection des données Djingo
        // Action : Vérification du message de confirmation d'acceptation de l'accord de protection des données Djingo
        Assert.assertTrue(djingoDataProtectionAgreementPage.isConfirmationMessageDisplayed());
    }

    @When("je clique sur la carte de données personnalisées {string}")
    public void jeCliqueSurLaCarteDeDonnéesPersonnalisées2(String dataUsageDjingoCard) {
        // Commentaire : Clique sur la carte de données personnalisées
        // Action : Clique sur la carte de données personnalisées
        trustBadgePage.clickDjingoCard();
        djingoDataProtectionAgreementPage = new DjingoDataProtectionAgreementPage();
        djingoDataProtectionAgreementPage.navigateTo();
    }

    @And("je clique sur le bouton {string}")
    public void jeCliqueSurLeBouton4(String djingoDataProtectionAgreementButton) {
        // Commentaire : Clique sur le bouton d'accord de protection des données Djingo
        // Action : Clique sur le bouton d'accord de protection des données Djingo
        djingoDataProtectionAgreementPage.clickDjingoDataProtectionAgreementButton();
    }

    @And("je désactive un élément de la liste des switchs {string}")
    public void jeDésactiveUnÉlémentDeLaListeDesSwitchs(String djingoSwitchItems) {
        // Commentaire : Désactivation d'un élément de la liste des switchs
        // Action : Désactivation d'un élément de la liste des switchs
        djingoDataProtectionAgreementPage.deselectDjingoSwitchItem();
    }

    @Then("je vois que l'élément est désactivé")
    public void jeVoisQueLElémentEstDésactivé() {
        // Commentaire : Vérification de la désactivation de l'élément
        // Action : Vérification de la désactivation de l'élément
        Assert.assertTrue(djingoDataProtectionAgreementPage.isDjingoSwitchItemDeselected());
    }

    @When("je clique sur la carte de données personnalisées {string}")
    public void jeCliqueSurLaCarteDeDonnéesPersonnalisées3(String dataUsageDjingoCard) {
        // Commentaire : Clique sur la carte de données personnalisées
        // Action : Clique sur la carte de données personnalisées
        trustBadgePage.clickOnCustomDataCard(dataUsageDjingoCard);
    }
}