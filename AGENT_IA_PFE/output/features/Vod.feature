Feature: VOD Page
  En tant qu'utilisateur, je veux accéder à la page VOD pour visualiser et gérer mes contenus vidéo.

  Scenario: Accéder à la page VOD
    Given que je suis connecté à l'application
    When je clique sur l'onglet "VOD"
    Then je devrais voir la page VOD avec les éléments suivants :
      | Élément         | Description                   |
      | heroZoneBlock   | Bloc de recommandations      |
      | catalog         | Onglet "Catalogue"             |
      | myVideos        | Onglet "Mes vidéos"           |
      | myList          | Onglet "Ma liste"             |
      | categoryTitle   | Titre de la catégorie        |
      | categoryStrip    | Bande de catégorie            |
      | itemImage       | Image de l'élément             |
      | itemPrimaryText | Texte principal de l'élément  |
      | itemSecondaryText | Texte secondaire de l'élément |

  Scenario: Rechercher un contenu vidéo dans le catalogue
    Given que je suis sur la page VOD
    When je clique sur l'onglet "Catalogue"
    And je recherche un contenu vidéo spécifique
    Then je devrais voir les résultats de recherche avec les éléments suivants :
      | Élément         | Description                   |
      | elementTitles   | Titres des éléments           |
      | vodCatalogElementsIOS | Éléments de catalogue iOS |
      | vodCategoryElementsTextIOS | Texte des éléments de catégorie iOS |

  Scenario: Ajouter un contenu vidéo à ma liste
    Given que je suis sur la page VOD
    When je clique sur l'onglet "Catalogue"
    And je sélectionne un contenu vidéo
    And je clique sur le bouton "Ajouter à ma liste"
    Then je devrais voir le contenu vidéo ajouté à ma liste avec les éléments suivants :
      | Élément         | Description                   |
      | myListCategoryTitle | Titre de la catégorie de ma liste |
      | myListElements | Éléments de ma liste          |
      | myListseeMoreButton | Bouton "Voir plus" de ma liste |

  Scenario: Visualiser les détails d'un contenu vidéo
    Given que je suis sur la page VOD
    When je clique sur un contenu vidéo
    Then je devrais voir les détails du contenu vidéo avec les éléments suivants :
      | Élément         | Description                   |
      | unitaryFilm     | Film unitaire                |
      | severalFilm     | Plusieurs films              |
      | itemPrimaryText | Texte principal de l'élément  |
      | itemSecondaryText | Texte secondaire de l'élément |

  Scenario: Gérer les alertes pour un contenu vidéo
    Given que je suis sur la page VOD
    When je clique sur un contenu vidéo
    And je clique sur le bouton "Créer une alerte"
    Then je devrais voir les options d'alerte avec les éléments suivants :
      | Élément         | Description                   |
      | createAlertText | Texte de création d'alerte  |
      | articleVodAlertDot | Dot d'alerte pour l'article |
      | tabbarVodAlertDot | Dot d'alerte pour la barre de tabs |

  Scenario: Confirmer l'ajout d'un contenu vidéo à ma liste
    Given que je suis sur la page VOD
    When je clique sur l'onglet "Catalogue"
    And je sélectionne un contenu vidéo
    And je clique sur le bouton "Ajouter à ma liste"
    Then je devrais voir une confirmation d'ajout avec les éléments suivants :
      | Élément         | Description                   |
      | snackBartText  | Texte de la barre de confirmation |
      | snackBarSuccessIconIOS | Icône de succès de la barre de confirmation |