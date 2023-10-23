from manim import *
from manim_slides.slide import Slide

class Perron_Frobenius_Statement(Slide):
    def construct(self):
        title = Text("Perron-Frobenius Theorem").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        assumption_1 = Tex(r"Let $G$ be a connected graph with adjacency matrix $A_G$.")
        assumption_2 = Tex(r"$A_G$ has eigenvalues $\mu_1\geq \mu_2 \geq \cdots \geq \mu_n$.")
        assumptions = [assumption_1, assumption_2]
        assumptions_group = VGroup(*assumptions).arrange(buff=0.5).shift(2 * UP)

        for assumption in assumptions:
            self.play(Write(assumption))
            self.next_slide()
        
        statement_1 = Tex(r"Eigenvalue $\mu_1$ has a strictly positive eigenvector")
        statement_2 = Tex(r"$\mu_1 \geq -\mu_n$")
        statement_3 = Tex(r"$\mu_1 > \mu_2$")
        statements = [statement_1, statement_2, statement_3]
        statements_group = VGroup(*statements).arrange(buff=0.5).shift(2 * UP)
        
        for statement in statements:
            self.play(Write(statement))
            self.next_slide()

        self.unwrite(title, assumption_1, assumption_2, statement_1, statement_2, statement_3)
        self.wait()

class Perron_Frobenius_Lemma(Slide):
    def construct(self):
        title = Text("Perron-Frobenius Lemma").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide

        assumption_1 = Tex(r"Let $G$ be a connected graph with adjacency matrix $A_G$")
        assumption_2 = Tex(r"Let $\phi$ be a non-negative eigenvector of $A_G$")
        assumptions = [assumption_1, assumption_2]
        assumptions_group = VGroup(*assumptions).arrange(buff=0.5).shift(2 * UP)

        for assumption in assumptions:
            self.play(Write(assumption))
            self.next_slide()
        
        statement = Tex(r"$\phi$ is strictly positive")
        self.play(Write(statement))
        self.next_slide()

        self.unwrite(assumption_1, assumption_2, statement)
        self.wait()

        title = Text("Proof of Perron-Frobenius Lemma").scale(0.5).to_corner(UL)

        step1 = MathTex(r"\phi")
        step2 = MathTex(r"\phi = \begin{bmatrix}\vdots \\ 0 \\ \vdots\end{bmatrix}")
        step3 = MathTex(r"\phi[v] = 0")
        step4 = MathTex(r"\mu\phi[v] = 0")
        step5 = MathTex(r"\mu\phi[v] = (A_G \phi)[v]")
        step6 = MathTex(r"\mu\phi[v] = \sum_{(u, v)\in E}\phi[u]")
        step7 = MathTex(r"\mu\phi[v] \geq \phi[w]")
        step8 = MathTex(r"\mu\phi[v] \geq 0")

        self.play(Write(title))
        self.next_slide()
        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4), (step4, step5), (step5, step6), (step6, step7), (step7, step8)]:
            self.next_slide()
            self.play(TransformMatchingTex(prev_step, next_step))
        
        self.next_slide()
        self.play(Unwrite(step8))
        self.next_slide()

        # BUT IS IT SHARP??? (Yes)
        sharp = Text("But is the bound sharp?")
        self.play(Write(sharp))
        self.next_slide()
        self.play(Unwrite(sharp))
        self.next_slide()

        step1 = MathTex(r"\mu\phi[v] \geq (A_G\phi)[v] \geq \sum_{(u, v)\in E}\phi[u] \geq \phi[w] \geq 0")
        step2 = MathTex(r"\mu\phi[v] = (A_G\phi)[v] = \sum_{(u, v)\in E}\phi[u] = \phi[w] = 0")
        step3 = MathTex(r"\sum_{(u, v)\in E}\phi[u] = 0")
        step4 = MathTex(r"\forall \{u \, | \, (u, v)\in E\}\, \phi[u] = 0")
        step5 = MathTex(r"\phi = \begin{bmatrix} 0 \\ \vdots \\ 0")

        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4), (step4, step5)]:
            self.next_slide()
            self.play(TransformMatchingTex(prev_step, next_step))

        self.next_slide()
        self.play(Unwrite(step5))

        conclusion = MathTex(r"\forall v \in V\, \phi[v] > 0")
        self.play(Write(conclusion))
        self.next_slide()
        self.play(Unwrite(conclusion), Unwrite(title))
        self.wait()
    
class Perron_Frobenius_Proof(Slide):
    def construct(self):
        title = Text("Proof of Perron-Frobenius Theorem").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        # Part A

        assumption_1 = Tex(r"Let $G$ be a connected graph with adjacency matrix $A_G$.")
        assumption_2 = Tex(r"$A_G$ has eigenvalues $\mu_1\geq \mu_2 \geq \cdots \geq \mu_n$.")
        assumptions = [assumption_1, assumption_2]
        assumptions_group = VGroup(*assumptions).arrange(buff=0.5).shift(2 * UP)

        for assumption in assumptions:
            self.play(Write(assumption))
            self.next_slide()

        statement = Tex(r"Eigenvalue $\mu_1$ has a strictly positive eigenvector")
        self.play(Write(statement))
        self.next_slide()

        # Need a move command for the statement
        self.play(Unwrite(assumption_1), Unwrite(assumption_2))
        self.next_slide()

        let_1 = Tex(r"Let $\phi_1$ be a unit eigenvector with corresponding eigenvalue $\mu_1$")
        let_2 = Tex(r"Consider the vector $x$, defined by $x[v] = |\phi_1[v]|$")
        let_3 = Tex(r"This implies $x^Tx = \phi_1^T\phi_1 = 1$")
        lets = [let_1, let_2, let_3]
        lets_group = VGroup(*lets).arrange(buff=0.5).shift(2 * UP)

        for let in lets:
            self.play(Write(let))
            self.next_slide()

        step1 = MathTex(r"\mu_1")
        step2 = MathTex(r"\mu_1 = \phi_1^T A_G \phi_1")
        step3 = MathTex(r"\mu_1 = \sum_{u,\,v}A_G[u][v]\phi_1[u]\phi_1[v]")
        step4 = MathTex(r"\mu_1 \leq \sum_{u,\,v}A_G[u][v]|\phi_1[u]||\phi_1[v]|")
        step5 = MathTex(r"\mu_1 \leq x^TA_Gx")
        step6 = MathTex(r"\mu_1 \leq \frac{x^T A_G x}{x^T x}")
        step7 = MathTex(r"\mu_1 = \frac{x^T A_G x}{x^T x}")

        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4), (step4, step5), (step5, step6), (step6, step7)]:
            self.next_slide()
            self.play(TransformMatchingTex(prev_step, next_step))
        
        self.next_slide()
        conclusion = Tex(r"$x$ is a strictly positive eigenvector of $\mu_1$")
        self.play(Write(conclusion))
        self.next_slide()
        self.play(Unwrite(conclusion))
        self.play(Unwrite(step7))
        for let in lets:
            self.play(Unwrite(let))
        self.play(Unwrite(statement))
        self.next_slide()

        # Part B

        statement = Tex(r"$\mu_1 \geq -\mu_n$")
        self.play(Write(statement))
        self.next_slide

        let_1 = Tex(r"Let $\phi_n$ be a unit eigenvector with corresponding eigenvalue $\mu_n$")
        let_2 = Tex(r"Consider the vector $y$, defined by $y[v] = |\phi_n[v]|$")
        let_3 = Tex(r"This implies $y^Ty = \phi_n^T\phi_n = 1$")
        lets = [let_1, let_2, let_3]
        lets_group = VGroup(*lets).arrange(buff=0.5).shift(2 * UP)

        for let in lets:
            self.play(Write(let))
            self.next_slide()
        
        step1 = MathTex(r"|\mu_n|")
        step2 = MathTex(r"|\mu_n| = |\phi_n^T A_G \phi_n|")
        step3 = MathTex(r"|\mu_n| \leq \sum_{u,\,v}A_G[u][v]y[a]y[b]")
        step4 = MathTex(r"|\mu_n| \leq \mu_1 y^T y")
        step5 = MathTex(r"|\mu_n| \leq \mu_1")

        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4), (step4, step5)]:
            self.next_slide()
            self.play(TransformMatchingTex(prev_step, next_step))

        self.next_slide()
        conclusion = MathTex(r"\mu_1 \geq -\mu_n")
        self.play(Write(conclusion))


        self.next_slide()
        self.play(Unwrite(conclusion))
        self.play(Unwrite(step5))
        for let in lets:
            self.play(Unwrite(let))
        self.play(Unwrite(statement))
        
        self.next_slide()

        # Part C

        statement = Tex(r"\mu_1 > \mu_2")
        self.play(Write(statement))
        self.next_slide

        let_1 = Tex(r"Let $\phi_2$ be a unit eigenvector corresponding to eigenvalue $\mu_2$, orthogonal to $\phi_1$")
        let_2 = Tex(r"Consider the vector $z$, defined by $z[v] = |\phi_2[v]|$")
        let_3 = Tex(r"This implies $z^Tz = \phi_2^T\phi_2 = 1$")
        lets = [let_1, let_2, let_3]
        lets_group = VGroup(*lets).arrange(buff=0.5).shift(2 * UP)

        for let in lets:
            self.play(Write(let))
            self.next_slide()

        step1 = MathTex(r"\mu_2")
        step2 = MathTex(r"\mu_2 = \phi_2^T A_G \phi_2")
        step3 = MathTex(r"\mu_2 \leq z^T A_G z")
        step4 = MathTex(r"\mu_2 \leq u_1")
        
        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4)]:
            self.next_slide()
            self.play(TransformMatchingTex(prev_step, next_step))

        self.next_slide()
        self.play(Unwrite(step4))

        # BUT IS IT SHARP??? (Yes)
        sharp = Text("But is the bound sharp?")
        self.play(Write(sharp))
        self.next_slide()
        self.play(Unwrite(sharp))
        self.next_slide()

        step1 = MathTex(r"\mu_2 = \phi_2^T A_G \phi_2 \leq z^T A_G z \leq u_1")
        step2 = MathTex(r"\mu_2 = \phi_2^T A_G \phi_2 = z^T A_G z = u_1")
        step3 = MathTex(r"z^T A_G z = u_1")

        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3)]:
            self.next_slide()
            self.play(TransformMatchingTex(prev_step, next_step))
        
        self.next_slide()
        self.play(Unwrite(step3))

        arg1 = Tex(r"$\exists\, (u,\,v)\in E\, | \, \phi_2[u] < 0 < \phi_2[v]$")
        arg2 = MathTex(r"\mu_2 = \phi_2^T A_G \phi_2 < z^T A_G z = \mu_1")

        self.next_slide()
        self.play(Write(arg1))
        self.next_slide()
        self.play(Write(arg2))
        self.next_slide()
        self.play(Unwrite(arg1), Unwrite(arg2))
        self.next_slide()

        conclusion = MathTex(r"\mu_2 < \mu_1")
        self.play(Write(conclusion))
        self.next_slide()
        self.play(Unwrite(conclusion), Unwrite(title))
        self.wait()