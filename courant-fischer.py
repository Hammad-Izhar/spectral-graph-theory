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
        v2 = MathTex(r"v_2 =", r"\begin{bmatrix}-1\\ 1\end{bmatrix}")
        w1 = MathTex(r"w_1 =", r"\begin{bmatrix}-1\\ 1\end{bmatrix}")
        w2 = MathTex(r"w_2 =", r"\begin{bmatrix} 1\\ 1\end{bmatrix}")

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
            start_anchor = ax.target.coords_to_point(0, 2)
            end_anchor = ax.target.coords_to_point(TAU, 2)
            x_axis_label.target.next_to(ax.target.x_axis.get_end(), RIGHT)
            y_axis_label.target.next_to(ax.target.y_axis.get_start() / 2 + ax.target.y_axis.get_end() / 2, LEFT)
            curve.target.shift(3 * LEFT).put_start_and_end_on(start_anchor, end_anchor)

        self.play(MoveToTarget(ax), MoveToTarget(curve), MoveToTarget(x_axis_label), MoveToTarget(y_axis_label))

        # maximum_line_1 = DashedLine(start=ax.coords_to_point(PI / 4, 0), end=ax.coords_to_point(PI / 4, 3), color=GREEN)
        # maximum_line_2 = DashedLine(start=ax.coords_to_point(5 * PI / 4, 0), end=ax.coords_to_point(5 * PI / 4, 3), color=GREEN)
        # minimum_line_1 = DashedLine(start=ax.coords_to_point(3 * PI / 4, 0), end=ax.coords_to_point(3 * PI / 4, 1), color=RED)
        # minimum_line_2 = DashedLine(start=ax.coords_to_point(7 * PI / 4, 0), end=ax.coords_to_point(7 * PI / 4, 1), color=RED)

        # maximum_point_1 = Dot(color=GREEN).move_to(ax.coords_to_point(PI / 4, 3))
        # maximum_point_2 = Dot(color=GREEN).move_to(ax.coords_to_point(5 * PI / 4, 3))
        # minimum_point_1 = Dot(color=RED).move_to(ax.coords_to_point(3 * PI / 4, 1))
        # minimum_point_2 = Dot(color=RED).move_to(ax.coords_to_point(7 * PI / 4, 1))

        # max_label_1 = MathTex(r"v_1").next_to(maximum_point_1, UP).scale(0.75)
        # max_label_2 = MathTex(r"v_2").next_to(maximum_point_2, UP).scale(0.75)
        # min_label_1 = MathTex(r"w_1").next_to(minimum_point_1, UP).scale(0.75)
        # min_label_2 = MathTex(r"w_2").next_to(minimum_point_2, UP).scale(0.75)

        # self.play(Create(maximum_line_1), Create(maximum_line_2), Create(minimum_line_1), Create(minimum_line_2))
        # self.play(Create(maximum_point_1), Create(maximum_point_2), Create(minimum_point_1), Create(minimum_point_2),
        #             Write(max_label_1), Write(max_label_2), Write(min_label_1), Write(min_label_2))

        # self.next_slide()

        # self.play(Unwrite(maximum_line_1), Unwrite(maximum_line_2), Unwrite(minimum_line_1), Unwrite(minimum_line_2),
        #           Unwrite(maximum_point_1), Unwrite(maximum_point_2), Unwrite(minimum_point_1), Unwrite(minimum_point_2),
        #           Unwrite(max_label_1), Unwrite(max_label_2), Unwrite(min_label_1), Unwrite(min_label_2),
        #           Unwrite(ax), Unwrite(curve), Unwrite(axis_label))
        # self.wait()

        # v1 = MathTex(r"v_1 =", r"\begin{bmatrix} 1\\ 1\end{bmatrix}")
        # v2 = MathTex(r"v_2 =", r"\begin{bmatrix}-1\\ 1\end{bmatrix}")
        # w1 = MathTex(r"w_1 =", r"\begin{bmatrix}-1\\ 1\end{bmatrix}")
        # w2 = MathTex(r"w_2 =", r"\begin{bmatrix} 1\\ 1\end{bmatrix}")

        # vectors = VGroup(v1, v2, w1, w2).arrange(buff=0.5).shift(2 * UP)

        # self.play(Write(vectors))
        # self.next_slide()

        # v1_quotient = MathTex(r"Mv_1 = 3v_1")
        # v2_quotient = MathTex(r"Mv_2 = 3v_2")
        # w1_quotient = MathTex(r"Mw_1 = w_1")
        # w2_quotient = MathTex(r"Mw_2 = w_2")

        # quotients = VGroup(v1_quotient, v2_quotient, w1_quotient, w2_quotient).arrange_in_grid(rows=2, cols=2, buff=1).shift(DOWN)

        # self.play(Write(quotients))

        # self.next_slide()
        # self.play(Unwrite(vectors), Unwrite(quotients), Unwrite(title))
        # self.wait()