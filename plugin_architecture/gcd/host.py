import itertools
import random

import pluggy

from gcd import hookspecs, lib

qual_score_list = {"Quality": 5, "Reuseability": 4, "Interoperability": 3}
quant_score_list = {"Signal Range": 3, "Accuracy": 5, "Response Time": 4}


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
    FAVORITE_QUANTS = ("Money", "Performance", "Energy Usage")

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
            ilities=qual_score_list
        )
        performance_comments = self.hook.gcd_average_score(
            quant=quant_score_list
        )
        print(f"Your Qualitative Attributes. Please consider {', '.join(self.quant)}")
        print(f"Some Qualitative Aspects? Examples for satellite subsystems include: {', '.join(qual_score_list.keys())}")
        print(f"Some Quantitative Aspects? Examples for satellite subsystems include: {', '.join(quant_score_list.keys())}")
        if any(score_comments):
            print("\n".join(score_comments))
        if any(performance_comments):
            print("\n".join(performance_comments))

if __name__ == "__main__":
    main()
