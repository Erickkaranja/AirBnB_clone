#!/usr/bin/python3
'''creating a unique file storage instance for our application.'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
