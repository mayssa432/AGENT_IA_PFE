Feature: Gestion des téléchargements
  En tant qu'utilisateur, je veux pouvoir gérer mes téléchargements pour accéder à mes contenus hors ligne.

  Scenario: Vérification de la page de téléchargements vide
    Given que je suis sur la page de téléchargements
    When la page est chargée
    Then je vois l'icône "noDownload"
    And je vois le texte "offline_myvideos_uitable_view_label"

  Scenario: Vérification de la liste des téléchargements
    Given que je suis sur la page de téléchargements
    And que j'ai des téléchargements en cours
    When la page est chargée
    Then je vois une liste de téléchargements
    And chaque téléchargement a une image
    And chaque téléchargement a un texte
    And chaque téléchargement a un icône de lecture
    And chaque téléchargement a un icône de suppression
    And chaque téléchargement a un indicateur de téléchargement

  Scenario: Vérification du détail d'un téléchargement
    Given que je suis sur la page de téléchargements
    And que j'ai des téléchargements en cours
    When je sélectionne un téléchargement
    Then je vois les détails du téléchargement
    And je vois le texte du téléchargement
    And je vois le sous-texte du téléchargement
    And je vois l'icône de lecture du téléchargement
    And je vois l'icône de suppression du téléchargement
    And je vois l'indicateur de téléchargement du téléchargement

  Scenario: Vérification de la suppression d'un téléchargement
    Given que je suis sur la page de téléchargements
    And que j'ai des téléchargements en cours
    When je sélectionne un téléchargement
    And je clique sur l'icône de suppression
    Then le téléchargement est supprimé de la liste
    And je vois un message de confirmation de suppression

  Scenario: Vérification de la lecture d'un téléchargement
    Given que je suis sur la page de téléchargements
    And que j'ai des téléchargements en cours
    When je sélectionne un téléchargement
    And je clique sur l'icône de lecture
    Then le téléchargement est lancé en lecture
    And je vois le contenu du téléchargement en lecture