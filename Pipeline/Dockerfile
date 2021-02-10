FROM continuumio/anaconda3

WORKDIR /pipeline

COPY . .

RUN chmod +x boot.sh
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "pipeline_env", "/bin/bash", "-c"]
RUN pip install requests
EXPOSE 5000

ENTRYPOINT ["conda", "run", "-n", "pipeline_env", "./boot.sh"]
