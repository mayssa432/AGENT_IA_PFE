Feature: Gestion du compte
  Description: Cette fonctionnalité permet à l'utilisateur de gérer son compte

  Scenario: Connexion au compte
    Given que l'utilisateur est sur la page de connexion
    When l'utilisateur clique sur le bouton "Identify"
    Then le système affiche les détails du compte

  Scenario: Déconnexion du compte
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur clique sur le bouton "Déconnexion"
    Then le système déconnecte l'utilisateur et affiche la page de connexion

  Scenario: Affichage des détails du compte
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur clique sur le bouton "Détails du compte"
    Then le système affiche les détails du compte, y compris les informations de service et les offres

  Scenario: Gestion des abonnements TV
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur clique sur le bouton "Gérer mes abonnements TV"
    Then le système affiche la page de gestion des abonnements TV

  Scenario: Vérification des informations d'identification
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur vérifie les informations d'identification
    Then le système affiche les informations d'identification correctes

  Scenario: Vérification des erreurs de connexion
    Given que l'utilisateur est sur la page de connexion
    When l'utilisateur entre des informations de connexion incorrectes
    Then le système affiche un message d'erreur de connexion

  Scenario: Vérification des détails de l'offre
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur vérifie les détails de l'offre
    Then le système affiche les détails de l'offre, y compris les informations de service et les offres

  Scenario: Vérification des détails de la souscription
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur vérifie les détails de la souscription
    Then le système affiche les détails de la souscription, y compris les informations de service et les offres

  Scenario: Vérification des détails de l'inclusion
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur vérifie les détails de l'inclusion
    Then le système affiche les détails de l'inclusion, y compris les informations de service et les offres

  Scenario: Vérification des détails des offres
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur vérifie les détails des offres
    Then le système affiche les détails des offres, y compris les informations de service et les offres

  Scenario: Vérification des détails de la page de gestion des abonnements TV
    Given que l'utilisateur est connecté à son compte
    When l'utilisateur clique sur le bouton "Gérer mes abonnements TV"
    Then le système affiche la page de gestion des abonnements TV avec les détails des abonnements TV.