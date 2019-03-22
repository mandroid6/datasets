import tensorflow_dataset.public_api as tfds

class YesNo(tfds.core.GeneratorBasedBuilder):
	"""
	contains 60 .wav files, sampled at 8 kHz. 
	All were recorded by the same male speaker, in Hebrew. 
	In each file, the individual says 8 words; 
	each word is either the Hebrew for "yes" or "no", 
	so each file is a random sequence of 8 yes-es or noes
	"""
	
	VERSION = tfds.core.Version('0.1.0')
	
	def _info(self):
		pass
		
	def _split_generators(self, dl_manager):
		pass
		
	def _generate_examples(self):
		pas
