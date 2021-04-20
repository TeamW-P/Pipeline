# stops, removes and builds an image for the pipeline
# NOTE: this is to be used ONLY if you intend for the pipeline to be running locally i.e. not public facing
# if you want it to be public facing, use the script deploy_public in the upper directory and refer to the documentation for how to configure for public use

sudo docker container stop pipeline
sudo docker container rm pipeline 

sudo docker build -t pipeline .
sudo docker run -p 5000:5000 -d -t --restart on-failure --network=PipelineNetwork  --name pipeline pipeline 
