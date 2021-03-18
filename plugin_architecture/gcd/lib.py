import gcd

@gcd.hookimpl
def gcd_pair_ilities():
    architecture_attributes = ["Loosely-Coupled", "Low-Cohesion"]
    primary_quality_attributes = ["Synergy", "Maturity"]
    pairing = architecture_attributes + primary_quality_attributes
    return pairing


@gcd.hookimpl
def gcd_ilities_score(ilities):
    ilities["Bandwidth"] = 5
