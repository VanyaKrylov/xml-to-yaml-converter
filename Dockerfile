FROM ubuntu:16.04
RUN apt update && apt install -y --no-install-recommends python3.5 python3-pip && apt clean && rm -rf /vat/lib/apt/lists/*
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install Flask==0.10.1
RUN pip3 install xmltodict==0.11.0
RUN pip3 install PyYAML==3.13
ENTRYPOINT ["python3"]
CMD ["app.py"]
