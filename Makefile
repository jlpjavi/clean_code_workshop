build:
	docker build -t clean_code_workshop .

env-start:
	docker run -ti -v $(PWD)/vending_machine:/app/vending_machine clean_code_workshop bash