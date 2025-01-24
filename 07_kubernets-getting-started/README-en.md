# Tutorial: Getting Started with Kubernetes – Deploying a Simple App to a Local Kubernetes Cluster

This tutorial will walk you through deploying a simple app to a local Kubernetes cluster. We'll assume that you already have `kubectl` installed, which is the command-line tool for interacting with Kubernetes clusters. We will also use Minikube, a tool for running Kubernetes clusters locally.

Install kubectl and Minikube [here](https://kubernetes.io/docs/tasks/tools/).


## Prerequisites

1. **kubectl Installed**: You've already installed `kubectl` to interact with Kubernetes.
2. **Minikube Installed**: Minikube is a tool that helps you set up a local Kubernetes cluster. If you don't have it installed, you can follow the installation guide on the [Minikube website](https://minikube.sigs.k8s.io/docs/).
3. **A working Kubernetes Cluster**: We'll set up a local cluster using Minikube in this tutorial.


## Step 1: Start a Local Kubernetes Cluster with Minikube

First, start Minikube to set up a local Kubernetes cluster. Open your terminal and run the following command:

```bash
minikube start
```

**Explanation**:  
- `minikube start`: This command initializes and starts the Kubernetes cluster on your local machine. It might take a couple of minutes.

Once the cluster is up and running, you can check the status with:

```bash
kubectl cluster-info
```

This will show the address of the Kubernetes cluster, confirming that your local cluster is running.


## Step 2: Create a Simple Application

We'll create a simple web application using Nginx as the base. This app will serve a basic "Hello, Kubernetes!" page. 

### Create `deployment.yaml`

Create a new file named `deployment.yaml` with the following content:

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

**Explanation**:
- `apiVersion: apps/v1`: Specifies the API version for the deployment.
- `kind: Deployment`: Defines a Kubernetes Deployment, which ensures that the specified number of replicas of a container are running.
- `metadata`: Includes the name for the deployment (`hello-k8s-deployment`).
- `spec`: Defines the desired state of the app.
  - `replicas: 1`: This specifies that one replica of the app should run.
  - `selector`: Kubernetes uses this to find which pods to manage for this deployment.
  - `template`: Defines the pod template that will be used to create pods.
    - `containers`: Defines the container to be used in the pod (Nginx in this case).


## Step 3: Deploy the Application to Kubernetes

Now, deploy the app using `kubectl`. Run the following command in the same directory as the `deployment.yaml` file:

```bash
kubectl apply -f deployment.yaml
```

**Explanation**:  
- `kubectl apply`: This command applies the Kubernetes configuration (from the YAML file) to the cluster.
- `-f deployment.yaml`: Specifies the file to use for the deployment.

Once the deployment is successful, you can check the status of your deployment:

```bash
kubectl get deployments
```

You should see the `hello-k8s-deployment` listed with the desired number of pods (replicas).


## Step 4: Expose the Application

In Kubernetes, an app running in a pod isn't accessible outside the cluster by default. To make the application accessible, you need to create a Service. This will expose the deployment to the external world.

Create a file named `service.yaml` with the following content:

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

**Explanation**:
- `apiVersion: v1`: Specifies the API version for the service.
- `kind: Service`: Defines a Kubernetes Service.
- `metadata`: Includes the name for the service (`hello-k8s-service`).
- `spec`: Defines how the service should behave.
  - `selector`: This links the service to the pods with the label `app: hello-k8s`.
  - `ports`: Defines the ports for the service. Here, it exposes port 80.
  - `type: LoadBalancer`: Ensures the service is exposed outside the cluster (works with cloud providers or Minikube in some cases).

Now, apply the service configuration:

```bash
kubectl apply -f service.yaml
```

After the service is created, run the following command to get the service details:

```bash
kubectl get services
```

Minikube uses a special command to expose services locally. Run the following to access the service:

```bash
minikube service hello-k8s-service
```

This command will open the service in your default web browser. You should see a page served by Nginx displaying a default page or "Hello, Kubernetes!" if you've customized it.


## Step 5: Verify the Application

You can check the pods and deployments at any time using the following commands:

- To see the pods running:
  ```bash
  kubectl get pods
  ```
- To check the logs of the running pod:
  ```bash
  kubectl logs <pod-name>
  ```

You should see the Nginx logs or any custom output you've configured.


## Step 6: Clean Up

When you're done, you can delete the deployment and service to clean up your Kubernetes resources:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

This will remove both the deployment and the service from your cluster.

