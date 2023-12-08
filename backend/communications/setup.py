import os
"""
SETUP
"""

PORT = 23455

USE_CACHING = False
CACHE_LIMIT = 1024  # The maximum allowed size of cache in MB
CACHE_DISALLOW = []  # Disallowed file extensions (for cache)

localdata = os.getenv('LOCALAPPDATA') + "\\leaDAW"
print(localdata)
if os.path.exists(localdata):
    print("Assuming all files exist")
else:
    os.mkdir(localdata)

