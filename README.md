# LLM NER Task

This task involves Named Entity Recognition (NER) for Large Language Models (LLMs). The script `prompts.py` is used to instruct the LLM (GPT-4o-mini) to identify and categorize entities in given text inputs.

## Example

**Input Title and Abstract:**

**Title:** Visualizing Attention in Transformer-Based Language Representation Models  
**Abstract:** We present an open-source tool for visualizing multi-head self-attention in Transformer-based language representation models. The tool extends earlier work by visualizing attention at three levels of granularity: the attention-head level, the model level, and the neuron level. We describe how each of these views can help to interpret the model, and we demonstrate the tool on the BERT model and the OpenAI GPT-2 model. We also present three use cases for analyzing GPT-2: detecting model bias, identifying recurring patterns, and linking neurons to model behavior.

**GPT Outputs:**

1. **Visualizing Attention** | True | KEYWORD | This phrase represents the main contribution of the paper, focusing on the visualization aspect of attention mechanisms in models.
2. **Transformer-Based Language Representation Models** | True | KEYWORD | This phrase describes the type of models being analyzed and is a significant aspect of the paper's contributions.
3. **open-source tool** | False | ==NONE== | This is a general term and does not specify a particular tool or scientific entity.
4. **multi-head self-attention** | True | METHOD | This is a specific technique used in Transformer models for attention mechanisms.
5. **BERT model** | True | METHOD | BERT (Bidirectional Encoder Representations from Transformers) is a well-known model in natural language processing.
6. **OpenAI GPT-2 model** | True | METHOD | GPT-2 (Generative Pre-trained Transformer 2) is another well-known model in natural language processing.
7. **detecting model bias** | True | KEYWORD | This phrase represents a specific use case of the tool, highlighting a significant aspect of the analysis performed in the paper.
8. **identifying recurring patterns** | True | KEYWORD | This phrase describes another use case of the tool, emphasizing its application in analyzing model behavior.
9. **linking neurons to model behavior** | True | KEYWORD | This phrase represents a third use case of the tool, showcasing its relevance in understanding model dynamics.

**Final Outputs:**

- **Entity 1:** Type: KEYWORD, Name: Visualizing Attention
- **Entity 2:** Type: KEYWORD, Name: Transformer-Based Language Representation Models
- **Entity 3:** Type: METHOD, Name: BERT model
- **Entity 4:** Type: METHOD, Name: OpenAI GPT-2 model
- **Entity 5:** Type: KEYWORD, Name: detecting model bias
- **Entity 6:** Type: KEYWORD, Name: identifying recurring patterns
- **Entity 7:** Type: KEYWORD, Name: linking neurons to model behavior
