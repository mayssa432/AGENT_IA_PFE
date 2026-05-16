Feature: Tutorial Page
  En tant qu'utilisateur, je veux pouvoir naviguer dans la page de tutoriel pour comprendre les fonctionnalités de l'application.

  Scenario: Vérifier la présence des éléments de la page de tutoriel
    Given que je suis sur la page de tutoriel
    When je regarde la page
    Then je vois le header de la liste de découverte
    And je vois la liste des éléments de découverte
    And je vois le header du tutoriel
    And je vois le corps du tutoriel
    And je vois le pied de page du tutoriel

  Scenario: Vérifier la présence des boutons de tutoriel
    Given que je suis sur la page de tutoriel
    When je regarde la page
    Then je vois le bouton "Partager ma TV d'Orange"
    And je vois le bouton "Enregistrer un contenu"
    And je vois le bouton "Caster un contenu"
    And je vois le bouton "Utiliser la télécommande"
    And je vois le bouton "Reprendre du début"

  Scenario: Vérifier la fonctionnalité du bouton "Reprendre du début"
    Given que je suis sur la page de tutoriel
    When je clique sur le bouton "Reprendre du début"
    Then je suis redirigé vers le début du tutoriel

  Scenario: Vérifier la fonctionnalité du bouton "Partager ma TV d'Orange"
    Given que je suis sur la page de tutoriel
    When je clique sur le bouton "Partager ma TV d'Orange"
    Then je suis redirigé vers la page de partage de ma TV d'Orange

  Scenario: Vérifier la fonctionnalité du bouton "Jouer au tutoriel"
    Given que je suis sur la page de tutoriel
    When je clique sur le bouton "Jouer au tutoriel"
    Then je suis redirigé vers le tutoriel

  Scenario: Vérifier la fonctionnalité de fermeture de la vue de tutoriel
    Given que je suis sur la page de tutoriel
    When je clique sur le bouton de fermeture de la vue de tutoriel
    Then la vue de tutoriel est fermée