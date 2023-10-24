from manim import *
from manim_slides.slide import Slide
import pickle

custom_tex_template = TexTemplate(
    documentclass=r"\documentclass[preview, varwidth=7in]{standalone}"
)
custom_tex_template.add_to_preamble(r"\usepackage[charter]{mathdesign}")
Tex.set_default(tex_template=custom_tex_template)

class LaplacianDefinition(Slide):
    def construct(self):
        title = Tex("Laplacian Matrix").scale(0.5).to_corner(UL)

        self.play(Write(title))
        self.wait()
        self.next_slide()

        laplacian_definition = MathTex(r"L_G = D_G - A_G").shift(UP)

        self.play(Write(laplacian_definition))
        self.wait()
        self.next_slide()

        laplacian_definition_equivalence = MathTex(r"L_G = D_G - A_G", r"\iff", r"\sum_{(a, b) \in E} w_{a, b}(\delta_a - \delta_b)(\delta_a - \delta_b)^T").shift(UP)

        self.play(TransformMatchingTex(laplacian_definition, laplacian_definition_equivalence))
        self.wait()
        self.next_slide()

        laplacian_quadratic_form = MathTex(r"x^TL_Gx = \sum_{(a, b) \in E} w_{a, b}(x(a) - x(b))^2").shift(DOWN)

        self.play(Write(laplacian_quadratic_form))
        self.wait()
        self.next_slide()

        self.play(Unwrite(laplacian_quadratic_form), Unwrite(laplacian_definition_equivalence), Unwrite(title))
        self.wait()


class EigenvalueDrawing(Slide):
    def construct(self):
        title = Tex("Drawing Graphs with Eigenvalues").scale(0.5).to_corner(UL)

        self.play(Write(title))
        self.wait()
        self.next_slide()

        condition1 = MathTex(r"\min_{x \in \mathbb{R}^{|V|}} x^TLx").shift(UP)
        condition2 = MathTex(r"\min_{x \in \mathbb{R}^{|V|}} x^TLx", r"\quad\quad", r"\sum_{a \in V} x(a)^2 = 1").shift(UP)
        condition3 = MathTex(r"\min_{x \in \mathbb{R}^{|V|}} x^TLx", r"\quad\quad", r"\sum_{a \in V} x(a)^2 = 1", r"\quad\quad", r"\sum_{a \in V} x(a) = 0").shift(UP)

        # draw line and map all points to 0
        line = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            include_numbers=False,
            numbers_to_include=[0]
        ).next_to(condition1, 3 * DOWN)

        dot1 = Dot(color=YELLOW).move_to(line.n2p(0))
        dot2 = Dot(color=YELLOW).move_to(line.n2p(5))
        dot3 = Dot(color=YELLOW).move_to(line.n2p(5))
        dot4 = Dot(color=YELLOW).move_to(line.n2p(5))
        dot5 = Dot(color=YELLOW).move_to(line.n2p(5))

        dot_label = MathTex(r"\frac{1}{\sqrt{n}}").scale(0.6).move_to(line.n2p(5)).shift(0.5 * DOWN)

        self.play(Write(condition1))
        self.wait()
        self.next_slide()
        self.play(Create(line), Create(dot1))
        self.next_slide()
        self.play(TransformMatchingTex(condition1, condition2))
        self.wait()
        self.next_slide()
        self.play(dot1.animate.move_to(line.n2p(5)), Write(dot_label))
        self.wait()
        self.next_slide()
        self.play(TransformMatchingTex(condition2, condition3))
        self.wait()
        self.next_slide()
        self.play(
            Unwrite(dot_label),
            dot1.animate.move_to(line.n2p(0)),
            dot2.animate.move_to(line.n2p(8)),
            dot3.animate.move_to(line.n2p(-4)),
            dot4.animate.move_to(line.n2p(-8)),
            dot5.animate.move_to(line.n2p(4)),
        )
        self.wait()
        self.next_slide()

        # highlight first condition when talking about courant-fischer theorem

        # can't use lambda_0, whose eigenvectors are the constant eigenvectors


        conditions_2d = MathTex(r"\min_{x,y \in \mathbb{R}^{|V|}} x^TLx + y^TLy", r"\\", r"\sum_{a \in V} x(a)^2 = 1 \text{ and } \sum_{a \in V} y(a)^2 = 1", r"\\", r"\sum_{a \in V} x(a) = 0 \text{ and } \sum_{a \in V} y(a) = 0", tex_environment="gather*")

        fixed_condition = MathTex(r"\langle x, y \rangle = \langle x, v_1 \rangle = \langle y, v_1 \rangle = 0")

        self.play(Transform(condition3, conditions_2d), Uncreate(line), Uncreate(dot1), Uncreate(dot2), Uncreate(dot3), Uncreate(dot4), Uncreate(dot5))
        self.wait()
        self.next_slide()
        self.play(condition3.animate.shift(0.75 * UP), Write(fixed_condition.shift(1.5 * DOWN)))
        self.wait()
        self.next_slide()

        self.play(Unwrite(fixed_condition), Unwrite(condition3), Unwrite(title))
        self.wait()


class EigenvalueDrawingExample(Slide):
    def construct(self):
        title = Tex("Drawing Graphs with Eigenvalues").scale(0.5).to_corner(UL)

        self.play(Write(title))
        self.wait()
        self.next_slide()

        # plot image
        original = ImageMobject("original.png").scale_to_fit_width(10)

        self.play(FadeIn(original))
        self.wait()
        self.next_slide()

        # plot image
        spectral = ImageMobject("spectral.png").scale_to_fit_width(10)
        self.play(FadeTransform(original, spectral))
        self.wait()
        self.next_slide()

class EigenvalueDrawingOptimality(Slide):
    def construct(self):
        title = Tex(r"Optimality of Eigenvalue Drawing").scale(0.5).to_corner(UL)
        assumption = Tex(r"Let $L$ be a Laplacian matrix with eigenvalues $\lambda_1 \leq \cdots \leq \lambda_n$ and corresponding unit eigenvectors $v_1, \cdots, v_n$. \\ Let $x_1, \cdots, x_k$ be orthonormal vectors that are orthogonal to $v_1$. Then:", tex_environment=None).scale(0.5).next_to(title, DOWN, aligned_edge=LEFT) # type: ignore
        equation = MathTex(r"\sum_{i=1}^k x_i^TLx_i \geq \sum_{i = 2}^{k + 1} \lambda_i").scale(0.6).shift(UP)

        step2 = Tex(r"(2) Combine the bounds to get the desired inequality").scale(0.5)
        step1 = Tex(r"(1) Bound $x_i^TLx_i$ for $0 \leq i \leq k$").scale(0.5).align_to(step2, LEFT)
        VGroup(step1, step2).arrange_in_grid(2, 1, col_alignments="l").to_edge(LEFT) # type: ignore

        self.play(Write(title))
        self.wait()
        self.next_slide()
        self.play(Write(assumption))
        self.play(Write(equation))
        self.wait()
        self.next_slide()
        self.play(Write(step1))
        self.wait()
        self.next_slide()
        self.play(Write(step2))
        self.wait()
        self.next_slide()

        step1.generate_target()
        if step1.target:
            step1.target.move_to(assumption, aligned_edge=LEFT)

        self.play(Unwrite(assumption), Unwrite(equation), Unwrite(step2))
        self.play(MoveToTarget(step1))

        self.next_slide()

        basis = Tex(r"$x_1, \cdots, x_k$", r"$,x_{k + 1}, \cdots, x_{n}$ be an orthonormal basis").scale(0.5).next_to(step1, DOWN, aligned_edge=LEFT)
        doubly_stochastic = MathTex(r"\sum_{j = 1}^n (v_j^Tx_i)^2 = 1", r"\text{ and }", r"\sum_{j = 1}^n (x_j^Tv_i)^2 = 1").scale(0.5).next_to(basis, DOWN, aligned_edge=LEFT)

        bound1 = MathTex(r"x_i^TLx_i", "=", r"\sum_{j = 1}^n", r"\lambda_j", r"(v_j^Tx_i)^2").scale(0.6)
        bound2 = MathTex(r"x_i^TLx_i", "=", r"\sum_{j = 2}^n", r"\lambda_j", r"(v_j^Tx_i)^2").scale(0.6)
        bound3 = MathTex(r"x_i^TLx_i", "=", r"\lambda_{k + 1} +", r"\sum_{j = 2}^n", r"(\lambda_j - \lambda_{k + 1})", r"(v_j^Tx_i)^2").scale(0.6)
        bound4 = MathTex(r"x_i^TLx_i", r"\geq", r"\lambda_{k + 1} +", r"\sum_{j = 2}^{k + 1}", r"(\lambda_j - \lambda_{k + 1})", r"(v_j^Tx_i)^2").scale(0.6)

        bounds = [(bound1, bound2), (bound2, bound3), (bound3, bound4)]

        self.play(Write(basis[0])) # type: ignore
        self.wait()
        self.next_slide()
        self.play(Write(basis[1])) # type: ignore
        self.wait()
        self.next_slide()
        self.play(Write(doubly_stochastic))
        self.wait()
        self.next_slide()
        self.play(Write(bound1))
        self.wait()
        self.next_slide()

        for prev_bound, next_bound in bounds:
            self.play(TransformMatchingTex(prev_bound, next_bound))
            self.wait()
            self.next_slide()

        save_bound = bound4

        step2 = Tex(r"(2) Combine the bounds to get the desired inequality").scale(0.5).shift(0.25 * DOWN).to_edge(LEFT)
        self.play(bound4.animate.shift(0.5 * UP), Write(step2))
        self.wait()
        self.next_slide()

        bound1 = MathTex(r"\sum_{i = 1}^k x_i^TLx_i \geq", r"\sum_{i = 1}^k", r"\Bigg(", r"\lambda_{k + 1} +", r"\sum_{j = 2}^{k + 1}", r"(\lambda_j - \lambda_{k + 1})", r"(v_j^Tx_i)^2", r"\Bigg)").scale(0.6).next_to(step2, DOWN, coor_mask=np.array([0, 1, 0]))
        bound2 = MathTex(r"\sum_{i = 1}^k x_i^TLx_i \geq", r"\sum_{i = 1}^k", r"\lambda_{k + 1} +", r"\sum_{i = 1}^k", r"\sum_{j = 2}^{k + 1}", r"(\lambda_j - \lambda_{k + 1})", r"(v_j^Tx_i)^2").scale(0.6).next_to(step2, DOWN, coor_mask=np.array([0, 1, 0]))
        bound3 = MathTex(r"\sum_{i = 1}^k x_i^TLx_i \geq", r"k", r"\lambda_{k + 1} +", r"\sum_{j = 2}^{k + 1}", r"(\lambda_j - \lambda_{k + 1})", r"\sum_{i = 1}^k", r"(v_j^Tx_i)^2").scale(0.6).next_to(step2, DOWN, coor_mask=np.array([0, 1, 0]))
        bound4 = MathTex(r"\sum_{i = 1}^k x_i^TLx_i \geq", r"k", r"\lambda_{k + 1} +", r"\sum_{j = 2}^{k + 1}", r"(\lambda_j - \lambda_{k + 1})").scale(0.6).next_to(step2, DOWN, coor_mask=np.array([0, 1, 0]))
        bound5 = MathTex(r"\sum_{i = 1}^k x_i^TLx_i \geq", r"\sum_{j = 2}^{k + 1}", r"\lambda_j").scale(0.6).next_to(step2, DOWN, coor_mask=np.array([0, 1, 0]))

        bounds = [(bound1, bound2), (bound2, bound3), (bound3, bound4), (bound4, bound5)]

        self.play(Write(bound1))
        self.wait()
        self.next_slide()
        for prev_bound, next_bound in bounds:
            self.play(TransformMatchingTex(prev_bound, next_bound))
            self.wait()
            self.next_slide()

        self.play(Unwrite(title), Unwrite(step1), Unwrite(step2), Unwrite(basis), Unwrite(doubly_stochastic), Unwrite(bound5), Unwrite(save_bound))
        self.wait()