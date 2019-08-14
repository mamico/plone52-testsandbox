from plone import api
import os
from plone.namedfile.file import NamedBlobFile


portal = api.portal.get()

if 'largefile' not in portal:
    obj = api.content.create(portal, id="largefile", type="File")
    SIZE = 256 * 1024 * 1024
    obj.file = NamedBlobFile(data=os.urandom(SIZE), filename=u'dummy.bin')

