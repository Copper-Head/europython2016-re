import os
import http.server
import socketserver
import argparse

from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('source'))


def build():
    template = template_env.get_template('index.html')
    rendered_template = template.render()
    with open('presentation/index.html', 'w') as fh:
        fh.write(rendered_template)


def serve():
    os.chdir('presentation')
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("serving at port", PORT)
    httpd.serve_forever()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('action', default='build', nargs='?')
    args = parser.parse_args()
    if args.action == 'serve':
        serve()
    else:
        build()
