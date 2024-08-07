# For testing: dump the contents of the initfs.
import initfs
import tarfile
import deflate
import io

print("Hello World from boot.py")

# Decompress and unpack the initial tarball.
with deflate.DeflateIO(io.BytesIO(initfs.tarball)) as fp:
    for fileinfo in tarfile.TarFile(fileobj=fp):
        print(fileinfo.name)

print("Goodbye from boot.py")

# Cleanup
del initfs, tarfile, deflate, io
