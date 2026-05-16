Feature: Remote Control
  En tant qu'utilisateur, je veux utiliser la télécommande pour contrôler mon appareil

  Scenario: Afficher la télécommande
    Given que je suis sur la page d'accueil
    When je clique sur le bouton de télécommande
    Then la télécommande est affichée
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible

  Scenario: Sélectionner un appareil
    Given que je suis sur la page de télécommande
    When je clique sur le menu déroulant de sélection de l'appareil
    And je sélectionne un appareil "Appareil 1"
    Then l'appareil "Appareil 1" est sélectionné
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible

  Scenario: Utiliser les boutons de navigation
    Given que je suis sur la page de télécommande
    When je clique sur le bouton de navigation "haut"
    Then la page de télécommande est mise à jour
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible
    When je clique sur le bouton de navigation "bas"
    Then la page de télécommande est mise à jour
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible

  Scenario: Utiliser les boutons de volume
    Given que je suis sur la page de télécommande
    When je clique sur le bouton de volume "augmenter"
    Then le volume est augmenté
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible
    When je clique sur le bouton de volume "diminuer"
    Then le volume est diminué
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible

  Scenario: Utiliser les boutons de numérotation
    Given que je suis sur la page de télécommande
    When je clique sur le bouton de numérotation "0"
    Then le numéro "0" est saisi
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible
    When je clique sur le bouton de numérotation "1"
    Then le numéro "1" est saisi
    And le bouton de retour est visible
    And le menu déroulant de sélection de l'appareil est visible
    And le bouton d'alimentation est visible
    And les boutons de navigation (haut, bas, gauche, droite) sont visibles
    And le bouton OK est visible
    And le bouton de réversion est visible
    And le bouton de menu est visible