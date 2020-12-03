import yaml
import json

def main():
    with open('familia.yml') as f:
        info = yaml.safe_load(f)
    with open('familia.json', 'w', encoding='utf8') as f:
        json.dump(info, f, ensure_ascii=False);


if __name__ == '__main__':
    main()