# -*- coding: utf-8 -*-
"""
File Writer - Sauvegarde les fichiers Java generes sur le disque
"""

import os


class JavaFileWriter:
    """
    Ecrit les fichiers Java generes dans le repertoire de sortie.
    """

    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def write_all(self, generated: dict) -> list[str]:
        """
        Ecrit tous les fichiers generes et retourne la liste des chemins crees.

        Args:
            generated: dict retourne par l'agent IA

        Returns:
            list[str]: chemins des fichiers crees
        """
        written_files = []

        for key, file_info in generated.items():
            if not isinstance(file_info, dict):
                continue
            filename = file_info.get("filename")
            content  = file_info.get("content")

            if not filename or not content:
                print(f"[WRITER] IGNORE Fichier '{key}' (filename ou content manquant)")
                continue

            # Construire le chemin complet
            full_path = os.path.join(self.output_dir, filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

            written_files.append(full_path)
            print(f"[WRITER] OK Fichier cree : {full_path}")

        return written_files

    def write_summary(self, written_files: list[str], feature_name: str):
        """Ecrit un fichier README de resume."""
        summary_path = os.path.join(self.output_dir, "GENERATION_SUMMARY.md")
        lines = [
            f"# Generation automatique - {feature_name}\n",
            f"**Date:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n",
            "## Fichiers generes\n\n",
        ]
        for f in written_files:
            rel = os.path.relpath(f, self.output_dir)
            lines.append(f"- `{rel}`\n")

        lines += [
            "\n## Structure du projet\n\n",
            "```\n",
            "output/\n",
            "└── src/\n",
            "    └── test/\n",
            "        ├── java/\n",
            "        │   ├── com/\n",
            "        │   │   └── orange/\n",
            "        │   │       └── otvp/\n",
            "        │   │           └── automation/\n",
            "        │   │               └── pages/\n",
            "        │   │                   └── mobile/        <- Page Objects (POM)\n",                              
            "        │   ├── steps/          <- Step Definitions Cucumber\n",
            "        │   └── runners/        <- Test Runners JUnit\n",
            "        └── resources/\n",
            "            └── features/       <- Fichiers .feature\n",
            "```\n",
            "\n## Prerequis Maven (pom.xml)\n\n",
            "```xml\n",
            "<dependencies>\n",
            "  <!-- Selenium -->\n",
            "  <dependency>\n",
            "    <groupId>org.seleniumhq.selenium</groupId>\n",
            "    <artifactId>selenium-java</artifactId>\n",
            "    <version>4.18.1</version>\n",
            "  </dependency>\n",
            "  <!-- Cucumber -->\n",
            "  <dependency>\n",
            "    <groupId>io.cucumber</groupId>\n",
            "    <artifactId>cucumber-java</artifactId>\n",
            "    <version>7.15.0</version>\n",
            "    <scope>test</scope>\n",
            "  </dependency>\n",
            "  <dependency>\n",
            "    <groupId>io.cucumber</groupId>\n",
            "    <artifactId>cucumber-junit-platform-engine</artifactId>\n",
            "    <version>7.15.0</version>\n",
            "    <scope>test</scope>\n",
            "  </dependency>\n",
            "  <!-- JUnit 5 -->\n",
            "  <dependency>\n",
            "    <groupId>org.junit.jupiter</groupId>\n",
            "    <artifactId>junit-jupiter</artifactId>\n",
            "    <version>5.10.2</version>\n",
            "    <scope>test</scope>\n",
            "  </dependency>\n",
            "  <!-- WebDriverManager -->\n",
            "  <dependency>\n",
            "    <groupId>io.github.bonigarcia</groupId>\n",
            "    <artifactId>webdrivermanager</artifactId>\n",
            "    <version>5.7.0</version>\n",
            "    <scope>test</scope>\n",
            "  </dependency>\n",
            "</dependencies>\n",
            "```\n",
        ]

        with open(summary_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        print(f"[WRITER] Resume cree : {summary_path}")
