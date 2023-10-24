from manim import *
from manim_slides.slide import Slide

class Eigenvalue_Bound(Slide):
    def construct(self):
        title = Text("Bounding Eigenvalues").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        assumption1 = Tex(r"Let $G$ be a graph")
        assumption2 = Tex(r"Let $\mu_1$ be the largest eigenvalue of $A_G$")
        assumption3 = Tex(r"Let $d_{max}$ be the maximum degree of $v$ in $G$")
        assumption4 = Tex(r"Let $d_{avg}$ be the average degree of $v$ in $G$")

        statement = MathTex(r"d_{avg} \leq \mu_1 \leq d_{max}")

        lower1 = MathTex(r"\mu_1")
        lower2 = MathTex(r"\mu_1", r"=", r"\max_{x} \frac{x^T A_G x}{x^T x}")
        lower3 = MathTex(r"\mu_1", r"\geq", r"\frac{1^T A_G 1}{1^T 1}")
        lower4 = MathTex(r"\mu_1", r"\geq", r"\frac{\sum_{u,\,v}A_G[u][v]}{n}")
        lower5 = MathTex(r"\mu_1", r"\geq", r"\frac{\sum_{v}d(v)}{n}")
        lower6 = MathTex(r"\mu_1", r"\geq", r"d_{avg}")

        upper1 = MathTex(r"\mu_1")
        upper2 = MathTex(r"\mu_1", r"=", r"\frac{A_G \phi_1[v]}{\phi_1[v]}")
        upper3 = MathTex(r"\mu_1", r"=", r"\frac{\sum_{u\, |\, (u, \,v)\in E}\phi_1[u]}{\phi_1[v]}")
        upper4 = MathTex(r"\mu_1", r"=", r"\sum_{u\,|\, (u, \,v)\in E}\frac{\phi_1[u]}{\phi_1[v]}")
        upper5 = MathTex(r"\mu_1", r"\leq", r"\sum_{u\,|\,(u, \,v)\in E}1")
        upper6 = MathTex(r"\mu_1", r"\leq", r"d(v)")
        upper7 = MathTex(r"\mu_1", r"\leq", r"d_{max}")

        # Render the assumptions
        assumption1.center().shift(2 * UP)
        assumption2.next_to(assumption1, DOWN, buff=0.5)
        assumption3.next_to(assumption2, DOWN, buff=0.5)
        assumption4.next_to(assumption3, DOWN, buff=0.5)

        self.play(Write(assumption1))
        self.next_slide()
        self.play(Write(assumption2))
        self.next_slide()
        self.play(Write(assumption3))
        self.next_slide()
        self.play(Write(assumption4))
        self.next_slide()

        statement.next_to(assumption4, DOWN, buff=0.5)
        self.play(Write(statement))
        self.next_slide()

        self.play(Unwrite(assumption1), Unwrite(assumption2), Unwrite(assumption3), Unwrite(assumption4))
        self.play(statement.animate.move_to(assumption1))
        self.next_slide()

        # Proof of lower bound
        let = Text("Consider the Rayleigh quotient with a vector of all 1's").scale(0.5)
        let.next_to(statement, DOWN, buff=0.5)
        self.play(Write(let))
        self.next_slide()
        lower1.next_to(let, DOWN, buff=0.5)
        self.play(Write(lower1))

        for prev_lower, next_lower in [(lower1, lower2), (lower2, lower3), (lower3, lower4), (lower4, lower5), (lower5, lower6)]:
            self.next_slide()
            next_lower.move_to(prev_lower)
            self.play(TransformMatchingTex(prev_lower, next_lower))
        
        self.next_slide()
        self.play(Unwrite(lower6), Unwrite(let))
        self.next_slide()

        # Proof of upper bound
        let = Tex(r"Let $\phi_1$ be an eigenvector of $\mu_1$ with $\phi_1[v]\geq \phi_1[u]$")
        let.next_to(statement, DOWN, buff=0.5)
        self.play(Write(let))
        self.next_slide()

        upper1.next_to(let, DOWN, buff=0.5)
        self.play(Write(upper1))

        for prev_upper, next_upper in [(upper1, upper2), (upper2, upper3), (upper3, upper4), (upper4, upper5), (upper5, upper6), (upper6, upper7)]:
            self.next_slide()
            next_upper.move_to(prev_upper)
            self.play(TransformMatchingTex(prev_upper, next_upper))
        
        self.next_slide()
        self.play(Unwrite(upper7), Unwrite(let))
        self.next_slide()

        self.play(statement.animate.shift(2 * DOWN))
        self.next_slide()
        self.play(Unwrite(statement), Unwrite(title))
