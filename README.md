# flask-mongo-api
<p>First fork and  create clone of the repo</p>

```bash
  git clone https://github.com/arup1221/flask-mongo-api.git
```
<p>Go to the Directory in your code editor and then Create virtual environment</p>

```bash
  python -m venv venv
```
<p>Update the requrirement.txt (if needed)</p>

```bash
  pip freeze > requirements.txt
```
### Activate the Virtual environment

on windows
```bash
  venv\Scripts\activate
```
on mac/linux
```bash
  source venv/bin/activate
```

### <p>Run the application</p>

```bash
  flask run
```
or (windows) 
```bash
py app.py
```
or (mac/linux)
```bash
    python3 app.py
```
## For Use with docker
<p>first create the Docker image </p>

```bash
  docker build -t myapp-image .
```

<p>Then Run the Image</p>

```bash
  Docker run -p 8000:8000 myapp-image
```
## test screen video google drive link is in the below:-

[Test Screenrecording using Flask run](https://drive.google.com/drive/u/0/folders/1i_pL75t4Q5WeShWQKS6t199Z82iIHWMK).

[Test Screenrecording using Docker Image](https://drive.google.com/drive/u/0/folders/19gWHtjfV-7jR26H5pQqPNj5JI3CGWNzF)

