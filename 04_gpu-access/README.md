# Tutorial: Accedere alla GPU all'interno di un Container Docker e Monitorare l'Uso della GPU

Questa guida ti aiuterà a configurare un container Docker che può accedere alla GPU del tuo sistema e ti mostrerà come monitorare l'uso della GPU all'interno del container.

## Prerequisiti

1. **GPU NVIDIA**: Assicurati di avere una GPU NVIDIA installata sul tuo sistema.
2. **Driver NVIDIA**: Installa i driver NVIDIA appropriati per la tua GPU.
3. **Docker Installato**: Assicurati che Docker sia installato sul tuo sistema.
4. **NVIDIA Container Toolkit**: Installa il NVIDIA Container Toolkit per abilitare l'accesso alla GPU in Docker.

### Installare NVIDIA Container Toolkit

Segui questi passaggi per installare il NVIDIA Container Toolkit:

```bash
# Aggiungi il repository dei pacchetti NVIDIA
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Aggiorna e installa
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# Riavvia il servizio Docker
sudo systemctl restart docker
```


## Passaggio 1: Creare una Semplice Immagine Docker

Crea una nuova cartella e aggiungi il seguente `Dockerfile` per definire una semplice immagine con supporto GPU.

### **Dockerfile**
```dockerfile
FROM nvidia/cuda:11.8.0-runtime-ubuntu20.04

# Installa Python e gli strumenti necessari
RUN apt-get update && apt-get install -y python3 python3-pip

# Installa una libreria Python (es. PyTorch con supporto GPU)
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Costruire l'Immagine Docker

Esegui il seguente comando per costruire l'immagine:

```bash
docker build -t gpu-app:1.0 .
```


## Passaggio 2: Eseguire il Container con Accesso alla GPU

Usa il flag `--gpus` per concedere al container l'accesso alla tua GPU:

```bash
docker run -it --gpus all --name gpu-container gpu-app:1.0
```

**Spiegazione**:
- `--gpus all`: Concede al container l'accesso a tutte le GPU disponibili.
- `-it`: Avvia il container in modalità interattiva.
- `--name gpu-container`: Assegna un nome al container per un riferimento più facile.
- `gpu-app:1.0`: Specifica l'immagine Docker da utilizzare.


## Passaggio 3: Verificare l'Accesso alla GPU all'interno del Container

Una volta dentro il container, puoi verificare l'accesso alla GPU utilizzando il comando `nvidia-smi`:

```bash
nvidia-smi
```

Dovresti vedere un elenco delle tue GPU insieme alle relative statistiche di utilizzo correnti.


## Passaggio 4: Monitorare l'Uso della GPU

### Utilizzando `nvidia-smi` sul Sistema Host

Esegui il seguente comando sulla tua macchina host per monitorare l'uso della GPU:

```bash
nvidia-smi
```

Questo fornisce informazioni in tempo reale sull'uso della GPU, sul consumo di memoria e sui processi in esecuzione.


## Passaggio 5: Fermare e Rimuovere il Container

Fermare il container quando hai finito:

```bash
docker stop gpu-container
```

Rimuovi il container:

```bash
docker rm gpu-container
```


## Note Aggiuntive

- Per limitare l'accesso alla GPU a specifiche GPU, usa il flag `--gpus` con gli ID dei dispositivi, ad esempio `--gpus '"device=0,1"'`.
- Per attività che richiedono molte risorse della GPU, considera di usare immagini Docker preconfigurate con librerie di ML/AI, come `nvidia/cuda` o framework come TensorFlow o PyTorch.