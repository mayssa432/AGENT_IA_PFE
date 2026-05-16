Feature: Paramètres de l'application
  En tant qu'utilisateur, je veux pouvoir accéder aux paramètres de l'application
  pour personnaliser mon expérience utilisateur.

  Scenario: Vérification de la présence des paramètres
    Given que je suis sur la page d'accueil de l'application
    When je clique sur le bouton de paramètres
    Then je vois la page des paramètres

  Scenario: Vérification de la fonctionnalité de rappel
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de rappel
    And je sélectionne une option de rappel
    Then je vois le texte de rappel mis à jour

  Scenario: Vérification de la fonctionnalité de qualité de streaming
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de qualité de streaming
    And je sélectionne une option de qualité de streaming
    Then je vois le texte de qualité de streaming mis à jour

  Scenario: Vérification de la fonctionnalité de téléchargement en réseau mobile
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de téléchargement en réseau mobile
    And je sélectionne une option de téléchargement en réseau mobile
    Then je vois le texte de téléchargement en réseau mobile mis à jour

  Scenario: Vérification de la fonctionnalité de lecture vidéo
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de lecture vidéo
    And je sélectionne une option de lecture vidéo
    Then je vois le texte de lecture vidéo mis à jour

  Scenario: Vérification de l'impact carbone de la qualité de streaming
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de qualité de streaming
    And je sélectionne une option de qualité de streaming
    Then je vois le texte d'impact carbone de la qualité de streaming mis à jour

  Scenario: Vérification de la fonctionnalité de stockage de téléchargement
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de stockage de téléchargement
    And je sélectionne une option de stockage de téléchargement
    Then je vois le texte de stockage de téléchargement mis à jour

  Scenario: Vérification de la fonctionnalité de validation
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de validation
    Then je vois la page de validation

  Scenario: Vérification de la fonctionnalité de retour en arrière
    Given que je suis sur la page des paramètres
    When je clique sur le bouton de retour en arrière
    Then je vois la page d'accueil de l'application