Feature: Player Overlay
  En tant qu'utilisateur, je veux interagir avec le player overlay pour contrôler la lecture de vidéos.

  Scenario: Afficher les informations de la vidéo
    Given que je suis sur la page de lecture de vidéo
    When je clique sur le bouton "Info" dans le player overlay
    Then je vois les informations de la vidéo, notamment le titre, le genre et la description

  Scenario: Changer la qualité de la vidéo
    Given que je suis sur la page de lecture de vidéo
    When je clique sur le bouton "Qualité" dans le player overlay
    And je sélectionne une qualité de vidéo différente
    Then la qualité de la vidéo est mise à jour

  Scenario: Gérer les langues audio et sous-titres
    Given que je suis sur la page de lecture de vidéo
    When je clique sur le bouton "Langues" dans le player overlay
    And je sélectionne une langue audio différente
    And je sélectionne un sous-titre différent
    Then la langue audio et le sous-titre sont mis à jour

  Scenario: Gérer la lecture de la vidéo
    Given que je suis sur la page de lecture de vidéo
    When je clique sur le bouton "Lecture/Pause" dans le player overlay
    Then la lecture de la vidéo est mise en pause ou reprise

  Scenario: Gérer les erreurs de lecture
    Given que je suis sur la page de lecture de vidéo
    When une erreur de lecture se produit
    Then je vois un message d'erreur avec un bouton "Réessayer"
    When je clique sur le bouton "Réessayer"
    Then la lecture de la vidéo est reprise

  Scenario: Afficher le carrousel de vidéos
    Given que je suis sur la page de lecture de vidéo
    When je clique sur le bouton "Carrousel" dans le player overlay
    Then je vois le carrousel de vidéos

  Scenario: Gérer la mise en plein écran
    Given que je suis sur la page de lecture de vidéo
    When je clique sur le bouton "Plein écran" dans le player overlay
    Then la vidéo est affichée en plein écran

  Scenario: Gérer la navigation dans le carrousel de vidéos
    Given que je suis sur la page de lecture de vidéo
    When je clique sur le bouton "Carrousel" dans le player overlay
    And je navigue dans le carrousel de vidéos
    Then je vois les différentes vidéos du carrousel

  Scenario: Gérer les publicités
    Given que je suis sur la page de lecture de vidéo
    When une publicité est affichée
    Then je vois la publicité avec un lien pour la visiter
    When je clique sur le lien de la publicité
    Then je suis redirigé vers la page de la publicité