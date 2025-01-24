## Utilizzo dei Persistent Volume Claims con MySQL in Kubernetes

### Obiettivo

Distribuire un database **MySQL** in Kubernetes con storage persistente usando i PVC. Questo garantisce che i dati del database vengano mantenuti anche se i Pod MySQL vengono riavviati.

---

### Passo 1: Creare un Persistent Volume (PV)

Crea un file chiamato `mysql-pv.yaml`:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv
spec:
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/mysql-data"
```

- **`hostPath`:** Specifica dove i dati verranno salvati sul nodo host di Minikube (`/mnt/mysql-data`).

Applica il file del PV:

```bash
kubectl apply -f mysql-pv.yaml
```

---

### Passo 2: Creare un Persistent Volume Claim (PVC)

Crea un file chiamato `mysql-pvc.yaml`:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

- **`resources.requests.storage`:** Richiede 1Gi dei 2Gi disponibili dal PV.

Applica il file del PVC:

```bash
kubectl apply -f mysql-pvc.yaml
```

---

### Passo 3: Distribuire il Pod MySQL con PVC

Crea un file chiamato `mysql-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:5.7
          env:
            - name: MYSQL_ROOT_PASSWORD
              value: rootpassword
            - name: MYSQL_DATABASE
              value: exampledb
          ports:
            - containerPort: 3306
          volumeMounts:
            - name: mysql-storage
              mountPath: /var/lib/mysql
      volumes:
        - name: mysql-storage
          persistentVolumeClaim:
            claimName: mysql-pvc
```

- **`MYSQL_ROOT_PASSWORD`:** Imposta la password di root per MySQL.
- **`MYSQL_DATABASE`:** Crea un database predefinito (`exampledb`).
- **`volumeMounts.mountPath`:** Monta il volume in `/var/lib/mysql`, il percorso predefinito per i dati di MySQL.
- **`persistentVolumeClaim.claimName`:** Collega il PVC al Pod.

Applica il Deployment:

```bash
kubectl apply -f mysql-deployment.yaml
```

---

### Passo 4: Esporre il Servizio MySQL

Crea un file chiamato `mysql-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  selector:
    app: mysql
  ports:
    - protocol: TCP
      port: 3306
      targetPort: 3306
  type: ClusterIP
```

Applica il file del servizio:

```bash
kubectl apply -f mysql-service.yaml
```

Questo servizio espone il Pod MySQL sulla porta `3306` all'interno del cluster Kubernetes.

---

### Passo 5: Verifica e Testa la Distribuzione

1. **Controlla lo stato del Pod:**

   ```bash
   kubectl get pods
   ```

   Assicurati che il Pod `mysql` sia in esecuzione.

2. **Connettiti al database MySQL:**

   Accedi al Pod MySQL:

   ```bash
   kubectl exec -it $(kubectl get pod -l app=mysql -o jsonpath="{.items[0].metadata.name}") -- /bin/bash
   ```

   All'interno del container, accedi a MySQL:

   ```bash
   mysql -u root -p
   ```

   Inserisci la password: `rootpassword`.

   Verifica il database:

   ```sql
   SHOW DATABASES;
   ```

3. **Testa la persistenza dei dati:**

   - Crea una tabella e inserisci dati nel database.
  
    ```sql
    USE exampledb;
    CREATE TABLE users (id INT, name VARCHAR(255));
    INSERT INTO users VALUES (1, 'Alice');
    ```
   - Riavvia il Pod:

     ```bash
     kubectl delete pod -l app=mysql
     ```

   - Dopo il riavvio del Pod, riconnettiti a MySQL e verifica che i dati siano ancora presenti.

---

### Passo 6: Pulizia

Per rimuovere le risorse, esegui:

```bash
kubectl delete -f mysql-service.yaml
kubectl delete -f mysql-deployment.yaml
kubectl delete -f mysql-pvc.yaml
kubectl delete -f mysql-pv.yaml
```

## Persistent Storage in Azure
Per creare un persistent storage su Azure si può usare il seguente comando:
```
az disk create --resource-group corso-aks --name my-disk-10gb --size-gb 10 --sku Standard_LRS
```

Per ottenere l'id del Azure Disk creato usare il comando:
```
az disk show --name my-disk-10gb --resource-group corso-aks --query id -o tsv
```

Inserire l'id del Azure Disk all'interno del file `azure-disk-pv.yaml`.

Infine, applicare il Persistent Volume e Persistent Volume Claim al cluster:
```
kubectl apply -f azure-disk-pv.yaml
kubectl apply -f azure-disk-pvc.yaml
```

Infine è possibile provare a fare il deploy di MySQL sul cluster AKS usando gli stessi comandi di cui sopra.
Andrà cambiato il nome del persistentVolumeClaim all'interno di `mysql-deployment.yaml` con lo stesso nome utilizato in `azure-disk-pvc.yaml`.