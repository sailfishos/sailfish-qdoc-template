TEMPLATE = subdirs
SUBDIRS += config doc

config.CONFIG += no_docs_target no_install_docs_target

prepareRecursiveTarget(docs)
prepareRecursiveTarget(install_docs)
QMAKE_EXTRA_TARGETS += docs install_docs

OTHER_FILES += \
    rpm/sailfish-qdoc-template.spec
