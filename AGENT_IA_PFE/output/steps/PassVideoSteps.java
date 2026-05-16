package com.orange.otvp.automation.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import com.orange.otvp.automation.pages.PassVideoPage;
import com.orange.otvp.automation.pages.PassVideoPageIpad;

public class PassVideoSteps {

    private PassVideoPage passVideoPage;
    private PassVideoPageIpad passVideoPageIpad;

    @Given("que je suis sur la page PassVideo")
    public void queJeSuisSurLaPagePassVideo() {
        // Commentaire : Initialisation de la page PassVideo
        // Action : Appel de la méthode pour initialiser la page PassVideo
        passVideoPage = new PassVideoPage();
    }

    @Given("que je suis sur la page PassVideo avec un appareil iPad")
    public void queJeSuisSurLaPagePassVideoAvecUnAppareilIpad() {
        // Commentaire : Initialisation de la page PassVideo avec un appareil iPad
        // Action : Appel de la méthode pour initialiser la page PassVideoIpad
        passVideoPageIpad = new PassVideoPageIpad();
    }

    @When("je vérifie la présence de l'élément svodInfoSubscription")
    public void jeVérifieLaPrésenceDeLÉlémentSvodInfoSubscription() {
        // Commentaire : Vérification de la présence de l'élément svodInfoSubscription
        // Action : Appel de la méthode pour vérifier la présence de l'élément svodInfoSubscription
        passVideoPage.isSvodInfoSubscriptionVisible();
    }

    @Then("l'élément svodInfoSubscription est visible")
    public void lÉlémentSvodInfoSubscriptionEstVisible() {
        // Commentaire : Vérification de la visibilité de l'élément svodInfoSubscription
        // Action : Appel de la méthode pour vérifier la visibilité de l'élément svodInfoSubscription
        Assert.assertTrue(passVideoPage.isSvodInfoSubscriptionVisible());
    }

    @When("je vérifie la présence des éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle")
    public void jeVérifieLaPrésenceDesÉlémentsSvodLogoSvodPartnerTitleEtSvodPartnerSubTitle() {
        // Commentaire : Vérification de la présence des éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle
        // Action : Appel de la méthode pour vérifier la présence des éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle
        passVideoPage.isSvodLogoSvodPartnerTitleSvodPartnerSubTitleVisible();
    }

    @Then("les éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle sont visibles")
    public void lesÉlémentsSvodLogoSvodPartnerTitleEtSvodPartnerSubTitleSontVisibles() {
        // Commentaire : Vérification de la visibilité des éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle
        // Action : Appel de la méthode pour vérifier la visibilité des éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle
        Assert.assertTrue(passVideoPage.isSvodLogoSvodPartnerTitleSvodPartnerSubTitleVisible());
    }

    @When("je clique sur le bouton svodPartnerDiscoverButton")
    public void jeCliqueSurLeBoutonSvodPartnerDiscoverButton() {
        // Commentaire : Clic sur le bouton svodPartnerDiscoverButton
        // Action : Appel de la méthode pour cliquer sur le bouton svodPartnerDiscoverButton
        passVideoPage.clickSvodPartnerDiscoverButton();
    }

    @Then("je suis redirigé vers la page de découverte du partenaire")
    public void jeSuisRedirigéVersLaPageDeDécouverteDuPartenaire() {
        // Commentaire : Vérification de la redirection vers la page de découverte du partenaire
        // Action : Appel de la méthode pour vérifier la redirection vers la page de découverte du partenaire
        // A compléter en fonction de la logique de l'application
    }

    @When("je vérifie la présence des éléments svodPartnerOfferButton")
    public void jeVérifieLaPrésenceDesÉlémentsSvodPartnerOfferButton() {
        // Commentaire : Vérification de la présence des éléments svodPartnerOfferButton
        // Action : Appel de la méthode pour vérifier la présence des éléments svodPartnerOfferButton
        passVideoPage.isSvodPartnerOfferButtonVisible();
    }

    @Then("les éléments svodPartnerOfferButton sont visibles")
    public void lesÉlémentsSvodPartnerOfferButtonSontVisibles() {
        // Commentaire : Vérification de la visibilité des éléments svodPartnerOfferButton
        // Action : Appel de la méthode pour vérifier la visibilité des éléments svodPartnerOfferButton
        Assert.assertTrue(passVideoPage.isSvodPartnerOfferButtonVisible());
    }

    @When("je vérifie la présence des éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad")
    public void jeVérifieLaPrésenceDesÉlémentsSvodPartnerTitleIpadEtSvodPartnerSubTitleIpad() {
        // Commentaire : Vérification de la présence des éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad
        // Action : Appel de la méthode pour vérifier la présence des éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad
        passVideoPageIpad.isSvodPartnerTitleIpadSvodPartnerSubTitleIpadVisible();
    }

    @Then("les éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad sont visibles")
    public void lesÉlémentsSvodPartnerTitleIpadEtSvodPartnerSubTitleIpadSontVisibles() {
        // Commentaire : Vérification de la visibilité des éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad
        // Action : Appel de la méthode pour vérifier la visibilité des éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad
        Assert.assertTrue(passVideoPageIpad.isSvodPartnerTitleIpadSvodPartnerSubTitleIpadVisible());
    }

    @When("je vérifie la présence des éléments svodPartnerDiscoverButton")
    public void jeVérifieLaPrésenceDesÉlémentsSvodPartnerDiscoverButton() {
        // Commentaire : Vérification de la présence des éléments svodPartnerDiscoverButton
        // Action : Appel de la méthode pour vérifier la présence des éléments svodPartnerDiscoverButton
        passVideoPageIpad.isSvodPartnerDiscoverButtonVisible();
    }

    @Then("les éléments svodPartnerDiscoverButton sont visibles et cliquables sur l'appareil iPad")
    public void lesÉlémentsSvodPartnerDiscoverButtonSontVisiblesEtCliquablesSurLAppareilIpad() {
        // Commentaire : Vérification de la visibilité et de la cliquabilité des éléments svodPartnerDiscoverButton sur l'appareil iPad
        // Action : Appel de la méthode pour vérifier la visibilité et la cliquabilité des éléments svodPartnerDiscoverButton sur l'appareil iPad
        Assert.assertTrue(passVideoPageIpad.isSvodPartnerDiscoverButtonVisible());
        Assert.assertTrue(passVideoPageIpad.isSvodPartnerDiscoverButtonClickable());
    }
}