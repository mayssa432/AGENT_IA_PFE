Feature: FipLive

  Scenario: Vérification de la présence des éléments sur la page FipLive
    Given que l'utilisateur est sur la page FipLive
    When l'utilisateur affiche la page
    Then les éléments suivants sont présents :
      And le titre de la page FipLive est affiché
      And le bouton de lecture est affiché
      And le bouton de redémarrage est affiché
      And le bouton de rappel est affiché
      And le bouton d'enregistrement est affiché
      And la liste des acteurs est affichée
      And la description du programme est affichée
      And la barre de progression est affichée

  Scenario: Vérification de la lecture d'un programme sur la page FipLive
    Given que l'utilisateur est sur la page FipLive
    When l'utilisateur clique sur le bouton de lecture
    Then le programme commence à être lu
    And la barre de progression commence à avancer
    And le bouton de lecture est remplacé par le bouton de pause

  Scenario: Vérification de l'enregistrement d'un programme sur la page FipLive
    Given que l'utilisateur est sur la page FipLive
    When l'utilisateur clique sur le bouton d'enregistrement
    Then le programme est enregistré
    And un message de confirmation d'enregistrement est affiché
    And le bouton d'enregistrement est remplacé par le bouton de modification de l'enregistrement

  Scenario: Vérification de la suppression d'un enregistrement sur la page FipLive
    Given que l'utilisateur est sur la page FipLive
    When l'utilisateur clique sur le bouton de suppression de l'enregistrement
    Then l'enregistrement est supprimé
    And un message de confirmation de suppression est affiché
    And le bouton de suppression de l'enregistrement n'est plus affiché

  Scenario: Vérification de la modification de l'enregistrement sur la page FipLive
    Given que l'utilisateur est sur la page FipLive
    When l'utilisateur clique sur le bouton de modification de l'enregistrement
    Then une page de modification de l'enregistrement est affichée
    And l'utilisateur peut modifier les paramètres de l'enregistrement
    And le bouton de modification de l'enregistrement est remplacé par le bouton d'enregistrement

  Scenario: Vérification de la présence des pictogrammes sur la page FipLive
    Given que l'utilisateur est sur la page FipLive
    When l'utilisateur affiche la page
    Then les pictogrammes suivants sont présents :
      And le pictogramme de genre est affiché
      And le pictogramme de durée est affiché
      And le pictogramme de pays est affiché

  Scenario: Vérification de la présence du bouton d'abonnement sur la page FipLive
    Given que l'utilisateur est sur la page FipLive
    When l'utilisateur affiche la page
    Then le bouton d'abonnement est affiché
    And l'utilisateur peut cliquer sur le bouton d'abonnement pour s'abonner au programme