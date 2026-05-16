Feature: Authentification
  En tant qu'utilisateur, je veux pouvoir m'authentifier pour accéder à l'application

  Scenario: Authentification réussie
    Given que je suis sur la page d'authentification
    When je saisis un nom d'utilisateur valide
    And je saisis un mot de passe valide
    And je clique sur le bouton "Se connecter"
    Then je devrais être connecté avec succès

  Scenario: Authentification échouée - nom d'utilisateur invalide
    Given que je suis sur la page d'authentification
    When je saisis un nom d'utilisateur invalide
    And je saisis un mot de passe valide
    And je clique sur le bouton "Se connecter"
    Then je devrais voir un message d'erreur "Nom d'utilisateur invalide"

  Scenario: Authentification échouée - mot de passe invalide
    Given que je suis sur la page d'authentification
    When je saisis un nom d'utilisateur valide
    And je saisis un mot de passe invalide
    And je clique sur le bouton "Se connecter"
    Then je devrais voir un message d'erreur "Mot de passe invalide"

  Scenario: Authentification avec rappel de mot de passe
    Given que je suis sur la page d'authentification
    When je clique sur le bouton "Mot de passe oublié"
    And je saisis mon adresse e-mail
    And je clique sur le bouton "Réinitialiser le mot de passe"
    Then je devrais recevoir un e-mail de réinitialisation de mot de passe

  Scenario: Authentification avec compte autre
    Given que je suis sur la page d'authentification
    When je clique sur le bouton "Compte autre"
    And je saisis mon nom d'utilisateur et mon mot de passe
    And je clique sur le bouton "Se connecter"
    Then je devrais être connecté avec succès

  Scenario: Authentification avec gestion des droits TV
    Given que je suis sur la page d'authentification
    When je clique sur le bouton "Gérer les droits TV"
    And je sélectionne mon fournisseur de services TV
    And je clique sur le bouton "Continuer"
    Then je devrais être en mesure de gérer mes droits TV

  Scenario: Authentification avec erreur de droits TV
    Given que je suis sur la page d'authentification
    When je clique sur le bouton "Gérer les droits TV"
    And je sélectionne un fournisseur de services TV non autorisé
    And je clique sur le bouton "Continuer"
    Then je devrais voir un message d'erreur "Droits TV non autorisés"