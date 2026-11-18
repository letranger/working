(TeX-add-style-hook
 "CourseDesign"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("ulem" "normalem") ("helvet" "scaled") ("geometry" "margin=2cm" "margin=1.0in") ("natbib" "numbers" "sort&compress" "square") ("babel" "english") ("ctex" "UTF8" "heading") ("sourcecodepro" "default") ("fontenc" "T1")))
   (add-to-list 'LaTeX-verbatim-environments-local "VerbatimOut")
   (add-to-list 'LaTeX-verbatim-environments-local "SaveVerbatim")
   (add-to-list 'LaTeX-verbatim-environments-local "LVerbatim*")
   (add-to-list 'LaTeX-verbatim-environments-local "LVerbatim")
   (add-to-list 'LaTeX-verbatim-environments-local "BVerbatim*")
   (add-to-list 'LaTeX-verbatim-environments-local "BVerbatim")
   (add-to-list 'LaTeX-verbatim-environments-local "Verbatim*")
   (add-to-list 'LaTeX-verbatim-environments-local "Verbatim")
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "Verb*")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "Verb")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "geometry"
    "hyperref"
    "inputenc"
    "fixltx2e"
    "graphicx"
    "longtable"
    "float"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "marvosym"
    "wasysym"
    "multicol"
    "amssymb"
    "listings"
    "titlesec"
    "helvet"
    "courier"
    "natbib"
    "glossaries"
    "setspace"
    "enumitem"
    "babel"
    "ctex"
    "xltxtra"
    "xeCJK"
    "lmodern"
    "verbatim"
    "tikz"
    "soul"
    "algorithm"
    "algorithmic"
    "fancyhdr"
    "fontspec"
    "xunicode"
    "CJKnumb"
    "amsfonts"
    "sourcecodepro"
    "fontenc"
    "color"
    "fancyvrb"
    "placeins")
   (TeX-add-symbols
    "sectionbreak")
   (LaTeX-add-labels
    "sec:org7b21f17"
    "sec:orgcacde21"
    "sec:orgb3d4aee"
    "sec:orgd8a9a8f"
    "sec:org845e327"
    "sec:org30b45de"
    "sec:org1ac06c3"
    "sec:org462a7f3"
    "sec:org2523e05"
    "sec:org3e10112"
    "sec:orgff7561e"
    "sec:org90786af"
    "sec:org627a346"
    "sec:orgf2827b7"
    "sec:orgbeb6a68"
    "sec:org89e5e1a"
    "sec:org7df788f"
    "sec:org28fa586"
    "sec:org90e3187"
    "sec:org00b5f32"
    "sec:orgd1d5245"
    "fig:CoreLiteracy"
    "sec:orge6100c4"
    "sec:org4ab3444"
    "sec:org57d7dbd"
    "sec:orgcf9629f"
    "sec:org3e7aa60"
    "sec:org5310778"
    "sec:org4df96e1")
   (LaTeX-add-color-definecolors
    "dkgreen"
    "dred"
    "dblue"
    "lgrey"
    "gray"
    "darkblue"
    "bubbles"
    "foreground"
    "background"
    "preprocess"
    "var"
    "string"
    "type"
    "function"
    "keyword"
    "comment"
    "doc"
    "comdil"
    "constant"))
 :latex)

