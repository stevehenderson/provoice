# Installing Provoice


## Create user database

Create a new `secrets` directory with a file caleld `users.json`:

```
mkdir secrets
cd secrets
touch users.json
```

Add a json arry with your users and passwords:


```
[
	{
		"id": 1,
		"username": "lue",
		"password": "somegoodpassword"
	},
	{
		"id": 2,
		"username": "ben",
		"password": "AnotherGoodPassword"
	}
]
```

## Install the flask service



### Prepare and Activate Python Virtual Environment


```
python --version
```

Ensure it's 3.7 or higher!


```
sudo apt update
sudo apt install python3-venv
```

Now make a virtual environment

```
python3 -m venv ve-api
```

Activate it:

```
source ve-api/bin/activate
```

### Install requirements into the virtual env

Upgrade pip

```
pip install --upgrade pip
```

Install the requirements:

```
pip install -r requirements.txt
```


## Install PM2 service controller

We recommend using [PM2](https://pm2.keymetrics.io/) for easy backend service management.

Install node:

```
sudo npm i -g pm2 
```

Install pm2

```
sudo npm i -g pm2 
```


## Start the API

```
pm2 start "python provoice-api-v2.py"
```

Check

```
curl http://localhost:5000
```

Should return:

```
{
  "description": "Request does not contain an access token", 
  "error": "Authorization Required", 
  "status_code": 401
}
```

### Test Login (curl)

```
curl -H "Content-Type: application/json" -X POST -d '{ "username": "lue", "password": "somegoodpassword" }' http://localhost:5000/auth
```

Should return:

```
{
  "access_token": "eyJ0eXAiOiJKV1...,,,,VaEyXT3OG5YlemXoKw"
}
```

