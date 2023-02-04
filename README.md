### Small example REST API tests by https://reqres.in. ATTENTION: WORK IN PROGRESS 
## [docker file](https://hub.docker.com/repository/docker/jeanskypoor/rest_api_example)
## [The latest allure report](https://jeanskypoor.github.io/REST_API_Example/)
## How to start:
```sh
git clone https://github.com/JeanSkyPoor/REST_API_Example
pip install -r requirements.txt
pytest --alluredir report test_api.py
allure serve report/
```