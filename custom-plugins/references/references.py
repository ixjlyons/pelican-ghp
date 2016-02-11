# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from pelican import signals

settings = dict()


class Reference(Directive):

    global settings
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'authors': directives.unchanged_required,
        'title': directives.unchanged_required,
        'proc': directives.unchanged_required,
        'year': directives.unchanged_required,
        'tail': directives.unchanged_required
    }
    final_argument_whitespace = False
    has_content = False

    def run(self):
        html = settings['template'].format(**self.options)

        return [
            nodes.raw('', html, format='html')
        ]


def pelican_init(pelicanobj):
    """
    Sets up the user settings for the plugin.
    """
    global settings
    settings['template'] = "<p>{authors}, ({year}), <i>{proc}</i>. {tail}</p>"

    try:
        user_settings = pelicanobj.settings['REFERENCES']
    except KeyError:
        return settings

    for key, value in ((key, user_settings[key]) for key in user_settings):
        settings[key] = value

    return settings


def register():
    signals.initialized.connect(pelican_init)
    directives.register_directive('reference', Reference)
