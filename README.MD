## Speak English bot
#### 0. Requirements
- python 3.10+
- pipenv

#### 1. Setp
1.1 Paste into .env_dev all necessary values.

1.2 Execute commands below. 
This command run local environment
```
pipenv shell  
```
and that will install all necessary dependencies:
```
pipenv sync
```
#### 2. How-to-run
To run script just execute command like that:
```
./start.sh <env> <text message to OpenAI>
```
Example:
```
./start.sh dev "Hi, my name is V and i want you to help me improve my english skills"
```

