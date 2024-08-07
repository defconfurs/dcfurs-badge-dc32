# For testing: dump the contents of the initfs.
import initfs
import tarfile
import deflate
import errno
import io
import os

def restore(stream):
    print("Restoring initial filesystem")

    def maybe_mkdir(filename):
        if filename[-1] == '/':
            filename = filename[:-1]
        try:
            os.mkdir(filename)
        except OSError as e:
            if e.errno == errno.EEXIST:
                return
            raise e

    with deflate.DeflateIO(stream) as gzfile:
        tf = tarfile.TarFile(fileobj=gzfile)
        for i in tf:
            # Strip the leading directory.
            filename=i.name.split('/', 1)[1]
            if len(filename) == 0:
                continue

            print(filename)
            if i.type == tarfile.DIRTYPE:
                maybe_mkdir(filename)
            else:
                fp = tf.extractfile(i)
                with open(filename, "wb") as outfile:
                    outfile.write(fp.read())

# Automatically restore the filesystem if main.py is missing.
if "main.py" not in os.listdir("/"):
    restore(io.BytesIO(initfs.tarball))

# Cleanup
del initfs, tarfile, deflate, errno, io, os, restore
