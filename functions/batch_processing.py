from concurrent.futures import ThreadPoolExecutor
from functions.evaluate_campaign import evaluate_campaign

def batch_process_campaigns(campaigns, target_cpa, min_ctr):
    def process_campaign(campaign):
        return evaluate_campaign(campaign, target_cpa, min_ctr)

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_campaign, [row for _, row in campaigns.iterrows()]))
    return results
