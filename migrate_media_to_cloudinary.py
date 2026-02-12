import os
import django
import cloudinary.uploader

# ========================
# Setup Django environment
# ========================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms_project.settings")
django.setup()

# ========================
# Import your models
# ========================
from lms.models import (
    HeroSection,
    HomeAboutSection,
    Category,
    Instructor,
    Tool,
    Course,
    HomeBanner,
    Testimonial,
    CourseReview,
    Video
)

# ========================
# Function to upload image
# ========================
def upload_image_to_cloudinary(local_path, folder="django_media_migration"):
    if not local_path:
        return None

    if not os.path.exists(local_path):
        print(f"File does not exist: {local_path}")
        return None

    try:
        result = cloudinary.uploader.upload(
            local_path,
            folder=folder,
            resource_type="image"
        )
        return result.get("secure_url")
    except Exception as e:
        print(f"Error uploading {local_path}: {e}")
        return None

# ========================
# Mapping model fields
# ========================
MODEL_FIELDS = [
    (HeroSection, ["hero_image"]),
    (HomeAboutSection, ["image"]),
    (Category, ["icon"]),
    (Instructor, ["profile_image"]),
    (Tool, ["icon_image"]),
    (Course, ["thumbnail"]),
    (HomeBanner, ["image"]),
    (Testimonial, ["profile_image"]),
    (CourseReview, ["photo"]),
    (Video, ["thumbnail"]),  # If some video thumbnails were local
]

# ========================
# Migrate images
# ========================
for model, fields in MODEL_FIELDS:
    instances = model.objects.all()
    for obj in instances:
        updated = False
        for field_name in fields:
            file_field = getattr(obj, field_name)
            if not file_field:
                continue

            # Get local file path
            local_path = file_field.path if hasattr(file_field, "path") else None
            if not local_path or not os.path.exists(local_path):
                continue

            # Upload to Cloudinary
            url = upload_image_to_cloudinary(local_path)
            if url:
                # Update model field to Cloudinary URL
                file_field.name = url  # Cloudinary storage will pick up
                updated = True
                print(f"Uploaded {field_name} for {obj} -> {url}")

        if updated:
            obj.save()
            print(f"Saved object {obj}")
