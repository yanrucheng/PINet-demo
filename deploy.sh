#!/bin/sh
gcloud builds submit --tag gcr.io/pinet-demo/pinetdemo:dev
gcloud run deploy --image gcr.io/pinet-demo/pinetdemo:dev --memory 2G --platform managed
