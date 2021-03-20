import pluggy

hookspec = pluggy.HookspecMarker("gcd")


@hookspec
def gcd_pair_ilities(quant: tuple):
    """Have a look at the pairings and edit.
    :param scores: the pairing, don't touch them!
    :return: a list of ility pairings
    """


@hookspec
def gcd_ilities_score(ilities: dict):
    """Reorganize the ilities tray to your heart's content.
    :param ilities: some QAs and stuff
    :return: a witty comment about your activity
    """

@hookspec
def gcd_average_score(score: dict):
    """Reorganize the ilities tray to your heart's content.
    :param ilities: some QAs and stuff
    :return: a witty comment about your activity
    """
