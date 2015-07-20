TEMPLATE = aux

MER_QDOC.project = mer-qdoc-template
MER_QDOC.config = mer-qdoc-template.qdocconf
MER_QDOC.style = offline
MER_QDOC.path = /usr/share/doc/mer-qdoc-template
MER_QDOC.template = $${PWD}/../config

OTHER_FILES = \
    src/index.qdoc

include(../config/mer-qdoc-template.prf)
