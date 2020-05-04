import yaml
import pystache


def main():
    with open('resume-data.yaml') as fd:
        data = yaml.safe_load(fd)
    with open('resume-template.hbs') as fd:
        templ = fd.read()
    rendered = pystache.render(templ, data)
    with open('index.html', 'w') as fd:
        fd.write(rendered)
    print(rendered)
    print('...done')


if __name__ == '__main__':
    main()
