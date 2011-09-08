# Extract .tar.* files with unicode filenames.
import tarfile, sys
def convert(members):
    for m in members:
        m.name=unicode(m.name, 'utf8')
        yield m
try:
    tar = tarfile.open(sys.argv[1])
except:
    print("Failed opening %s"%sys.argv[1])
    sys.exit(1)

tar.extractall(members=convert(tar.getmembers()))
tar.close()

