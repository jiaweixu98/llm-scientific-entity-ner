from tqdm import tqdm
import pandas as pd

# Create a list to store valid control papers
valid_controls = []
llm_related = filtered_all_arxiv[filtered_all_arxiv['is_llm_related'] == 1]
non_llm_related = filtered_all_arxiv[filtered_all_arxiv['is_llm_related'] == 0]

# Precompute time window (2 months)
time_window = pd.to_timedelta(60, unit='days')

# Iterate over non-LLM-related papers
for idx, control_paper in tqdm(non_llm_related.iterrows(), total=non_llm_related.shape[0]):
    # Filter LLM-related papers within the 2-month window and with matching peer-review status
    candidate_papers = llm_related[
        (abs(llm_related['v1_date'] - control_paper['v1_date']) <= time_window) & 
        (llm_related['is_peer_reviewed'] == control_paper['is_peer_reviewed'])
    ]
    
    # Further filter by CCF level if it exists
    if control_paper['ccf_level'] is not None:
        candidate_papers_temp = candidate_papers[candidate_papers['ccf_level'] == control_paper['ccf_level']]
        if any(candidate_papers_temp['categories_set'].apply(lambda x: x == control_paper['categories_set'])):
            valid_controls.append(idx)
            continue
    
    # Check for identical categories; also the case if we cannot find a match for CCF level
    if any(candidate_papers['categories_set'].apply(lambda x: x == control_paper['categories_set'])):
        valid_controls.append(idx)

# Filter the dataframe to include only valid control papers
filtered_control_papers = non_llm_related.loc[valid_controls]

# Combine the LLM-related papers with the filtered control papers
update_filtered_all_arxiv = pd.concat([llm_related, filtered_control_papers], ignore_index=True)
len(update_filtered_all_arxiv)