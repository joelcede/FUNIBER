import limpiar, colorText

def welcome():
    return """
Bienvenido al Lago Musical. 
Introduce un sonido para conocer los sonidos restantes de la canción.
Tienes estas opciones:
- brr
- birip
- plop
- brrah
- croac
Escribe 'salir' para terminar el programa: 
"""

class LakeMusical:
    def __init__(self):
        self.songs = {
            'brr': ['fiu', 'cric-cric', 'brrah'],
            'birip': ['trri-trri', 'croac'],
            'plop': ['cric-cric', 'brrah'],
            'brrah': [],
            'croac': []
        }

    def play_sounds(self, init_sound):
        TResponse = colorText.TypeResponses()
        remaining_sounds = self.songs.get(init_sound, None)
        if remaining_sounds is not None and remaining_sounds:
            return ', '.join(remaining_sounds)
        elif remaining_sounds == []:
            return ""
        else:
            return TResponse.error("Sonido no reconocido")

def main():
    lake_musical = LakeMusical()
    TResponse = colorText.TypeResponses()
    while True:
        init_sound = input(welcome()).strip()
        if init_sound.lower() == 'salir':
            print(TResponse.generic("Saliendo del Lago Musical."))
            break
        response = lake_musical.play_sounds(init_sound)
        limpiar.limpiar_consola()
        print(TResponse.succes("Respuesta: "+ response))
        
if __name__ == "__main__":
    main()

