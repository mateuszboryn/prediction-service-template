# prediction-service-template

Template for deploying prediction services as REST API

# Build and run sample

    docker build . -t prediction-service-template
    docker run  --rm -it -p 80:80 prediction-service-template

Go to:

    http://localhost/prediction?x=2