from manim import *
from manim_slides.slide import Slide

class Perron_Frobenius_Statement(Slide):
    def construct(self):
        title = Text("Perron-Frobenius Theorem").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        assumption_1 = Tex(r"Let $G$ be a connected graph with adjacency matrix $A_G$.")
        assumption_2 = Tex(r"$A_G$ has eigenvalues $\mu_1\geq \mu_2 \geq \cdots \geq \mu_n$.")
        assumption_2.next_to(assumption_1, DOWN, buff=0.5)
        assumptions = [assumption_1, assumption_2]
        assumptions_group = VGroup(*assumptions).center().shift(2 * UP)

        for assumption in assumptions:
            self.play(Write(assumption))
            self.next_slide()
        
        goal = Text("Want to show:")
        statement_1 = Tex(r"Eigenvalue $\mu_1$ has a strictly positive eigenvector")
        statement_2 = Tex(r"$\mu_1 \geq -\mu_n$")
        statement_3 = Tex(r"$\mu_1 > \mu_2$")
        statements = [goal, statement_1, statement_2, statement_3]
        statement_1.next_to(goal, DOWN, buff=0.5)
        statement_2.next_to(statement_1, DOWN, buff=0.5)
        statement_3.next_to(statement_2, DOWN, buff=0.5)
        statements_group = VGroup(*statements).center().shift(DOWN)
        
        for statement in statements:
            self.play(Write(statement))
            self.next_slide()

        self.play(Unwrite(title), Unwrite(goal), Unwrite(assumption_1), Unwrite(assumption_2), Unwrite(statement_1), Unwrite(statement_2), Unwrite(statement_3))
        self.wait()

class Perron_Frobenius_Lemma(Slide):
    def construct(self):
        title = Text("Perron-Frobenius Lemma").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide

        assumption_1 = Tex(r"Let $G$ be a connected graph with adjacency matrix $A_G$")
        assumption_2 = Tex(r"Let $\phi$ be a non-negative eigenvector of $A_G$")
        assumptions = [assumption_1, assumption_2]
        assumptions_group = VGroup(*assumptions).center().shift(2 * UP)

        self.play(Write(assumption_1))
        self.next_slide()
        assumption_2.next_to(assumption_1, DOWN, buff=0.5)
        self.play(Write(assumption_2))
        self.next_slide()
        
        statement = Tex(r"$\phi$ is strictly positive")
        self.play(Write(statement))
        self.next_slide()

        self.play(Unwrite(assumption_1), Unwrite(assumption_2), Unwrite(title), Unwrite(statement))

        title = Text("Proof of Perron-Frobenius Lemma").scale(0.5).to_corner(UL)

        step1 = MathTex(r"\phi")
        step2 = MathTex(r"\phi", "=", r"\begin{bmatrix}\vdots \\ 0 \\ \vdots\end{bmatrix}")
        step3 = MathTex(r"\phi[v]", "=", r"0")
        step4 = MathTex(r"\mu\phi[v]", "=", r"0")
        step5 = MathTex(r"\mu\phi[v]", "=", r"(A_G \phi)[v]")
        step6 = MathTex(r"\mu\phi[v]", "=", r"\sum_{(u, v)\in E}\phi[u]")
        step7 = MathTex(r"\mu\phi[v]",  r"\geq", r"\phi[w]")
        step8 = MathTex(r"\mu\phi[v]", r"\geq", r"0")

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

        step1 = MathTex(r"\mu\phi[v]", r"\geq" r"(A_G\phi)[v]", r"\geq", r"\sum_{(u, v)\in E}\phi[u]", r"\geq", r"\phi[w]", r"\geq", r"0")
        step2 = MathTex(r"\mu\phi[v] = (A_G\phi)[v] = \sum_{(u, v)\in E}\phi[u] = \phi[w] = 0")
        step3 = MathTex(r"\sum_{(u, v)\in E}\phi[u] = 0")
        step4 = MathTex(r"\forall \{u \, | \, (u, v)\in E\}\, \phi[u] = 0")
        step5 = MathTex(r"\phi = \begin{bmatrix} 0 \\ \vdots \\ 0\end{bmatrix}")

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
        assumption_2.next_to(assumption_1, DOWN, buff=0.5)
        assumptions_group = VGroup(*assumptions).center().shift(2 * UP)

        for assumption in assumptions:
            self.play(Write(assumption))
            self.next_slide()

        statement = Tex(r"Eigenvalue $\mu_1$ has a strictly positive eigenvector")
        statement.next_to(assumptions_group, DOWN, buff=0.5)
        self.play(Write(statement))
        self.next_slide()

        # Need a move command for the statement
        self.play(Unwrite(assumption_1), Unwrite(assumption_2))
        self.play(statement.animate.move_to(assumption_1))
        self.next_slide()

        let_1 = Tex(r"Let $\phi_1$ be a unit eigenvector with corresponding eigenvalue $\mu_1$")
        let_2 = Tex(r"Consider the vector $x$, defined by $x[v] = |\phi_1[v]|$")
        let_3 = Tex(r"This implies $x^Tx = \phi_1^T\phi_1 = 1$")
        lets = [let_1, let_2, let_3]
        let_2.next_to(let_1, DOWN, buff=0.5)
        let_3.next_to(let_2, DOWN, buff=0.5)
        lets_group = VGroup(*lets).next_to(statement, DOWN, buff=0.5)

        for let in lets:
            self.play(Write(let))
            self.next_slide()

        step1 = MathTex(r"\mu_1")
        step2 = MathTex(r"\mu_1", "=", r"\phi_1^T A_G \phi_1")
        step3 = MathTex(r"\mu_1", "=", r"\sum_{u,\,v}A_G[u][v]\phi_1[u]\phi_1[v]")
        step4 = MathTex(r"\mu_1", r"\leq", r"\sum_{u,\,v}A_G[u][v]|\phi_1[u]||\phi_1[v]|")
        step5 = MathTex(r"\mu_1", r"\leq", r"x^TA_Gx")
        step6 = MathTex(r"\mu_1", r"\leq", r"\frac{x^T A_G x}{x^T x}")
        step7 = MathTex(r"\mu_1", "=", r"\frac{x^T A_G x}{x^T x}")

        step1.next_to(let_3, DOWN, buff=0.5)
        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4), (step4, step5), (step5, step6), (step6, step7)]:
            self.next_slide()
            next_step.move_to(prev_step)
            self.play(TransformMatchingTex(prev_step, next_step))
        
        self.next_slide()
        self.play(Unwrite(let_1), Unwrite(let_2), Unwrite(let_3))
        self.play(step7.animate.move_to(let_1))
        
        conclusion = Tex(r"$x$ is a strictly positive eigenvector of $\mu_1$")
        conclusion.next_to(step7, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.next_slide()
        self.play(Unwrite(conclusion))
        self.play(Unwrite(step7))
        self.play(Unwrite(statement))
        self.next_slide()

        # Part B

        statement = Tex(r"$\mu_1 \geq -\mu_n$")
        statement.move_to(assumption_1)
        self.play(Write(statement))
        self.next_slide

        let_1 = Tex(r"Let $\phi_n$ be a unit eigenvector with corresponding eigenvalue $\mu_n$")
        let_2 = Tex(r"Consider the vector $y$, defined by $y[v] = |\phi_n[v]|$")
        let_3 = Tex(r"This implies $y^Ty = \phi_n^T\phi_n = 1$")
        lets = [let_1, let_2, let_3]
        let_2.next_to(let_1, DOWN, buff=0.5)
        let_3.next_to(let_2, DOWN, buff=0.5)
        lets_group = VGroup(*lets).next_to(statement, DOWN, buff=0.5)

        for let in lets:
            self.play(Write(let))
            self.next_slide()
        
        step1 = MathTex(r"|\mu_n|")
        step2 = MathTex(r"|\mu_n|", "=", r"|\phi_n^T A_G \phi_n|")
        step3 = MathTex(r"|\mu_n|", r"\leq", r"\sum_{u,\,v}A_G[u][v]y[a]y[b]")
        step4 = MathTex(r"|\mu_n|", r"\leq", r"\mu_1 y^T y")
        step5 = MathTex(r"|\mu_n|", r"\leq", r"\mu_1")

        step1.next_to(let_3, DOWN, buff=0.5)
        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4), (step4, step5)]:
            self.next_slide()
            next_step.move_to(prev_step)
            self.play(TransformMatchingTex(prev_step, next_step))

        self.next_slide()
        self.play(Unwrite(let_1), Unwrite(let_2), Unwrite(let_3))
        self.play(step5.animate.move_to(let_1))
        
        self.next_slide()
        conclusion = MathTex(r"\mu_1 \geq -\mu_n")
        conclusion.next_to(step5, DOWN, buff=0.5)
        self.play(Write(conclusion))


        self.next_slide()
        self.play(Unwrite(conclusion))
        self.play(Unwrite(step5))
        self.play(Unwrite(statement))
        
        self.next_slide()

        # Part C

        statement = MathTex(r"\mu_1 > \mu_2")
        statement.move_to(assumption_1)
        self.play(Write(statement))
        self.next_slide

        let_1 = Tex(r"Let $\phi_2$ be a unit eigenvector with eigenvalue $\mu_2$")
        let_2 = Tex(r"Let $\phi_2$ be orthogonal to $\phi_1$")
        let_3 = Tex(r"Consider the vector $z$, defined by $z[v] = |\phi_2[v]|$")
        let_4 = Tex(r"This implies $z^Tz = \phi_2^T\phi_2 = 1$")
        lets = [let_1, let_2, let_3, let_4]
        let_2.next_to(let_1, DOWN, buff=0.5)
        let_3.next_to(let_2, DOWN, buff=0.5)
        let_4.next_to(let_3, DOWN, buff=0.5)
        lets_group = VGroup(*lets).next_to(statement, DOWN, buff=0.5)

        for let in lets:
            self.play(Write(let))
            self.next_slide()

        step1 = MathTex(r"\mu_2")
        step2 = MathTex(r"\mu_2", "=", r"\phi_2^T A_G \phi_2")
        step3 = MathTex(r"\mu_2", r"\leq", r"z^T A_G z")
        step4 = MathTex(r"\mu_2", r"\leq", r"u_1")
        
        step1.next_to(let_4, DOWN, buff=0.5)
        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3), (step3, step4)]:
            self.next_slide()
            next_step.move_to(prev_step)
            self.play(TransformMatchingTex(prev_step, next_step))

        self.next_slide()
        self.play(Unwrite(step4), Unwrite(let_1), Unwrite(let_2), Unwrite(let_3), Unwrite(let_4))

        # BUT IS IT SHARP??? (Yes)
        sharp = Text("But is the bound sharp?")
        sharp.center()
        self.play(Write(sharp))
        self.next_slide()
        self.play(Unwrite(sharp))
        self.next_slide()

        step1 = MathTex(r"\mu_2", r"=", r"\phi_2^T A_G \phi_2", r"\leq", r"z^T A_G z", r"\leq u_1")
        step2 = MathTex(r"\mu_2", "=", r"\phi_2^T A_G \phi_2", r"=", r"z^T A_G z", r"=", r"u_1")
        step3 = MathTex(r"z^T A_G z", r"=", r"u_1")

        step1.center()
        self.play(Write(step1))

        for prev_step, next_step in [(step1, step2), (step2, step3)]:
            self.next_slide()
            next_step.move_to(prev_step)
            self.play(TransformMatchingTex(prev_step, next_step))
        
        self.next_slide()
        self.play(Unwrite(step3))

        arg1 = Tex(r"$\exists\, (u,\,v)\in E\, | \, \phi_2[u] < 0 < \phi_2[v]$")
        arg2 = MathTex(r"\mu_2 = \phi_2^T A_G \phi_2 < z^T A_G z = \mu_1")

        self.next_slide()
        arg1.move_to(step3)
        self.play(step3.animate.next_to(statement, DOWN, buff=0.5))
        self.play(Write(arg1))
        self.next_slide()
        arg2.next_to(arg1, DOWN, buff=0.5)
        self.play(Write(arg2))
        self.next_slide()
        self.play(Unwrite(arg1), Unwrite(arg2))
        self.next_slide()

        conclusion = MathTex(r"\mu_2 < \mu_1")
        conclusion.move_to(arg1)
        self.play(Write(conclusion))
        self.next_slide()
        self.play(Unwrite(conclusion), Unwrite(title), Unwrite(statement))
        self.wait()