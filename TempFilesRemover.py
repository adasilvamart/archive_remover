import os
import shutil
import errno

class ArchiveRemover:
    def __init__(self, directory):
        self.__directory = self.validate_directory(directory)

    def get_directory(self):
        return self.__directory

    def validate_directory(self, directory):
        if os.path.exists(directory):
            return directory
        else:
            print('[!] The directory does not exist')

    def list_archives_to_remove(self):
        directory = self.get_directory()
        archives = []
        for archive in os.listdir(directory):
            archive_path = os.path.join(self.get_directory(), archive)
            archives.append(archive_path)
            print(f'{archive}')
        return archives
    
    def remove_archives(self):
        archives = self.list_archives_to_remove()
        for archive in archives:
            try:
                if os.path.isfile(archive):
                    os.remove(archive)
                elif os.path.isdir(archive):
                    shutil.rmtree(archive)
            except Exception as e:
                if isinstance(e, OSError) and e.errno == errno.EACCES:
                    print(f"{archive} it's in use and can't be deleted.")
                    continue
                else:
                    print(f"Error trying to delete the file {archive}: {e}")


if __name__ == '__main__':
                           
    directories = [ """ Add your directories here """ ]
    
    for directory in directories:
        directory_to_remove = ArchiveRemover(directory)
        directory_to_remove.remove_archives()