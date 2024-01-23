import os
import shutil

def clear_fivem_cache():
    cache_path = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app', 'cache')
    browser_path = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app', 'browser')

    try:
        shutil.rmtree(cache_path)
        shutil.rmtree(browser_path)
        print('Cache effacé avec succès.')
    except Exception as e:
        print(f"Erreur lors de l'effacement du cache : {e}")

if __name__ == "__main__":
    clear_fivem_cache()
    input("Appuyez sur Entrée pour quitter.")
