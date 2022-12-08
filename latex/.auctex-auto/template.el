(TeX-add-style-hook
 "template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "UTF8")))
   (TeX-run-style-hooks
    "latex2e"
    "preamble"
    "macros"
    "letterfonts"
    "report"
    "rep10"
    "CJKutf8"
    "xeCJK"
    "CJK")
   (TeX-add-symbols
    '("zht" 1))
   (LaTeX-add-labels
    "n:1"
    "n:2"
    "n:3"
    "pnorm"
    "exs1")
   (LaTeX-add-environments
    '("myclaim" LaTeX-env-args ["argument"] 0)
    '("myproof" LaTeX-env-args ["argument"] 0)))
 :latex)

