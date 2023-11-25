def apagarArquivo(pasta, arquivo):
    import os

    arquivos = os.listdir(pasta)

    if arquivo in arquivos:
        os.remove(pasta + arquivo)
