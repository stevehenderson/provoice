# Installing Provoice

Install node:

```
sudo npm i -g pm2 
```

Install pm2

```
sudo npm i -g pm2 
```


## Prepare and Activate Python Virtual Environment


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

Upgrade pip

```
pip install --upgrade pip
```

Install the requirements:

```
pip install -r requirements.txt
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

## Login (curl)

```
curl -H "Content-Type: application/json" -X POST -d '{ "username": "<user>", "password": "<some-password>" }' http://localhost:5000/auth
```

Should return:

```
{
  "access_token": "eyJ0eXAiOiJKV1...,,,,VaEyXT3OG5YlemXoKw"
}
```

