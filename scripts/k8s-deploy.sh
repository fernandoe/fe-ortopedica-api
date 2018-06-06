#!/bin/bash

kubectl create namespace "${PROJECT_NAME}-${TAG//./-}"
