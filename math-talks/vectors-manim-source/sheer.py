from manim import *

class ShearTransformation(Scene):
    def construct(self):
        # Calculate ranges to ensure square grid cells
        x_span = 15  # from -6 to 9
        y_span = 9   # from -2 to 7
        grid_size = 8  # Base size for the grid
        
        # Make grid cells truly square by matching the aspect ratio
        axes = Axes(
            x_range=[-6, 9, 1],
            y_range=[-2, 7, 1],
            x_length=grid_size,
            y_length=grid_size * (y_span / x_span),  # Scale y_length to maintain square cells
            axis_config={
                "color": BLUE,
                "stroke_width": 2,
            },
            tips=False,
        )
        
        # Create grid with square cells
        grid = NumberPlane(
            x_range=[-6, 9, 1],
            y_range=[-2, 7, 1],
            x_length=grid_size,
            y_length=grid_size * (y_span / x_span),
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.8,
            }
        )
        
        # Create background grid (light copy that stays fixed)
        background_grid = grid.copy()
        background_grid.set_stroke(opacity=0.2)
        
        # Create point A
        point_A = Dot(axes.coords_to_point(3, 4), color=RED, radius=0.1)
        
        # Create basis vectors
        vector_i = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, 0),
            color=GREEN,
            stroke_width=4,
            buff=0
        )
        
        vector_j = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(0, 1),
            color=ORANGE,
            stroke_width=4,
            buff=0
        )
        
        # Create mask to hide negative x region initially
        mask = Rectangle(
            width=4,
            height=grid_size * (y_span / x_span) + 1,  # Match the grid height
            fill_color=BLACK,
            fill_opacity=1,
            stroke_opacity=0
        )
        mask.move_to(axes.coords_to_point(-3, 2.5))
        
        # Set up initial scene with mask
        self.add(background_grid)
        self.add(mask)
        
        self.play(
            Create(grid),
            Create(axes),
            Create(point_A),
            Create(vector_i),
            Create(vector_j),
            run_time=2
        )
        
        self.wait(1)
        
        # Apply shear transformation
        def shear_transform(point):
            coords = axes.point_to_coords(point)
            new_x = coords[0] + coords[1]
            new_y = coords[1]
            return axes.coords_to_point(new_x, new_y)
        
        # Create transformed objects
        transformed_grid = grid.copy()
        transformed_axes = axes.copy()
        
        # Transform all points in the grid and axes
        for mob in [transformed_grid, transformed_axes]:
            for submob in mob.family_members_with_points():
                submob.points = np.array([shear_transform(point) for point in submob.points])
        
        # Transform point A
        transformed_point_A = Dot(shear_transform(point_A.get_center()), color=RED, radius=0.1)
        
        # Transform vectors
        transformed_vector_i = Arrow(
            axes.coords_to_point(0, 0),
            shear_transform(vector_i.get_end()),
            color=GREEN,
            stroke_width=4,
            buff=0
        )
        
        transformed_vector_j = Arrow(
            axes.coords_to_point(0, 0),
            shear_transform(vector_j.get_end()),
            color=ORANGE,
            stroke_width=4,
            buff=0
        )
        
        # Animate the transformation
        self.play(
            Transform(grid, transformed_grid),
            Transform(axes, transformed_axes),
            Transform(point_A, transformed_point_A),
            Transform(vector_i, transformed_vector_i),
            Transform(vector_j, transformed_vector_j),
            run_time=4
        )
        
        # Remove mask to reveal the complete transformed grid
        self.play(
            FadeOut(mask),
            run_time=1
        )
        
        self.wait(3)
