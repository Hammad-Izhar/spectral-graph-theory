intro:
	manim intro.py
	manim-slides Intro

eigenvalue-bound:
	manim eigenvalue-bound.py
	manim-slides Eigenvalue_Bound

wilf:
	manim wilf.py
	manim-slides Wilf_Theorem

perron-frobenius:
	manim perron-frobenius.py
	manim-slides Perron_Frobenius_Statement Perron_Frobenius_Lemma Perron_Frobenius_Proof
all:
	manim-slides RayleighQuotientDefinition RayleighExampleOne RayleighEigenvectors RayleighExampleTwo CourantFischerTheorem LaplacianDefinition EigenvalueDrawing EigenvalueDrawingOptimality

courant-fischer:
	manim courant-fischer.py
	manim-slides RayleighQuotientDefinition RayleighExampleOne RayleighEigenvectors RayleighExampleTwo CourantFischerTheorem

graph-drawing:
	manim graph-drawing.py
	manim-slides LaplacianDefinition EigenvalueDrawing EigenvalueDrawingExample EigenvalueDrawingOptimality