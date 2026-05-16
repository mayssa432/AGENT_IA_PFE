Feature: Aide et Contact
  En tant qu'utilisateur, je veux pouvoir accéder à la page d'aide et de contact pour obtenir des informations et contacter un conseiller.

  Scenario: Vérifier le titre de la page d'aide
    Given que je suis sur la page d'aide
    When je regarde le titre de la page
    Then je vois le titre "Orange TV"

  Scenario: Vérifier les éléments de la liste d'aide
    Given que je suis sur la page d'aide
    When je regarde la liste d'aide
    Then je vois les éléments suivants :
      | Élément 1 | Élément 2 | Élément 3 | Élément 4 |
      | Chatter avec un conseiller Orange | Du lundi au samedi de 8h à 22h | Posez directement votre question à un conseiller. | Chatter |

  Scenario: Vérifier le fonctionnement du bouton de chat
    Given que je suis sur la page d'aide
    When je clique sur le bouton de chat
    Then je suis redirigé vers la page de chat

  Scenario: Vérifier les titres des FAQs
    Given que je suis sur la page d'aide
    When je regarde les titres des FAQs
    Then je vois les titres suivants :
      | Titre 1 | Titre 2 | Titre 3 |
      | FAQ 1 | FAQ 2 | FAQ 3 |

  Scenario: Vérifier le contenu d'un élément de la liste d'aide
    Given que je suis sur la page d'aide
    When je clique sur l'élément 1 de la liste d'aide
    Then je vois le contenu de l'élément 1

  Scenario: Vérifier le fonctionnement du bouton de chatter
    Given que je suis sur la page d'aide
    When je clique sur le bouton de chatter
    Then je suis redirigé vers la page de chatter

  Scenario: Vérifier les questions des FAQs
    Given que je suis sur la page d'aide
    When je regarde les questions des FAQs
    Then je vois les questions suivantes :
      | Question 1 | Question 2 | Question 3 |
      | Question 1 | Question 2 | Question 3 |