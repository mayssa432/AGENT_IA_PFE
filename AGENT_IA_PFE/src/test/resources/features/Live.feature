Feature: Live Page
  En tant qu'utilisateur, je veux accéder à la page Live pour visionner des programmes en direct.

  Scenario: Accéder à la page Live
    Given que je suis sur la page d'accueil
    When je clique sur le bouton "Programme TV"
    Then je suis redirigé vers la page Live

  Scenario: Voir les programmes en direct
    Given que je suis sur la page Live
    When je clique sur le bouton "En ce moment à la TV"
    Then je vois la liste des programmes en direct
    And je vois les informations de chaque programme, notamment le titre, la chaîne et l'heure de diffusion

  Scenario: Lancer un programme en direct
    Given que je suis sur la page Live
    When je clique sur un programme en direct
    Then le programme démarre et je peux le visionner
    And je vois les contrôles de lecture, notamment les boutons de pause et de stop

  Scenario: Changer de chaîne
    Given que je suis sur la page Live
    When je clique sur le bouton "Tout le live"
    Then je vois la liste de toutes les chaînes disponibles
    And je peux sélectionner une chaîne pour la visionner

  Scenario: Voir les programmes à venir
    Given que je suis sur la page Live
    When je clique sur le bouton "Programmes à venir"
    Then je vois la liste des programmes qui seront diffusés plus tard
    And je peux voir les informations de chaque programme, notamment le titre, la chaîne et l'heure de diffusion

  Scenario: Utiliser les filtres de recherche
    Given que je suis sur la page Live
    When je clique sur le bouton de filtre
    Then je peux sélectionner des critères de recherche, notamment la chaîne ou le genre de programme
    And je vois les résultats de la recherche, notamment la liste des programmes qui correspondent aux critères sélectionnés

  Scenario: Voir les recommandations de programmes
    Given que je suis sur la page Live
    When je clique sur le bouton "Recommandations"
    Then je vois la liste des programmes recommandés, notamment les programmes qui sont populaires ou qui correspondent à mes préférences
    And je peux voir les informations de chaque programme, notamment le titre, la chaîne et l'heure de diffusion