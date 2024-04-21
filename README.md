# Justeat Takeaway.com Coding Test

This repo contains the code for Justeat Takeaway.com coding test.

## Setting up environment.

### In local environment
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

### In Docker:
First pull the image:
```
docker pull ghcr.io/GryffindorLi/justeat_code_test:latest
```

then run the docker container:
```
docker run -it justeat_code_test
```

## Usage
For usage:
```
>>> -s/--search <POSTCODE> # Search for first 10 restaurants at the location of <POSTCODE>
>>> -s/--help # Help information
>>> -q/--quit # quit the program
```

## Assumptions & Not-Clear Things
1. Whether the data is updated frequently, or the data is seldom updated? I assume the data is not frequently updated, thus a local cache is used to improve the speed.
2. Is there any rate limiting and quotas for this API. I assumpe there is no rate limiting and quotas for this API. However, it's important to follow the rules if there is one.

## Improvements
1. The first improvement I made is to cache the query results so the responseness of the repeat queries is improved. I use the @lru_cache in Python for now, and we could further cache it using a database.
2. To ensure the consistence of the running environment, I orchestrated the code using a Docker container. In this way, there is no need to install the dependencies locally and the service becomes more manageable.
3. Besides the source code and the testing code, I also configured the lint and code-style for the clearness of the code.