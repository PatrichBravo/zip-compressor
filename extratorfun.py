import zipfile
import pathlib
            
def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath,'r') as archive:
        archive.extractall(dest_dir)

               
if __name__ == "__main__":
    extract_archive("/Users/patrichbravo/Desktop/Udemy/Python/zip compressor/extratorfun.zip",
                    "/Users/patrichbravo/Desktop/Udemy/Python/zip compressor")