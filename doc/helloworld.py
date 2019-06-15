from docutils import nodes
from docutils.parsers.rst import Directive


class HelloWorld(Directive):

    def run(self):
        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]

class HelloWorld2(Directive):

    def run(self):
        paragraph_node = nodes.paragraph(text='Hello World!'+'...a este')
        return [paragraph_node]


def setup(app):
    app.add_directive("helloworld", HelloWorld)
    app.add_directive("helloworld2", HelloWorld2)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
