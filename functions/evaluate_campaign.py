from functions.calculate_metrics import calculate_metrics

def evaluate_campaign(campaign, target_cpa, min_ctr):
    """
    Evaluate a campaign and provide recommendations.

    Args:
        campaign (dict): A single campaign's data.
        target_cpa (float): Target cost per acquisition.
        min_ctr (float): Minimum click-through rate.

    Returns:
        dict: Recommendation and associated reasons.
    """
    metrics = calculate_metrics(campaign)
    recommendation = {
        "campaign_id": campaign["Campaign ID"],
        "current_status": campaign["Status"],
        "current_status_reason": "",
        "action": "No Action",
        "reason": "",
        "metrics": metrics
    }

    # Determine reason for current status
    if campaign["Status"] == "Paused":
        if metrics["ROAS"] > 4:
            recommendation[
                "current_status_reason"] = f"Paused despite high ROAS: {metrics['ROAS']:.2f} (Exceeds 4x threshold)"
        elif metrics["CTR"] < min_ctr:
            recommendation[
                "current_status_reason"] = f"Paused due to low CTR: {metrics['CTR']:.2%} (Below {min_ctr:.2%})"
        elif metrics["CPA"] > (3 * target_cpa):
            recommendation[
                "current_status_reason"] = f"Paused due to high CPA: ${metrics['CPA']:.2f} (3x Target ${target_cpa})"
        else:
            recommendation["current_status_reason"] = "Paused by user or system for unspecified reasons."

    elif campaign["Status"] == "Active":
        recommendation["current_status_reason"] = "Campaign is actively running and delivering ads."

    # Evaluate actions
    if metrics["CTR"] < min_ctr:
        recommendation.update({
            "action": "PAUSE",
            "reason": f"Low CTR: {metrics['CTR']:.2%} (Below {min_ctr:.2%})"
        })
    elif metrics["CPA"] > (3 * target_cpa):
        recommendation.update({
            "action": "PAUSE",
            "reason": f"High CPA: ${metrics['CPA']:.2f} (3x Target ${target_cpa})"
        })
    elif metrics["ROAS"] > 4:
        recommendation.update({
            "action": "INCREASE_BUDGET",
            "reason": f"High ROAS: {metrics['ROAS']:.2f} (Exceeds 4x threshold)"
        })
    elif metrics["ROAS"] < 1.5:
        recommendation.update({
            "action": "DECREASE_BUDGET",
            "reason": f"Low ROAS: {metrics['ROAS']:.2f} (Below 1.5x threshold)"
        })

    return recommendation

