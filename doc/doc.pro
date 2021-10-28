TEMPLATE = aux

SAILFISH_QDOC.project = sailfish-qdoc-template
SAILFISH_QDOC.config = sailfish-qdoc-template.qdocconf
SAILFISH_QDOC.style = offline
SAILFISH_QDOC.path = /usr/share/doc/sailfish-qdoc-template
SAILFISH_QDOC.template = $${PWD}/../config

OTHER_FILES = \
    src/index.qdoc

include(../config/sailfish-qdoc-template.prf)
