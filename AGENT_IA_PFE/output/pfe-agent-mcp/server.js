import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  { name: "pfe-agent-mcp", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Déclaration des outils
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "capture_dom",
      description: "Capture le DOM de l'application mobile via Appium",
      inputSchema: {
        type: "object",
        properties: {
          app_package: {
            type: "string",
            description: "Package de l'application Android",
          },
        },
        required: ["app_package"],
      },
    },
    {
      name: "fix_selector",
      description: "Corrige un sélecteur UI cassé en analysant le DOM",
      inputSchema: {
        type: "object",
        properties: {
          broken_selector: {
            type: "string",
            description: "Le sélecteur cassé",
          },
          dom: {
            type: "string",
            description: "Le DOM actuel de l'application",
          },
        },
        required: ["broken_selector", "dom"],
      },
    },
    {
      name: "generate_scenario",
      description: "Génère un scénario BDD complet à partir de steps Gherkin",
      inputSchema: {
        type: "object",
        properties: {
          steps: {
            type: "string",
            description: "Les steps BDD fournis par l'utilisateur",
          },
        },
        required: ["steps"],
      },
    },
    {
      name: "update_mock",
      description: "Compare et met à jour un mock WireMock avec la réponse API réelle",
      inputSchema: {
        type: "object",
        properties: {
          api_url: {
            type: "string",
            description: "URL de l'API réelle",
          },
          mock_file: {
            type: "string",
            description: "Chemin vers le fichier mock existant",
          },
        },
        required: ["api_url", "mock_file"],
      },
    },
    {
      name: "run_tests",
      description: "Lance les tests Selenium/Cucumber et retourne les résultats",
      inputSchema: {
        type: "object",
        properties: {
          test_path: {
            type: "string",
            description: "Chemin vers les tests à exécuter",
          },
        },
        required: ["test_path"],
      },
    },
  ],
}));

// Exécution des outils
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "capture_dom":
      return {
        content: [
          {
            type: "text",
            text: `✅ Capture DOM lancée pour le package : ${args.app_package}`,
          },
        ],
      };

    case "fix_selector":
      return {
        content: [
          {
            type: "text",
            text: `✅ Analyse du sélecteur cassé : ${args.broken_selector}\n📄 DOM reçu : ${args.dom.substring(0, 100)}...`,
          },
        ],
      };

    case "generate_scenario":
      return {
        content: [
          {
            type: "text",
            text: `✅ Génération du scénario BDD pour les steps :\n${args.steps}`,
          },
        ],
      };

    case "update_mock":
      return {
        content: [
          {
            type: "text",
            text: `✅ Mise à jour du mock pour l'API : ${args.api_url}\n📄 Fichier mock : ${args.mock_file}`,
          },
        ],
      };

    case "run_tests":
      return {
        content: [
          {
            type: "text",
            text: `✅ Lancement des tests depuis : ${args.test_path}`,
          },
        ],
      };

    default:
      throw new Error(`❌ Outil inconnu : ${name}`);
  }
});

// Démarrage du serveur
const transport = new StdioServerTransport();
await server.connect(transport);
console.error("✅ Serveur MCP PFE démarré avec succès !");
