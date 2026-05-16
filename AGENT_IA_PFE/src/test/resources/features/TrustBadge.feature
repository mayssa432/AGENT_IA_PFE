Feature: TrustBadge
  Description: Cette fonctionnalité permet de tester les éléments de la page TrustBadge

  Scenario: Vérification de la présence des éléments de la page TrustBadge
    Given que je suis sur la page TrustBadge
    When je vérifie la présence des éléments de la page
    Then je vois le nom de l'application "dataUsageAppName"
    And je vois le sous-titre de la page "dataUsageHeader"
    And je vois le sous-titre de la page "dataUsageSubtitle"
    And je vois la carte de données "dataUsageDataCard"
    And je vois la carte d'utilisation "dataUsageUsageCard"
    And je vois la carte de conditions "dataUsageTermsCard"
    And je vois la carte de données personnalisées "dataUsageDjingoCard"

  Scenario: Vérification de la navigation vers la page de gestion des consentements
    Given que je suis sur la page TrustBadge
    When je clique sur le bouton "manageConsentButton"
    Then je suis redirigé vers la page de gestion des consentements

  Scenario: Vérification de l'acceptation de l'accord de protection des données Djingo
    Given que je suis sur la page TrustBadge
    When je clique sur la carte de données personnalisées "dataUsageDjingoCard"
    And je clique sur le bouton "djingoDataProtectionAgreementButton"
    And je coche la case "djingoDataProtectionAgreementCheckbox"
    And je clique sur le bouton "djingoDataProtectionAgreementAcceptButton"
    Then je vois un message de confirmation d'acceptation de l'accord de protection des données Djingo

  Scenario: Vérification de la désactivation d'un élément de la liste des switchs Djingo
    Given que je suis sur la page TrustBadge
    When je clique sur la carte de données personnalisées "dataUsageDjingoCard"
    And je clique sur le bouton "djingoDataProtectionAgreementButton"
    And je désactive un élément de la liste des switchs "djingoSwitchItems"
    Then je vois que l'élément est désactivé

  Scenario: Vérification de la suppression d'un élément de la liste des boutons de suppression Djingo
    Given que je suis sur la page TrustBadge
    When je clique sur la carte de données personnalisées "dataUsageDjingoCard"
    And je clique sur le bouton "djingoDataProtectionAgreementButton"
    And je clique sur un élément de la liste des boutons de suppression "djingoDeleteButtons"
    Then je vois que l'élément est supprimé