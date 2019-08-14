from plone import api
import os
from plone.namedfile.file import NamedBlobFile
import sys
import transaction


portal = api.portal.get()

SIZE = 1024 * 1024 * 1024
if 'largefile' not in portal:
    obj = api.content.create(portal, id="largefile", type="File")
    obj.file = NamedBlobFile(data=os.urandom(SIZE), filename=u'dummy.bin')
elif '--overrides' in sys.argv:
    obj = portal.largefile
    obj.file = NamedBlobFile(data=os.urandom(SIZE), filename=u'dummy.bin')

if '--commit' in sys.argv:
    transaction.commit()

