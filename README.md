# Basisproject

* Mijn GitHub repository voor de API: https://github.com/Mykyta-Garbuzov/basisproject
* Mijn GitHub repository voor de front-end: https://github.com/Mykyta-Garbuzov/mykyta-garbuzov.github.io
* Mijn hosted API link: https://web-mykyta-garbuzov.cloud.okteto.net/	
* Mijn hosted front-end link: https://web-mykyta-garbuzov.cloud.okteto.net/

# INLEIDING
- Voor Basis Project heb ik mijn voorkeur gegeven aan Flask API, samen met SQLAlchemy om de gegevens te behandelen en Swagger voor OpenAPI Specification.
- Ik heb Flask API gekozen omdat ik al eerder ervaring heb gehad met flask python dus de kennis van deze programmeertaal was nog redelijk vers en ik kon het op juiste manier aan het project toe te passen.
- Voor database wordt er SQLAlchemy gekozen omdat de gegevens moesten behoud worden na herstart van applicatie en niet gewoon verdwijnen.
- Tijdens het onderzoek naar OpenAPI, heb ik gezien dat je Flask samen met swagger kan gebruiken en zij creëren samen een methode die Flask app op eindpoint inspecteert -die YALM docstrings met Swagger 2.0 operation-objecten bevatten.
# API
## api.py
![image](https://user-images.githubusercontent.com/71609618/202864387-97947d70-7d9d-4ed3-bd79-322a0bb7d679.png)

App.py is hoofd file van mijn Flask API. In het begin importeren we verschillende modules vanuit flask, os van operation system, config flask_cors voor de behandeling van Cross Origin Resource Sharing (CORS) zodat we de data van de database kunnen halen voor ons front-end en vanuit modellen importeren we database.
Op de lijn 9 biedt de configuratie module de Flask-app met Connexion-flavored voor ons. Dus Flask App wordt niet meer in app.py gemaakt maar verwijst naar config.connex_app.
CORS(app.app) is http header dat de toestemming aan server geeft om andere oorsprong (domein, schema of poort) dan zijn eigen te gebruiken en waaruit een browser het laden van bronnen moeten toestaan.
Bij app.rout wordt er url-route gekoppeld aan home() functie. Deze functie roept Flask render_template functie om home.html te halen vanuit templates directory en sturen naar browser.
De laatste lijn zorgt ervoor dat de server alleen draait als het script vanuit Python-interpreteer wordt uitgevoerd. In het begin was er een port 8000 in plaats van woord PORT maar we gebruiken Docker compose hebben we dat niet meer nodig.
Afgekort draait deze code basis web server en gebruikt home.html als onze template.

## Swagger.yml
Het Swagger-configuratiebestand is een YAML bestande dat onze Open-API definities bevat. Dit bestande bevat alle informatie die nodig is om de server te configureren en om invoerparametervalidatie, uitvoerresponsgegevensvalidatie en URL-eindpuntdefinitie te bieden.
Eerst moeten we vermelden welke versie van OpenAPI wordt gebruikt met sleutel woord “”

![image](https://user-images.githubusercontent.com/71609618/202864421-11693fe3-3e85-4bf2-903a-c9c5cbd8514a.png)
![image](https://user-images.githubusercontent.com/71609618/202864434-fac1aabc-4b2d-4c0c-92d6-2be4171b5e3e.png)
![image](https://user-images.githubusercontent.com/71609618/202864441-94dedbcd-6fec-4048-972c-465c5cabf0a4.png)

Afgekort is swagger.yml een basis script voor onze API. Binnen deze file welke data onze server kan gebruiken en hoe de server op de data moet reageren.

## Database.py.
Zoals api.py beginnen we met import van verschillende modules. Verder worden er vijf diverse python functie aangemaakt. Elke functie heeft unieke naam die swagger.yml gebruikt om te bepalen welke functie te gebruiken.
In het algemeen hebben we een Get functie die volledige overzicht van database geeft, nog een get functie die toont een persoon van database met specifieke achternaam, een POST, een Update en een delete.
![image](https://user-images.githubusercontent.com/71609618/202864505-13789597-5df9-46bf-8711-026d58d442e6.png)
![image](https://user-images.githubusercontent.com/71609618/202864517-fd91c0e0-5e55-4b2e-8454-a18ae9215736.png)

## Config.py
Deze file wordt gebruikt om configuraties van Flask, Connexion, SQLAlchemy, en Marshmallow te creëren en uitvoeren.
Eerste vier lijnen is import van de modules
Basedir – variabel die naar directory verwijst waar programma wordt uitgevoerd
Page 8
Connex – gebruikt basedir om de instatie van de Connexion-app te maken en verwijst naar directory en pad wordt gegeven naar de directory die onze config bestand bevat.
App – creëert variable
Eerste app.config – vertelt SQLAlchemy om SQLite te gebruiken als de database en de bestande met de naam people.db in onze directory
Tweede app.config – schakelt het SQLAlchemy-gebeurtenissysteem uit. Die hebben we niet nodig omdat het veel problemen creëert.
Db - initialiseert SQLAlchemy met behulp van app
Ma - initialiseert Marshmallow en laat het werken met SQLAlchemy elementen die aan de app gekoppeld zijn.
![image](https://user-images.githubusercontent.com/71609618/202864566-039377b8-e82b-43d3-a1da-36463d60d6da.png)

## Models.py
Models bevat SQLAchemy class definities voor onze database. SQLAchemy bevat diverse functies om met database te werken. Een die functie is object-relationele mapper (ORM), het laat ons werken met onze database met behulp van python.
We importeren eerst modules om tijdstip te creëren en onze database. Op derde lijn maken we definitie class die toegang aan ons geeft tot database en tabel. Verder connecteren we class definitie tot onze tabel. De rest binnen deze class bepaalt welk primary key is, wat uniek is en algemeen informatie.
Tweede class zal definiëren hoe de kenmerken van een class worden omgezet naar JSON formaat. Marshmallow zorgt er ook voor dat alle attributen aanwezig zijn en het verwachte gegevenstype bevatten.
Omdat SQLAlchey gegevens retourneert als Python class , kan Connexion deze class instantie niet serialiseren naar JSON format gegevens.
![image](https://user-images.githubusercontent.com/71609618/202864598-d22b6f67-3a69-4f92-b4e7-166c700ee73d.png)
![image](https://user-images.githubusercontent.com/71609618/202864606-60ea8e33-611d-4c1d-8277-8d6ea7d9eb0a.png)

# DOCKER & GITHUB ACTION
## Dockerfile
Met docker built wordt er Docker image gemaakt van onze Flask API.
![image](https://user-images.githubusercontent.com/71609618/202864644-d9457124-6ed6-4d6a-a3ca-8c6a128c1330.png)
Nadat docker image wordt aangemaakt, kunnen we het terugvinden in Dockers desktop
![image](https://user-images.githubusercontent.com/71609618/202864655-495e15f6-226c-4c5e-8f4f-bce728d48d28.png)

## Docker compose
Met behulp van Docker compose up kunnen we net gemaakte image gebruiken om die te deploy.
![image](https://user-images.githubusercontent.com/71609618/202864671-1602a189-f16e-47fd-8c4c-03d63ad08776.png)
![image](https://user-images.githubusercontent.com/71609618/202864679-64aa4c4d-abd2-4e5b-a7f2-377c9c158ebb.png)
Na uitvoeren van docker compose up wordt nieuwe container aangemaakt en we kunnen die terug vinden in docker desktop.
![image](https://user-images.githubusercontent.com/71609618/202864749-2358a118-f825-4a85-92ee-ed3585054072.png)

## Git Action
De code heb ik van de cursus genomen en enige wat ik heb aangepast hoe de credentials worden verifiëren met DockerHub.
![image](https://user-images.githubusercontent.com/71609618/202864759-04b74007-5ffa-4ceb-8f14-e6a40fa56c8a.png)

Run: docker login -u ${{ secrets.DOCKER_USER }} -p ${{ secrets.DOCKER_PASSWORD }} – werkte totaal niet bij me en git hub action kon geen verbinding maken. In plaats van dat hebben ik “with username/passoword” gebruikt om credentials te verifiëren.
Als een resultaat wordt niuewe image aangemaakt en gestuurd naar DockerHub wanneer we git push uitvoeren van ons project.
![image](https://user-images.githubusercontent.com/71609618/202864770-9e7c9f1d-3e87-49ec-b9ac-860a39ad3a11.png)
![image](https://user-images.githubusercontent.com/71609618/202864786-d6be07ea-1659-4954-8263-070ac6629030.png)

# Okteta Cloud 
Op Okteta Cloud wordt onze GitHub repository geüploade en opgestart.
![image](https://user-images.githubusercontent.com/71609618/202864815-d34761af-36c9-4304-8016-0fd054fd65b7.png)

Enige probleem dat als er niks binnen 24 uren zal gebeuren, zet Okteta Cloud applicatie in “sleeping mode”
![image](https://user-images.githubusercontent.com/71609618/202864821-d0946272-9917-4258-a0aa-ca2dee82b029.png)

# Front-End
Front-End wordt aangemaakt op bassi van Alpine js. Hieronder worden de stukjes van code die iets te maken hebben met Apline js. De rest van de code is html en bootstrap.
In het begin moete we een verbinding maken met framework van Alpine js.
![image](https://user-images.githubusercontent.com/71609618/202864859-f2dc55a6-5705-432e-b6aa-69ec92420ba5.png)
Eerst heb ik script gemaakt om overzicht van de mensen in database te tonen. Wanner de knop wordt gedrukt, worden de gegevens opgehaald van database en op basis van de volgorde worden zij getoond op de website. getData = ! getData zodat we de lijst kunnen sluiten als we het niet nodig.
![image](https://user-images.githubusercontent.com/71609618/202864882-a65efe46-d063-4652-b672-cf28eb025708.png)
De tweede script is meer combinatie van Post en Get endpoint. Op de websiteschrijven we de naam en achternaam van een persoon en daarna klikken we op submit. De persoon wordt toegevoegd aan database en op dezelfde moment krijgen we unieke nummer van nieuwe persoon en tijdstip wanneer dit persoon wordt aangemaakt.

![image](https://user-images.githubusercontent.com/71609618/202864959-34392cd6-9d2b-46ca-9d7f-ef1fe048493e.png)

In Foto's kunt u zien hoe het helemaal werkt.
Tijdens front-end gedeelte wou ik dat elke persoon in database op de website zal verschijnen. Daarvoor moest ik javascript maken. Voor tweede scrip wou ik alleen de datums krijgen wanneer persoon wordt gecreëerd. Helaas omdat ik niet genoeg tijd had , kon ik die ideeën niet realiseren en wat ik heb gemaakt, werkte niet.

# Foto's
## OpenAPI
  - Algemene pagina
    ![image](https://user-images.githubusercontent.com/71609618/202863317-5c3fdcb8-6a1b-4882-b94a-aad3ececee69.png)
  - Iedereen van database
    ![image](https://user-images.githubusercontent.com/71609618/202863518-db25e57c-0812-4b76-a061-0db63c532979.png)
    ![image](https://user-images.githubusercontent.com/71609618/202863525-369d3c27-6840-4988-85a5-ac2b841f4fba.png)
  - Create one person
    ![image](https://user-images.githubusercontent.com/71609618/202863596-f2c78358-a7c7-4aac-b9b0-2ff355613931.png)
    ![image](https://user-images.githubusercontent.com/71609618/202863600-3618fdbf-d6c8-4fab-bca4-c31765106727.png)
  - Delete one person
    ![image](https://user-images.githubusercontent.com/71609618/202863613-f06e35cf-690b-417d-b688-c590000d0706.png)
  - Get one person
    ![image](https://user-images.githubusercontent.com/71609618/202863639-4b314f4c-5fe6-4223-b79f-c8cb31c2ed1c.png)
  - Update one person
    ![image](https://user-images.githubusercontent.com/71609618/202863657-6ab69c32-aa48-44ad-9b2c-2fad713f3959.png)
    ![image](https://user-images.githubusercontent.com/71609618/202863667-2087cc75-b856-4ae3-b73f-c3b3ed7703a8.png)
## Postman
  - Iedereen van database
    ![image](https://user-images.githubusercontent.com/71609618/202863755-35078ddd-4b62-4abc-a790-96208fb38cad.png)
  - Get one person
    ![image](https://user-images.githubusercontent.com/71609618/202863763-23229873-b5fa-494e-a1e5-b35aa58954d3.png)
  - Create one person
    ![image](https://user-images.githubusercontent.com/71609618/202863768-f8cbd067-cddc-4a10-a3d1-815925263a4b.png)
    ![image](https://user-images.githubusercontent.com/71609618/202863771-95b10890-dc28-4449-a6d9-ac19a07b7cb5.png)
## Front-End
  - Pagina
    ![image](https://user-images.githubusercontent.com/71609618/202863860-c985a917-35db-42a7-b1c0-1f7daa8eba0d.png)
  - Eerste Script
    ![image](https://user-images.githubusercontent.com/71609618/202863870-abc4ccad-60da-46f2-b917-568d43ff4be6.png)
  - Tweede Script
    ![image](https://user-images.githubusercontent.com/71609618/202863875-d2380d94-e63b-462f-9111-f2b788ac3bdf.png)







