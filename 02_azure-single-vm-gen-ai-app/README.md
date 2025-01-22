# Eseguire un'App di Intelligenza Generativa Utilizzando Docker su Azure Container Instance

Questa guida spiega come eseguire su Azure Container Instance un container Docker per un'app di Intelligenza Generativa utilizzando un'immagine da Docker Hub.

## Passaggio 1: Creare una Container Instance

Crea una Container Instance dal portale Azure.
Usa l'immagine fabiovisionsystem/ollama-qwen2.5 ed esponi la porta 11434.

## Passaggio 2: Testa il servizio

Puoi mandare richieste HTTP all'applicazione con `curl` (vedi tutorial su [Ollama API](../00_ollama-api/README.md)):

```bash
curl http://<ip_address>/api/generate -d '{
   "model": "qwen2.5:1.5b",
   "prompt":"How can I substitute a wrong article from Amazon?",
   "stream": false
   }'
```