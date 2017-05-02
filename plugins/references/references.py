# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from pelican import signals


class Reference(Directive):
    """A reference.

    Example
    -------
    .. reference:: journal
        :author: A. Einstein, B. Podolsky, and N. Rosen
        :title: Can quantum-mechanical description of physical reality be considered complete?
        :journal: Physical Review
        :volume: 47
        :number: 10
        :pages: 777
        :paper: https://doi.org/10.1103/PhysRev.47.777
    """

    required_arguments = 0
    optional_arguments = 12
    option_spec = {
        'author': directives.unchanged_required,
        'title': directives.unchanged_required,
        'proc': directives.unchanged_required,
        'year': directives.unchanged_required,
        'tail': directives.unchanged_required,
        'paper': directives.unchanged_required,
        'poster': directives.unchanged_required,
        'abstract': directives.unchanged_required,
        'address': directives.unchanged_required,
        'volume': directives.unchanged_required,
        'number': directives.unchanged_required,
        'pages': directives.unchanged_required
    }
    final_argument_whitespace = False
    has_content = False

    def run(self):
        template = pelican_generator.get_template('publication')
        html = template.render(publication=self.options)
        return [nodes.raw('', html, format='html')]


pelican_generator = None
def get_template_env(generator):
    global pelican_generator
    pelican_generator = generator


def register():
    directives.register_directive('reference', Reference)
    signals.generator_init.connect(get_template_env)
