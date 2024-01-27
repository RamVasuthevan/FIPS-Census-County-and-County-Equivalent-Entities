import unittest
import filecmp
import shutil
import os
from download import download_data  # you might need to adjust this import based on your actual code structure

class TestDownloadOutputs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Copy current output folders and files to a backup location
        cls.backup_dirs = {'2010': 'fips_2010_backup', '2020': 'fips_2020_backup'}
        cls.backup_files = {'2010': 'fips_2010.tsv.backup', '2020': 'fips_2020.tsv.backup'}
        
        for year, backup_dir in cls.backup_dirs.items():
            shutil.copytree(f'fips_{year}', backup_dir)
        
        for year, backup_file in cls.backup_files.items():
            shutil.copy(f'fips_{year}.tsv', backup_file)
        
        # Run the download script
        download_data()

    @classmethod
    def tearDownClass(cls):
        # Clean up: delete backup folders and files
        for backup_dir in cls.backup_dirs.values():
            shutil.rmtree(backup_dir)
        
        for backup_file in cls.backup_files.values():
            os.remove(backup_file)

    def test_directory_contents_unchanged(self):
        for year, backup_dir in self.backup_dirs.items():
            dir_cmp = filecmp.dircmp(f'fips_{year}', backup_dir)
            self.assertListEqual(dir_cmp.diff_files, [], f"Files in fips_{year} have changed.")
    
    def test_file_contents_unchanged(self):
        for year, backup_file in self.backup_files.items():
            with open(f'fips_{year}.tsv', 'r') as f1, open(backup_file, 'r') as f2:
                self.assertEqual(f1.read(), f2.read(), f"Contents of fips_{year}.tsv have changed.")

if __name__ == '__main__':
    unittest.main()
