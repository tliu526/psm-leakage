import pandas as pd

def compute_study_pairs(ps_rct_df):
    """
    Computes pairwise differences between RCT/PS study pairs.
    """
    pair_df = pd.DataFrame()
    for clinic_set, group in ps_rct_df.groupby("clinical_setting"):
        ps_df = group[group['study_type'] == 'PS']
        rct_df = group[group['study_type'] == 'RCT']
        for ps_idx, ps in ps_df.iterrows():
            ps_dict = {
                "ps_study_id": [],
                "rct_study_id": [],
                "rct_year": [],
                "ps_year": [],
                "year_diff": [],
                "rct_est": [],
                "ps_est": [],
                "clinical_setting": [],
                'rct_ci_diff': [],
                'ps_ci_diff': [],
                'rct_upper_ci': [],
                'ps_upper_ci': [],
                "meta_study": []
            }
            for rct_idx, rct in rct_df.iterrows():
                ps_dict['ps_study_id'].append(ps['study_id'])
                ps_dict['rct_study_id'].append(rct['study_id'])
                ps_dict['ps_year'].append(ps['year'])
                ps_dict['rct_year'].append(rct['year'])
                ps_dict['year_diff'].append(ps['year'] - rct['year'])
                ps_dict['rct_est'].append(rct['estimate'])
                ps_dict['ps_est'].append(ps['estimate'])
                ps_dict['clinical_setting'].append(ps['clinical_setting'])
                ps_dict['rct_ci_diff'].append(rct['ci_diff'])
                ps_dict['ps_ci_diff'].append(ps['ci_diff'])
                ps_dict['rct_upper_ci'].append(rct['upper_ci'])
                ps_dict['ps_upper_ci'].append(ps['upper_ci'])
                ps_dict['meta_study'].append(ps['meta_study'])

            
            df = pd.DataFrame.from_dict(ps_dict)
            pair_df = pair_df.append(df)

    return pair_df