import itertools
import random

import pluggy

from gcd import hookspecs, lib

score_list = {"Quality": 5, "Accuracy": 4, "Response Time": 6}


def main():
    pm = get_plugin_manager()
    do = Ility_Manager(pm.hook)
    do.add_ilities()
    do.shuffle_ilities()
    do.return_ilities()


def get_plugin_manager():
    pm = pluggy.PluginManager("gcd")
    pm.add_hookspecs(hookspecs)
    pm.load_setuptools_entrypoints("gcd")
    pm.register(lib)
    return pm


class Ility_Manager:
    FAVORITE_QUANTS = ("Cost", "Performance", "Energy Usage")

    def __init__(self, hook):
        self.hook = hook
        self.quant = None

    def add_ilities(self):
        results = self.hook.gcd_pair_ilities(
            quant=self.FAVORITE_QUANTS
        )
        my_ilities = list(self.FAVORITE_QUANTS)
        # each hook returns a list - so we chain this list of lists
        other_ilities = list(itertools.chain(*results))
        self.quant = my_ilities + other_ilities

    def shuffle_ilities(self):
        random.shuffle(self.quant)

    def return_ilities(self):
        score_comments = self.hook.gcd_ilities_score(
            ilities=score_list
        )
        print(f"Your Qualitative Attributes. Please consider {', '.join(self.quant)}")
        print(f"Some Quantitative Aspects? Examples for satellite subsystems include: {', '.join(score_list.keys())}")
        if any(score_comments):
            print("\n".join(score_comments))


if __name__ == "__main__":
    main()
