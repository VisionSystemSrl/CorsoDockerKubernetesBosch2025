# Avvio Rapido: Eseguire un'App di Intelligenza Generativa Utilizzando Docker

Questa guida spiega come eseguire un container Docker per un'app di Intelligenza Generativa utilizzando un'immagine da Docker Hub. Imparerai anche a gestire il ciclo di vita del container (avvio, arresto, riavvio, visualizzazione dei log, ecc.).

## Passaggio 1: Scarica l'Immagine Docker Pre-Costruita

Utilizzeremo un'immagine pre-costruita da Docker Hub che fornisce un'API di Intelligenza Generativa basata sul modello GPT-2 di Hugging Face.

Esegui il seguente comando per scaricare l'immagine:

```bash
docker pull fabiovisionsystem/generative-ai-app:1.0
```

**Spiegazione**:
- `docker pull`: Scarica l'immagine Docker da un registro (in questo caso, Docker Hub o GitHub Container Registry).
- `fabiovisionsystem/generative-ai-app:1.0`: Il nome completo dell'immagine.

## Passaggio 2: Eseguire il Container Docker

Avvia il container con il seguente comando:

```bash
docker run -d -p 8080:8080 --name gpt2-app fabiovisionsystem/generative-ai-app:1.0
```

**Spiegazione**:
- `docker run`: Avvia un nuovo container.
- `-d`: Esegue il container in modalità distaccata (in background).
- `-p 8080:8080`: Mappa la porta 8080 sulla tua macchina alla porta 8080 nel container. Questo consente di accedere all'app localmente.
- `--name gpt2-app`: Assegna un nome (gpt2-app) al container per una gestione più semplice.
- `fabiovisionsystem/generative-ai-app:1.0`: Specifica l'immagine da utilizzare.

Dopo aver eseguito questo comando, l'app di Intelligenza Generativa è ora in esecuzione in un container Docker.

## Passaggio 3: Testare l'App di Intelligenza Generativa

Puoi testare l'app in esecuzione inviando una richiesta POST all'endpoint API. Usa curl o uno strumento come Postman.

**Utilizzando curl**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Once upon a time"}' http://localhost:8080/generate
```

**Risposta Attesa**:
```json
{
"generated_text": "Once upon a time, in a faraway kingdom, a young prince discovered an ancient treasure..."
}
```

## Gestione del Ciclo di Vita del Container

Ecco alcuni comandi comuni per gestire il ciclo di vita del container:

### 1. Visualizzare i Container in Esecuzione

Per vedere un elenco di tutti i container in esecuzione:
```bash
docker ps
```

Per vedere un elenco di tutti i container sia in esecuzione che terminati:
```bash
docker ps -a
```

### 2. Fermare il Container

Per fermare il container gpt2-app:
```bash
docker stop gpt2-app
```

### 3. Riavviare il Container

Per riavviare il container gpt2-app:
```bash
docker restart gpt2-app
```

### 4. Visualizzare i Log

Per vedere i log del container gpt2-app:
```bash
docker logs gpt2-app
```

### 5. Rimuovere il Container

Se non hai più bisogno del container, fermalo prima e poi rimuovilo:
```bash
docker rm gpt2-app
```

### 6. Rimuovere l'Immagine Docker

Se desideri pulire l'immagine dal tuo sistema:
```bash
docker rmi fabiovisionsystem/generative-ai-app:1.0
```