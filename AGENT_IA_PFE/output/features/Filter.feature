Feature: Filtre de contenu
  En tant qu'utilisateur, je veux pouvoir filtrer les contenus pour trouver ce que je cherche plus facilement

  Scenario: Filtrer par genre
    Given que je suis sur la page de filtre
    When je clique sur le bouton de filtre par genre
    And je sélectionne le genre "Action"
    Then je vois uniquement les contenus de genre "Action"

  Scenario: Filtrer par jour
    Given que je suis sur la page de filtre
    When je clique sur le bouton de filtre par jour
    And je sélectionne le jour "Aujourd'hui"
    Then je vois uniquement les contenus diffusés aujourd'hui

  Scenario: Filtrer par heure
    Given que je suis sur la page de filtre
    When je clique sur le bouton de filtre par heure
    And je sélectionne l'heure "18h-20h"
    Then je vois uniquement les contenus diffusés entre 18h et 20h

  Scenario: Filtrer par catégorie VOD
    Given que je suis sur la page de filtre
    When je clique sur le bouton de filtre par catégorie VOD
    And je sélectionne la catégorie "Films"
    Then je vois uniquement les contenus VOD de catégorie "Films"

  Scenario: Réinitialiser les filtres
    Given que je suis sur la page de filtre
    When je clique sur le bouton de réinitialisation des filtres
    Then tous les filtres sont réinitialisés et je vois tous les contenus

  Scenario: Appliquer les filtres
    Given que je suis sur la page de filtre
    When je clique sur le bouton d'application des filtres
    Then les contenus sont affichés en fonction des filtres sélectionnés

  Scenario: Sélectionner plusieurs filtres
    Given que je suis sur la page de filtre
    When je clique sur le bouton de filtre par genre
    And je sélectionne le genre "Action"
    And je clique sur le bouton de filtre par jour
    And je sélectionne le jour "Aujourd'hui"
    Then je vois uniquement les contenus de genre "Action" diffusés aujourd'hui