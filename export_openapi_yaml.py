import yaml
from main import app

if __name__ == "__main__":
    spec = app.openapi()
    with open("./specs/openapi.yaml", "w") as f:
        yaml.dump(spec, f, sort_keys=False)
