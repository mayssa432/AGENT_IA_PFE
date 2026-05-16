Feature: EPG (Electronic Program Guide)
  Description: Cette fonctionnalité permet aux utilisateurs de consulter les programmes télévisés à venir.

  Scenario: Vérification de la présence des éléments de la page EPG
    Given que l'utilisateur est sur la page EPG
    When l'utilisateur consulte la liste des chaînes
    Then les éléments suivants sont affichés :
      | Élément         | Description                 |
      | channelLists    | Liste des chaînes           |
      | channelPrograms  | Liste des programmes        |
      | heroZoneEPG     | Zone héro de la page EPG    |
      | tabBar          | Barre de tabulation         |
      | channelLogo     | Logo de la chaîne           |
      | channelNumber   | Numéro de la chaîne         |
      | genreTitle      | Titre du genre              |
      | programPlayButton| Bouton de lecture du programme|
      | programThumbnail | Image miniature du programme|
      | programProgressBar| Barre de progression du programme|

  Scenario: Vérification de la lecture d'un programme en direct
    Given que l'utilisateur est sur la page EPG
    When l'utilisateur sélectionne un programme en direct
    And l'utilisateur clique sur le bouton de lecture
    Then le programme est lancé en lecture

  Scenario: Vérification de l'accès aux informations d'un programme
    Given que l'utilisateur est sur la page EPG
    When l'utilisateur sélectionne un programme
    And l'utilisateur clique sur le bouton d'informations
    Then les informations suivantes sont affichées :
      | Informations    | Description                 |
      | programTime      | Heure de diffusion du programme|
      | programTitle     | Titre du programme           |
      | programGenre    | Genre du programme           |

  Scenario: Vérification de la navigation entre les chaînes et les programmes
    Given que l'utilisateur est sur la page EPG
    When l'utilisateur navigue entre les chaînes
    And l'utilisateur sélectionne un programme
    Then les informations du programme sont affichées

  Scenario: Vérification de la recherche d'un programme
    Given que l'utilisateur est sur la page EPG
    When l'utilisateur recherche un programme
    And l'utilisateur sélectionne le programme recherché
    Then les informations du programme sont affichées

  Scenario: Vérification de la vérification de la présence des éléments de la page EPG sur différents appareils
    Given que l'utilisateur est sur la page EPG sur un appareil Android
    When l'utilisateur consulte la liste des chaînes
    Then les éléments suivants sont affichés :
      | Élément         | Description                 |
      | channelLists    | Liste des chaînes           |
      | channelPrograms  | Liste des programmes        |
      | heroZoneEPG     | Zone héro de la page EPG    |
      | tabBar          | Barre de tabulation         |
      | channelLogo     | Logo de la chaîne           |
      | channelNumber   | Numéro de la chaîne         |
      | genreTitle      | Titre du genre              |
      | programPlayButton| Bouton de lecture du programme|
      | programThumbnail | Image miniature du programme|
      | programProgressBar| Barre de progression du programme|
    And que l'utilisateur est sur la page EPG sur un appareil iOS
    When l'utilisateur consulte la liste des chaînes
    Then les éléments suivants sont affichés :
      | Élément         | Description                 |
      | channelLists    | Liste des chaînes           |
      | channelPrograms  | Liste des programmes        |
      | heroZoneEPG     | Zone héro de la page EPG    |
      | tabBar          | Barre de tabulation         |
      | channelLogo     | Logo de la chaîne           |
      | channelNumber   | Numéro de la chaîne         |
      | genreTitle      | Titre du genre              |
      | programPlayButton| Bouton de lecture du programme|
      | programThumbnail | Image miniature du programme|
      | programProgressBar| Barre de progression du programme|