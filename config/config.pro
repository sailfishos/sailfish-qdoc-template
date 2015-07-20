TEMPLATE = aux

config.files = \
    offline.qdocconf \
    common.qdocconf \
    fileextensions.qdocconf \
    mer-html-templates.qdocconf \
    mer-html-default-styles.qdocconf
config.path = $$[QT_INSTALL_DOCS]/mer-qdoc-template

images.files = \
    images/breadcrumb.png \
    images/bullet_dn.png \
    images/bullet_gt.png \
    images/bullet_sq.png \
    images/bullet_up.png
images.path = $$[QT_INSTALL_DOCS]/mer-qdoc-template/images

styles.files = \
    style/offline.css
styles.path = $$[QT_INSTALL_DOCS]/mer-qdoc-template/style

feature.files = mer-qdoc-template.prf
feature.path = $$[QT_INSTALL_DATA]/mkspecs/features

INSTALLS += config images styles feature

OTHER_FILES = \
    $$config.files \
    $$images.files \
    $$styles.files \
    $$feature.files
