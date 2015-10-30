# Pipe pipe_125e9fe8bb5f84526d21bebfec3ad116 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipetextinput import pipe_textinput
from pipe2py.modules.pipeitembuilder import pipe_itembuilder
from pipe2py.modules.pipeurlbuilder import pipe_urlbuilder
from pipe2py.modules.pipeloop import pipe_loop
from pipe2py.modules.pipefetchdata import pipe_fetchdata
from pipe2py.modules.pipeloop import pipe_loop
from pipe2py.modules.piperename import pipe_rename
from pipe2py.modules.pipeoutput import pipe_output


def pipe_125e9fe8bb5f84526d21bebfec3ad116(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return [(u'', u'textinput1', u'Enter Text', u'text', u'defunkt')]

    if context and context.describe_dependencies:
        return [u'pipefetchdata', u'pipeitembuilder', u'pipeloop', u'pipeoutput', u'piperename', u'pipetextinput', u'pipeurlbuilder']

    forever = pipe_forever()

    # We need to wrap submodules (used by loops) so we can pass the
    # input at runtime (as we can to subpipelines)
    def pipe_sw_72(context=None, _INPUT=None, conf=None, **kwargs):
        # todo: insert submodule description here
        return pipe_urlbuilder(context, _INPUT, conf=conf)

    # We need to wrap submodules (used by loops) so we can pass the
    # input at runtime (as we can to subpipelines)
    def pipe_sw_150(context=None, _INPUT=None, conf=None, **kwargs):
        # todo: insert submodule description here
        return pipe_fetchdata(context, _INPUT, conf=conf)

    sw_479 = pipe_textinput(
        context, forever, conf={'debug': {'type': 'text', 'value': 'defunkt'}, 'default': {'type': 'text', 'value': 'defunkt'}, 'prompt': {'type': 'text', 'value': 'Enter Text'}, 'name': {'type': 'text', 'value': 'textinput1'}, 'position': {'type': 'number', 'value': ''}})

    sw_467 = pipe_itembuilder(
        context, forever, conf={'attrs': [{'value': {'terminal': 'attrs_1_value', 'type': 'text'}, 'key': {'type': 'text', 'value': 'title'}}]}, attrs_1_value=sw_479)

    sw_61 = pipe_loop(
        context, sw_467, embed=pipe_sw_72, conf={'assign_part': {'type': 'text', 'value': 'all'}, 'assign_to': {'type': 'text', 'value': 'api'}, 'emit_part': {'type': 'text', 'value': 'all'}, 'mode': {'type': 'text', 'value': 'assign'}, 'embed': {'type': 'module', 'value': {'type': 'urlbuilder', 'id': 'sw-72', 'conf': {'BASE': {'type': 'text', 'value': 'https://api.github.com/search/users'}, 'PARAM': [{'value': {'type': 'text', 'subkey': 'title'}, 'key': {'type': 'text', 'value': 'q'}}]}}}, 'with': {'type': 'text', 'value': ''}})

    sw_142 = pipe_loop(
        context, sw_61, embed=pipe_sw_150, conf={'assign_part': {'type': 'text', 'value': 'first'}, 'assign_to': {'type': 'text', 'value': 'info'}, 'mode': {'type': 'text', 'value': 'assign'}, 'embed': {'type': 'module', 'value': {'type': 'fetchdata', 'id': 'sw-150', 'conf': {'URL': {'type': 'url', 'subkey': 'api'}, 'path': {'type': 'text', 'value': 'items'}}}}, 'with': {'type': 'text', 'value': ''}})

    sw_351 = pipe_rename(
        context, sw_142, conf={'RULE': [{'field': {'type': 'text', 'value': 'language.0.content'}, 'op': {'type': 'text', 'value': 'copy'}, 'newval': {'type': 'text', 'value': 'description'}}]})

    _OUTPUT = pipe_output(
        context, sw_351, conf={})

    return sw_142


if __name__ == "__main__":
    pipeline = pipe_125e9fe8bb5f84526d21bebfec3ad116(Context())

    for i in pipeline:
        print i
