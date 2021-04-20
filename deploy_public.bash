# stops, removes and builds an image for the pipeline
# NOTE: this is only meant to be used if you are deploying the pipeline for public usage (i.e. it will be hosted on the VM address)
# see documentation for how to set this up
# if you are just trying to run the pipeline based on its launch configuration, this is not the right script!

sudo docker container stop pipeline
sudo docker container rm pipeline 

sudo docker container stop reverse_proxy
sudo docker container rm reverse_proxy 

sudo docker-compose build
sudo docker-compose up -d  