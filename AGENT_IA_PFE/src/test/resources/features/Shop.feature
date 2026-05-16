Feature: Shop Page
  Description: La page Shop permet aux utilisateurs de parcourir les offres et de s'abonner à des canaux.

  Scenario: Vérification de la présence des offres sur la page Shop
    Given que l'utilisateur est sur la page Shop
    When l'utilisateur parcourt les offres disponibles
    Then les offres sont affichées avec leurs images et leurs catégories
    And les offres sont classées par catégorie

  Scenario: Vérification de la fonctionnalité de s'abonnement à une offre
    Given que l'utilisateur est sur la page Shop
    When l'utilisateur sélectionne une offre et clique sur le bouton "S'ABONNER"
    Then l'utilisateur est redirigé vers la page de détails de l'offre
    And les détails de l'offre sont affichés, y compris le nom, le prix et les canaux disponibles
    And le bouton "S'ABONNER" est présent et fonctionnel

  Scenario: Vérification de la gestion des erreurs sur la page Shop
    Given que l'utilisateur est sur la page Shop
    When une erreur se produit lors du chargement des offres
    Then un message d'erreur est affiché à l'utilisateur
    And le message d'erreur est clair et concis
    And l'utilisateur peut réessayer de charger les offres

  Scenario: Vérification de la fonctionnalité de visualisation des canaux disponibles pour une offre
    Given que l'utilisateur est sur la page Shop
    When l'utilisateur sélectionne une offre et clique sur le lien "Voir tous les canaux"
    Then la liste des canaux disponibles pour l'offre est affichée
    And les canaux sont classés par ordre alphabétique
    And l'utilisateur peut revenir à la page précédente

  Scenario: Vérification de la fonctionnalité de visualisation des détails d'une offre
    Given que l'utilisateur est sur la page Shop
    When l'utilisateur sélectionne une offre et clique sur le bouton "Détails"
    Then les détails de l'offre sont affichés, y compris le nom, le prix et les canaux disponibles
    And les détails de l'offre sont clairs et concis
    And l'utilisateur peut revenir à la page précédente