#!/bin/bash

./scripts/az login --service-principal --username $AZURE_APP_ID --password $AZURE_PASSWORD --tenant $AZURE_TENANT_ID
./scripts/az aks get-credentials --resource-group $AZURE_RESOURCE_GROUP --name $AZURE_CLUSTER_NAME

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl

NAMESPACE="${PROJECT_NAME}-${TAG//./-}"

if ! ./kubectl get namespace "${NAMESPACE}"; then
    ./kubectl create namespace "${NAMESPACE}"
fi

./kubectl apply -f ./k8s/3.ortopedica-api-deployment.yml -n ${NAMESPACE}
