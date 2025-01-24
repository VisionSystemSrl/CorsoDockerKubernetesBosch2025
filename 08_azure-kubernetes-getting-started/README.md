# Tutorial: Distribuire una Semplice App su Azure Kubernetes Service (AKS)

In questo tutorial, imparerai come distribuire una semplice app su un cluster Kubernetes ospitato su Azure utilizzando il servizio Azure Kubernetes Service (AKS). Copriremo tutto, dalla configurazione dell'Azure CLI alla distribuzione dell'app, passo dopo passo.


## Prerequisiti

1. **Azure CLI Installata**: Assicurati di avere l'Azure CLI installata sul tuo sistema. Puoi installarla eseguendo il seguente comando:

   ```bash
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   ```

2. **kubectl Installato**: Verifica di avere `kubectl` installato per interagire con Kubernetes. Se non l'hai installato, segui le istruzioni [qui](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

3. **Account Azure**: Dovresti avere un account Azure attivo. Se non ne hai uno, puoi registrarti per un account gratuito [qui](https://azure.microsoft.com/free/).

4. **Abbonamento Azure**: Assicurati di avere un abbonamento su Azure dove puoi creare risorse.


## Passaggio 1: Effettuare il Login su Azure

Se non hai ancora effettuato il login con Azure CLI, fallo eseguendo il seguente comando:

```bash
az login
```

Questo ti chiederà di autenticarti con il tuo account Azure.


## Passaggio 2: Creare un Cluster di Azure Kubernetes Service (AKS)

Crea un cluster kubernetes dal portale Azure.


## Passaggio 4: Connettersi al Cluster AKS

Una volta creato il cluster, dovrai configurare `kubectl` per interagire con il cluster AKS. Usa il seguente comando:

```bash
az aks get-credentials --resource-group corso-kubernetes --name cluster-corso
```

Questo aggiornerà il tuo file kubeconfig per puntare al cluster AKS appena creato. Verifica la connessione eseguendo:

```bash
kubectl get nodes
```

Questo dovrebbe mostrare i nodi nel tuo cluster AKS.


## Passaggio 5: Distribuire l'Applicazione

Esegui il seguente comando per applicare la configurazione di distribuzione al tuo cluster AKS:

```bash
kubectl apply -f deployment.yaml
```

Puoi verificare che la distribuzione sia stata effettuata correttamente controllando le distribuzioni nel tuo cluster:

```bash
kubectl get deployments
```

---

## Passaggio 7: Esporre l'Applicazione

Ora, applica la configurazione del servizio per esporre la tua applicazione:

```bash
kubectl apply -f service.yaml
```

Controlla i servizi nel tuo cluster:

```bash
kubectl get services
```

Vedrai un indirizzo IP pubblico sotto la colonna `EXTERNAL-IP` una volta che il servizio è stato provisioning.

---

## Passaggio 8: Accedere all'Applicazione

Potrebbe volerci un minuto per il provisioning del bilanciatore di carico e per la visualizzazione dell'indirizzo IP esterno. Una volta che l'indirizzo IP è disponibile, puoi accedere all'applicazione tramite un browser visitando l'IP fornito.

Una volta che l'indirizzo IP appare, aprilo in un browser e dovresti vedere la pagina predefinita di Nginx.

---

## Passaggio 9: Verificare l'Applicazione

Per verificare che l'app sia in esecuzione, puoi controllare i log del container Nginx:

```bash
kubectl logs <pod-name>
```

Ottieni il nome del pod eseguendo:

```bash
kubectl get pods
```

---

## Passaggio 10: Pulire le Risorse

Per evitare addebiti continui, è importante pulire le risorse quando hai finito. Esegui il seguente comando per eliminare il cluster AKS e le risorse associate:

```bash
az aks delete --resource-group corso-kubernetes --name cluster-corso --yes --no-wait
```

Questo eliminerà il cluster AKS. Inoltre, puoi eliminare il gruppo di risorse se non è più necessario:

```bash
az group delete --name corso-kubernetes --yes --no-wait
```


## Conclusione

Congratulazioni! Hai distribuito con successo una semplice app su Azure Kubernetes Service (AKS). Ecco un riepilogo dei passaggi:

1. Configurato l'Azure CLI ed effettuato il login nel tuo account Azure.
2. Creato un gruppo di risorse e un cluster AKS su Azure.
3. Configurato `kubectl` per usare il cluster AKS.
4. Creato una semplice app usando Nginx e distribuita su AKS.
5. Esposto l'app utilizzando un servizio LoadBalancer e acceduto tramite un IP pubblico.

Ora puoi esplorare funzionalità più avanzate di AKS e Kubernetes!