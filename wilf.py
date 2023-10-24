from manim import *
from manim_slides.slide import Slide

class Wilf_Theorem(Slide):
    def construct(self):
        title = Text("Wilf's Theorem").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        assumption = Tex(r"Let $G$ be a graph with chromatic number $\chi(G)$")
        statement1 = MathTex(r"\chi(G) \leq \lfloor \mu_1 \rfloor + 1")
        statement2 = Tex(r"Where $\mu_1$ is the first eigenvalue of the Laplacian")
        proof = [assumption, statement1, statement2]
        proof_lines = VGroup(*proof).center().shift(2 * UP)

        statement1.next_to(assumption, DOWN, buff=0.5)
        statement2.next_to(statement1, DOWN, buff=0.5)

        for line in proof:
            self.play(Write(line))
            self.next_slide()
        
        self.play(Unwrite(assumption), Unwrite(statement2))
        self.play(statement1.animate.move_to(assumption))
        
        induction1 = Text("Base case:")
        induction2 = MathTex(r"V=\{v\},\, E=\emptyset")
        induction3 = MathTex(r"\chi(G) = 1\, \mu_1 = 0")
        
        induction1.next_to(statement1, DOWN, buff=0.5)
        induction2.next_to(induction1, DOWN, buff=0.5)
        induction3.next_to(induction2, DOWN, buff=0.5)

        self.next_slide()
        self.play(Write(induction1))
        self.next_slide()
        self.play(Write(induction2))
        self.next_slide()
        self.play(Write(induction3))
        self.next_slide()

        self.play(Unwrite(induction1), Unwrite(induction2), Unwrite(induction3))


        induction4 = Text("Inductive step:")
        induction5 = MathTex(r"\exists v \in V \, | \, d(v) \leq \lfloor \mu_1 \rfloor")
        induction6 = Tex(r"Apply inductive assumption to subgraph $S=G\setminus \{v\}$")
        induction7 = Tex(r"Color $G$ the same as $S$")
        induction8 = Tex(r"Coloring is valid because we have $\lfloor \mu_1\rfloor + 1$ colors")

        induction4.next_to(statement1, DOWN, buff=0.5)
        induction5.next_to(induction4, DOWN, buff=0.5)
        induction6.next_to(induction5, DOWN, buff=0.5)
        induction7.next_to(induction6, DOWN, buff=0.5)
        induction8.next_to(induction7, DOWN, buff=0.5)

        self.next_slide()
        self.play(Write(induction4))
        self.next_slide()
        self.play(Write(induction5))
        self.next_slide()
        self.play(Write(induction6))
        self.next_slide()
        self.play(Write(induction7))
        self.next_slide()
        self.play(Write(induction8))
        self.next_slide()

        self.play(Unwrite(induction4), Unwrite(induction5), Unwrite(induction6), Unwrite(induction7), Unwrite(induction8))
        self.next_slide()

        self.play(Unwrite(statement1), Unwrite(title))
        self.next_slide()
        self.wait()