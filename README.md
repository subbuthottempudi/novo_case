# novo_case

docker build . -t sparkhome
docker image ls
docker run --platform linux/amd64 -p 8888:8888 --name spark -d sparkhome


CMD ["python", "./src/AWBShipment_db_loader.py"]
