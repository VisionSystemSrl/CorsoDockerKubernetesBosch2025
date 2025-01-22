# Come Costruire ed Eseguire l'App di Intelligenza Generativa con Docker

Questa guida spiega come costruire ed eseguire un'app Dockerizzata di Intelligenza Generativa che utilizza la libreria [Hugging Face's transformers](https://pypi.org/project/transformers/) e un'API Flask.

## Passaggio 1: Preparare i File

Assicurati che siano presenti la seguente struttura di directory e i file:

```
generative-ai-app/
├── app.py
├── requirements.txt
└── Dockerfile
```

**Descrizione dei File**:
- `app.py`: Codice dell'applicazione Python che configura un'API Flask e utilizza la libreria Hugging Face's transformers per la generazione di testo.
- `requirements.txt`: Elenca tutte le dipendenze Python necessarie per eseguire l'applicazione.
- `Dockerfile`: Definisce i passaggi per creare un'immagine Docker per l'app.

## Passaggio 2: Costruire l'Immagine Docker

Esegui il seguente comando nel tuo terminale dalla directory generative-ai-app:

```bash
docker build -t generative-ai-app:1.0 .
```

**Spiegazione**:
- `docker build`: Il comando per costruire un'immagine Docker.
- `-t generative-ai-app:1.0`: Assegna all'immagine il nome generative-ai-app e la versione 1.0.
- `.`: Specifica la directory corrente come contesto di build.

## Passaggio 3: Eseguire il Container Docker

Esegui il container utilizzando l'immagine costruita:

```bash
docker run -d -p 8080:8080 --name generative-app generative-ai-app:1.0
```

**Spiegazione**:
- `docker run`: Avvia un nuovo container.
- `-d`: Esegue il container in modalità distaccata (in background).
- `-p 8080:8080`: Mappa la porta 8080 sulla tua macchina alla porta 8080 nel container.
- `--name generative-app`: Assegna al container un nome (generative-app).
- `generative-ai-app:1.0`: Specifica l'immagine Docker da utilizzare.

## Passaggio 4: Testare l'App

Testa l'app in esecuzione inviando una richiesta POST all'endpoint API. Puoi utilizzare curl o uno strumento come Postman.

**Utilizzando curl**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Once upon a time"}' http://localhost:8080/generate
```

**Risposta Attesa**:
```json
[
 {
 "generated_text": "Once upon a time, in a faraway land, there lived a wise old king..."
 }
]
```

## Passaggio 5: Monitorare l'Uso delle Risorse

Puoi monitorare l'utilizzo delle risorse (CPU, memoria, ecc.) del tuo container con il comando:
```
docker stats
```
**Descrizione**:
- `docker stats`: Mostra in tempo reale l'utilizzo delle risorse di tutti i container in esecuzione. Puoi individuare il container desiderato dal nome o dall'ID.

## Passaggio 6: Fermare e Rimuovere il Container

Ferma il container quando hai finito:

```bash
docker stop generative-app
```

Rimuovi il container:

```bash
docker rm generative-app
```

## Passaggio 7: Distribuire l'Immagine Docker su Docker Hub

Puoi condividere la tua immagine Docker distribuendola su Docker Hub.

### 1. Accedi a Docker Hub

Esegui il seguente comando e inserisci le tue credenziali di Docker Hub:

```bash
docker login
```

### 2. Tagga l'Immagine

Assegna un tag all'immagine con il tuo nome utente Docker Hub e il nome del repository desiderato:

```bash
docker tag generative-ai-app:1.0 <tuo-username-dockerhub>/generative-ai-app:1.0
```

**Esempio**:

```bash
docker tag generative-ai-app:1.0 johndoe/generative-ai-app:1.0
```

### 3. Pubblica l'Immagine su Docker Hub

Carica l'immagine taggata su Docker Hub:

```bash
docker push <tuo-username-dockerhub>/generative-ai-app:1.0
```

**Esempio**:

```bash
docker push johndoe/generative-ai-app:1.0
```

Una volta completato il caricamento, la tua immagine sarà disponibile su Docker Hub nel tuo account.

### 4. Verifica l'Immagine su Docker Hub

Accedi al sito web di Docker Hub e controlla i tuoi repository per assicurarti che l'immagine sia elencata.

### 5. Pubblica l'immagine su un repository privato
#### 5.1 Azure Container Registry
Se hai un account Azure, puoi utilizzare Azure Container Registry per archiviare le tue immagini Docker in un repository privato.
Login:
```bash
az acr login --name your_registry_name 
```

Tag:
```bash
docker tag generative-ai-app:1.0 your_registry_name.azurecr.io/generative-ai-app:1.0
```

Push:
```bash
docker push your_registry_name.azurecr.io/generative-ai-app:1.0
```

#### 5.2 GitHub Container Registry
Se hai un account GitHub, puoi utilizzare GitHub Container Registry per archiviare le tue immagini Docker in un repository privato.
Login:
```bash
echo "<YOUR_PERSONAL_ACCESS_TOKEN>" | docker login ghcr.io -u <YOUR_GITHUB_USERNAME> --password-stdin
```

Tag:
```bash
docker tag generative-ai-app:1.0 ghcr.io/your_github_username/generative-ai-app:1.0
```

Push:
```bash
docker push ghcr.io/your_github_username/generative-ai-app:1.0
```

## Note Aggiuntive

- Se devi ricostruire l'immagine dopo aver apportato modifiche al codice o al Dockerfile, ri-esegui il comando `docker build`.
- Per verificare i container in esecuzione, usa:
  ```bash
  docker ps
  ```
- Per visualizzare i log del container in esecuzione, usa:
  ```bash
  docker logs generative-app
  ```