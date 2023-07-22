# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from jinja2 import Template
from pelican import signals
from pelican.generators import PelicanTemplateNotFound


class Reference(Directive):
    """A reference.

    Example
    -------
    .. reference:: journal
        :author: A. Einstein, B. Podolsky, and N. Rosen
        :title: Can quantum-mechanical description of physical reality be
            considered complete?
        :journal: Physical Review
        :volume: 47
        :number: 10
        :pages: 777
        :doi: 10.1103/PhysRev.47.777
        :pdf: {static}/doc_hosted_on_site.pdf
    """

    # just a basic template: author, title, proc, year.
    template = Template(('{% block reference %}<p>'
                         '{{ reference.author }}, "{{ reference.title }}," '
                         '<i>{{ reference.proc }}</i>, {{ reference.year }}.'
                         '{% endblock %}'))

    required_arguments = 0
    optional_arguments = 12
    option_spec = {
        'author': directives.unchanged_required,
        'title': directives.unchanged_required,
        'proc': directives.unchanged_required,
        'year': directives.unchanged_required,
        'address': directives.unchanged_required,
        'volume': directives.unchanged_required,
        'number': directives.unchanged_required,
        'pages': directives.unchanged_required,
        'doi': directives.unchanged_required,
        'pdf': directives.unchanged_required,
        'poster': directives.unchanged_required,
        'abstract': directives.unchanged_required,
    }
    final_argument_whitespace = False
    has_content = False

    def run(self):
        html = self.template.render(reference=self.options)
        return [nodes.raw('', html, format='html')]


def generator_init_callback(generator):
    try:
        Reference.template = generator.get_template('reference')
    except PelicanTemplateNotFound:
        pass
    directives.register_directive('reference', Reference)


def register():
    signals.generator_init.connect(generator_init_callback)
