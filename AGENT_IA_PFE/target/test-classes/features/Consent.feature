Feature: Consent Page
  Description: Cette fonctionnalité permet de gérer les consentements sur la page de consentement.

  Scenario: Afficher la page de consentement
    Given L'utilisateur est sur la page de consentement
    When La page de consentement est affichée
    Then Le texte de description du consentement est affiché
    And Le lien de politique de consentement est affiché
    And Le bouton d'acceptation est affiché
    And Le bouton de refus est affiché
    And Le bouton de personnalisation est affiché

  Scenario: Cliquer sur le bouton d'acceptation
    Given L'utilisateur est sur la page de consentement
    When L'utilisateur clique sur le bouton d'acceptation
    Then La page de consentement est fermée
    And L'utilisateur est redirigé vers la page suivante

  Scenario: Cliquer sur le bouton de personnalisation
    Given L'utilisateur est sur la page de consentement
    When L'utilisateur clique sur le bouton de personnalisation
    Then La page de personnalisation des consentements est affichée
    And Les options de personnalisation sont affichées
    And L'utilisateur peut sélectionner les options de personnalisation

  Scenario: Cliquer sur le lien de politique de consentement
    Given L'utilisateur est sur la page de consentement
    When L'utilisateur clique sur le lien de politique de consentement
    Then La page de politique de consentement est affichée
    And Les informations de politique de consentement sont affichées

  Scenario: Sélectionner les options de personnalisation
    Given L'utilisateur est sur la page de personnalisation des consentements
    When L'utilisateur sélectionne les options de personnalisation
    And L'utilisateur clique sur le bouton de sauvegarde
    Then Les options de personnalisation sont enregistrées
    And L'utilisateur est redirigé vers la page suivante

  Scenario: Cliquer sur le bouton de refus
    Given L'utilisateur est sur la page de consentement
    When L'utilisateur clique sur le bouton de refus
    Then La page de consentement est fermée
    And L'utilisateur est redirigé vers la page suivante

  Scenario: Vérifier les éléments de la page de consentement
    Given L'utilisateur est sur la page de consentement
    When La page de consentement est affichée
    Then Le texte de description du consentement est affiché
    And Le lien de politique de consentement est affiché
    And Le bouton d'acceptation est affiché
    And Le bouton de refus est affiché
    And Le bouton de personnalisation est affiché
    And Les options de personnalisation sont affichées
    And Les informations de politique de consentement sont affichées