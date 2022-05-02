build:
	docker build -t clean_code_workshop .

env-start:
	docker run -ti --rm --name clean_code_workshop -v $(PWD)/vending_machine:/app/vending_machine clean_code_workshop bash
