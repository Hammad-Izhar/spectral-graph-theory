from manim import *
from manim_slides.slide import Slide

class Intro(Slide):
    def construct(self):
        title = Text("An Introduction to Spectral Graph Theory")
        author = Text("Daniel A. Spielman")
        author.next_to(title, DOWN, buff=0.5)

        title_slide = VGroup(title, author).center()

        self.play(Write(title_slide))
        self.next_slide()
        self.play(Unwrite(title_slide))