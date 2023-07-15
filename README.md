# Rotary Embedding TF


Description: A tensorflow implementation of Lucidrain's [rotary-embedding-torch](https://github.com/lucidrains/rotary-embedding-torch) repo.


### Notes:


### Status 

 * WIP: Just started working on it.


### References:

 - ROFORMER: ENHANCED TRANSFORMER WITH ROTARY POSITION EMBEDDING ((original white paper)[https://arxiv.org/pdf/2104.09864.pdf])
 - Paperswithcode (page)[https://paperswithcode.com/paper/roformer-enhanced-transformer-with-rotary] on the Roformer
 - Huggingface Roformer (model documentation)[https://huggingface.co/docs/transformers/model_doc/roformer]
 - Huggingface Roformer (model code)[https://github.com/huggingface/transformers/tree/main/src/transformers/models/roformer]
     - Sourced from (JunnYu's)[https://huggingface.co/junnyu] (repo)[https://github.com/JunnYu/RoFormer_pytorch/tree/roformer_v2]
 - EleutherAI (blog)[https://blog.eleuther.ai/rotary-embeddings/] on Rotary Embeddings
 - Relative position embedding implementation in (Bert4Keras)[https://github.com/bojone/bert4keras/blob/master/bert4keras/layers.py#L904] with Tensorflow and the related (white paper)[https://arxiv.org/pdf/1803.02155.pdf]
 - Roformer (implementation)[https://github.com/ZhuiyiTechnology/roformer] referenced in Huggingface Roformer model documentation (uses Bert4Keras in the backend)
 - Lucidrain's rotary embedding in pytorch (repo)[https://github.com/lucidrains/rotary-embedding-torch]
    - Tensorflow (implementation)[https://github.com/AryaAftab/rotary-embedding-tensorflow] of Lucidrain's repo
