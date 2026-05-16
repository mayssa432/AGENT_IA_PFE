Feature: FipVod Page
  En tant qu'utilisateur, je veux accéder à la page FipVod pour visualiser les détails d'un programme.

  Scenario: Vérification de la présence des éléments de la page FipVod
    Given que je suis sur la page FipVod
    When je vérifie la présence des éléments de la page
    Then je vois l'image de la vidéo "bigThumbnail"
    And je vois le bouton de marque-page "bookmarkButton"
    And je vois le titre du programme "programTitle"
    And je vois le bouton de lecture "playButton"
    And je vois le bouton de téléchargement "downloadButton"

  Scenario: Vérification de la fonctionnalité de lecture
    Given que je suis sur la page FipVod
    When je clique sur le bouton de lecture "playButton"
    Then je vois la vidéo en cours de lecture

  Scenario: Vérification de la fonctionnalité de téléchargement
    Given que je suis sur la page FipVod
    When je clique sur le bouton de téléchargement "downloadButton"
    Then je vois l'indicateur de téléchargement "downloadIndicator"
    And je vois le bouton de suppression du téléchargement "setDeleteAlertButton"

  Scenario: Vérification de la fonctionnalité de création d'alerte
    Given que je suis sur la page FipVod
    When je clique sur le bouton de création d'alerte "setCreateAlertButton"
    Then je vois le bouton de suppression d'alerte "deleteAlertButton"

  Scenario: Vérification de la fonctionnalité d'affichage des détails du programme
    Given que je suis sur la page FipVod
    When je clique sur le bouton d'affichage des détails "showMoreButton"
    Then je vois les détails du programme "programGenreYear", "programLanguages", "programActors", "programDescription"

  Scenario: Vérification de la fonctionnalité de notation
    Given que je suis sur la page FipVod
    When je clique sur le bouton de notation "ratingIcon"
    Then je vois les notes et les commentaires "ratingTextsIOS", "ratingStarsIOS"

  Scenario: Vérification de la fonctionnalité de qualité de la vidéo
    Given que je suis sur la page FipVod
    When je clique sur le bouton de qualité SD "qualitySDButtonAndroid"
    Then je vois la vidéo en qualité SD
    When je clique sur le bouton de qualité HD "qualityHDButtonAndroid"
    Then je vois la vidéo en qualité HD

  Scenario: Vérification de la fonctionnalité de location ou d'achat
    Given que je suis sur la page FipVod
    When je clique sur le bouton de location "rentButtonAndroid"
    Then je vois les options de location
    When je clique sur le bouton d'achat "buyButtonAndroid"
    Then je vois les options d'achat

  Scenario: Vérification de la fonctionnalité d'affichage des épisodes
    Given que je suis sur la page FipVod
    When je clique sur le bouton d'affichage des épisodes "episodeListTitle"
    Then je vois la liste des épisodes "seasonEpisodes"

  Scenario: Vérification de la fonctionnalité d'affichage des packs de films
    Given que je suis sur la page FipVod
    When je clique sur le bouton d'affichage des packs de films "packMovies"
    Then je vois la liste des packs de films "packMovies"