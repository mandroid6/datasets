
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import api_utils
import tensorflow_dataset.public_api as tfds

# class YesNoConfig(tfds.core.BuilderConfig):
# 	"""BuilderConfig for YesNo."""

# 	@api_utils.disallow_positional_args
# 	def __init__(self, data=None, **kwargs):
# 		"""Constructs a YesNoConfig.
# 		Args:
# 		  data: `str`, one of `_DATA_OPTIONS`.
#           **kwargs: keyword arguments forwarded to super.
#         """
# 		    super(YesNoConfig, self).__init__(**kwargs)
#     		self.data = data
_SAMPLE_LENGTH = 48000  # 6 seconds * 8000 samples / second
_DL_URL = "http://www.openslr.org/resources/1/waves_yesno.tar.gz"
class YesNo(tfds.core.GeneratorBasedBuilder):
	"""
	Sixty recordings of one individual saying yes or no in Hebrew; each recording is eight words long.
	"""
	
	_DESCRIPTION ='contains 60 .wav files, sampled at 8 kHz. \
	All were recorded by the same male speaker, in Hebrew. \
	In each file, the individual says 8 words; \
	each word is either the Hebrew for "yes" or "no", \
	so each file is a random sequence of 8 yes-es or noes'

	VERSION = tfds.core.Version('0.1.0')
	
	def _info(self):
		return tfds.core.DatasetInfo(
			builder=self,
			description=_DESCRIPTION,
			features=tfds.features.FeaturesDict({
				"audio":tfds.features.Audio(),
				"text": tfds.features.Text()
			}),
			urls=["http://www.openslr.org/1/"]
		)
		
		
	def _split_generators(self, dl_manager):
		dl_url = _DL_URL
		dl_paths = dl_manager.download_and_extract(dl_urls)
		
		dl_paths[create_and_return_transcript_file
		self.info.features["labels"] = labels

		return [
			tfds.core.SplitGenerator(
				name=tfds.Split.TRAIN,
				num_shards=100,
				gen_kwargs={
					"dirs": dl_paths[tfds.Split.TRAIN],
				}),
			tfds.core.SplitGenerator(
				name=tfds.Split.VALIDATION,
				num_shards=10,
				gen_kwargs={
					"dirs": dl_paths[tfds.Split.VALIDATION],
				}),
			tfds.core.SplitGenerator(
				name=tfds.Split.TEST,
				num_shards=10,
				gen_kwargs={
					"dirs": dl_paths[tfds.Split.TEST],
				}),
		]
		
	def _generate_examples(self):
		pass

	def create_and_return_transcript_file(directory):
		labels = []
		for filename in os.listdir(directory):
    		if filename.endswith('.wav'):
				label =filename.split('.')[0].split('_')
				labels.append(label)

		output_file = open('transcript.txt', 'w')
		for label in labels:
			for ch in label:
				output_file.write(str(ch))
				output_file.write(' ')
			output_file.write('\n')
		output_file.close()

		return os.path.join(directory,'transcript.txt')

	def _walk_yesno_dir(directory):
		"""Walk a YesNo directory and yield examples."""

		directory = os.path.join(directory, 'YesNo')
		
		for path, _, files in tf.io.gfile.walk(directory):
			if not files:
				continue

			


