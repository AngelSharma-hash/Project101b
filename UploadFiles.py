from locale import locale_alias
import dropbox
import os
class TransferData:
    def __init__(self, access_token): 
         self.access_token = access_token
    def upload_file(self):
        dbx = dropbox.Dropbox(self.access_token)
        file_from = str(input("Enter the file path"))
        local_path = ""
        file_to = str(input("Enter where the file needs to go"))
        for root, dirs, files in os.walk(file_from):
            #print("Files:",files)
            for name in files:
                local_path = os.path.join(root,name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path,"rb") as f:
                    dbx.files_upload(f.read(), dropbox_path)

            #relative_path = os.path.relpath(local_path, file_from)
            #dropbox_path = os.path.join(file_to, relative_path)
        #for name in files:
           # with open(local_path, 'rb') as f:
             #   dbx.files_upload(f.read(), dropbox_path, mode-WriteMode('overwrite'))
           # local_path = os.path.join(root,name)

        
def main():
    uploadfilesobject = TransferData("sl.BM3wlRIvgRTNr0gRE-Iujzv9ALts1ovEoQ1IZgZ9FObFKDNC3lZpL7UrABF2gUE94NSc1lGq69RoqLtidr1AyuKALKAfVDPq6SFpOpyuPTzVfSosAUTX0Rhxz6n_EhIDP2_c0FY")
    uploadfilesobject.upload_file()
main()
print("File uploaded")

