# Generation automatique - Login functionality
**Date:** 2026-05-02 20:55:04

## Fichiers generes

- `src\test\resources\features\LoginFunctionality.feature`
- `src\test\java\steps\LoginStepDefinitions.java`
- `src\test\java\pages\LoginPage.java`
- `src\test\java\pages\BasePage.java`
- `src\test\java\runners\LoginTestRunner.java`

## Structure du projet

```
output/
└── src/
    └── test/
        ├── java/
        │   ├── pages/          <- Page Objects (POM)
        │   ├── steps/          <- Step Definitions Cucumber
        │   └── runners/        <- Test Runners JUnit
        └── resources/
            └── features/       <- Fichiers .feature
```

## Prerequis Maven (pom.xml)

```xml
<dependencies>
  <!-- Selenium -->
  <dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>4.18.1</version>
  </dependency>
  <!-- Cucumber -->
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>7.15.0</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-junit-platform-engine</artifactId>
    <version>7.15.0</version>
    <scope>test</scope>
  </dependency>
  <!-- JUnit 5 -->
  <dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
  </dependency>
  <!-- WebDriverManager -->
  <dependency>
    <groupId>io.github.bonigarcia</groupId>
    <artifactId>webdrivermanager</artifactId>
    <version>5.7.0</version>
    <scope>test</scope>
  </dependency>
</dependencies>
```
