Feature: Recherche de programmes sur l'application mobile

  Scenario: Recherche de programmes avec un terme de recherche valide
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "le" dans la barre de recherche
    And L'utilisateur clique sur le bouton de recherche
    Then La liste des résultats de recherche est affichée
    And La vue des résultats de recherche contient des éléments de recherche

  Scenario: Recherche de programmes avec un terme de recherche vide
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur clique sur le bouton de recherche sans saisir de terme de recherche
    Then Un message d'erreur est affiché pour indiquer que le terme de recherche est vide

  Scenario: Sélection d'une catégorie de recherche
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "le" dans la barre de recherche
    And L'utilisateur clique sur le bouton de recherche
    And L'utilisateur sélectionne la catégorie "Films"
    Then La liste des résultats de recherche affiche uniquement des films

  Scenario: Affichage des détails d'un programme
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "le" dans la barre de recherche
    And L'utilisateur clique sur le bouton de recherche
    And L'utilisateur sélectionne un programme dans la liste des résultats de recherche
    Then Les détails du programme sont affichés, notamment le titre, la durée et la note

  Scenario: Recherche de programmes avec un terme de recherche qui ne donne pas de résultats
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "azerty" dans la barre de recherche
    And L'utilisateur clique sur le bouton de recherche
    Then Un message est affiché pour indiquer que aucun résultat n'a été trouvé

  Scenario: Utilisation du bouton "Effacer le texte" pour vider la barre de recherche
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "le" dans la barre de recherche
    And L'utilisateur clique sur le bouton "Effacer le texte"
    Then La barre de recherche est vidée

  Scenario: Utilisation du bouton "Voir en replay" pour accéder à un programme en replay
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "le" dans la barre de recherche
    And L'utilisateur clique sur le bouton de recherche
    And L'utilisateur sélectionne un programme dans la liste des résultats de recherche
    And L'utilisateur clique sur le bouton "Voir en replay"
    Then Le programme est lancé en replay

  Scenario: Utilisation du bouton "Voir en VOD" pour accéder à un programme en VOD
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "le" dans la barre de recherche
    And L'utilisateur clique sur le bouton de recherche
    And L'utilisateur sélectionne un programme dans la liste des résultats de recherche
    And L'utilisateur clique sur le bouton "Voir en VOD"
    Then Le programme est lancé en VOD

  Scenario: Utilisation du bouton "Voir les épisodes" pour accéder à la liste des épisodes d'un programme
    Given L'utilisateur est sur la page d'accueil de l'application
    When L'utilisateur saisit le terme de recherche "le" dans la barre de recherche
    And L'utilisateur clique sur le bouton de recherche
    And L'utilisateur sélectionne un programme dans la liste des résultats de recherche
    And L'utilisateur clique sur le bouton "Voir les épisodes"
    Then La liste des épisodes du programme est affichée