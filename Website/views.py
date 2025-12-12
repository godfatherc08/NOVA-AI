from flask import Blueprint, render_template, request
from sympy.physics.units import atmosphere

import json
from .FIBO_AI.Generate import Generate

views = Blueprint("views", __name__)
generate = Generate()


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/editor", methods=["GET", "POST"])
def editor():
    refine = True
    if request.method == "POST":
        action = request.form.get("action")
        if action == "generate":
            query = request.form.get("query")
            image_url, structured_prompt, seed= generate.return_image(query)
            return render_template("editor.html", image_url=image_url, structured_prompt=structured_prompt,seed=seed)
        elif action == "refine":
            camera_angle = request.form.get("camera_angle")
            shot_size = request.form.get("shot_size")
            lens = request.form.get("lens")
            camera_height = request.form.get("camera_height")
            camera_movement = request.form.get("camera_movement")
            lighting_type = request.form.get("lighting_type")
            light_direction = request.form.get("light_direction")
            color_temp = request.form.get("color_temp")
            time_of_day = request.form.get("time_of_day")
            shadow_intensity = request.form.get("shadow_intensity")
            highlight_intensity = request.form.get("highlight_intensity")
            color_grade =request.form.get("color_grade")
            saturation =request.form.get("saturation")
            contrast = request.form.get("contrast")
            brightness = request.form.get("brightness")
            hdr_enabled = request.form.get("hdr_enabled")
            bit_depth = request.form.get("bit_depth")
            depth_of_field = request.form.get("depth_of_field")
            aperture = request.form.get("aperture")
            focus_distance = request.form.get("focus_distance")
            composition_ruler = request.form.get("composition_ruler")
            subject_position = request.form.get("subject_position")
            aspect_ratio = request.form.get("aspect_ratio")
            film_stock = request.form.get("film_stock")
            grain_intensity = request.form.get("grain_intensity")
            vignette = request.form.get("vignette")
            lens_distortion = request.form.get("lens_distortion")
            chromatic_aberration = request.form.get("chromatic_aberration")
            weather = request.form.get("weather")
            atmosphere1 = request.form.get("atmosphere")
            fog_density = request.form.get("fog_density")
            structured_prompt = request.form.get("structured_prompt")
            seed = request.form.get("seed")

            refinement_dictionary = {
                "camera_angle": camera_angle,
                "shot_size": shot_size,
                "lens": lens,
                "camera_height": camera_height,
                "camera_movement": camera_movement,
                "lighting_type": lighting_type,
                "light_direction": light_direction,
                "color_temp": color_temp,
                "time_of_day": time_of_day,
                "shadow_intensity": shadow_intensity,
                "highlight_intensity": highlight_intensity,
                "color_grade": color_grade,
                "saturation": saturation,
                "contrast": contrast,
                "brightness": brightness,
                "hdr_enabled": hdr_enabled,
                "bit_depth": bit_depth,
                "depth_of_field": depth_of_field,
                "aperture": aperture,
                "focus_distance": focus_distance,
                "composition_ruler": composition_ruler,
                "subject_position": subject_position,
                "aspect_ratio": aspect_ratio,
                "film_stock": film_stock,
                "grain_intensity": grain_intensity,
                "vignette": vignette,
                "lens_distortion": lens_distortion,
                "chromatic_aberration": chromatic_aberration,
                "weather": weather,
                "atmosphere": atmosphere1,
                "fog_density": fog_density
            }
            refinement_string = json.dumps(refinement_dictionary)
            refined_image_url, new_structured_prompt, new_seed = generate.return_image_refine(refinement_string, structured_prompt, seed)
            return render_template("editor.html",image_url=refined_image_url, structured_prompt=new_structured_prompt, seed=new_seed)
        else:
            return render_template("404.html")
    else:
        return render_template("editor.html")

