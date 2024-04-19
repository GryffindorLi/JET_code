# Justeat Takeaway.com Coding Test

This repo contains the code for Justeat Takeaway.com coding test.

## How to run

### Run in local environment
Optionally, you can create a new python environment using conda:
```
conda create -n justeat python=3.12.2
conda activate justeat
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the code:
```
python main.py
```

For usage:
```
>>> -s/--search <POSTCODE> # Search for first 10 restaurants at the location of <POSTCODE>
>>> -s/--help # Help information
>>> -q/--quit # quit the program
```

### Run in Docker:
First pull the image:
```
docker pull ghcr.io/GryffindorLi/justeat_code_test:latest
```

then run the docker container:
```
docker run -it justeat_code_test
```

## Not-Clear Assumptions

## Improvements