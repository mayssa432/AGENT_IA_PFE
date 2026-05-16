Feature: Gestion de la page Cast

  Scenario: Vérification de la présence des éléments de la page Cast
    Given que l'utilisateur est sur la page Cast
    When l'utilisateur affiche la liste des appareils
    Then la liste des appareils est affichée
    And le bouton de déconnexion du ChromeCast est affiché
    And le bouton de déconnexion de la STB est affiché
    And le titre de la média est affiché
    And le bouton de réduction est affiché
    And le bouton d'expansion est affiché
    And le titre de l'appareil est affiché
    And la couverture de la média est affichée
    And le logo de la chaîne est affiché
    And l'heure de début est affichée
    And l'heure de fin est affichée
    And la barre de progression est affichée
    And le bouton de lecture/pause est affiché
    And le bouton d'information est affiché
    And le bouton d'enregistrement est affiché
    And le bouton de langues et sous-titres est affiché
    And le bouton de volume est affiché

  Scenario: Sélection d'un appareil et vérification des éléments de contrôle
    Given que l'utilisateur est sur la page Cast
    When l'utilisateur sélectionne un appareil dans la liste
    And l'utilisateur affiche les éléments de contrôle
    Then le bouton de lecture/pause est affiché
    And le bouton de réduction est affiché
    And le bouton d'expansion est affiché
    And le bouton d'enregistrement est affiché
    And le bouton de langues et sous-titres est affiché
    And le bouton de volume est affiché
    And la barre de progression est affichée
    And l'heure de début est affichée
    And l'heure de fin est affichée

  Scenario: Vérification de la fonctionnalité de déconnexion
    Given que l'utilisateur est sur la page Cast
    When l'utilisateur clique sur le bouton de déconnexion du ChromeCast
    Then la déconnexion est effectuée avec succès
    And l'utilisateur est redirigé vers la page de connexion
    When l'utilisateur clique sur le bouton de déconnexion de la STB
    Then la déconnexion est effectuée avec succès
    And l'utilisateur est redirigé vers la page de connexion

  Scenario: Vérification de la fonctionnalité de lecture/pause
    Given que l'utilisateur est sur la page Cast
    When l'utilisateur clique sur le bouton de lecture/pause
    Then la lecture est lancée ou mise en pause avec succès
    And l'état du bouton de lecture/pause est mis à jour

  Scenario: Vérification de la fonctionnalité de réduction et d'expansion
    Given que l'utilisateur est sur la page Cast
    When l'utilisateur clique sur le bouton de réduction
    Then la page est réduite avec succès
    And l'utilisateur peut afficher les éléments de contrôle
    When l'utilisateur clique sur le bouton d'expansion
    Then la page est agrandie avec succès
    And l'utilisateur peut afficher les éléments de contrôle

  Scenario: Vérification de la fonctionnalité de langues et sous-titres
    Given que l'utilisateur est sur la page Cast
    When l'utilisateur clique sur le bouton de langues et sous-titres
    Then la liste des langues et sous-titres est affichée
    And l'utilisateur peut sélectionner une langue ou un sous-titre
    And la sélection est appliquée avec succès

  Scenario: Vérification de la fonctionnalité de volume
    Given que l'utilisateur est sur la page Cast
    When l'utilisateur clique sur le bouton de volume
    Then la barre de volume est affichée
    And l'utilisateur peut ajuster le volume
    And l'ajustement est appliqué avec succès