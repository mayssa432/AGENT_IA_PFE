Feature: Page About
  Description: La page About affiche les informations relatives à l'application

  Scenario: Afficher les informations de base de l'application
    Given L'utilisateur est sur la page About
    When L'utilisateur affiche les informations de base
    Then Les éléments suivants sont affichés :
      And Le logo Orange est visible
      And Le nom de l'application "Orange TV" est visible
      And Le numéro de version est visible
      And Le texte "about" est visible

  Scenario: Afficher les déclarations d'accessibilité
    Given L'utilisateur est sur la page About
    When L'utilisateur clique sur l'élément "Déclarations d'accessibilité"
    Then Les éléments suivants sont affichés :
      And Le titre "Déclarations d'accessibilité" est visible
      And La barre de progression est visible
      And Le détail du résultat est visible
      And La date est visible
      And Le déclarant est visible
      And Le référentiel est visible
      And La technologie est visible
      And Le bouton "Voir plus" est visible

  Scenario: Afficher les mentions légales
    Given L'utilisateur est sur la page About
    When L'utilisateur clique sur l'élément "Mentions légales"
    Then Les éléments suivants sont affichés :
      And Le logo Orange est visible
      And Le nom de l'application "Orange TV" est visible
      And Le numéro de version est visible
      And Le texte "about" est visible

  Scenario: Vérifier la présence des éléments de la page About
    Given L'utilisateur est sur la page About
    When L'utilisateur affiche les éléments de la page
    Then Les éléments suivants sont présents :
      And La liste des éléments est non vide
      And Le logo Orange est présent
      And Le nom de l'application "Orange TV" est présent
      And Le numéro de version est présent
      And Le texte "about" est présent

  Scenario: Vérifier la navigation entre les éléments de la page About
    Given L'utilisateur est sur la page About
    When L'utilisateur clique sur l'élément "1"
    Then L'élément "1" est sélectionné
    When L'utilisateur clique sur l'élément "2"
    Then L'élément "2" est sélectionné
    When L'utilisateur clique sur l'élément "3"
    Then L'élément "3" est sélectionné