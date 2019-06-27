TEMPLATE = aux

# note: not $$[QT_INSTALL_DOCS]/mer-qdoc-template
# since the sdk prevents installing to /usr/share/doc
DOC_INSTALL_PATH = /usr/share/mer-qdoc-template

config.files = \
    offline.qdocconf \
    common.qdocconf \
    fileextensions.qdocconf \
    qt-cpp-defines.qdocconf \
    mer-html-templates.qdocconf \
    mer-html-default-styles.qdocconf
config.path = $$DOC_INSTALL_PATH

images.files = \
    images/breadcrumb.png \
    images/bullet_dn.png \
    images/bullet_gt.png \
    images/bullet_sq.png \
    images/bullet_up.png
images.path = $$DOC_INSTALL_PATH/images

styles.files = \
    style/offline.css
styles.path = $$DOC_INSTALL_PATH/style

feature.files = mer-qdoc-template.prf
feature.path = $$[QT_INSTALL_DATA]/mkspecs/features

INSTALLS += config images styles feature

OTHER_FILES = \
    $$config.files \
    $$images.files \
    $$styles.files \
    $$feature.files
