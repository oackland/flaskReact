to create react with vite run this:

```bash

npx create-vite@latest my-react-app --template react-ts
```

- cd my-react-app
- npm install
- npm run dev

### STRUCTURE
```text
root = flaskReact/
basedir = root/app/

compose = basedir/docker-compose.yml

docker = basedir/docker/

python_docker = docker/python-app/

python_dockerfile = python_docker/Dockerfile entrypoint.sh

react_docker = docker/react-app/

react_dockerfile = react_docker/Dockerfile entrypoint.sh
```

```scss
flaskReact/ (root)
└── app/ (basedir)
    ├── docker/
    │   ├── python-app/
    │   │   ├── Dockerfile
    │   │   └── entrypoint.sh
    │   └── react-app/
    │       ├── Dockerfile
    │       └── entrypoint.sh
    ├── flask_app/
    ├── my-react-app/
    └── docker-compose.yml
```
