Feature: Gestion des PopUpMessages
  En tant qu'utilisateur, je veux gérer les pop-up messages pour une expérience utilisateur fluide.

  Scenario: Afficher un pop-up message personnalisé
    Given que l'application est ouverte
    When je clique sur un élément qui déclenche un pop-up message personnalisé
    Then le pop-up message personnalisé est affiché
    And le titre du pop-up message personnalisé est "Titre du pop-up"
    And le texte du pop-up message personnalisé est "Texte du pop-up"

  Scenario: Cliquer sur le bouton positif d'un pop-up message personnalisé
    Given que l'application est ouverte
    And que le pop-up message personnalisé est affiché
    When je clique sur le bouton positif du pop-up message personnalisé
    Then le pop-up message personnalisé disparaît
    And l'application continue à fonctionner normalement

  Scenario: Cliquer sur le bouton négatif d'un pop-up message personnalisé
    Given que l'application est ouverte
    And que le pop-up message personnalisé est affiché
    When je clique sur le bouton négatif du pop-up message personnalisé
    Then le pop-up message personnalisé disparaît
    And l'application continue à fonctionner normalement

  Scenario: Gérer les pop-up messages de démarrage
    Given que l'application est ouverte pour la première fois
    When je clique sur le bouton de démarrage
    Then les pop-up messages de démarrage sont affichés
    And je peux cliquer sur le bouton positif pour les fermer

  Scenario: Gérer les pop-up messages de rappel
    Given que l'application est ouverte
    And que je suis inscrit pour recevoir des rappels
    When je reçois un rappel
    Then le pop-up message de rappel est affiché
    And je peux cliquer sur le bouton positif pour le fermer

  Scenario: Gérer les pop-up messages de notification
    Given que l'application est ouverte
    And que je suis inscrit pour recevoir des notifications
    When je reçois une notification
    Then le pop-up message de notification est affiché
    And je peux cliquer sur le bouton positif pour le fermer

  Scenario: Gérer les pop-up messages de changement de compte
    Given que l'application est ouverte
    And que je suis connecté à un compte
    When je clique sur le bouton de changement de compte
    Then le pop-up message de changement de compte est affiché
    And je peux cliquer sur le bouton positif pour le fermer

  Scenario: Gérer les pop-up messages de déconnexion
    Given que l'application est ouverte
    And que je suis connecté à un compte
    When je clique sur le bouton de déconnexion
    Then le pop-up message de déconnexion est affiché
    And je peux cliquer sur le bouton positif pour le fermer