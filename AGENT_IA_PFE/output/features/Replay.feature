Feature: Replay Page
  En tant qu'utilisateur, je veux accéder à la page Replay pour visualiser les contenus de replay.

  Scenario: Accéder à la page Replay
    Given que je suis sur la page d'accueil
    When je clique sur le bouton "Replay"
    Then je devrais voir la page Replay avec le titre "Replay"

  Scenario: Visualiser les chaînes de replay
    Given que je suis sur la page Replay
    When je clique sur le bouton "Toutes les chaînes"
    Then je devrais voir la liste des chaînes de replay
    And je devrais voir les logos des chaînes de replay

  Scenario: Sélectionner une chaîne de replay
    Given que je suis sur la page Replay
    When je clique sur une chaîne de replay
    Then je devrais voir les détails de la chaîne de replay sélectionnée
    And je devrais voir les épisodes disponibles pour la chaîne de replay sélectionnée

  Scenario: Utiliser le menu de tri et de filtrage
    Given que je suis sur la page Replay
    When je clique sur le menu de tri et de filtrage
    Then je devrais voir les options de tri et de filtrage
    And je devrais pouvoir sélectionner une option de tri ou de filtrage

  Scenario: Rechercher un contenu de replay
    Given que je suis sur la page Replay
    When je saisie un mot-clé dans le champ de recherche
    Then je devrais voir les résultats de la recherche pour le mot-clé saisi

  Scenario: Afficher les informations d'un épisode de replay
    Given que je suis sur la page Replay
    When je clique sur un épisode de replay
    Then je devrais voir les informations détaillées de l'épisode de replay sélectionné
    And je devrais voir les options pour regarder ou télécharger l'épisode de replay sélectionné

  Scenario: Vérifier la présence du logo Orange
    Given que je suis sur la page Replay
    Then je devrais voir le logo Orange en haut de la page

  Scenario: Vérifier la présence du bouton "Continuer"
    Given que je suis sur la page Replay
    Then je devrais voir le bouton "Continuer" en bas de la page

  Scenario: Vérifier la présence de la barre de recherche
    Given que je suis sur la page Replay
    Then je devrais voir la barre de recherche en haut de la page

  Scenario: Vérifier la présence des boutons de navigation
    Given que je suis sur la page Replay
    Then je devrais voir les boutons de navigation en bas de la page

  Scenario: Vérifier la présence des éléments de la grille de replay
    Given que je suis sur la page Replay
    Then je devrais voir les éléments de la grille de replay
    And je devrais voir les informations détaillées de chaque élément de la grille de replay