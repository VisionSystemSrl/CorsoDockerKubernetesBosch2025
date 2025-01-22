# Gestione di un'App AI Generativa con Vector Database usando Docker Compose

## Obiettivo

L'applicazione consisterà di due servizi:
1. **API Python (FastAPI):** Una API che utilizza un modello generativo per generare embedding e rispondere a query.
2. **Vector Database (Chroma):** Un database per immagazzinare e recuperare embedding vettoriali, che consente ricerche semantiche.

Docker Compose semplifica il setup di questi due servizi, gestendo automaticamente rete, volumi e dipendenze.

---

## **Prerequisiti**
1. Installa Docker e Docker Compose:
   - [Guida per installare Docker](https://docs.docker.com/get-docker/)
   - Docker Compose è incluso nelle versioni moderne di Docker Desktop. Se usi Linux, puoi installarlo [da qui](https://docs.docker.com/compose/install/).
2. Python >=3.8 per testare il servizio localmente, se necessario.

---

## **Passo 1: Configura la struttura del progetto**

Crea una cartella per il progetto e organizza i file come segue:

```plaintext
ai-app/
├── docker-compose.yml
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
```

---

## **Passo 2: Scrivi il file `docker-compose.yml`**

Questo file definirà i due servizi: l'API Python e il database Chroma.

Crea il file `docker-compose.yml`:

```yaml
version: '3.9'

services:
  api:
    build:
      context: ./api
    container_name: ai-api
    ports:
      - "8000:8000"
    environment:
      CHROMA_HOST: chroma
      CHROMA_PORT: 8001
    depends_on:
      - chroma

  chroma:
    image: ghcr.io/chroma-core/chroma:latest
    container_name: chroma
    ports:
      - "8001:8000"
    volumes:
      - chroma_data:/chroma

volumes:
  chroma_data:
```

- **API Python (`api`):**
  - Costruisce l'immagine da una directory locale.
  - Comunica con il servizio Chroma per inserire e recuperare embedding.

- **Chroma (`chroma`):**
  - Utilizza l'immagine ufficiale di Chroma.
  - Archivia i dati nel volume `chroma_data` per persistenza.

---

### **Passo 3: Avvia i container**

1. Avvia i servizi con Docker Compose:

   ```bash
   docker-compose up --build
   ```

2. Verifica che i container siano in esecuzione:

   ```bash
   docker ps
   ```

   Dovresti vedere due container: `ai-api` e `chroma`.

---

### **Passo 5: Testa l'applicazione**

1. **Aggiungi un documento:**

   Usa `curl` o un client API come Postman per aggiungere un documento:

   ```bash
   curl -X POST "http://localhost:8000/add" \
        -H "Content-Type: application/json" \
        -d '{"id": "1", "text": "AI generativa è incredibile!"}'
   ```

   Risultato atteso:

   ```json
   {"message": "Document 1 added successfully."}
   ```

2. **Effettua una ricerca semantica:**

   Esegui una query per trovare documenti simili:

   ```bash
   curl -X GET "http://localhost:8000/search?query=AI generativa"
   ```

   Risultato atteso (esempio):

   ```json
   {
       "ids": ["1"],
       "documents": ["AI generativa è incredibile!"],
       "distances": [1.11]
   }
   ```

---

### **Pulizia**

Per rimuovere i container e i volumi creati:

```bash
docker-compose down --volumes
```

---

### **Perché Docker Compose è utile qui?**
1. **Semplicità:** Tutta la configurazione è centralizzata in un file `docker-compose.yml`.
2. **Networking:** Docker Compose crea automaticamente una rete per i container, consentendo loro di comunicare usando i nomi dei servizi (ad esempio, `chroma`).
3. **Scalabilità:** Puoi aggiungere facilmente nuovi servizi (ad esempio, un frontend per interagire con l'API).
4. **Persistenza:** I volumi assicurano che i dati del database vettoriale siano salvati anche dopo lo spegnimento dei container.
