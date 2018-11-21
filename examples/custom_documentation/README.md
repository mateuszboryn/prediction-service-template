# Custom documentation example

# Meaning of files

* model_serialization_example.py - Python script to train sample model and serialize it with pickle to file *model.pkl*
* model.pkl - serialized model
* predictive_model.py - customized *predict* and *calculate_features* functions    
* documentation.py - swagger documentation customizations

## Build image

    docker build . -t prediction-service-custom-documentation

## Run docker container

    docker run  --rm -it -p 80:80 prediction-service-custom-documentation

## Check in internet browser

    http://localhost/prediction?x=2