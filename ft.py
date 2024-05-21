from bertalign import Bertalign

pt_file = "1/xt/!2.txt"
it_file = "1/nerina/!2.txt"

pt = ""
with open(pt_file, "r") as f:
    pt = f.read()

it = ""
with open(it_file, "r") as f:
    it = f.read()

aligner = Bertalign(pt, it)
aligner.align_sents()

aligner.print_sents()
