
"""    Test tool for Retrieval.Py code

       Intention: To test and check the relevance of the retrieved chunks
"""

from Retrieval import Retrieval

Retrieval = Retrieval()

retrieved_chunks = Retrieval.devectorizeBM25("I want to shoot a high quality scene, what do i need to do?")


""""error:OSError: Can't load the model for 'BAAI/bge-reranker-large'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'BAAI/bge-reranker-large' is the correct path to a directory containing a file named pytorch_model.bin, tf_model.h5, model.ckpt or flax_model.msgpack."""