Feature: Gestion des enregistrements
  En tant qu'utilisateur, je veux pouvoir gérer mes enregistrements pour accéder à mes programmes préférés.

  Scenario: Afficher la liste des enregistrements
    Given que l'utilisateur est sur la page d'accueil
    When l'utilisateur clique sur le bouton "Enregistrements"
    Then la liste des enregistrements est affichée
    And le bouton "Enregistrer" est visible
    And le bouton "Programmer" est visible

  Scenario: Enregistrer un programme
    Given que l'utilisateur est sur la page d'enregistrement
    When l'utilisateur sélectionne un programme à enregistrer
    And l'utilisateur clique sur le bouton "Enregistrer"
    Then le programme est enregistré avec succès
    And un message de confirmation est affiché

  Scenario: Programmer un enregistrement
    Given que l'utilisateur est sur la page de programmation
    When l'utilisateur sélectionne un programme à programmer
    And l'utilisateur clique sur le bouton "Programmer"
    Then le programme est programmé avec succès
    And un message de confirmation est affiché

  Scenario: Supprimer un enregistrement
    Given que l'utilisateur est sur la page d'enregistrements
    When l'utilisateur sélectionne un enregistrement à supprimer
    And l'utilisateur clique sur le bouton "Supprimer"
    Then l'enregistrement est supprimé avec succès
    And un message de confirmation est affiché

  Scenario: Afficher les détails d'un enregistrement
    Given que l'utilisateur est sur la page d'enregistrements
    When l'utilisateur clique sur un enregistrement
    Then les détails de l'enregistrement sont affichés
    And le titre de l'enregistrement est visible
    And la description de l'enregistrement est visible

  Scenario: Modifier un enregistrement
    Given que l'utilisateur est sur la page d'enregistrements
    When l'utilisateur sélectionne un enregistrement à modifier
    And l'utilisateur clique sur le bouton "Modifier"
    Then la page de modification de l'enregistrement est affichée
    And les champs de modification sont visibles
    And l'utilisateur peut modifier les détails de l'enregistrement

  Scenario: Enregistrer un programme avec une date et une heure spécifiques
    Given que l'utilisateur est sur la page d'enregistrement
    When l'utilisateur sélectionne un programme à enregistrer
    And l'utilisateur sélectionne une date et une heure spécifiques
    And l'utilisateur clique sur le bouton "Enregistrer"
    Then le programme est enregistré avec la date et l'heure spécifiques
    And un message de confirmation est affiché

  Scenario: Programmer un enregistrement avec une date et une heure spécifiques
    Given que l'utilisateur est sur la page de programmation
    When l'utilisateur sélectionne un programme à programmer
    And l'utilisateur sélectionne une date et une heure spécifiques
    And l'utilisateur clique sur le bouton "Programmer"
    Then le programme est programmé avec la date et l'heure spécifiques
    And un message de confirmation est affiché