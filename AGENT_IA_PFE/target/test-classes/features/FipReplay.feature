Feature: FipReplay
  En tant qu'utilisateur, je veux pouvoir accéder aux fonctionnalités de FipReplay pour visualiser et gérer les contenus de réplay.

  Scenario: Afficher la liste des programmes de réplay
    Given que l'utilisateur est sur la page d'accueil de FipReplay
    When l'utilisateur clique sur l'onglet "Réplay"
    Then la liste des programmes de réplay est affichée
    And le titre du programme est affiché
    And la miniature du programme est affichée
    And le logo de la chaîne est affiché
    And le nombre d'épisodes est affiché

  Scenario: Afficher les détails d'un programme de réplay
    Given que l'utilisateur est sur la page d'accueil de FipReplay
    When l'utilisateur clique sur un programme de réplay
    Then les détails du programme sont affichés
    And le titre du programme est affiché
    And la miniature du programme est affichée
    And le logo de la chaîne est affiché
    And la disponibilité du programme est affichée
    And la description du programme est affichée
    And le bouton de lecture est affiché

  Scenario: Lancer la lecture d'un épisode de réplay
    Given que l'utilisateur est sur la page d'accueil de FipReplay
    When l'utilisateur clique sur un programme de réplay
    And l'utilisateur clique sur un épisode de réplay
    Then la lecture de l'épisode est lancée
    And le bouton de pause est affiché
    And le temps de lecture est affiché

  Scenario: S'abonner à un programme de réplay
    Given que l'utilisateur est sur la page d'accueil de FipReplay
    When l'utilisateur clique sur un programme de réplay
    And l'utilisateur clique sur le bouton "S'abonner"
    Then la page d'abonnement est affichée
    And les informations d'abonnement sont affichées
    And le bouton de validation est affiché

  Scenario: Afficher les informations d'un épisode de réplay
    Given que l'utilisateur est sur la page d'accueil de FipReplay
    When l'utilisateur clique sur un programme de réplay
    And l'utilisateur clique sur un épisode de réplay
    Then les informations de l'épisode sont affichées
    And le titre de l'épisode est affiché
    And la description de l'épisode est affichée
    And le temps de lecture est affiché