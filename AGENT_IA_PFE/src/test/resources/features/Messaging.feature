Feature: Messaging
  En tant qu'utilisateur, je veux pouvoir interagir avec la page de messagerie pour envoyer et recevoir des messages.

  Scenario: Vérifier la présence des éléments de la page de messagerie
    Given que je suis sur la page de messagerie
    Then je vois le titre de la barre d'outils "lpui_toolbar_title"
    And je vois l'avatar de l'agent "lpui_toolbar_agent_avatar"
    And je vois le bouton de navigation "Revenir en haut de la page"
    And je vois le bouton de menu "Plus d'options"
    And je vois la liste des éléments d'options "content"

  Scenario: Envoyer un message
    Given que je suis sur la page de messagerie
    When je tape un message dans le champ de texte "lpui_enter_message_text"
    And je clique sur le bouton d'envoi "lpui_enter_message_send"
    Then je vois le message envoyé dans la liste des messages "lpui_message_text"

  Scenario: Répondre à un message avec un bouton de réponse rapide
    Given que je suis sur la page de messagerie
    And je vois un message avec un bouton de réponse rapide "QuickReplyTableViewCellQuickReplyContainerView0"
    When je clique sur le bouton de réponse rapide
    And je tape un message dans le champ de texte "lpui_enter_message_text"
    And je clique sur le bouton d'envoi "lpui_enter_message_send"
    Then je vois le message envoyé dans la liste des messages "lpui_message_text"

  Scenario: Fermer la page de messagerie
    Given que je suis sur la page de messagerie
    When je clique sur le bouton de navigation "Revenir en haut de la page"
    Then je ne vois plus la page de messagerie

  Scenario: Vérifier la présence des éléments de la page de feedback
    Given que je suis sur la page de messagerie
    And je clique sur le bouton de menu "Plus d'options"
    And je sélectionne l'option "Feedback"
    Then je vois le bouton de skip de feedback "CustomerSatisfactionSkipButton"
    And je vois l'avatar de feedback "CustomerSatisfactionAgentAvatarImageView"
    And je vois le bouton de soumission de feedback "CustomerSatisfactionSubmitButton"