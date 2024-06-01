###########################################################################
###							    		###
### 		@title Baby Shark pour l'Ecole Lina Ritter  		###
### 		@date 2024-MAY-06		       	    		###
### 		@author Cédric Ramassamy		    		###
###					 		    		###
###########################################################################

# Import de la bibliothèque des fonctions mathématiques.
import numpy as np
# Import de la bibliothèque des fonctions de gestion des sons.
import sounddevice as sd

# Définition de la fonction d'éxécution de la bande son.
def sound(x,z):
	frequency = x # Fréquence correspondant à la note (ex.: le LA du téléphone: 440 Hz)
	fs = 44100  # 44100 échantillons par seconde
	seconds = z  # Durée de la note en seconde
	# Génération d'un tableau avec les produits de secondes par la fréquence d'échantillonnage.
	# (de 0 au nombre z de secondes)
	t = np.linspace(0, seconds, int(seconds * fs), False)
	# Génération d'une onde sinusoïdale numérique.
	note = np.sin(frequency * t * 2 * np.pi)
	# Garantir que la valeur la plus haute reste dans la bande des 16-bit.
	audio = note * (2**15 - 1) / np.max(np.abs(note))
	# Conversion en valeur 16-bit.
	audio = audio.astype(np.int16)
	# Jouer le son
	sd.play(audio, fs)
	# Attendre que le son soit joué en entier avant de quitter.
	sd.wait()

# Calcul du multiplicateur pour sélectionner l'octave.
octave_multi = 2 * 6

# Définition des notes par leur fréquences à l'octave 0.
C  = 32.70 #Hz - DO
D  = 36.71 #Hz - RE
E  = 41.20 #Hz - MI
F  = 43.65 #Hz - FA
Fd = 46.25 #Hz - FA#
G  = 49.00 #Hz - SOL
A  = 55.00 #Hz - LA
B  = 61.74 #Hz - SI

# Définition de la partition musicale (suite de paires: Note, Durée)
baby_shark_notes=[
			[D,1/2], [E,1/2], [G,1/4], [G,1/4], [G,1/4], [G,1/8], [G,1/8], [G,1/8], [G,1/2],
			[D,1/2], [E,1/2], [G,1/4], [G,1/4], [G,1/4], [G,1/8], [G,1/8], [G,1/8], [G,1/2],
			[D,1/2], [E,1/2], [G,1/4], [G,1/4], [G,1/4], [G,1/8], [G,1/8], [G,1/8], [G,1/8], [G,1/4], [G,1/4], [Fd,1/4],
		]

# Boucle pour parcourir et jouer toutes les notes de façon séquentielle.
for note, duration in baby_shark_notes :
	# print ( note * octave_multi, duration )
	sound ( note * octave_multi, duration )
