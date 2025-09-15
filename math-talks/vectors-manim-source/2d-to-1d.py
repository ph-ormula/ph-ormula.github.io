from manim import *
import numpy as np

class AngleProjectionScene(Scene):
    def construct(self):
        # Larger coordinate system for higher quality
        axis_length = 10
        grid_range = 3
        grid_step = 0.5

        # Create coordinate axes
        x_axis = Arrow(start=LEFT*axis_length/2, end=RIGHT*axis_length/2, 
                      color=WHITE, stroke_width=2, tip_length=0.2)
        y_axis = Arrow(start=DOWN*axis_length/2, end=UP*axis_length/2, 
                      color=WHITE, stroke_width=2, tip_length=0.2)

        # Create grid lines
        grid_lines = VGroup()
        for x in np.arange(-grid_range, grid_range + grid_step, grid_step):
            if abs(x) > 1e-4:
                line = Line(np.array([x, -grid_range, 0]), np.array([x, grid_range, 0]),
                           stroke_width=1, stroke_opacity=0.3, color=GRAY)
                grid_lines.add(line)
        for y in np.arange(-grid_range, grid_range + grid_step, grid_step):
            if abs(y) > 1e-4:
                line = Line(np.array([-grid_range, y, 0]), np.array([grid_range, y, 0]),
                           stroke_width=1, stroke_opacity=0.3, color=GRAY)
                grid_lines.add(line)

        self.play(Create(grid_lines), Create(x_axis), Create(y_axis))

        # Define points A, B, C
        angle_AOC = 30 * DEGREES
        angle_BOC = 45 * DEGREES
        O = ORIGIN
        C = np.array([1, 0, 0])
        A = np.array([np.cos(angle_AOC), np.sin(angle_AOC), 0])
        B = np.array([np.cos(angle_BOC), np.sin(angle_BOC), 0])

        # Create points with original size
        point_radius = 0.08
        point_O = Dot(O, color=YELLOW, radius=point_radius)
        point_A = Dot(A, color=BLUE, radius=point_radius)
        point_B = Dot(B, color=GREEN, radius=point_radius)
        point_C = Dot(C, color=RED, radius=point_radius)

        # Create lines OA, OB, OC
        line_OA = Line(O, A, color=BLUE, stroke_width=3)
        line_OB = Line(O, B, color=GREEN, stroke_width=3)
        line_OC = Line(O, C, color=RED, stroke_width=3)

        self.play(FadeIn(point_O), FadeIn(point_A), FadeIn(point_B), FadeIn(point_C))

        # Create labels with original size
        label_font_size = 18
        label_O = Text("O", font_size=label_font_size, color=YELLOW).next_to(point_O, DOWN + LEFT, buff=0.1)
        label_A = Text("A", font_size=label_font_size, color=BLUE).next_to(point_A, UP + RIGHT, buff=0.1)
        label_B = Text("B", font_size=label_font_size, color=GREEN).next_to(point_B, UP + LEFT, buff=0.1)
        label_C = Text("C", font_size=label_font_size, color=RED).next_to(point_C, DOWN + RIGHT, buff=0.1)

        self.play(Write(label_O), Write(label_A), Write(label_B), Write(label_C))

        # Draw radius lines OA, OB, OC
        self.play(Create(line_OA), Create(line_OB), Create(line_OC))
        self.wait(1)

        # Direction vector of line OA
        OA_direction = A / np.linalg.norm(A)

        # Show projection line OA
        projection_line = Line(-grid_range * OA_direction, grid_range * OA_direction,
                              color=BLUE, stroke_width=5)
        self.play(Create(projection_line))

        # Function to project points onto line OA
        def project_point(point):
            p2d = point[:2]
            dir2d = OA_direction[:2]
            scalar = np.dot(p2d, dir2d)
            proj = scalar * dir2d
            return np.append(proj, 0)

        # Project grid lines
        projected_grid = VGroup()
        for line in grid_lines:
            start_proj = project_point(line.get_start())
            end_proj = project_point(line.get_end())
            proj_line = Line(start_proj, end_proj, stroke_width=2, stroke_opacity=0.7, color=ORANGE)
            projected_grid.add(proj_line)

        # Project all lines OA, OB, OC
        proj_line_OA = Line(project_point(O), project_point(A), color=BLUE, stroke_width=3)
        proj_line_OB = Line(project_point(O), project_point(B), color=GREEN, stroke_width=3)
        proj_line_OC = Line(project_point(O), project_point(C), color=RED, stroke_width=3)

        # Project points
        A_proj = Dot(project_point(A), color=BLUE, radius=point_radius)
        B_proj = Dot(project_point(B), color=GREEN, radius=point_radius)
        C_proj = Dot(project_point(C), color=RED, radius=point_radius)
        O_proj = Dot(project_point(O), color=YELLOW, radius=point_radius)

        # Create projected axes
        x_axis_proj = Arrow(start=project_point(LEFT*axis_length/2), 
                           end=project_point(RIGHT*axis_length/2),
                           color=WHITE, stroke_width=2, tip_length=0.2)
        y_axis_proj = Arrow(start=project_point(DOWN*axis_length/2),
                           end=project_point(UP*axis_length/2), 
                           color=WHITE, stroke_width=2, tip_length=0.2)

        # Create new label positions that follow the points but don't collapse onto the line
        offset_A = np.array([0.2, 0.15, 0])   # Offset for label A
        offset_B = np.array([-0.2, 0.15, 0])  # Offset for label B  
        offset_C = np.array([0.15, -0.15, 0]) # Offset for label C (ADDED THIS)

        label_A_new = Text("A", font_size=label_font_size, color=BLUE).move_to(project_point(A) + offset_A)
        label_B_new = Text("B", font_size=label_font_size, color=GREEN).move_to(project_point(B) + offset_B)
        label_C_new = Text("C", font_size=label_font_size, color=RED).move_to(project_point(C) + offset_C)

        # Animate the projection transformation
        self.play(
            Transform(grid_lines, projected_grid),
            Transform(x_axis, x_axis_proj),
            Transform(y_axis, y_axis_proj),
            Transform(line_OA, proj_line_OA),
            Transform(line_OB, proj_line_OB),
            Transform(line_OC, proj_line_OC),
            Transform(point_A, A_proj),
            Transform(point_B, B_proj),
            Transform(point_C, C_proj),
            Transform(point_O, O_proj),
            Transform(label_A, label_A_new),
            Transform(label_B, label_B_new),
            Transform(label_C, label_C_new),  # ADDED THIS LINE
            run_time=3
        )

        self.wait(2)
