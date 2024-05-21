from bertalign import Bertalign

pt_file = "1/xt/!10.txt"
it_file = "1/nerina/!10.txt"

pt = ""
with open(pt_file, "r") as f:
    pt = f.read()

it = ""
with open(it_file, "r") as f:
    it = f.read()

aligner = Bertalign(pt, it)
aligner.align_sents()

aligner.print_sents()
