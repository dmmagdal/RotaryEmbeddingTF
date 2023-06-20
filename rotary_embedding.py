# rotary_embedding.py


from math import pi, log
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# Helper functions.
def exists(val):
	return val is not None


def broadcat(tensors, axis=-1):
	num_tensors = len(tensors)
	shape_lens = set(list(map(lambda t: len(t.shape), tensors)))
	assert len(shape_lens) == 1, 'tensors must all have the same number of dimensions'
	shape_len = list(shape_lens)[0]

	axis = (axis + shape_len) if axis < 0 else axis
	dims = list(zip(*map(lambda t: list(t.shape), tensors)))

	expandable_dims = [(i, val) for i, val in enumerate(dims) if i != axis]
	assert all([*map(lambda t: len(set(t[1])) <= 2, expandable_dims)]), 'invalid dimensions for broadcastable concatentation'
	max_dims = list(map(lambda t: (t[0], max(t[1])), expandable_dims))
	expanded_dims = list(
		map(lambda t: (t[0], (t[1],) * num_tensors), max_dims)
	)
	expanded_dims.insert(axis, (axis, dims[axis]))
	expandable_shapes = list(zip(*map(lambda t: t[1], expanded_dims)))
	tensors = list(
		map(lambda t: t[0].expand(*t[1]), zip(tensors, expandable_shapes))
	)
	return tf.concat(tensors, axis=axis)


# Rotary embedding helper functions.
def rotate_half():
	pass


def apply_rotary_emb(freqs, t, start_index=0, scale=1.0):
	freqs = freqs.to(t)
	rot_dim = freqs.shape[-1]
	end_index = start_index + rot_dim
	assert rot_dim <= t.shape[-1], f'feature dimension {t.shape[-1]} is not of sufficient size to rotate in all the positions {rot_dim}'
	t_left, t, t_right = t[..., :start_index], t[..., start_index:end_index], t[..., end_index:]
	t = (t * tf.math.cos(freqs) * scale) + (rotate_half(t) * tf.math.sin(freqs) * scale)
	return tf.concat((t_left, t, t_right), axis=-1)


# Learned rotation helpers.
def apply_learned_rotations():
	pass


# Classes.
class RotaryEmbedding(layers.Layer):
	def __init__(self, axis, custom_freqs=None, freqs_for='lang',
			theta=10000, max_freq=10, num_freqs=1, learned_freq=False,
			use_xpos=False, xpos_scale_base=512,):
		super(RotaryEmbedding, self).__init__()
		if exists(custom_freqs):
			freqs = custom_freqs
		elif freqs_for == 'lang':
			freqs = 1. / (theta ** (torch.arange(0, axis, 2)[:(axis // 2)].float() / axis))
		elif freqs_for == 'pixel':
			freqs = torch.linspace(1., max_freq / 2, axis // 2) * pi
		elif freqs_for == 'constant':
			freqs = tf.ones(num_freqs, dtype=tf.float32)
		else:
			raise ValueError(f'unknown modality {freqs_for}')
		pass


	def rotate_queries_or_keys(self, ):
		pass


	def rotate_queries_and_keys(self, ):
		pass


	def get_scale(self, ):
		pass


	def call(self, ):
		pass