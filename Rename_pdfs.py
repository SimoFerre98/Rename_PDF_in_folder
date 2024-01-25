import os

def rename_pdfs_in_folders(base_folder):
    for root, dirs, files in os.walk(base_folder):
        for file_name in files:
            if file_name.lower().endswith('.pdf'):
                folder_name = os.path.basename(root)
                new_file_name = f"{folder_name}.pdf"
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"Rinominato '{old_file_path}' in '{new_file_path}'")

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            print(f"Sono entrato nella directory '{dir_path}'")

# Imposta il percorso della cartella base che contiene le sottocartelle
base_folder_path = r'C:\Users\simon\Downloads\dataset\pdfs'

# Chiama la funzione per rinominare i file PDF in tutte le cartelle nidificate
rename_pdfs_in_folders(base_folder_path)
