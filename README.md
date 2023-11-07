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


### Create new version

1. change version ```poetry version ``` like `poetry version 0.5.3`
2. create docker ```task build-docker-bot-without-run -- '-p'```  `create production version`
3. create docker ```task build-docker-bot-without-run```  `create test version with`
4. push to docker ```docker image push --all-tags zimkaa/sales_bot```
