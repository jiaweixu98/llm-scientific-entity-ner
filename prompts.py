# configration
[components.llm.task]
@llm_tasks = "spacy.NER.v3"
labels = ["KEYWROD", "METHOD", "DATASET", "METRIC", "TOOL", "OTHER_SCIENTIFIC_ENTITY"]
description = "Entities are scientific terms, including the names of keywords, methods, datasets, metrics, tools, and other scientific entities. Adjectives, verbs, adverbs, and pronouns are not entities. If the scientific entity is an abbreviation (e.g., LLMs), use the full name followed by the abbreviation in parentheses (e.g., Large Language Models (LLMs))."

[components.llm.task.label_definitions]
KEYWROD = "**List at least three KEYWROD entities.** These entities represent the **novelty** and **main contributions** of the paper and can be longer keyphrases or keywords. If the KEYWROD entities are not specific, you must briefly annotate them to make them precise and representative of a scientific entity from the paper, use the annotated entities as KEYWORD entities. For example, if the key contributions of the paper are about visualizing attention mechanisms but are expressed as 'visualizing attention' in the provided text, 'visualizing attention' can be annotated as 'visualizing attention mechanism', the extracted KEYWROD should be 'visualizing attention mechanism'. ** KEYWROD entities are the only case where annotations are allowed; never annotate METHOD, DATASET, METRIC, TOOL, or OTHER_SCIENTIFIC_ENTITY entities."
METHOD = "Models, algorithms, techniques, protocols, etc., e.g., Large Language Models (LLMs), ChatGPT, Heuristic Evaluation, Chain of Thought (CoT), Support Vector Machine (SVM), User-Centered Design, Long short-term memory (LSTM),  Bidirectional Encoder Representations from Transformers (BERT), Generative Pre-trained Transformer (GPT), GPT-4v, Transformer Model, Ethnographic Study, Grounded Theory, Eye Tracking."
DATASET = "Corpus, dataset, database, catalog, etc., e.g. ImageNet, Brown Corpus, Penn Treebank, WordNet, Twitter Data, Facebook Social Graph, Human Activity Recognition Dataset, Reddit Comments Dataset"
METRIC = "Indicators which are used to evaluate experimental results. e.g. Accuracy, Precision, Recall, F1-score, BLEU, Usability Score, Task Completion Time, Error Rate, System Usability Scale, NASA-TLX. Specific numbers (e.g., 0.15 seconds, 95.4%) are not considered METRIC scientific entities."
TOOL = "Instruments, programming languages, software, or open-source tools, etc., e.g. Qualtrics, Python, GIZA++, TensorFlow, PyTorch, R language, MATLAB, NVivo, Eye Tracker, Usability Testing Software"
OTHER_SCIENTIFIC_ENTITY = "Any other relevant scientific entities that cannot be classified as METHOD, DATASET, METRIC, TOOL, or KEYWROD. Do not include people's names. Examples: Scaling Law, Uncertainty Quantification, Digital Divide, Net Neutrality."

# prompts
You are an expert Named Entity Recognition (NER) system. Your task is to extract named entities from the Title and Abstract of a paper.
Entities must have one of the following labels: {{ ', '.join(labels) }}.
If a span is not an entity label it: `==NONE==`.
{# whitespace #}
{# whitespace #}
{%- if description -%}
{# whitespace #}
{{ description }}
{# whitespace #}
{%- endif -%}
{%- if label_definitions -%}
Below are definitions of each label to guide you in identifying the correct named entities. Follow these expert-written definitions closely.
{# whitespace #}
{%- for label, definition in label_definitions.items() -%}
{{ label }}: {{ definition }}
{# whitespace #}
{%- endfor -%}
{# whitespace #}
{# whitespace #}
{%- endif -%}
{%- if prompt_examples -%}
Given the paragraph below, identify a list of entities that are highly likely to be desired scientific entities. For each entry, explain why it is or is not an entity. Output entities in the order they occur in the input paragraph, and do not repeat any entity that has already been output.
{# whitespace #}
{# whitespace #}
{%- for example in prompt_examples -%}
Paragraph: {{ example.text }}
Answer:
{# whitespace #}
{%- for span in example.spans -%}
{{ loop.index }}. {{ span.to_str() }}
{# whitespace #}
{%- endfor -%}
{# whitespace #}
{# whitespace #}
{%- endfor -%}
{%- else -%}
{# whitespace #}
Here is an example of the output format for a paragraph using different labels than this task requires.
Use this output format, but use the labels provided above instead of the ones defined in the example below.
Only output entities in this format, and do not include any other information.
Output entities in the order they occur in the input paragraph, and do not repeat any entity that has already been output.

Q: Given the paragraph below, identify a list of entities, and for each entry explain why it is or is not an entity:

Paragraph: Sriracha sauce goes really well with hoisin stir fry, but you should add it after you use the wok.
Answer:
1. Sriracha sauce | True | INGREDIENT | is an ingredient to add to a stir fry
2. really well | False | ==NONE== | is a description of how well sriracha sauce goes with hoisin stir fry
3. hoisin stir fry | True | DISH | is a dish with stir fry vegetables and hoisin sauce
4. wok | True | EQUIPMENT | is a piece of cooking equipment used to stir fry ingredients
{# whitespace #}
{# whitespace #}
{%- endif -%}
Given the paragraph below, identify a list of entities that are highly likely to be desired scientific entities. For each entry, explain why it is or is not an entity. Output entities in the order they occur in the input paragraph, and do not repeat any entity that has already been output.
Paragraph: {{ text }}
Answer:
