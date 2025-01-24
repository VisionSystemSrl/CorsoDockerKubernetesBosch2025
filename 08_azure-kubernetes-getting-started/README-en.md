# Tutorial: Deploying a Simple App to Azure Kubernetes Service (AKS)

In this tutorial, you'll learn how to deploy a simple app to a Kubernetes cluster hosted on Azure using the Azure Kubernetes Service (AKS). We'll cover everything from setting up your Azure CLI to deploying the app, step by step.


## Prerequisites

1. **Azure CLI Installed**: You should have the Azure CLI installed on your system. You can install it by running the following command:
   
   ```bash
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   ```

2. **kubectl Installed**: Ensure that you have `kubectl` installed for interacting with Kubernetes. If you don't have it installed, follow the instructions [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

3. **Azure Account**: You should have an active Azure account. If you don’t have one, you can sign up for a free account [here](https://azure.microsoft.com/free/).

4. **Azure Subscription**: Ensure you have a subscription on Azure where you can create resources.


## Step 1: Log in to Azure

If you haven't logged into Azure CLI yet, do so by running the following command:

```bash
az login
```

This will prompt you to authenticate with your Azure account.


## Step 2: Create an Azure Kubernetes Service (AKS) Cluster

Now, let’s create the AKS cluster.

Inserire immagini qui

## Step 4: Connect to Your AKS Cluster

Once the cluster is created, you'll need to configure your `kubectl` to interact with the AKS cluster. Use the following command:

```bash
az aks get-credentials --resource-group corso-kubernetes --name cluster-corso
```

This will update your kubeconfig file to point to your newly created AKS cluster. Verify the connection by running:

```bash
kubectl get nodes
```

This should show the nodes in your AKS cluster.


## Step 5: Deploy the Application

Run the following command to apply the deployment configuration to your AKS cluster:

```bash
kubectl apply -f deployment.yaml
```

You can verify that the deployment was successful by checking the deployments in your cluster:

```bash
kubectl get deployments
```


## Step 7: Expose the Application

Now, apply the service configuration to expose your application:

```bash
kubectl apply -f service.yaml
```

Check the services in your cluster:

```bash
kubectl get services
```

You will see a public IP address under the `EXTERNAL-IP` column once the service is provisioned.


## Step 8: Access the Application

It may take a minute for the load balancer to be provisioned and for the external IP address to appear. Once the IP address is available, you can access the application via a browser by visiting the provided IP.


Once the IP address appears, open it in a browser, and you should see the default Nginx page.


## Step 9: Verify the Application

To verify the app is running, you can check the logs of the Nginx container:

```bash
kubectl logs <pod-name>
```

Get the pod name by running:

```bash
kubectl get pods
```

## Step 10: Clean Up Resources

To avoid any ongoing charges, it's important to clean up the resources when you're done. Run the following command to delete the AKS cluster and its associated resources:

```bash
az aks delete --resource-group corso-kubernetes --name cluster-corso --yes --no-wait
```

This will delete the AKS cluster. Additionally, you can delete the resource group if it's no longer needed:

```bash
az group delete --name corso-kubernetes --yes --no-wait
```


## Conclusion

Congratulations! You’ve successfully deployed a simple app on Azure Kubernetes Service (AKS). Here’s a recap of the steps:

1. Set up the Azure CLI and logged into your Azure account.
2. Created a resource group and AKS cluster on Azure.
3. Configured `kubectl` to use the AKS cluster.
4. Created a simple app using Nginx and deployed it on AKS.
5. Exposed the app using a LoadBalancer service and accessed it via a public IP.

Now, you can explore more advanced features of AKS and Kubernetes!