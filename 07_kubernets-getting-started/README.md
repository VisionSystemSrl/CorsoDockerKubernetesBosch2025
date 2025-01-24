# Tutorial: Introduzione a Kubernetes – Distribuire una Semplice App su un Cluster Kubernetes Locale

Questo tutorial ti guiderà nel processo di distribuzione di una semplice app su un cluster Kubernetes locale. Supponiamo che tu abbia già installato `kubectl`, lo strumento da riga di comando per interagire con i cluster Kubernetes. Utilizzeremo anche Minikube, uno strumento per eseguire cluster Kubernetes localmente.


## Prerequisiti

1. **kubectl Installato**: Hai già installato `kubectl` per interagire con Kubernetes.
2. **Minikube Installato**: Minikube è uno strumento che ti aiuta a configurare un cluster Kubernetes locale. Se non lo hai ancora installato, puoi seguire la guida all'installazione sul [sito ufficiale di Minikube](https://minikube.sigs.k8s.io/docs/).
3. **Un Cluster Kubernetes Funzionante**: In questo tutorial, creeremo un cluster locale utilizzando Minikube.


## Passaggio 1: Avviare un Cluster Kubernetes Locale con Minikube

Prima di tutto, avvia Minikube per configurare un cluster Kubernetes locale. Apri il terminale ed esegui il seguente comando:

```bash
minikube start
```

**Spiegazione**:  
- `minikube start`: Questo comando inizializza e avvia il cluster Kubernetes sulla tua macchina locale. Potrebbero volerci un paio di minuti.

Una volta che il cluster è avviato, puoi verificare lo stato con il comando:

```bash
kubectl cluster-info
```

Questo mostrerà l'indirizzo del cluster Kubernetes, confermando che il tuo cluster locale è in esecuzione.


## Passaggio 2: Creare una Semplice Applicazione

Creeremo una semplice applicazione web utilizzando Nginx come base. Questa app servirà una semplice pagina "Hello, Kubernetes!".


### Creare `deployment.yaml`

Crea un nuovo file chiamato `deployment.yaml` con il seguente contenuto:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-k8s-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-k8s
  template:
    metadata:
      labels:
        app: hello-k8s
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

**Spiegazione**:
- `apiVersion: apps/v1`: Specifica la versione dell'API per il deployment.
- `kind: Deployment`: Definisce un Deployment di Kubernetes, che garantisce che il numero specificato di repliche di un container sia in esecuzione.
- `metadata`: Include il nome del deployment (`hello-k8s-deployment`).
- `spec`: Definisce lo stato desiderato dell'app.
  - `replicas: 1`: Specifica che deve essere eseguita una replica dell'app.
  - `selector`: Kubernetes utilizza questo per trovare quali pod gestire per questo deployment.
  - `template`: Definisce il modello del pod che verrà utilizzato per creare i pod.
    - `containers`: Definisce il container che sarà utilizzato nel pod (in questo caso, Nginx).


## Passaggio 3: Distribuire l'Applicazione su Kubernetes

Ora distribuiamo l'app utilizzando `kubectl`. Esegui il seguente comando nella stessa directory del file `deployment.yaml`:

```bash
kubectl apply -f deployment.yaml
```

**Spiegazione**:  
- `kubectl apply`: Questo comando applica la configurazione di Kubernetes (dal file YAML) al cluster.
- `-f deployment.yaml`: Specifica il file da utilizzare per il deployment.

Una volta che il deployment è riuscito, puoi controllare lo stato del tuo deployment con il comando:

```bash
kubectl get deployments
```

Dovresti vedere il `hello-k8s-deployment` elencato con il numero di pod desiderati (repliche).


## Passaggio 4: Esporre l'Applicazione

In Kubernetes, un'app in esecuzione in un pod non è accessibile all'esterno del cluster per impostazione predefinita. Per rendere l'app accessibile, devi creare un servizio. Questo esporrà il deployment al mondo esterno.

Crea un file chiamato `service.yaml` con il seguente contenuto:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-k8s-service
spec:
  selector:
    app: hello-k8s
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

**Spiegazione**:
- `apiVersion: v1`: Specifica la versione dell'API per il servizio.
- `kind: Service`: Definisce un servizio Kubernetes.
- `metadata`: Include il nome del servizio (`hello-k8s-service`).
- `spec`: Definisce come dovrebbe comportarsi il servizio.
  - `selector`: Collega il servizio ai pod con l'etichetta `app: hello-k8s`.
  - `ports`: Definisce le porte per il servizio. In questo caso, espone la porta 80.
  - `type: LoadBalancer`: Garantisce che il servizio venga esposto all'esterno del cluster (funziona con provider di cloud o Minikube in alcuni casi).

Ora, applica la configurazione del servizio:

```bash
kubectl apply -f service.yaml
```

Dopo che il servizio è stato creato, esegui il seguente comando per ottenere i dettagli del servizio:

```bash
kubectl get services
```

Minikube usa un comando speciale per esporre i servizi localmente. Esegui il seguente comando per accedere al servizio:

```bash
minikube service hello-k8s-service
```

Questo comando aprirà il servizio nel tuo browser predefinito. Dovresti vedere una pagina servita da Nginx che mostra la pagina predefinita o "Hello, Kubernetes!" se l'hai personalizzata.


## Passaggio 5: Verificare l'Applicazione

Puoi controllare i pod e i deployment in qualsiasi momento utilizzando i seguenti comandi:

- Per vedere i pod in esecuzione:
  ```bash
  kubectl get pods
  ```
- Per controllare i log del pod in esecuzione:
  ```bash
  kubectl logs <nome-pod>
  ```

Dovresti vedere i log di Nginx o qualsiasi output personalizzato che hai configurato.


## Passaggio 6: Pulire le Risorse

Quando hai finito, puoi eliminare il deployment e il servizio per pulire le risorse Kubernetes:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

Questo rimuoverà sia il deployment che il servizio dal tuo cluster.


## Conclusione

Hai distribuito con successo una semplice app su un cluster Kubernetes locale utilizzando Minikube. Ecco un rapido riepilogo dei passaggi che abbiamo seguito:
1. Avviato un cluster Kubernetes locale con Minikube.
2. Creato una semplice applicazione web usando Nginx.
3. Distribuito l'app su Kubernetes con un deployment.
4. Esposto l'app con un servizio per accedervi dall'esterno del cluster.
5. Pulito le risorse dopo l'uso.

Ora sei pronto per esplorare altre funzionalità avanzate di Kubernetes e distribuire le tue applicazioni.