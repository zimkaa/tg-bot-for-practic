# Python telegram bot for sales

- [x] Instagram link
- [x] Photo
- [x] Button Emoji
- [ ] Delete all unnecessary
- [x] Add admin chatID
- [x] Start on new bot
- [x] Create universal script to get picture file_id number
- [x] Create universal script to get user ID
- [x] Other button
- [x] Personalize message about payment
- [ ] Add github actions

## Create new version

1. Change version like `poetry version 0.5.3`

    ```sh
    poetry version 
    ```

2. Create docker `create production version`

    ```sh
    task build-docker-bot-without-run -- '-p'
    ```

3. Create docker `create test version with`

    ```sh
    task build-docker-bot-without-run
    ```

4. Push container to docker registry

    ```sh
    docker image push --all-tags zimkaa/sales_bot
    ```

    or

    ```sh
    task push-docker-container
    ```

## Run on server

1. Stop old container

    ```sh
    docker stop [CONTAINER_NAME]
    ```

2. Check it by

    ```sh
    docker ps
    ```

3. Run new version

    ```sh
    docker run --env-file [ENV_PATH] -d zimkaa/sales_bot:[NEW_VERSION]
    ```
