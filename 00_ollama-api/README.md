# Tutorial: Utilizzo di Ollama e delle sue API REST

Ollama è un tool per l'uso di modelli di intelligenza artificiale, progettato per facilitare l'interazione con modelli linguistici tramite API REST. Questo tutorial ti guiderà passo passo nell'installazione di Ollama, nel download di un modello (ad esempio **Llama 3.1**) e nell'utilizzo delle sue API.


## Passo 1: Installare Ollama

1. **Visita il sito ufficiale**  
   Scarica Ollama dal sito ufficiale: [https://ollama.com](https://ollama.com).

2. **Verifica dell'installazione**  
   Dopo l'installazione, apri un terminale e digita:
   ```bash
   ollama --version
   ```
   Se l'installazione è avvenuta con successo, vedrai il numero di versione installato.

---

3. **Installazione tramite Docker**
   
   Se preferisci utilizzare Docker, puoi eseguire Ollama come un container Docker. Ecco un esempio di comando per farlo:

   ```bash
   docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
   ```

   Questo comando avvierà Ollama come un container Docker e ti permetterà di utilizzarlo direttamente dal terminale.

## Passo 2: Scaricare un Modello (es. Llama 3.1)

Ollama permette di scaricare e gestire i modelli direttamente dal terminale.

1. **Scarica un modello**:
   ```bash
   ollama pull llama3.1
   ```
   Questo comando scaricherà il modello **Llama 3.1** sul tuo sistema.

   Su Docker, puoi eseguire lo stesso comando all'interno del container per scaricare il modello.
   ```
   docker exec -it ollama ollama pull llama3.1
   ```

2. **Controlla lo stato del download**:  
   Durante il download, vedrai una barra di progresso. Dopo il completamento, il modello sarà disponibile localmente.

3. **Verifica i modelli installati**:  
   Puoi visualizzare l'elenco dei modelli disponibili con:
   ```bash
   ollama list
   ```

---

## Passo 3: Configurare e Avviare il Server API REST

Ollama supporta l'esposizione dei modelli tramite un'API REST.

1. **Avvia il server API**:
   ```bash
   ollama serve
   ```
   Questo comando avvierà un server locale che espone le API.

2. **Verifica che il server sia attivo**:  
   Di default, il server sarà accessibile su `http://localhost:11434`.

---

## Passo 4: Utilizzare le API REST

Una volta che il server è attivo, puoi inviare richieste API per interagire con il modello.

Per rendere disponibile un modello, usare:
```bash
ollama run llama3.1
```

### Endpoint principali

1. **Generare testo**:
   - **Metodo**: `POST`  
   - **Endpoint**: `/api/generate`  
   - **Esempio di richiesta**:
     ```bash
     curl http://localhost:11434/api/generate -d '{
        "model": "llama3.1",
        "prompt":"Why is the sky blue?",
        "stream": false
        }'

     ```
   - **Risposta esempio**:
     ```json
     {
        "model":"llama3.1",
        "response": "..."
     }
     ```

2. **Elenco dei modelli disponibili**:
   - **Metodo**: `GET`  
   - **Endpoint**: `/v1/models`  
   - **Esempio di richiesta**:
     ```bash
     curl -X GET http://localhost:11434/v1/models
     ```
   - **Risposta esempio**:
     ```json
     {
        "object": "list",
        "data": [
            {
            "id": "llama3.1:latest",
            "object": "model",
            "created": 1735901200,
            "owned_by": "library"
            },
            {
            "id": "llama3.2-vision:latest",
            "object": "model",
            "created": 1731066228,
            "owned_by": "library"
            }
        ]
    }
     ```

3. **Informazioni su un modello specifico**:
   - **Metodo**: `GET`  
   - **Endpoint**: `/v1/models/{model_name}`  
   - **Esempio**:
     ```bash
     curl -X GET http://localhost:11434/v1/models/llama3.1
     ```

1. **Scambiare messaggi**:
   - **Metodo**: `POST`  
   - **Endpoint**: `/api/chat`  
   - **Esempio di richiesta**:
     ```bash
     curl http://localhost:11434/api/chat -d '{
        "model": "llama3.1",
        "stream": false,
        "messages": [
            { "role": "user", "content": "why is the sky blue?" }
        ]
        }'

     ```
   - **Risposta esempio**:
     ```json
     {
        "model":"llama3.1",
        "message": "..."
     }
     ```


## Conclusione

In questo tutorial hai imparato a:

1. Installare Ollama.
2. Scaricare un modello come **Llama 3.1**.
3. Utilizzare il server API REST per interagire con il modello.