### Setup

```
Create .env in same dir

docker build -t sadhguru-gpt .

docker run -it --env-file ./.env sadhguru-gpt

docker-compose up -d
```