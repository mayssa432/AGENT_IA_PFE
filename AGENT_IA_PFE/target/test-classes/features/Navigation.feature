Feature: Navigation
  En tant qu'utilisateur, je veux pouvoir naviguer dans l'application pour accéder à différentes fonctionnalités.

  Scenario: Accéder à la page d'accueil
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Accueil"
    Then je devrais être redirigé vers la page d'accueil

  Scenario: Accéder à la page de replay
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Espace Replay"
    Then je devrais être redirigé vers la page de replay

  Scenario: Accéder à la page de TV en direct
    Given que je suis sur la page de navigation
    When je clique sur le bouton "TV en direct"
    Then je devrais être redirigé vers la page de TV en direct

  Scenario: Accéder à la page de VOD
    Given que je suis sur la page de navigation
    When je clique sur le bouton "VOD"
    Then je devrais être redirigé vers la page de VOD

  Scenario: Accéder à la page de boutique TV
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Boutique TV"
    Then je devrais être redirigé vers la page de boutique TV

  Scenario: Accéder à la page de recherche
    Given que je suis sur la page de navigation
    When je clique sur le bouton de recherche
    Then je devrais être redirigé vers la page de recherche

  Scenario: Accéder à la page de mon compte
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Mon compte"
    Then je devrais être redirigé vers la page de mon compte

  Scenario: Accéder à la page de partage de ma TV d'Orange
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Partage de ma TV d'Orange"
    Then je devrais être redirigé vers la page de partage de ma TV d'Orange

  Scenario: Accéder à la page de mes réglages
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Mes réglages"
    Then je devrais être redirigé vers la page de mes réglages

  Scenario: Accéder à la page de mes achats
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Mes achats"
    Then je devrais être redirigé vers la page de mes achats

  Scenario: Accéder à la page de pass vidéo
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Pass vidéo"
    Then je devrais être redirigé vers la page de pass vidéo

  Scenario: Accéder à la page de mes enregistrements
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Mes enregistrements"
    Then je devrais être redirigé vers la page de mes enregistrements

  Scenario: Accéder à la page de notation de l'application
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Noter l'application"
    Then je devrais être redirigé vers la page de notation de l'application

  Scenario: Accéder à la page de programmation
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Programmation"
    Then je devrais être redirigé vers la page de programmation

  Scenario: Accéder à la page de badge de confiance
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Badge de confiance"
    Then je devrais être redirigé vers la page de badge de confiance

  Scenario: Accéder à la page d'aide et de contact
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Aide & contact"
    Then je devrais être redirigé vers la page d'aide et de contact

  Scenario: Accéder à la page d'a propos
    Given que je suis sur la page de navigation
    When je clique sur le bouton "A propos"
    Then je devrais être redirigé vers la page d'a propos

  Scenario: Accéder à la page de découverte de l'application
    Given que je suis sur la page de navigation
    When je clique sur le bouton "Découverte de l'application"
    Then je devrais être redirigé vers la page de découverte de l'application

  Scenario: Utiliser le bouton de retour
    Given que je suis sur la page de navigation
    When je clique sur le bouton de retour
    Then je devrais être redirigé vers la page précédente

  Scenario: Utiliser le bouton de recherche
    Given que je suis sur la page de navigation
    When je clique sur le bouton de recherche
    And je saisie une chaîne de caractères dans le champ de recherche
    Then je devrais voir les résultats de la recherche

  Scenario: Utiliser le bouton de partage
    Given que je suis sur la page de navigation
    When je clique sur le bouton de partage
    Then je devrais voir les options de partage

  Scenario: Utiliser le bouton de paramètres
    Given que je suis sur la page de navigation
    When je clique sur le bouton de paramètres
    Then je devrais voir les paramètres de l'application

  Scenario: Utiliser le bouton de déconnexion
    Given que je suis sur la page de navigation
    When je clique sur le bouton de déconnexion
    Then je devrais être déconnecté de l'application

  Scenario: Vérifier la présence des éléments de navigation
    Given que je suis sur la page de navigation
    Then je devrais voir les éléments de navigation suivants :
      | Élément         | Visible |
      | Accueil         | oui     |
      | Espace Replay   | oui     |
      | TV en direct    | oui     |
      | VOD             | oui     |
      | Boutique TV     | oui     |
      | Recherche       | oui     |
      | Mon compte      | oui     |
      | Partage de ma TV| oui     |
      | Mes réglages    | oui     |
      | Mes achats      | oui     |
      | Pass vidéo     | oui     |
      | Mes enregistrements| oui     |
      | Noter l'application| oui     |
      | Programmation   | oui     |
      | Badge de confiance| oui     |
      | Aide & contact  | oui     |
      | A propos        | oui     |
      | Découverte de l'application| oui     |