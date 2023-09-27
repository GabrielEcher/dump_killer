import os

def dmp_killer():
    folder_path = '' # CAMINHO DA PASTA EM QUE OS MINIDUMPS SERÃO EXCLUÍDOS

    for root, dirs, files in os.walk(folder_path): # PERCORRE A RAIZ, PASTAS, SUBPASTAS E ARQUIVOS
        for file_name in files:
            if file_name.endswith('.dmp'): # VERIFICA A EXTENSÃO DO ARQUIVO
                file_path = os.path.join(root, file_name) # FAZ UM JOIN COM A RAIZ DO ARQUIVO E O NOME DELE
                os.remove(file_path) # EXCLUI O ARQUIVO
                           
if __name__ == "__main__":
    dmp_killer()