import gcd


@gcd.hookimpl
def gcd_pair_ilities(quant):
    """Here the caller expects us to return a list."""
    if "Cost" in quant:
        feedback = ["Budget-Derived", "Manage-Budget"]
    else:
        feedback = ["Needs-Financial-Analysis", "Do-Feasibility-Study"]
    return feedback


@gcd.hookimpl
def gcd_ilities_score(ilities):
    """Here the caller passes a mutable object, so we mess with it directly."""
    try:
        del ilities["Sustainability"]
    except KeyError:
        pass
    ilities["Extensibility"] = 42
    return "This looks like a system engineering problem..."

@gcd.hookimpl
def gcd_average_score(score):
    """Here the caller expects us to return a list."""
    score = "Performance" 
    if "Performance" in score:
        designer1_score = 5
        designer2_score = 4
        designer3_score = 4
        average_score = (designer1_score + designer2_score + designer3_score)/3
        feedback = print("The average score for Performance is {}" .format(average_score))

    else:
        feedback = "Do-Performance-Scoring" 
    return feedback
