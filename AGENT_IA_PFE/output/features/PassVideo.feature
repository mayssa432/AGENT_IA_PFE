Feature: PassVideo Page
  En tant qu'utilisateur, je veux accéder à la page PassVideo pour découvrir les offres de partenaires

  Scenario: Vérification de la présence de l'élément svodInfoSubscription
    Given que je suis sur la page PassVideo
    When je vérifie la présence de l'élément svodInfoSubscription
    Then l'élément svodInfoSubscription est visible

  Scenario: Vérification de la présence des éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle
    Given que je suis sur la page PassVideo
    When je vérifie la présence des éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle
    Then les éléments svodLogo, svodPartnerTitle et svodPartnerSubTitle sont visibles

  Scenario: Vérification du clic sur le bouton svodPartnerDiscoverButton
    Given que je suis sur la page PassVideo
    When je clique sur le bouton svodPartnerDiscoverButton
    Then je suis redirigé vers la page de découverte du partenaire

  Scenario: Vérification de la présence des éléments svodPartnerOfferButton
    Given que je suis sur la page PassVideo
    When je vérifie la présence des éléments svodPartnerOfferButton
    Then les éléments svodPartnerOfferButton sont visibles

  Scenario: Vérification de la compatibilité avec les appareils iPad
    Given que je suis sur la page PassVideo avec un appareil iPad
    When je vérifie la présence des éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad
    Then les éléments svodPartnerTitleIpad et svodPartnerSubTitleIpad sont visibles

  Scenario: Vérification de la présence des éléments svodPartnerDiscoverButton sur les appareils iPad
    Given que je suis sur la page PassVideo avec un appareil iPad
    When je vérifie la présence des éléments svodPartnerDiscoverButton
    Then les éléments svodPartnerDiscoverButton sont visibles et cliquables sur l'appareil iPad