from manim import *
from manim_slides.slide import Slide

def compute_rayleigh_sweep(matrix):
    theta = np.arange(0, 2*np.pi, 0.01)
    vectors = np.array([np.cos(theta), np.sin(theta)])
    return np.sum(vectors * (matrix @ vectors), axis=0)

SYM_MATRIX_TEX = r"\begin{bmatrix}2 & 1 \\ 1 & 2\end{bmatrix}"
BAD_MATRIX_TEX = r"\begin{bmatrix}1 & 3 \\ -2 & 6\end{bmatrix}"
EXAMPLE_VECTOR_TEX = r"\begin{bmatrix}1 \\ 0\end{bmatrix}"
TRANSPOSE_VECTOR_TEX = r"\begin{bmatrix}1 & 0\end{bmatrix}"

class RayleighQuotientDefinition(Slide):
    def construct(self):
        title = Text("Rayleigh Quotient").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()


        quotient1 = MathTex(r"x^TMx")
        quotient2 = MathTex(r"\frac{x^TMx}{x^Tx}")
        quotient3 = MathTex(r"R(M, x) := \frac{x^TMx}{x^Tx} = \frac{\langle x,Mx\rangle}{\langle x,x\rangle}")

        self.play(Write(quotient1))
        for quotient in [quotient2, quotient3]:
            self.next_slide()
            self.play(Transform(quotient1, quotient))

        self.next_slide()
        self.play(Unwrite(quotient1), Unwrite(title))
        self.wait()


class RayleighExampleOne(Slide):
    def construct(self):
        title = Text("Example 1").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        matrix = MathTex(r"M =", SYM_MATRIX_TEX).shift(2 * LEFT)
        vector = MathTex(r"x =", EXAMPLE_VECTOR_TEX).shift(2 * RIGHT)

        self.play(Write(matrix), Write(vector))
        self.next_slide()

        matrix.generate_target()
        vector.generate_target()
        if matrix.target and vector.target:
            matrix.target.shift(2 * UP)
            vector.target.shift(2 * UP)
        self.play(MoveToTarget(matrix), MoveToTarget(vector))

        quotient_tex = r"R(M, x)"
        step1 = MathTex(quotient_tex, "=", r"\frac{x^TMx}{x^Tx}")
        step2 = MathTex(quotient_tex, "=", r"x^TMx")
        step3 = MathTex(quotient_tex, "=", TRANSPOSE_VECTOR_TEX, SYM_MATRIX_TEX, EXAMPLE_VECTOR_TEX)
        step4 = MathTex(quotient_tex, "=", TRANSPOSE_VECTOR_TEX, r"\begin{bmatrix}2 \\ 1\end{bmatrix}")
        step5 = MathTex(quotient_tex, "=", r"2")
        steps = [(step1, step2), (step2, step3), (step3, step4), (step4, step5)]

        self.play(Write(step1))
        self.wait(0.25)
        for prev_step, next_step in steps:
            self.play(TransformMatchingTex(prev_step, next_step))
            self.wait(0.75)
        self.next_slide()
        self.play(Unwrite(step5), Unwrite(matrix), Unwrite(vector))

        circle = Circle(radius=2).shift(3 * LEFT)
        dot = Dot().shift(LEFT)
        arrow = Arrow(start=LEFT, end=RIGHT).put_start_and_end_on(circle.get_center(), dot.get_center()) # type: ignore
        ax = Axes(
            x_range=[0, TAU, PI / 4],
            y_range=[0, 3],
            tips=False,
            y_axis_config={"include_numbers": True}
        ).scale(0.5).shift(3 * RIGHT)
        x_axis_label = ax.get_x_axis_label(r"\theta").scale(0.6)
        y_axis_label = ax.get_y_axis_label(r"R(M, x)").scale(0.6)
        x_axis_label.next_to(ax.x_axis.get_end(), RIGHT)
        y_axis_label.next_to(ax.y_axis.get_end(), UP)
        axis_label = VMobject()
        axis_label.add(x_axis_label, y_axis_label)

        x_pos = [t for t in np.arange(0, TAU + 0.1, PI/4)]
        x_labels = [""] + [r"$\frac{" + str(i) + r"\pi}{4}$" for i in range(1, 9)]
        for pos, label in zip(x_pos, x_labels):
            ax.x_axis.add(Tex(f"{label}", color=WHITE).next_to(ax.x_axis.n2p(pos), DOWN).scale(0.6))

        self.play(Create(circle), Create(ax), Create(dot), Create(arrow), Write(axis_label))
        self.wait()
        self.next_slide()

        theta = np.abs(np.arange(0, TAU, 0.01))
        sweep = compute_rayleigh_sweep(np.array([[2, 1], [1, 2]]))
        curve = VMobject()
        curve.set_points_smoothly([ax.coords_to_point(t, s) for t, s in zip(theta, sweep)])

        self.play(MoveAlongPath(dot, circle), Rotate(arrow, TAU, about_point=arrow.get_start()), Create(curve), run_time=5, rate_functions=linear)
        self.next_slide()

        self.play(Unwrite(circle), Unwrite(dot), Unwrite(arrow))
        ax.generate_target()
        curve.generate_target()
        x_axis_label.generate_target()
        y_axis_label.generate_target()
        if ax.target and curve.target and x_axis_label.target and y_axis_label.target:
            ax.target.scale(1.5).shift(3 * LEFT)
            start_anchor = ax.target.coords_to_point(0, 2)
            end_anchor = ax.target.coords_to_point(TAU, 2)
            x_axis_label.target.next_to(ax.target.x_axis.get_end(), RIGHT)
            y_axis_label.target.next_to(ax.target.y_axis.get_start() / 2 + ax.target.y_axis.get_end() / 2, LEFT)
            curve.target.shift(3 * LEFT).put_start_and_end_on(start_anchor, end_anchor)

        self.play(MoveToTarget(ax), MoveToTarget(curve), MoveToTarget(x_axis_label), MoveToTarget(y_axis_label))

        maximum_line_1 = DashedLine(start=ax.coords_to_point(PI / 4, 0), end=ax.coords_to_point(PI / 4, 3), color=GREEN)
        maximum_line_2 = DashedLine(start=ax.coords_to_point(5 * PI / 4, 0), end=ax.coords_to_point(5 * PI / 4, 3), color=GREEN)
        minimum_line_1 = DashedLine(start=ax.coords_to_point(3 * PI / 4, 0), end=ax.coords_to_point(3 * PI / 4, 1), color=RED)
        minimum_line_2 = DashedLine(start=ax.coords_to_point(7 * PI / 4, 0), end=ax.coords_to_point(7 * PI / 4, 1), color=RED)

        maximum_point_1 = Dot(color=GREEN).move_to(ax.coords_to_point(PI / 4, 3))
        maximum_point_2 = Dot(color=GREEN).move_to(ax.coords_to_point(5 * PI / 4, 3))
        minimum_point_1 = Dot(color=RED).move_to(ax.coords_to_point(3 * PI / 4, 1))
        minimum_point_2 = Dot(color=RED).move_to(ax.coords_to_point(7 * PI / 4, 1))

        max_label_1 = MathTex(r"v_1").next_to(maximum_point_1, UP).scale(0.75)
        max_label_2 = MathTex(r"v_2").next_to(maximum_point_2, UP).scale(0.75)
        min_label_1 = MathTex(r"w_1").next_to(minimum_point_1, UP).scale(0.75)
        min_label_2 = MathTex(r"w_2").next_to(minimum_point_2, UP).scale(0.75)

        self.play(Create(maximum_line_1), Create(maximum_line_2), Create(minimum_line_1), Create(minimum_line_2))
        self.play(Create(maximum_point_1), Create(maximum_point_2), Create(minimum_point_1), Create(minimum_point_2),
                    Write(max_label_1), Write(max_label_2), Write(min_label_1), Write(min_label_2))

        self.next_slide()

        self.play(Unwrite(maximum_line_1), Unwrite(maximum_line_2), Unwrite(minimum_line_1), Unwrite(minimum_line_2),
                  Unwrite(maximum_point_1), Unwrite(maximum_point_2), Unwrite(minimum_point_1), Unwrite(minimum_point_2),
                  Unwrite(max_label_1), Unwrite(max_label_2), Unwrite(min_label_1), Unwrite(min_label_2),
                  Unwrite(ax), Unwrite(curve), Unwrite(axis_label))
        self.wait()

        v1 = MathTex(r"v_1 =", r"\begin{bmatrix} 1\\ 1\end{bmatrix}")
        v2 = MathTex(r"v_2 =", r"\begin{bmatrix}-1\\ -1\end{bmatrix}")
        w1 = MathTex(r"w_1 =", r"\begin{bmatrix}-1\\ 1\end{bmatrix}")
        w2 = MathTex(r"w_2 =", r"\begin{bmatrix} 1\\ -1\end{bmatrix}")

        vectors = VGroup(v1, v2, w1, w2).arrange(buff=0.5).shift(2 * UP)

        self.play(Write(vectors))
        self.next_slide()

        v1_quotient = MathTex(r"Mv_1 = 3v_1")
        v2_quotient = MathTex(r"Mv_2 = 3v_2")
        w1_quotient = MathTex(r"Mw_1 = w_1")
        w2_quotient = MathTex(r"Mw_2 = w_2")

        quotients = VGroup(v1_quotient, v2_quotient, w1_quotient, w2_quotient).arrange_in_grid(rows=2, cols=2, buff=1).shift(DOWN)

        self.play(Write(quotients))

        self.next_slide()
        self.play(Unwrite(vectors), Unwrite(quotients), Unwrite(title))
        self.wait()

class RayleighEigenvectors(Slide):
    def construct(self):
        title = Text("Rayleigh Quotient of an Eigenvector").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        assumption = Tex(r"Let $M$ be a matrix with eigenvector $v$ and corresponding eigenvalue $\lambda$").scale(0.5).to_corner(UL).shift(DOWN)
        statement = Tex(r"Then the Rayleigh quotient of $v$ with respect to $M$ is given by:").scale(0.5).to_corner(UL).shift(1.5 * DOWN)
        proof1 = MathTex(r"R(M, v)")
        proof2 = MathTex(r"R(M, v)", r"=\frac{v^TMv}{v^Tv}")
        proof3 = MathTex(r"R(M, v)", r"=\frac{v^TMv}{v^Tv}", r"=\frac{v^T\lambda v}{v^Tv}")
        proof4 = MathTex(r"R(M, v)", r"=\frac{v^TMv}{v^Tv}", r"=\frac{v^T\lambda v}{v^Tv}", r"=\frac{\lambda v^Tv}{v^Tv}")
        proof5 = MathTex(r"R(M, v)", r"=\frac{v^TMv}{v^Tv}", r"=\frac{v^T\lambda v}{v^Tv}", r"=\frac{\lambda v^Tv}{v^Tv}", r"=\lambda")

        self.play(Write(assumption))
        self.next_slide()
        self.play(Write(statement))
        self.next_slide()

        self.play(Write(proof1))
        self.wait(0.75)
        for prev_step, next_step in [(proof1, proof2), (proof2, proof3), (proof3, proof4), (proof4, proof5)]:
            self.play(TransformMatchingTex(prev_step, next_step))
            self.wait(0.75)
        self.next_slide()

        self.play(Unwrite(assumption), Unwrite(statement), Unwrite(proof5), Unwrite(title))
        self.wait()

class RayleighExampleTwo(Slide):
    def construct(self):
        title = Text("Example 2").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        matrix = MathTex(r"M =", BAD_MATRIX_TEX).shift(2 * LEFT)
        vector = MathTex(r"x =", EXAMPLE_VECTOR_TEX).shift(2 * RIGHT)

        self.play(Write(matrix), Write(vector))
        self.next_slide()

        matrix.generate_target()
        vector.generate_target()
        if matrix.target and vector.target:
            matrix.target.shift(2 * UP)
            vector.target.shift(2 * UP)
        self.play(MoveToTarget(matrix), MoveToTarget(vector))

        quotient_tex = r"R(M, x)"
        step1 = MathTex(quotient_tex, "=", r"\frac{x^TMx}{x^Tx}")
        step2 = MathTex(quotient_tex, "=", r"x^TMx")
        step3 = MathTex(quotient_tex, "=", TRANSPOSE_VECTOR_TEX, BAD_MATRIX_TEX, EXAMPLE_VECTOR_TEX)
        step4 = MathTex(quotient_tex, "=", TRANSPOSE_VECTOR_TEX, r"\begin{bmatrix}1 \\ -2\end{bmatrix}")
        step5 = MathTex(quotient_tex, "=", r"1")
        steps = [(step1, step2), (step2, step3), (step3, step4), (step4, step5)]

        self.play(Write(step1))
        self.wait(0.25)
        for prev_step, next_step in steps:
            self.play(TransformMatchingTex(prev_step, next_step))
            self.wait(0.75)
        self.next_slide()
        self.play(Unwrite(step5), Unwrite(matrix), Unwrite(vector))

        circle = Circle(radius=2).shift(3 * LEFT)
        dot = Dot().shift(LEFT)
        arrow = Arrow(start=LEFT, end=RIGHT).put_start_and_end_on(circle.get_center(), dot.get_center()) # type: ignore
        ax = Axes(
            x_range=[0, TAU, PI / 4],
            y_range=[0, 6, 2],
            tips=False,
            y_axis_config={"include_numbers": True}
        ).scale(0.5).shift(3 * RIGHT)
        x_axis_label = ax.get_x_axis_label(r"\theta").scale(0.6)
        y_axis_label = ax.get_y_axis_label(r"R(M, x)").scale(0.6)
        x_axis_label.next_to(ax.x_axis.get_end(), RIGHT)
        y_axis_label.next_to(ax.y_axis.get_end(), UP)
        axis_label = VMobject()
        axis_label.add(x_axis_label, y_axis_label)

        x_pos = [t for t in np.arange(0, TAU + 0.1, PI/4)]
        x_labels = [""] + [r"$\frac{" + str(i) + r"\pi}{4}$" for i in range(1, 9)]
        for pos, label in zip(x_pos, x_labels):
            ax.x_axis.add(Tex(f"{label}", color=WHITE).next_to(ax.x_axis.n2p(pos), DOWN).scale(0.6))

        self.play(Create(circle), Create(ax), Create(dot), Create(arrow), Write(axis_label))
        self.wait()
        self.next_slide()

        theta = np.abs(np.arange(0, TAU, 0.01))
        sweep = compute_rayleigh_sweep(np.array([[1, 3], [-2, 6]]))
        curve = VMobject()
        curve.set_points_smoothly([ax.coords_to_point(t, s) for t, s in zip(theta, sweep)])

        self.play(MoveAlongPath(dot, circle), Rotate(arrow, TAU, about_point=arrow.get_start()), Create(curve), run_time=5, rate_functions=linear)
        self.next_slide()

        self.play(Unwrite(circle), Unwrite(dot), Unwrite(arrow))
        ax.generate_target()
        curve.generate_target()
        x_axis_label.generate_target()
        y_axis_label.generate_target()
        if ax.target and curve.target and x_axis_label.target and y_axis_label.target:
            ax.target.scale(1.5).shift(3 * LEFT)
            start_anchor = ax.target.coords_to_point(0, 1)
            end_anchor = ax.target.coords_to_point(TAU, 1)
            x_axis_label.target.next_to(ax.target.x_axis.get_end(), RIGHT)
            y_axis_label.target.next_to(ax.target.y_axis.get_start() / 2 + ax.target.y_axis.get_end() / 2, LEFT)
            curve.target.shift(3 * LEFT).put_start_and_end_on(start_anchor, end_anchor)

        self.play(MoveToTarget(ax), MoveToTarget(curve), MoveToTarget(x_axis_label), MoveToTarget(y_axis_label))

        maximum_line_1 = DashedLine(start=ax.coords_to_point(PI / 4, 0), end=ax.coords_to_point(PI / 4, 4), color=GREEN)
        maximum_line_2 = DashedLine(start=ax.coords_to_point(5 * PI / 4, 0), end=ax.coords_to_point(5 * PI / 4, 4), color=GREEN)
        minimum_line_1 = DashedLine(start=ax.coords_to_point(np.arctan(2/3), 0), end=ax.coords_to_point(np.arctan(2/3), 3), color=RED)
        minimum_line_2 = DashedLine(start=ax.coords_to_point(PI + np.arctan(2/3), 0), end=ax.coords_to_point(PI + np.arctan(2/3), 3), color=RED)

        maximum_point_1 = Dot(color=GREEN).move_to(ax.coords_to_point(PI / 4, 4))
        maximum_point_2 = Dot(color=GREEN).move_to(ax.coords_to_point(5 * PI / 4, 4))
        minimum_point_1 = Dot(color=RED).move_to(ax.coords_to_point(np.arctan(2/3), 3))
        minimum_point_2 = Dot(color=RED).move_to(ax.coords_to_point(PI + np.arctan(2/3), 3))

        max_label_1 = MathTex(r"v_1").next_to(maximum_point_1, 0.5 * (UP + LEFT)).scale(0.75)
        max_label_2 = MathTex(r"v_2").next_to(maximum_point_2, 0.5 * (UP + LEFT)).scale(0.75)
        min_label_1 = MathTex(r"w_1").next_to(minimum_point_1, 0.5 * (UP + LEFT)).scale(0.75)
        min_label_2 = MathTex(r"w_2").next_to(minimum_point_2, 0.5 * (UP + LEFT)).scale(0.75)

        self.play(Create(maximum_line_1), Create(maximum_line_2), Create(minimum_line_1), Create(minimum_line_2))
        self.play(Create(maximum_point_1), Create(maximum_point_2), Create(minimum_point_1), Create(minimum_point_2),
                    Write(max_label_1), Write(max_label_2), Write(min_label_1), Write(min_label_2))

        self.next_slide()

        self.play(Unwrite(maximum_line_1), Unwrite(maximum_line_2), Unwrite(minimum_line_1), Unwrite(minimum_line_2),
                  Unwrite(maximum_point_1), Unwrite(maximum_point_2), Unwrite(minimum_point_1), Unwrite(minimum_point_2),
                  Unwrite(max_label_1), Unwrite(max_label_2), Unwrite(min_label_1), Unwrite(min_label_2),
                  Unwrite(ax), Unwrite(curve), Unwrite(axis_label))
        self.wait()

        self.next_slide()

        sym_matrix = Matrix([[2, 1], [1, 2]])
        bad_matrix = Matrix([[1, 3], [-2, 6]])
        matrices = VGroup(sym_matrix, bad_matrix).arrange(buff=1.5)

        self.play(Write(matrices))
        self.next_slide()

        sym_matrix_entries = sym_matrix.get_entries()
        bad_matrix_entries = bad_matrix.get_entries()

        sym_matrix_entries[1].generate_target()
        sym_matrix_entries[2].generate_target()
        bad_matrix_entries[1].generate_target()
        bad_matrix_entries[2].generate_target()

        if sym_matrix_entries[1].target and sym_matrix_entries[2].target and bad_matrix_entries[1].target and bad_matrix_entries[2].target:
            sym_matrix_entries[1].target.move_to(sym_matrix_entries[2], RIGHT)
            sym_matrix_entries[2].target.move_to(sym_matrix_entries[1], RIGHT)
            bad_matrix_entries[1].target.move_to(bad_matrix_entries[2], RIGHT)
            bad_matrix_entries[2].target.move_to(bad_matrix_entries[1], RIGHT)

            sym_matrix_entries[1].target.set_color(GREEN) # type: ignore
            sym_matrix_entries[2].target.set_color(GREEN) # type: ignore
            bad_matrix_entries[1].target.set_color(RED)   # type: ignore
            bad_matrix_entries[2].target.set_color(RED)   # type: ignore


        self.play(MoveToTarget(sym_matrix_entries[1]), MoveToTarget(sym_matrix_entries[2]), MoveToTarget(bad_matrix_entries[1]), MoveToTarget(bad_matrix_entries[2]))

        self.next_slide()

        self.play(Unwrite(title), Unwrite(matrices))
        self.wait()

class CourantFischerTheorem(Slide):
    def construct(self):
        title = Text("Courant-Fischer Theorem").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        assumption = Tex(r"Let $M$ be a symmetric matrix with eigenvalues $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$. Then:").scale(0.5).to_corner(UL).shift(DOWN)
        theorem = MathTex(r"\lambda_k", "=",
                          r"\max_{\substack{S \subseteq \mathbb{R}^n \\ \operatorname{dim}(S) = k}} \min_{\substack{x \in S \\ x \neq 0}} \frac{x^TMx}{x^Tx}", "=",
                          r"\min_{\substack{T \subseteq \mathbb{R}^n \\ \operatorname{dim}(T) = n - k + 1}} \max_{\substack{x \in T \\ x \neq 0}} \frac{x^TMx}{x^Tx}").shift(UP)
        simplified_theorem = MathTex(r"\lambda_k", "=",
                          r"\max_{\substack{S \subseteq \mathbb{R}^n \\ \operatorname{dim}(S) = k}} \min_{\substack{x \in S \\ x \neq 0}} \frac{x^TMx}{x^Tx}").shift(UP)

        self.play(Write(assumption))

        self.next_slide()

        self.play(Write(theorem))

        self.next_slide()

        self.play(TransformMatchingTex(theorem, simplified_theorem))

        self.next_slide()
        self.play(Unwrite(title), Unwrite(assumption), Unwrite(simplified_theorem))
        self.wait()

        self.next_slide()

        title = Text("Lemma").scale(0.5).to_corner(UL)
        self.play(Write(title))
        self.next_slide()

        assumption1 = Tex(r"\text{Let $M$ be a symmetric matrix with eigenvalues $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$ and a corresponding orthonormal basis").scale(0.5).to_corner(UL).shift(DOWN)
        assumption2 = Tex(r"\text{of eigenvectors $v_1, \dots, v_n$.}}").scale(0.5).to_corner(UL).shift(1.5 * DOWN)
        assumption3 = Tex(r"Let $x$ be a vector in $\mathbb{R}^n$ whose expansion is given by $x = \sum_{i=1}^n \alpha_i v_i$. Then:").scale(0.5).to_corner(UL).shift(2 * DOWN)
        lemma = MathTex(r"x^TMx", "=", r"\sum_{i=1}^n \lambda_i \alpha_i^2")

        self.play(Write(assumption1))
        self.play(Write(assumption2))
        self.next_slide()
        self.play(Write(assumption3))
        self.next_slide()
        self.play(Write(lemma))

        self.next_slide()
        self.play(Unwrite(title), Unwrite(assumption1), Unwrite(assumption2), Unwrite(assumption3), Unwrite(lemma))
        self.wait()

        self.next_slide()

        title = Text("Proof of Lemma").scale(0.5).to_corner(UL)
        self.play(Write(title))

        self.next_slide()

        step1 = MathTex(r"x^TMx")
        step2 = MathTex(r"x^TMx", "=", r"\left(\sum_{i=1}^n \alpha_i v_i\right)^T", r"M", r"\left(\sum_{i=1}^n \alpha_i v_i\right)")
        step3 = MathTex(r"x^TMx", "=", r"\left(\sum_{i=1}^n \alpha_i v_i\right)^T\left(\sum_{i=1}^n \alpha_i", r"M", r"v_i\right)")
        step4 = MathTex(r"x^TMx", "=", r"\left(\sum_{i=1}^n \alpha_i v_i\right)^T\left(\sum_{i=1}^n \alpha_i \lambda_iv_i\right)")
        step5 = MathTex(r"x^TMx", "=", r"\sum_{i=1}^n\sum_{j=1}^n \alpha_i\alpha_j \lambda_i", r"\langle v_i, v_j\rangle")
        step6 = MathTex(r"x^TMx", "=", r"\sum_{i=1}^n \alpha_i^2 \lambda_i")

        self.play(Write(step1))
        steps = [(step1, step2), (step2, step3), (step3, step4), (step4, step5), (step5, step6)]
        for prev_step, next_step in steps:
            if prev_step == step5 and step5.target:
                self.remove(step5.target)

            self.next_slide()
            self.play(TransformMatchingTex(prev_step, next_step))

            if next_step == step5:
                self.next_slide()
                step5.generate_target()
                if step5.target:
                    step5.target.set_color_by_tex(r"\langle v_i, v_j\rangle", YELLOW)
                self.play(FadeTransform(step5, step5.target))

        self.next_slide()
        self.play(Unwrite(title), Unwrite(step6))
        self.wait()

        self.next_slide()

        title = Text("Proof of Courant-Fischer Theorem").scale(0.5).to_corner(UL)

        self.play(Write(title))

        assumption = Tex(r"Let $M$ be a symmetric matrix with eigenvalues $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$. Then:").scale(0.5).to_corner(UL).shift(1 * DOWN)
        simplified_theorem = MathTex(r"\lambda_k", "=",
                          r"\max_{\substack{S \subseteq \mathbb{R}^n \\ \operatorname{dim}(S) = k}} \min_{\substack{x \in S \\ x \neq 0}} \frac{x^TMx}{x^Tx}").shift(UP)

        self.play(Write(assumption), Write(simplified_theorem))

        self.next_slide()

        step1 = Tex(r"(1) Show that $\lambda_k$ bounds the Rayleigh quotient for all $k$-dimensional subspaces").scale(0.5).shift(0.5 * DOWN).to_edge(LEFT)
        step2 = Tex(r"(2) Show that $\lambda_k$ is attained by some $k$-dimensional subspace").scale(0.5).next_to(step1, 0.5 * DOWN, aligned_edge=LEFT)

        self.play(Write(step1))
        self.next_slide
        self.play(Write(step2))

        self.next_slide()

        step1.generate_target()
        if step1.target:
            step1.target.next_to(title, DOWN, aligned_edge=LEFT)

        self.play(Unwrite(assumption), Unwrite(simplified_theorem), Unwrite(step2))
        self.play(MoveToTarget(step1))
        self.wait()

        self.next_slide()

        T = MathTex(r"T = \operatorname{span}\{v_k, \dots, v_n\}").scale(0.6).to_edge(UP).shift(1.5 * DOWN + 3.3 * LEFT)
        T_dim = MathTex(r"\implies", r"\operatorname{dim}(T) = n - k + 1").scale(0.6).next_to(T, 0.6 * RIGHT)
        nontrivial_intersection = MathTex(r"\implies", r"T \cap S \neq \{0\}").scale(0.6).next_to(T_dim, 0.6 * RIGHT)

        inequality1 = MathTex(r"\min_{\substack{x \in S \\ x \neq 0}} \frac{x^TMx}{x^Tx}").scale(0.6).to_edge(UP).shift(2.5 * DOWN + 2.2 * LEFT)
        inequality2 = MathTex(r"\leq", r"\min_{\substack{x \in S \cap T \\ x \neq 0}} \frac{x^TMx}{x^Tx}").scale(0.6).next_to(inequality1, 0.6 * RIGHT)
        inequality3 = MathTex(r"\leq", r"\max_{\substack{x \in T \\ x \neq 0}} \frac{x^TMx}{x^Tx}").scale(0.6).next_to(inequality2, 0.6 * RIGHT)

        x = MathTex(r"x = \sum_{i=k}^n \alpha_i v_i").scale(0.6).to_edge(UP).shift(3.8 * DOWN)

        bound1 = MathTex(r"\frac{x^TMx}{x^Tx}").scale(0.6).to_edge(UP).shift(5.3 * DOWN + 3.5 * LEFT)
        bound2 = MathTex("=", r"\frac{\sum_{i = k}^n \lambda_i\alpha_i^2}{\sum_{i = k}^n \alpha_i^2}").scale(0.6).next_to(bound1, 0.6 * RIGHT)
        bound3 = MathTex(r"\leq", r"\frac{\sum_{i = k}^n \lambda_k\alpha_i^2}{\sum_{i = k}^n \alpha_i^2}").scale(0.6).next_to(bound2, 0.6 * RIGHT)
        bound4 = MathTex("=", r"\lambda_k \cdot \frac{\sum_{i = k}^n \alpha_i^2}{\sum_{i = k}^n \alpha_i^2}").scale(0.6).next_to(bound3, 0.6 * RIGHT)
        bound5 = MathTex("=", r"\lambda_k").scale(0.6).next_to(bound4, 0.6 * RIGHT)

        self.play(Write(T))
        self.next_slide()
        self.play(Write(T_dim))
        self.next_slide()
        self.play(Write(nontrivial_intersection))
        self.next_slide()

        self.play(Write(inequality1))
        self.next_slide()
        self.play(Write(inequality2))
        self.next_slide()
        self.play(Write(inequality3))
        self.next_slide()


        self.play(Write(x))
        self.next_slide()

        for bound in [bound1, bound2, bound3, bound4, bound5]:
            self.play(Write(bound))
            self.next_slide()

        self.play(Unwrite(T), Unwrite(T_dim), Unwrite(nontrivial_intersection), Unwrite(inequality1), Unwrite(inequality2), Unwrite(inequality3), Unwrite(x), Unwrite(bound1), Unwrite(bound2), Unwrite(bound3), Unwrite(bound4), Unwrite(bound5))

        step2 = Tex(r"(2) Show that $\lambda_k$ is attained by some $k$-dimensional subspace").scale(0.5).next_to(title, DOWN, aligned_edge=LEFT)

        self.play(Transform(step1, step2))

        self.wait()
        self.next_slide()

        S = MathTex(r"S = \operatorname{span}\{v_1, \dots, v_k\}").scale(0.6).to_edge(UP).shift(1.5 * DOWN + 1.5 * LEFT)
        x = MathTex(r"x = \sum_{i=k}^n \alpha_i v_i").scale(0.6).next_to(S, 3 * RIGHT)

        bound1 = MathTex(r"\frac{x^TMx}{x^Tx}").scale(0.6).to_edge(UP).shift(2.5 * DOWN + 3.5 * LEFT)
        bound2 = MathTex("=", r"\frac{\sum_{i = 1}^k \lambda_i\alpha_i^2}{\sum_{i = 1}^k \alpha_i^2}").scale(0.6).next_to(bound1, 0.6 * RIGHT)
        bound3 = MathTex(r"\geq", r"\frac{\sum_{i = 1}^k \lambda_k\alpha_i^2}{\sum_{i = 1}^k \alpha_i^2}").scale(0.6).next_to(bound2, 0.6 * RIGHT)
        bound4 = MathTex("=", r"\lambda_k \cdot \frac{\sum_{i = 1}^k \alpha_i^2}{\sum_{i = 1}^k \alpha_i^2}").scale(0.6).next_to(bound3, 0.6 * RIGHT)
        bound5 = MathTex("=", r"\lambda_k").scale(0.6).next_to(bound4, 0.6 * RIGHT)

        upshot = MathTex(r"\implies", r"\min_{\substack{x \in S \\ x \neq 0}} \frac{x^TMx}{x^Tx} \geq \lambda_k").scale(0.6).to_edge(UP).shift(4 * DOWN)

        self.play(Write(S))
        self.next_slide()
        self.play(Write(x))
        self.next_slide()

        for bound in [bound1, bound2, bound3, bound4, bound5]:
            self.play(Write(bound))
            self.next_slide()

        self.play(Write(upshot))