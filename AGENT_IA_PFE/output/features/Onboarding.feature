Feature: Onboarding
  Description: Cette fonctionnalité permet à l'utilisateur de naviguer à travers les écrans d'onboarding

  Scenario: Affichage de l'écran d'onboarding
    Given L'utilisateur lance l'application
    When L'utilisateur est sur l'écran d'onboarding
    Then L'utilisateur voit le texte "Et profitez"
    And L'utilisateur voit le texte "Hors connexion"

  Scenario: Connexion à l'application
    Given L'utilisateur est sur l'écran d'onboarding
    When L'utilisateur clique sur le bouton "M'identifier"
    Then L'utilisateur est redirigé vers l'écran de connexion

  Scenario: Découverte de l'application en tant que visiteur
    Given L'utilisateur est sur l'écran d'onboarding
    When L'utilisateur clique sur le bouton "DÉCOUVRIR"
    Then L'utilisateur est redirigé vers l'écran de découverte
    And L'utilisateur voit les options de découverte de télévision

  Scenario: Affichage des options de découverte de télévision
    Given L'utilisateur est sur l'écran de découverte
    When L'utilisateur voit les options de découverte de télévision
    Then L'utilisateur voit le titre de l'option de télévision
    And L'utilisateur voit le texte de l'option de télévision
    And L'utilisateur voit le fournisseur de l'option de télévision
    And L'utilisateur voit le bouton d'abonnement à l'option de télévision

  Scenario: Abonnement à une option de télévision
    Given L'utilisateur est sur l'écran de découverte
    When L'utilisateur clique sur le bouton d'abonnement à une option de télévision
    Then L'utilisateur est redirigé vers l'écran de connexion pour s'identifier

  Scenario: Arrêt du partage de l'écran d'onboarding
    Given L'utilisateur est sur l'écran d'onboarding
    When L'utilisateur clique sur le bouton d'arrêt du partage
    Then L'utilisateur n'est plus sur l'écran d'onboarding

  Scenario: Affichage de la page de téléchargements
    Given L'utilisateur est sur l'écran d'onboarding
    When L'utilisateur clique sur le bouton "Mes téléchargements"
    Then L'utilisateur est redirigé vers la page de téléchargements

  Scenario: Réessayer la connexion
    Given L'utilisateur est sur l'écran d'onboarding
    When L'utilisateur clique sur le bouton "RÉESSAYER"
    Then L'utilisateur est redirigé vers l'écran de connexion pour réessayer la connexion

  Scenario: S'identifier à l'application
    Given L'utilisateur est sur l'écran d'onboarding
    When L'utilisateur clique sur le bouton "S'IDENTIFIER"
    Then L'utilisateur est redirigé vers l'écran de connexion pour s'identifier

  Scenario: Nouvelle adresse
    Given L'utilisateur est sur l'écran d'onboarding
    When L'utilisateur clique sur le champ de saisie de nouvelle adresse
    Then L'utilisateur peut saisir une nouvelle adresse